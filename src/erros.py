class usuario_existente(Exception):
    def __init__(self, message="O usuário já possui uma conta"):
        self.__message = message
        super().__init__(self.__message)
        
class usuario_ou_senha_incorretos(Exception):
    def __init__(self, message="Usuário ou senha incorretos"):
        self.__message = message
        super().__init__(self.__message)

class usuario_inexistente(Exception):
    def __init__(self, message="O usuário não existe!"):
        self.__message = message
        super().__init__(self.__message)

class dinheiro_insuficiente(Exception):
    def __init__(self, message="Dinheiro insuficiente"):
        self.__message = message
        super().__init__(self.__message)