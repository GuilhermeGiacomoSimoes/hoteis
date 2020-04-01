from sql_alchemy import banco

class HotelModel(banco.Model):
    __tablename__ = 'hoteis' 

    hotel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String)
    estrelas = banco.Column(banco.Float(precision = 1))
    diaria = banco.Column(banco.Float(precision = 2))
    cidade = banco.Column(banco.String)

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome' : self.nome,
            'estrelas': self.estrelas,
            'daria': self.diaria,
            'cidade': self.cidade
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()  # select *from hoteis where hotel_id = x limit 1
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()

    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        