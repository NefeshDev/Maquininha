def menu():              
    print("COMPRAS E SEUS DESCONTOS")
    print("="*20)
    print("Tipo da Compra: ")
    print("1- À vista")
    print("2- Crédito")
    print("3- Debito")
    print("4- Sair")


def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite apenas números!")
def ler_valor():
    while True:
        valor = float(input("VALOR A SER PROCESSADO(R$): "))

        if valor > 0:
            return valor

        print("Valor deve ser maior que zero!")
def ler_sn(msg):
    while True:
        resposta = input(msg).lower().strip()

        if resposta in ("s", "n"):
            return resposta

        print("Digite apenas 's' ou 'n'.")

def resumo_pagamento(forma_pagamento, valor, status):
    print("\n===== RESUMO =====")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Status: {status}")
    print("==================")

def avista():
    print("1- Pix")
    print("2- Cartão")
    print ("3- Dinheiro em Espécie")
    vistaOpcoes = int(input ("Qual será a forma de prosseguir? ->"))
    while True: 
        if vistaOpcoes == 1:
            valorFinalPix = ler_valor()
            if valorFinalPix < 1:
                print("Valor indisponível para ser repassado: ")
            else:
                print("QR Code gerado com sucesso!!!")
                print(f"Valor final: R$ {valorFinalPix:.2f}")
                print("AGUARDANDO PAGAMENTO...")
                retornoPix = ler_sn(input("Compra realizado com sucesso? s/n"))
                if retornoPix == "s".lower():
                    print("Compra finalizada com Sucesso!!!")
                    resumo_pagamento("PIX", valorFinalPix, "Aprovado")
                else:
                    print("Compra cancelada!!!")
            print("Deseja realizar outra compra? s/n")
            retornoMenuPix = ler_sn(input("->"))
            if retornoMenuPix == "s":
                print("Retornando ao menu inicial...")
                break
            else:
                print("Finalizando o programa...")
                exit()
        if vistaOpcoes == 2:

            valorFinalCartao = float(input("VALOR A SER PROCESSADO(R$): "))
            if valorFinalCartao < 1:
                print("Valor indisponível para ser repassado: ")
            else:
                debitoOpcoes = int(input("1- Débito\n2- Crédito\nQual será a forma de prosseguir? ->"))

                if debitoOpcoes == 1:
                    print("Compra realizada com sucesso no cartão de débito!!!")
                    print("Compra finalizada com Sucesso!!!")
                    resumo_pagamento("Débito", valorFinalCartao, "Aprovado")
                elif debitoOpcoes == 2:
                    print("Compra realizada com sucesso no cartão de crédito!!!")
                    print("Compra finalizada com Sucesso!!!")
                    resumo_pagamento("Crédito", valorFinalCartao, "Aprovado")
                    print("Opção inválida. Finalizando o programa...")
                    exit()
                print("Compra realizada confirmada com sucesso!!!")

            print("Deseja realizar outra compra? s/n")
            retornoMenuCartao = ler_sn(input("->")).lower()
            if retornoMenuCartao == "s":
                print("Retornando ao menu inicial...")
                break
            else:
                print("Finalizando o programa...")
                exit()
        if vistaOpcoes == 3:
                valorFinalDinheiro = float(input("VALOR A SER PROCESSADO(R$): "))
                if valorFinalDinheiro < 1:
                    print("Valor indisponível para ser repassado: ")
                else:
                    print("Compra realizada com sucesso em dinheiro!!!")
                    resumo_pagamento("Dinheiro em Espécie", valorFinalDinheiro, "Aprovado")
                print("Deseja realizar outra compra? s/n")
                retornoMenuDinheiro = ler_sn(input("->")).lower()
                if retornoMenuDinheiro == "s":
                    print("Retornando ao menu inicial...")
                    break
                else:
                    print("Finalizando o programa...")
                    exit()
