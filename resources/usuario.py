from flask_restful import Resource, reqparse
from models.usuario import UserModel

class User(Resource):
    
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        
        if user:
            return user.json()
        
        return {'message': 'User not found'}, 404 #not found

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        
        try:
            if user: 
                user.delete_user()
                return {'messages': 'User delete'}
            else:
                return {'message':'user not found'}, 404
        except:
            return {'message':'An internal error'}, 500
    

class UserRegister(Resource):
    # /cadastro
    def post(sefl):
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help="The field login cannot be left blank")
        atributos.add_argument('senha', type=str, required=True, help="The field senha cannot be left blank")
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message": "The login '{}' already exists".format(dados['login'])}
        
        user = UserModel(**dados)
        user.save_user()

        return {'message': 'user creating successfully!'}, 201 #Creating