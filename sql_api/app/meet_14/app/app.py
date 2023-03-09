from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
rest_app = Api(app=app)

main_space = rest_app.namespace('main', description="main")
user_id_space = rest_app.namespace('user', description="Get User's Data by ID")
users_space = rest_app.namespace('users', description="Get All User's Data")


users = [
    {
        "id": 1,
        "username": "userpertama",
        "firstname": "rudi",
        "lastname": "roundhouse",
        "email": "rudi.roundhouse@gmail.com"
    },
    {
        "id": 2,
        "username": "userkedua",
        "firstname": "shiroe",
        "lastname": "ishigami",
        "email": "shiroe.ishigami@gmail.com"
    },
    {
        "id": 3,
        "username": "userketiga",
        "firstname": "akatsuki",
        "lastname": "horizon",
        "email": "akatsuki.horizon@gmail.com"
    }
]

def search_user_by_id(id):
    for user in users:
        if user['id'] == (int(id)):
            return user
        
def search_users():
    return users


@main_space.route('/')
class MainClass(Resource):
    def get(self):
        return {
            'Ihsan API' : 'Welcome to Ihsan API'
        }

@user_id_space.route('/<id>')
class MainClass(Resource):
    def get(self, id):
        return search_user_by_id(id)
    
@users_space.route('/')
class MainClass(Resource):
    def get(self):
        return {
            'result' : search_users()
        }

# @app.route('/user/<id>', methods=['GET'])
# def search_user(id):
#     return search_user_by_id(id)

# @app.route('/trainer/', methods=["GET"])
# def trainer():
#     return 'Halo nama saya trainer'


if __name__ == "__main__":
    app.run(debug=True)