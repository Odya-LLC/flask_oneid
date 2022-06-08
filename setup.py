"""
Flask-OneID
-------------

This is the description for that library
"""
from setuptools import setup

long_description = """
# Flask-OneID

![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/Odya-LLC/flask_oneid/OneID%20test/main)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Odya-LLC/flask_oneid)
![GitHub top language](https://img.shields.io/github/languages/top/Odya-LLC/flask_oneid)
![GitHub](https://img.shields.io/github/license/Odya-LLC/flask_oneid)
> Only for Uzbekistan

OneID integration for Flask application

## Links

* [About OneID](https://id.egov.uz/)
* [Examples](https://github.com/Odya-LLC/flask_oneid/tree/main/examples)

## How it Works

### Install 

```
pip install Flask-OneID
```

### Add your credentials from OneID to config file

```python
ONEID_LOGIN = "your login"
ONEID_PASSWORD = "your pasword"
ONEID_URL = "url from OneID" # defaul https://sso.egov.uz/sso/oauth/Authorization.do 

```

### Create Flask App With OneID 

```python
from flask_oneid import OneID
from flask import *
def create_app():
    oneid = OneID()
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    oneid.init_app(app)
    
    @app.route("/", methods=['GET'])
    def index():
        return "Hello World"
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

### Add route to catch data from OneId

```python
@app.route("/params", methods=['GET'])
def params():
    print(request.args)
    return redirect(url_for('index'))

```

### Use builtin function to convert request args to dict 

```python
@app.route("/params", methods=['GET'])
def params():
    data = oneid.Params_To_Dict(request.args)
    print(data)
    return redirect(url_for('index'))

```

### Register your Callback Url for OneID module

```python
with app.test_request_context():
    oneid.Set_Callback(url_for('params'))
```

### Full Code 

```python
from flask_oneid import OneID
from flask import *
def create_app():
    oneid = OneID()
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    oneid.init_app(app)
    
    @app.route("/", methods=['GET'])
    def index():
        return "Hello World"
    @app.route("/params", methods=['GET'])
    def params():
        data = oneid.Params_To_Dict(request.args)
        return jsonify(data)
    
    with app.test_request_context():
        oneid.Set_Callback(url_for('params'))
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

```

### OneID route

After run app go to route `/oneid/login` to login oneid and get data about user 

### Return data

Example of data in callback

```json
{
    "_pport_expr_date": "",
    "_pport_issue_date": "",
    "birth_date": "",
    "birth_place": "",
    "ctzn": "",
    "email": "",
    "first_name": "",
    "full_name": "",
    "gd": "",
    "legal_info": null,
    "mid_name": "",
    "mob_phone_no": "",
    "natn": "",
    "per_adr": "",
    "pin": "",
    "pport_expr_date": "",
    "pport_issue_date": "",
    "pport_issue_place": "",
    "pport_no": "",
    "ret_cd": "",
    "sess_id": "",
    "sur_name": "",
    "tin": "",
    "user_id": "",
    "user_type": "",
    "valid": ""
}

```

U can use it to create user and login with Flask-Admin

## License

This project is licensed under the MIT License (see the `LICENSE` file for details).


"""

setup(
    name='Flask-OneID',
    version='1.0.3',
    url='https://github.com/Odya-LLC/flask_oneid',
    license='MIT',
    author='odya',
    author_email='support@odya.uz',
    description='OneID integration with Flask application, (only for Uzbekistan)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['flask_oneid'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',"requests"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)