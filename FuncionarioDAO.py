from flask_restful import Resource

# Criar os endpoints de Funcionario: GET, POST, PUT, DELETE

class Funcionario(Resource):

    def get(self, id):
        return {"msg": "GET Funcionario executado"}, 200

    def post(self, id):
        return {"msg": "POST Funcionario executado"}, 201

    def put(self, id):
        return {"msg": "PUT Funcionario executado"}, 200

    def delete(self, id):
        return {"msg": "DELETE Funcionario executado"}, 200