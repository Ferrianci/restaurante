def atv ():
    lista = []
    conta_cliente = []
    conta = 0
    while True:
        print("*** Serviço Restaurante ***")
        print("*** 1-Cadastro ***")
        print("*** 2-Cardápio ***")
        print("*** 3-Consultar cadastro ***")
        print("*** 4-Consultar Conta do cliente ***")
        print("*** 5-Excluir *** ")
        print("*** 6-sair ***")
        print("-----------------------------")
        resposta = int(input("Digite a opção desejada: "))

        if resposta == 1:
            print("-----------------------------")
            lista.append (input("digite o número da mesa: "))
            print("-----------------------------")
            lista.append (input("Digite o nome do cliente: "))
            print("-----------------------------")

        elif resposta == 2:
            while True:
                print("*** Cardápio ***")
                print("1-Prato 1 = R$25,00")
                print("2-Prato 2 = R$50,00")
                print("3-Prato 3 = R$37,00")
                print("4-Promoção da semana = R$28,00")
                print("5-Finalizar compra")    
                print("-----------------------------")
                prato = int(input("Digite a opção desejada: "))
                print("-----------------------------")
                if prato == 1:
                    conta = conta + 25
                    conta_cliente.append(prato)
                elif prato == 2:
                    conta = conta + 50
                    conta_cliente.append(prato)
                elif prato == 3:
                    conta = conta + 37
                    conta_cliente.append(prato)
                elif prato == 4:
                    conta = conta + 28
                    conta_cliente.append(prato)
                elif prato == 5:
                    break

        elif resposta == 3:
            print("-----------------------------")
            print (lista)

        elif resposta == 4:
            print("-----------------------------")
            print ("A conta do cliente é: R${0}".format(conta))
            print(conta_cliente)
            print("-----------------------------")
            
        elif resposta == 5:
            print("-----------------------------")
            busca = input("Digite o nome p/ excluir: ")
            lista.remove(busca)       

        elif resposta == 6:
            break
                
                
            

    
