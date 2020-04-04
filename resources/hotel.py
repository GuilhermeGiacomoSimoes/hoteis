from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'alpha hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de janeiro'
    },

    {
        'hotel_id': 'bravo',
        'nome': 'bravo hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Florianópolis'
    },

    {
        'hotel_id': 'charlie',
        'nome': 'charlie hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Florianópolis'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [Hotel.json() for in HotelModel.query.all()]}

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            return hotel.json()
        
        return {'message': 'Hotel not found'}, 404 #not found

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400
        
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200 #editado

        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()

        return hotel.json(), 201 #criado

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel: 
            hotel.delete_hotel()
            return {'messages': 'Hotel delete'}
        else:
            return {'message':'hotel not found'}, 404