import mysql.connector
from mysql.connector import errorcode

def resultados(status, sucesso):
    return {
        'status': status,
        'sucesso': sucesso
        }

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
        return resultados(status,False)
    status = "Usuario inserido com sucesso"
    return resultados(status,True)

def validacaoUsuario(usuario,senha):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="gamdb"
        )

    mycursor = mydb.cursor()

    sql = "SELECT CASE WHEN EXISTS  (SELECT * FROM `usuarios` WHERE Usuario = %s AND Senha = %s)THEN '1' ELSE '0' END"
    val = (usuario, senha)
    mycursor.execute(sql, val)
    resultado = mycursor.fetchone()
    if resultado[0] == '1':
        return resultados("usuário existe no banco de dados", True)
    return resultados("usuário não existe no banco de dados", False)

