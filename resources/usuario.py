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
