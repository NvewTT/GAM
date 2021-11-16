from flask import Flask
from flask_restful import Resource, Api
from ConsultaDB import *

app = Flask(__name__)
api = Api(app)


class CriarUsuario(Resource):
    def get(self, usuario, senha):
        return insereUsuario(usuario, senha)


class ValidacaoLogin(Resource):
    def get(self, usuario, senha):
        return validacaoUsuario(usuario, senha)


api.add_resource(CriarUsuario, '/criarUsuario/<string:usuario>:<string:senha>')
api.add_resource(ValidacaoLogin, '/login/<string:usuario>:<string:senha>')
if __name__ == '__main__':
    app.run(debug=True)
