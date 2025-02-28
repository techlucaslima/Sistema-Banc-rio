from pessoa import pessoa

# Função para adquirir os valores necessários para realizar o registro
def registrar():
    print("Para a realização do registro, dê as seguintes informações: ")

    # Repetição para garantir a digitação correta do CPF
    while True:
        try:
            cpf = input('''Digite o seu CPF (sem pontos e traços, contendo 11 dígitos): 
["sair" para voltar ao menu]
R: ''').strip().replace(" ", "")

            # Verificação caso o usuário deseje fechar o registro
            if cpf.lower() == "sair":
                menu_inicial()
                break

            # Verificação para garantir que o CPF tenha apenas números e exatamente 11 dígitos
            if len(cpf) != 11 or not cpf.isdigit():
                print("Erro! CPF inválido, digite novamente.")
                continue

        except ValueError:
            print("Erro! CPF inválido, digite novamente.")

        except Exception:
            print("Erro inesperado! CPF inválido, digite novamente.")

        else:
            print(f"CPF digitado: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
            break

    # Repetição para garantir a digitação correta da senha
    while True:
        try:
            senha = input("Digite uma senha para a sua conta: ").strip()

            # Verificação para que a senha tenha, no mínimo, 8 caracteres
            if len(senha) < 8:
                print("Erro! Sua senha deve ter, no mínimo, 8 dígitos.")
                continue

            # Verificação para que a senha tenha, no mínimo, 1 letra maiúscula
            if not any(d.isupper() for d in senha):
                print("Erro! Sua senha deve ter, no mínimo, uma letra maiúscula.")
                continue

            # Verificação para que a senha tenha, no mínimo, 1 letra minúscula
            if not any(d.islower() for d in senha):
                print("Erro! Sua senha deve ter, no mínimo, uma letra minúscula.")
                continue

            # Verificação de confirmação da senha
            confirmar_senha = input("Digite a senha novamente para confirmar: ").strip()

            if confirmar_senha != senha:
                print("Erro! Confirmação da senha não corresponde à digitada anteriormente, digite novamente.")
                continue

        except ValueError:
            print("Erro! Senha inválida, digite novamente.")

        except Exception:
            print("Erro inesperado! Senha inválida, digite novamente.")

        else:
            print(f"Senha cadastrada com sucesso! ")
            break
        


# Função para adquirir os valores necessários para realizar o login
def login():
    print("Para realizar o seu login, nos dê algumas informações: ")

    # While para pegar o CPF do usuário
    while True:
        try:
            cpf = input('''Digite o seu CPF (sem pontos e traços, contendo 11 dígitos):
["sair" para voltar ao menu]
R: ''').strip().replace(" ", "")

            if cpf.lower() == "sair":
                menu_inicial()
                return  # Sai da função para evitar que continue executando

            # Verificação para garantir que o CPF tenha apenas números e exatamente 11 dígitos
            if not cpf.isdigit() or len(cpf) != 11:
                print("Erro! CPF inválido, digite novamente.")
                continue

        except ValueError:
            print("Erro! CPF inválido, digite novamente.")

        except Exception:
            print("Erro inesperado! CPF inválido, digite novamente.")

        else:
            print(f"CPF digitado: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
            break

    # Repetição para garantir a digitação correta da senha
    while True:
        try:
            senha = input("Digite a senha da sua conta: ").strip()

            # Verificação para que a senha tenha, no mínimo, 8 caracteres
            if len(senha) < 8:
                print("Erro! Senha incorreta.")
                continue

            # Verificação para que a senha tenha, no mínimo, 1 letra maiúscula
            if not any(d.isupper() for d in senha):
                print("Erro! Senha incorreta.")
                continue

            # Verificação para que a senha tenha, no mínimo, 1 letra minúscula
            if not any(d.islower() for d in senha):
                print("Erro! Senha incorreta.")
                continue

            # Verificação de confirmação da senha
            confirmar_senha = input("Digite a senha novamente para confirmar: ").strip()

            if confirmar_senha != senha:
                print("Erro! Confirmação da senha não corresponde à digitada anteriormente, digite novamente.")
                continue

        except ValueError:
            print("Erro! Senha incorreta.")

        except Exception:
            print("Erro inesperado! Senha incorreta.")

        else:
            print("Senha confirmada com sucesso!")
            break



# Função para o menu de registrar e login
def menu_inicial():
    while True:
        try:
            # Introdução e escolha entre registro e login
            escolha = input('''------Bem-vindo-ao-caixa-eletrônico-Bahia!------
Por favor escolha entre realizar um login ou o registro em nosso aplicativo:
[1] Registrar
[2] Login
''')
            
            # 
            if escolha != '1' and escolha != '2':
                print("Erro, tente novamente: ")
                continue

            else:
                if escolha == 1:
                    registrar()
                
                if escolha == 2:
                    login()

        except ValueError:
            print("Erro! Tente novamente: ")

        except Exception:
            print("Erro! Tente novamente: ")

# Função para o menu de Transação, Depósito e Saque
def menu_principal(saldo, cpf):
    # instância da classe pessoa
    user = pessoa(saldo, cpf)

    while True:
        try:
            # Introdução e escolha entre transação, depósito e saque
            escolha = input('''------Bem-vindo-ao-caixa-eletrônico-Bahia!------
Por favor escolha entre realizar uma transação, um depósito ou um saque em nosso aplicativo:
[1] Transação
[2] Ver saldo
[3] Depósito
[4] Saque
[5] Sair
''')
        
            # Verifica se foi digitado algo diferente do que foi pedido
            if escolha < 1 or escolha > 5:
                print("Erro, tente novamente: ")
                continue
            
            if escolha == 1:
                while True:
                    try:
                        quantia = int(input('Digite a quantia que você quer fazer a transação ("1" para voltar): '))

                        if quantia == 1:
                            break

                        if quantia < saldo:
                            print("Você não tem dinheiro suficiente para realizar essa transação, escolha outro valor ou saia. ")
                            continue
                    
                    except ValueError:
                        print("Erro na digitalização, tente novamente. ")

                    except Exception:
                        print("Erro na digitalização, tente novamnete. ")
                    
                    else:
                        ...

            elif escolha == 2:
                user.mostrar_saldo()
            
            elif escolha == 3:
                user.depositar()
            
            elif escolha == 4:
                user.sacar()
            
            elif escolha == 5:
                print("Obrigado por usar o nosso sistema, até mais! ")
        
        except ValueError:
            print("Escolha inválida, tente novamente! ")

        except Exception:
            print("Escolha inválida, tente novamente! ")