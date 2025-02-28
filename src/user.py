import json
import os
from erros import usuario_existente, usuario_ou_senha_incorretos

class user:
    def verificar_usuario_existente(self, cpf: str):
        basedir = os.path.abspath(os.path.dirname(__file__))

        with open(basedir + "\\..\\bd\\users.json", "r", encoding="utf-8") as users_file:
            info = json.load(users_file)

        if cpf in info:
            raise usuario_existente

    def registrar(self, cpf: str, senha: str):
        basedir = os.path.abspath(os.path.dirname(__file__))

        with open(basedir + "\\..\\bd\\users.json", "r", encoding="utf-8") as users_file:
            info = json.load(users_file)
                
        info[cpf] = {"senha": senha,
                    "saldo": 0}
                
        with open(basedir + "\\..\\bd\\users.json", "w", encoding="utf-8") as users_file:
            json.dump(info, users_file, ensure_ascii=False, indent=4)
                
    def logar(self, cpf: str, senha: str):
        basedir = os.path.abspath(os.path.dirname(__file__))
        
        with open(basedir + "\\..\\bd\\users.json", "r", encoding="utf-8") as users_file:
            info = json.load(users_file)
            
        if cpf in info:
            if info[cpf]["senha"] == senha:
                with open("user_logged.json", "w", encoding="utf-8") as users_file:
                    json.dump(info, users_file, ensure_ascii=False, indent=4)
            else:
                raise usuario_ou_senha_incorretos
        else:
            raise usuario_ou_senha_incorretos
            