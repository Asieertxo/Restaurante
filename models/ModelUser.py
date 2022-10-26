from .entities.User import User


class ModelUser():

    @classmethod #para no tener que instanciar
    def login(self, mysql, user):
        try:
            conn = mysql.connection.cursor()
            sql = "SELECT * FROM user WHERE name = '{}'".format(user.name)
            conn.execute(sql)
            row = conn.fetchone()

            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password))#llamada a funcion para comprobar pass # crear objeto user pasandolo los parametros necesarios, User.py __init__
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_id(self, mysql, id):
        try:
            conn = mysql.connection.cursor()
            sql = "SELECT id, name FROM user WHERE id = {}".format(id)
            conn.execute(sql)
            row = conn.fetchone()
            if row != None:
                return User(row[0], row[1], None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)