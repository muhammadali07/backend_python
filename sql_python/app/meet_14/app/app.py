from flask import Flask
# from flask_restx import Api, Resources

app = Flask(__name__)
# rest_app = Api(app=app)


@app.route('/')
def index():
    return "Hello World"

@app.route('/nama/', methods=["GET"])
def nama():
    return 'Halo nama saya Ihsan Solusi Informatika'

@app.route('/trainer/', methods=["GET"])
def trainer():
    return 'Halo nama saya trainer'


if __name__ == "__main__":
    app.run(debug=True)