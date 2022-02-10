id = 1
class Usuario:
    def __init__(self, name):
        global id
        self.name = name
        self.followers = 0
        self.following = 0
        self.id = id
        print(f"Nuevo usuario creandose, usuario {id}")
        id += 1
    def follow(self, user):
        self.following += 1
        user.followers += 1
    pass

name = input("Ingrese su nombre: ")
user = Usuario(name)

name = input("Ingrese su nombre: ")
user2 = Usuario(name)

user2.follow(user)

user2.report()