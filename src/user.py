import json
from erros import senhas_nao_iguais, usuario_existente, usuario_ou_senha_incorretos

class user:
    def registrar(self, cpf: str, senha: str):
        with open("../bd/users.json", "r", encoding="utf-8") as users_file:
            info = json.load(users_file)
                
        if not cpf in info:
            info[cpf] = {"senha": senha,
                        "saldo": 0}
        else:
            raise usuario_existente
                
        with open("bd/users.json", "w", encoding="utf-8") as users_file:
            json.dump(info, users_file, ensure_ascii=False, indent=4)
                
        with open("user_logged.json", "w", encoding="utf-8") as users_file:
            json.dump(info[cpf], users_file, ensure_ascii=False, indent=4)
                
    def logar(self, cpf: str, senha: str):
        with open("bd/users.json", "r", encoding="utf-8") as users_file:
            info = json.load(users_file)
            
        if cpf in info:
            if info[cpf]["senha"] == senha:
                with open("user_logged.json", "w", encoding="utf-8") as users_file:
                    json.dump(info, users_file, ensure_ascii=False, indent=4)
            else:
                raise usuario_ou_senha_incorretos
        else:
            raise usuario_ou_senha_incorretos
            