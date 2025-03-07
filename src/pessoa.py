import json
import os
from erros import dinheiro_insuficiente, usuario_inexistente

class pessoa:
    def __init__(self, cpf: str, saldo: float):
        self.__saldo = saldo
        self.__cpf = cpf

    def atualizar_dados(self) -> float:
        basedir = os.path.abspath(os.path.dirname(__file__))

        with open("_internal/users.json", "r", encoding="utf-8") as users_file:
            info = json.load(users_file)

        self.__saldo = info[self.__cpf]["saldo"]

    def depositar(self, quantia: float):
        self.__saldo += quantia

        basedir = os.path.abspath(os.path.dirname(__file__))

        with open("_internal/users.json", "r", encoding="utf-8") as users_file:
                info = json.load(users_file)

        info[self.__cpf]["saldo"] += quantia

        with open("_internal/users.json", "w", encoding="utf-8") as users_file:
            json.dump(info, users_file, ensure_ascii=False, indent=4)

    def transacao(self, quantia: float, cpf_conta_2: str):  
        if quantia < self.__saldo:
            self.__saldo -= quantia

            basedir = os.path.abspath(os.path.dirname(__file__))

            with open("_internal/users.json", "r", encoding="utf-8") as users_file:
                info = json.load(users_file)

            if cpf_conta_2 in info:
                info[cpf_conta_2]["saldo"] += quantia
                info[self.__cpf]["saldo"] -= quantia

                with open("_internal/users.json", "w", encoding="utf-8") as users_file:
                    json.dump(info, users_file, ensure_ascii=False, indent=4)
            else:
                raise usuario_inexistente
        else:
            raise dinheiro_insuficiente
    
    def sacar(self, quantia: float):
        if quantia <= self.__saldo:
            self.__saldo -= quantia

            basedir = os.path.abspath(os.path.dirname(__file__))

            with open("_internal/users.json", "r", encoding="utf-8") as users_file:
                info = json.load(users_file)

            info[self.__cpf]["saldo"] -= quantia

            with open("_internal/users.json", "w", encoding="utf-8") as users_file:
                    json.dump(info, users_file, ensure_ascii=False, indent=4)
        else:
            raise dinheiro_insuficiente
                
    def mostrar_saldo(self):
        return self.__saldo