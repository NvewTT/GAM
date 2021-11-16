import mysql.connector
from mysql.connector import errorcode


def insereUsuario(usuario: str, senha: str):
    status = ""
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="gamdb"
        )

    mycursor = mydb.cursor()

    sql = "INSERT INTO usuarios(Usuario, Senha) VALUES (%s, %s)"
    val = (usuario, senha)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.IntegrityError as error:
        status = error.msg
        return {
            'status': status,
            'sucesso': False
            }
    status = "Usuario inserido com sucesso"
    return {
        'status': status,
        'sucesso': True
        }

