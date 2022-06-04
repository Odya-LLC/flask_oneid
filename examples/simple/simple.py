from flask_oneid import OneID
from flask import Flask, request, redirect, jsonify, url_for, session
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
        print(data)
        return redirect(url_for('index'))
    
    with app.test_request_context():
        oneid.Set_Callback(url_for('params'))
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)