def menu():
    # Criação das bombas com valores iniciais
    bomba_etanol = "BombaEtanol" (valor_litro=3.50, quantidade_disponivel=1000)
    bomba_gasolina = "BombaGasolina" (valor_litro=5.00, quantidade_disponivel=1000)
    
    while True:
        print("\n*** Menu de Abastecimento ***")
        print("1. Abastecer Etanol por Valor")
        print("2. Abastecer Etanol por Litro")
        print("3. Abastecer Gasolina por Valor")
        print("4. Abastecer Gasolina por Litro")
        print("5. Abastecer Gasolina com Aditivo por Valor")
        print("6. Abastecer Gasolina com Aditivo por Litro")
        print("7. Verificar Quantidade Disponível de Etanol")
        print("8. Verificar Quantidade Disponível de Gasolina")
        print("9. Sair")
        
        escolha = input("Escolha uma opção (1-9): ")
        
        if escolha == '1':
            valor = float(input("Informe o valor a ser abastecido: R$ "))
            litros = bomba_etanol.abastecer_por_valor(valor)
            if litros == -1:
                print("Não há quantidade suficiente de etanol para abastecer.")
            else:
                print(f"Abastecido {litros:.2f} litros de etanol.")
        
        elif escolha == '2':
            litros = float(input("Informe a quantidade de litros a ser abastecida: "))
            valor = bomba_etanol.abastecer_por_litro(litros)
            if valor == -1:
                print("Não há quantidade suficiente de etanol para abastecer.")
            else:
                print(f"Valor a pagar: R$ {valor:.2f}.")
        
        elif escolha == '3':
            valor = float(input("Informe o valor a ser abastecido: R$ "))
            litros = bomba_gasolina.abastecer_por_valor(valor)
            if litros == -1:
                print("Não há quantidade suficiente de gasolina para abastecer.")
            else:
                print(f"Abastecido {litros:.2f} litros de gasolina.")
        
        elif escolha == '4':
            litros = float(input("Informe a quantidade de litros a ser abastecida: "))
            valor = bomba_gasolina.abastecer_por_litro(litros)
            if valor == -1:
                print("Não há quantidade suficiente de gasolina para abastecer.")
            else:
                print(f"Valor a pagar: R$ {valor:.2f}.")
        
        elif escolha == '5':
            valor = float(input("Informe o valor a ser abastecido com aditivo: R$ "))
            litros = bomba_gasolina.abastecer_por_valor_com_aditivo(valor)
            if litros == -1:
                print("Não há quantidade suficiente de gasolina para abastecer com aditivo.")
            else:
                print(f"Abastecido {litros:.2f} litros de gasolina com aditivo.")
        
        elif escolha == '6':
            litros = float(input("Informe a quantidade de litros a ser abastecida com aditivo: "))
            valor = bomba_gasolina.abastecer_por_litro_com_aditivo(litros)
            if valor == -1:
                print("Não há quantidade suficiente de gasolina para abastecer com aditivo.")
            else:
                print(f"Valor a pagar com aditivo: R$ {valor:.2f}.")
        
        elif escolha == '7':
            print(f"Quantidade disponível de etanol: {bomba_etanol.quantidade_disponivel:.2f} litros.")
        
        elif escolha == '8':
            print(f"Quantidade disponível de gasolina: {bomba_gasolina.quantidade_disponivel:.2f} litros.")
        
        elif escolha == '9':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 9.")

# Rodar o menu
menu()
