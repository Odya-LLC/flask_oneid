"""
    flask_oneid
    ~~~~~~~~~~~~~~~
    :author: Odya <mmuhtor@gmail.com>
    :copyright: (c) 2022 by Odya.
    :license: MIT, see LICENSE for more details.
"""

import json, requests
from flask import Blueprint, request, redirect, jsonify, url_for, session
from .exceptions import Flask_ONEID_Exception
class OneID:

    ONEID_LOGIN_URL = "/oneid/login"
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
    def init_app(self, app) -> None:
        """ OneID integration with Flask application(only Uzbekistan).
        About ONEID: https://id.egov.uz
        
        Args:
            app (flask.Flask): Flask APP

        Raises:
            Flask_ONEID_Exception: When ONEID_LOGIN or ONEID_PASSWORD is not set

       
        """        
        self.__oneid_url__ = "https://sso.egov.uz/sso/oauth/Authorization.do"
        self.__callback_url = "/"
        self.__one_id_keys = []
        self.__client_id__ = app.config.get('ONEID_LOGIN')
        if self.__client_id__ is None:
            raise Flask_ONEID_Exception("ONEID_LOGIN is not set, please set it in config.py")
        self.__client_secret__ = app.config.get('ONEID_PASSWORD')
        if self.__client_secret__ is None:
            raise Flask_ONEID_Exception("ONEID_PASSWORD is not set, please set it in config.py")
        self.__oneid_url__ = app.config.get('ONEID_URL', "https://sso.egov.uz/sso/oauth/Authorization.do")
        app.secret_key = "secret"
        oneid = Blueprint('oneid', __name__, url_prefix="/oneid")
        @oneid.route('/get_user_data')
        def get_user_data():
            token = session['oneid_access_token']
            url = self.__oneid_url__ + "?grant_type=one_access_token_identify&client_id=%s&client_secret=%s&access_token=%s&scope=%s"%(self.__client_id__, self.__client_secret__, token, self.__client_id__)
            x = requests.post(url)
            data = x.text
            data = json.loads(data)
            params = "?"
            for key, value in data.items():
                self.__one_id_keys.append(key)
                if type(value) == str:
                    params += key + "=" + value + "&"
                elif type(value) == list:
                    for item in value:
                        params += key + "=" + item + "&"
            return redirect(self.__callback_url+params)
        @oneid.route('/auth', methods=['GET'])
        def oneid_auth():
            code = request.args.get('code')
            self.__oneid_authorize__ = self.__oneid_url__ + "?grant_type=one_authorization_code&client_id=%s&client_secret=%s&redirect_uri=%s&code=%s"%(self.__client_id__,self.__client_secret__,self.__redirect__,code)
            x = requests.post(self.__oneid_authorize__)
            data = x.json()
            session['oneid_access_token'] = data['access_token']
            self.__redirect__ = request.host_url + "oneid/get_user_data"
            return redirect(self.__redirect__)
        @oneid.route('/login', methods=['GET'])
        def oneid_login():
            self.__redirect__ = request.host_url + "oneid/auth"
            self.__one_code__ = self.__oneid_url__ + "?response_type=one_code&client_id=%s&redirect_uri=%s&scope=%s&state=IDWP"%(self.__client_id__, self.__redirect__,self.__client_id__)
            url = self.__one_code__
            return redirect(url)
        app.register_blueprint(oneid)
    def Params_To_Dict(self, args) -> dict:
        """Converts a list of query parameters to a dictionary.

        Args:
            args (flask.request.args): flask.request.args

        Returns:
            dict: Dictionary of query parameters
        """        
        data = {}
        for key in self.__one_id_keys:
            val = args.get(key) 
            data[key] = val
        return data
    def Set_Callback(self, callback_url):
        """Set callback url for OneID.
        Args:
            callback_url (string): Callback url for redirect with data from OneID
        """        
        self.__callback_url = callback_url
    @property
    def oneid_login(self):
        return self.ONEID_LOGIN_URL
    

    