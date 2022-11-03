from .entities.User import User


class ModelUser():

    @classmethod #para no tener que instanciar
    def login(self, mysql, user):
        try:
            conn = mysql.connection.cursor()
            sql = "SELECT id, pass FROM users WHERE nombre = '{}'".format(user.nombre)
            conn.execute(sql)
            row = conn.fetchone()

            if row != None:
                user = User(row[0], None, None, None, None, None, None, User.check_password(row[1], user.password))#llamada a funcion para comprobar pass # crear objeto user pasandolo los parametros necesarios, User.py __init__
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_id(self, mysql, id):
        try:
            conn = mysql.connection.cursor()
            sql = "SELECT * FROM users WHERE id = {}".format(id)
            conn.execute(sql)
            row = conn.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)