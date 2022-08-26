from flask_restful import Resource

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE

class Cliente(Resource):

    def get(self, id):
        return {"msg": "GET Cliente executado"}, 200

    def post(self, id):
        return {"msg": "POST Cliente executado"}, 201

    def put(self, id):
        return {"msg": "PUT Cliente executado"}, 200

    def delete(self, id):
        return {"msg": "DELETE Cliente executado"}, 200