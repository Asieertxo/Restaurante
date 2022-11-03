from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, nombre, apellido, email, nacimiento, registro, foto, password) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.nacimiento = nacimiento
        self.registro = registro
        self.foto = foto
        self.password = password

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

print(generate_password_hash("1234"))