def credito():
    print("1- Cartão de Crédito")
    print("2- Boleto Bancário")
    creditoOpcoes = int(input("Qual será a forma de prosseguir? ->"))
    while True:
            if creditoOpcoes == 1:

                valorFinalCredito = ler_valor()
                juros = valorFinalCredito * 0.05    #valor do juros de 5% para compras no cartão de crédito
                valorFinalCredito += juros          #atualiza o valor final da compra com o juros aplicado
                parcelas = int(input("Em quantas parcelas deseja dividir? ->")) #pergunta ao usuário em quantas parcelas deseja dividir a compra
                

                if valorFinalCredito <= 1:
                    print("Valor indisponível para ser repassado: ")

                elif parcelas < 1 or parcelas > 12:   #verifica se o número de parcelas é válido (entre 1 e 12)
                    print("Número de parcelas inválido. Coloque um número entre 1 e 12.")
                else:
                    print(f"Valor original da compra: {(valorFinalCredito - juros):.2f} R$")               #exibe o valor original da compra antes do juros ser aplicado
                    print(f"Valor do juros aplicado: {juros:.2f} R$")                                   #exibe o valor do juros aplicado
                    print(f"Valor das parcelas: {(valorFinalCredito / parcelas):.2f} R$")                             #exibe o valor de cada parcela
                    print(f"Compra no valor de {valorFinalCredito:.2f} R$ realizada com sucesso!!!")     #exibe o valor final da compra com o juros aplicado
                    resumo_pagamento("Crédito", valorFinalCredito, "Aprovado") #notinha de pagamento
                
                print("Deseja realizar outra compra? s/n")
                retornoMenuCredito = ler_sn(input("->")).lower()
                if retornoMenuCredito == "s":
                    print("Retornando ao menu inicial...")
                    break
                else:
                    print("Finalizando o programa...")
                    exit()
            if creditoOpcoes == 2:

                valorFinalBoleto = float(input("VALOR A SER PROCESSADO(R$): "))
                if valorFinalBoleto < 1:
                    print("Valor indisponível para ser repassado: ")
                else:
                    print("Boleto gerado com sucesso!!!")
                    resumo_pagamento("Boleto", valorFinalBoleto, "Gerado e Pronto para Pagamento") #notinha de pagamento

                print("Deseja realizar outra compra? s/n")

                retornoMenuBoleto = ler_sn(input("->")).lower()

                if retornoMenuBoleto == "s":
                    print("Retornando ao menu inicial...")
                    break
                else:
                    print("Finalizando o programa...")
                    exit()
def debito():
        print("1- Cartão de Débito")
        print("2- Transferência Bancária")
        debitoOpcoes = int(input("Qual será a forma de prosseguir? ->"))
        while True:
            if debitoOpcoes == 1:
                valorFinalDebito = ler_valor()
                if valorFinalDebito < 1:
                    print("Valor indisponível para ser repassado: ")
                else:
                    print("Compra realizada com sucesso!!!")
                    resumo_pagamento("Débito", valorFinalDebito, "Aprovado")
                print("Deseja realizar outra compra? s/n")
                retornoMenuDebito = ler_sn(input("->")).lower()
                if retornoMenuDebito == "s":
                    print("Retornando ao menu inicial...")
                    break
                else:
                    print("Finalizando o programa...")
                    exit()
            if debitoOpcoes == 2:
                valorFinalTransferencia = float(input("VALOR A SER PROCESSADO(R$): "))
                if valorFinalTransferencia < 1:
                    print("Valor indisponível para ser repassado: ")
                else:
                    print("Compra realizada com sucesso!!!")
                    resumo_pagamento("Transferencia Bancária", valorFinalTransferencia, "Pagamento Realizado") #notinha de pagamento
                print("Deseja realizar outra compra? s/n")
                retornoMenuTransferencia = ler_sn(input("->")).lower()
                if retornoMenuTransferencia == "s":
                    print("Retornando ao menu inicial...")
                    break
                else:
                    print("Finalizando o programa...")
                    exit()

while True:
    menu()
    tipoDaCompra = ler_inteiro(int(input("Qual o tipo da compra? ->")))
    if tipoDaCompra == 1:
        avista()
        
    elif tipoDaCompra == 2:
        credito()

    elif tipoDaCompra == 3:
        debito()
    elif tipoDaCompra == 4:
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")