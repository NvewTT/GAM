from flask import Flask
from flask_restful import Resource, Api
from ConsultaDB import *
app = Flask(__name__)
api = Api(app)


class CriarUsuario(Resource):
    def get(self, usuario, senha):

        return insereUsuario(usuario,senha)


api.add_resource(CriarUsuario, '/criarUsuario/<string:usuario>:<string:senha>')

if __name__ == '__main__':
    app.run(debug=True)
