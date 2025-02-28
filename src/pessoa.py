class pessoa:
    def __init__(self, saldo, cpf):
        self.__saldo = saldo
        self.__cpf = cpf
    
    def depositar(self, quantia):
        self.__saldo += quantia

    def transacao(self, quantia, saldo_conta2):
        self.__saldo -= quantia
        saldo_conta2 += quantia
    
    def sacar(self, quantia):
        self.__saldo -= quantia
    
    def mostrar_saldo(self):
        return self.__saldo