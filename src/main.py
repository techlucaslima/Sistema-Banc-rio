import user
import pessoa
from os import system
from time import sleep

tempo_sleep = 2
tempo_sleep_info = 5

# Função para o menu de Transação, Depósito e Saque
def menu_principal(cpf: str, isRegister = False):
    system('cls')

    # instância da classe pessoa
    usr = None
    if isRegister:
        usr = pessoa.pessoa(cpf, 0)
    else:
        usr = pessoa.pessoa(cpf, 0)
        usr.atualizar_dados()

    while True:
        try:
            system('cls')
            # Introdução e escolha entre transação, depósito e saque
            escolha = int(input('''------Bem-vindo-ao-caixa-eletrônico-Bahia!------
Por favor escolha entre realizar uma transação, um depósito ou um saque em nosso aplicativo:
[1] Transação
[2] Ver saldo
[3] Depósito
[4] Saque
[5] Sair
'''))
        
            # Verifica se foi digitado algo diferente do que foi pedido
            if escolha not in [1, 2, 3, 4, 5]:
                system('cls')
                print("Erro, tente novamente: ")
                sleep(tempo_sleep)
                continue
            

            # Verifica se quer fazer transação
            if escolha == 1:
                while True:
                    try:
                        system('cls')
                        quantia = float(input('Digite a quantia que você quer fazer a transação ("-1" para voltar): '))

                        if quantia < 0:
                            break

                        cpf_outroUsuario = input('Digite o CPF da pessoa que quer fazer a transação ("-1" para sair): ')
                        cpf_outroUsuario = cpf_outroUsuario.strip().replace(" ", "")

                        if cpf_outroUsuario == "-1":
                            continue

                        # Verificação para garantir que o CPF tenha apenas números e exatamente 11 dígitos
                        if len(cpf_outroUsuario) != 11 or not cpf_outroUsuario.isdigit():
                            system('cls')
                            print("Erro! CPF inválido, digite novamente.")
                            sleep(tempo_sleep)
                            continue
                    
                    except ValueError:
                        system('cls')
                        print("Erro na digitalização, tente novamente. ")
                        sleep(tempo_sleep)

                    except Exception:
                        system('cls')
                        print("Erro na digitalização, tente novamente. ")
                        sleep(tempo_sleep)
                    
                    else:
                        try: 
                            usr.transacao(quantia, cpf_outroUsuario)
                            print(f"Uma transação de R${quantia} foi feita no cpf {cpf_outroUsuario}! ")
                            sleep(tempo_sleep_info)
                        except Exception as e:
                            system('cls')
                            print(e)
                            sleep(tempo_sleep)

            # Verifica se quer ver o saldo
            elif escolha == 2:
                system('cls')
                print('saldo: R$' + str(usr.mostrar_saldo()))
                sleep(tempo_sleep_info)

            
            # Verifica se quer fazer depósito
            elif escolha == 3:
                while True:
                    try:
                        system('cls')
                        quantia = float(input('Digite a quantia que você quer fazer o depósito ("-1" para voltar): '))

                        if quantia < 0:
                            break
                    
                    except ValueError:
                        system('cls')
                        print("Erro na digitalização, tente novamente. ")
                        sleep(tempo_sleep)

                    except Exception:
                        system('cls')
                        print("Erro na digitalização, tente novamente. ")
                        sleep(tempo_sleep)
                    
                    else:
                        usr.depositar(quantia)
                        print(f"Um depósito de R${quantia} foi feita na sua conta! ")
                        sleep(tempo_sleep_info)
                        break

            
            # Verifica se quer fazer o saque
            elif escolha == 4:
                while True:
                    try:
                        system('cls')
                        quantia = float(input('Digite a quantia que você quer fazer o saque ("-1" para voltar): '))

                        if quantia < 0:
                            break

                    except ValueError:
                        system('cls')
                        print("Erro na digitalização, tente novamente. ")
                        sleep(tempo_sleep)

                    except Exception:
                        system('cls')
                        print("Erro na digitalização, tente novamnete. ")
                        sleep(tempo_sleep)
                    
                    else:
                        try:
                            usr.sacar(quantia)
                            print(f"Foi realizado o saque, debitando da sua conta a quantia de R${quantia}! ")
                            sleep(tempo_sleep_info)
                        except Exception as e:
                            system('cls')
                            print(e)
                            sleep(tempo_sleep)

            # Verifica se quer encerrar o sistema
            elif escolha == 5:
                system('cls')
                print("Obrigado por usar o nosso sistema, até mais! ")
                sleep(tempo_sleep)
                exit()
                return
        
        except ValueError:
            system('cls')
            print("Escolha inválida, tente novamente! ")
            sleep(tempo_sleep)

        except Exception:
            system('cls')
            print("Escolha inválida, tente novamente! ")
            sleep(tempo_sleep)



