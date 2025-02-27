class senhas_nao_iguais(Exception):
    def __init__(self, message="As senhas estão diferentes"):
        self.__message = message
        super().__init__(self.__message)

class usuario_existente(Exception):
    def __init__(self, message="O usuário já possui uma conta"):
        self.__message = message
        super().__init__(self.__message)
        
class usuario_inexistente(Exception):
    def __init__(self, message="usuário ou senha incorretos"):
        self.__message = message
        super().__init__(self.__message)