# Função para adquirir os valores necessários para realizar o registro
def registrar():
    cpf_global = ""
    senha_global = ""

    # Repetição para garantir a digitação correta do CPF
    while True:
        try:
            system('cls')
            print("Para a realização do registro, dê as seguintes informações: ")

            cpf = input('''Digite o seu CPF (sem pontos e traços, contendo 11 dígitos): 
["sair" para voltar ao menu]
R: ''').strip().replace(" ", "")

            # Verificação caso o usuário deseje fechar o registro
            if cpf.lower() == "sair":
                menu_inicial()
                break

            # Verificação para garantir que o CPF tenha apenas números e exatamente 11 dígitos
            if len(cpf) != 11 or not cpf.isdigit():
                system('cls')
                print("Erro! CPF inválido, digite novamente.")
                sleep(tempo_sleep)
                continue

        except ValueError:
            system('cls')
            print("Erro! CPF inválido, digite novamente.")
            sleep(tempo_sleep)

        except Exception:
            system('cls')
            print("Erro inesperado! CPF inválido, digite novamente.")
            sleep(tempo_sleep)

        else:
            print(f"CPF digitado: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
            
            try:
                usr = user.user()
                usr.verificar_usuario_existente(cpf)
                cpf_global = cpf
                break
            except Exception as e:
                system('cls')
                print(e)
                sleep(tempo_sleep)

    # Repetição para garantir a digitação correta da senha
    while True:
        try:
            system('cls')
            senha = input("Digite uma senha para a sua conta: ").strip()

            # Verificação para que a senha tenha, no mínimo, 8 caracteres
            if len(senha) < 8:
                system('cls')
                print("Erro! Sua senha deve ter, no mínimo, 8 dígitos.")
                sleep(tempo_sleep)
                continue

            # Verificação para que a senha tenha, no mínimo, 1 letra maiúscula
            if not any(d.isupper() for d in senha):
                system('cls')
                print("Erro! Sua senha deve ter, no mínimo, uma letra maiúscula.")
                sleep(tempo_sleep)
                continue

            # Verificação para que a senha tenha, no mínimo, 1 letra minúscula
            if not any(d.islower() for d in senha):
                system('cls')
                print("Erro! Sua senha deve ter, no mínimo, uma letra minúscula.")
                sleep(tempo_sleep)
                continue

            # Verificação de confirmação da senha
            confirmar_senha = input("Digite a senha novamente para confirmar: ").strip()

            if confirmar_senha != senha:
                system('cls')
                print("Erro! Confirmação da senha não corresponde à digitada anteriormente, digite novamente.")
                sleep(tempo_sleep)
                continue

        except ValueError:
            system('cls')
            print("Erro! Senha inválida, digite novamente.")
            sleep(tempo_sleep)

        except Exception:
            system('cls')
            print("Erro inesperado! Senha inválida, digite novamente.")
            sleep(tempo_sleep)

        else:
            print(f"Senha cadastrada com sucesso! ")

            senha_global = senha
            usr = user.user()
            usr.registrar(cpf_global, senha_global)
            menu_principal(cpf, True)
            break
        

# Função para adquirir os valores necessários para realizar o login
def login():
    cpf_global = ""
    senha_global = ""

    print("Para realizar o seu login, nos dê algumas informações: ")

    # While para pegar o CPF do usuário
    while True:
        try:
            system('cls')
            cpf = input('''Digite o seu CPF (sem pontos e traços, contendo 11 dígitos):
["sair" para voltar ao menu]
R: ''').strip().replace(" ", "")

            if cpf.lower() == "sair":
                menu_inicial()
                return  # Sai da função para evitar que continue executando

            # Verificação para garantir que o CPF tenha apenas números e exatamente 11 dígitos
            if not cpf.isdigit() or len(cpf) != 11:
                system('cls')
                print("Erro! CPF inválido, digite novamente.")
                sleep(tempo_sleep)
                continue

        except ValueError:
            system('cls')
            print("Erro! CPF inválido, digite novamente.")
            sleep(tempo_sleep)

        except Exception:
            system('cls')
            print("Erro inesperado! CPF inválido, digite novamente.")
            sleep(tempo_sleep)

        else:
            print(f"CPF digitado: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")

            try:
                usr = user.user()
                usr.verificar_usuario_inexistente(cpf)
                cpf_global = cpf
                break
            except Exception as e:
                system('cls')
                print(e)
                sleep(tempo_sleep)

    # Repetição para garantir a digitação correta da senha
    while True:
        try:
            system('cls')
            senha = input("Digite a senha da sua conta: ").strip()

            # Verificação para que a senha tenha, no mínimo, 8 caracteres
            if len(senha) < 8:
                system('cls')
                print("Erro! Senha incorreta.")
                sleep(tempo_sleep)
                continue

            # Verificação para que a senha tenha, no mínimo, 1 letra maiúscula
            if not any(d.isupper() for d in senha):
                system('cls')
                print("Erro! Senha incorreta.")
                sleep(tempo_sleep)
                continue

            # Verificação para que a senha tenha, no mínimo, 1 letra minúscula
            if not any(d.islower() for d in senha):
                system('cls')
                print("Erro! Senha incorreta.")
                sleep(tempo_sleep)
                continue

        except ValueError:
            system('cls')
            print("Erro! Senha incorreta.")
            sleep(tempo_sleep)

        except Exception:
            system('cls')
            print("Erro inesperado! Senha incorreta.")
            sleep(tempo_sleep)

        else:
            try:
                senha_global = senha
                usr = user.user()
                usr.logar(cpf_global, senha_global)
                menu_principal(cpf_global)
            except Exception as e:
                system('cls')
                print(e)   
                sleep(tempo_sleep)        

# Função para o menu de registrar e login
def menu_inicial():
    while True:
        try:
            system('cls')

            # Introdução e escolha entre registro e login
            escolha = int(input('''------Bem-vindo-ao-caixa-eletrônico-Bahia!------
Por favor escolha entre realizar um login ou o registro em nosso caixa:
[1] Registrar
[2] Login
'''))
            
            # Verifica se a escolha está nos requisitos
            if not escolha in [1, 2]:
                system('cls')
                print("Erro, tente novamente: ")
                sleep(tempo_sleep)
                continue
            
            # Chama as respectivas funções
            else:
                if escolha == 1:
                    registrar()
                
                if escolha == 2:
                    login()

        except ValueError:
            system('cls')
            print("Erro! Tente novamente: ")
            sleep(tempo_sleep)

        except Exception:
            system('cls')
            print("Erro! Tente novamente: ")
            sleep(tempo_sleep)


if __name__ == "__main__":
    menu_inicial()
