def validador ():
    l_produtos_vendidos = []
    l_produtos = [111, 222, 333, 444, 555, 666, 777]
    while True:
        while True:
            try:
                a = int(input("digita ai: "))
                b = 0
                break
            except:
                print("lamento, aceitamos apenas números.")
        if a == 111 or a == 222 or a == 333 or a == 444 or a == 555 or a == 666 or a == 777:
            checar = l_produtos_vendidos.count(a)
            if checar == 1:
                print("não é possivel realizar a mesma compra duas vezes.")
            else:
                l_produtos_vendidos.append(a)
                print(f"Compra aprovada :)\nsua lista atualmente está composta com os itens {l_produtos_vendidos}")
                while True:
                    finalizador = input("caso deseje finalizar a compra digite 'fim', caso contrário digite 'continuar'\n").lower()
                    if finalizador == "fim" or finalizador == "continuar":
                        break
                    else:
                        continue

                if finalizador == "fim":
                    break
                elif finalizador == "continuar":
                    continue

        else:
            print("Compra não aprovada, possíveis erros:\n-digitar o código errado\n-inserir letras")
    return l_produtos_vendidos


preco_total= validador()

def total():
    a = preco_total.count(111) * 10.50
    a2 = preco_total.count(222) * 10.50
    a3 = preco_total.count(333) * 10.50
    b = preco_total.count(444) * 12.00
    b2 = preco_total.count(555) * 12.00
    b3 = preco_total.count(666) * 12.00
    c = preco_total.count(777) * 15.30

    soma = a + a2 + a3 + b + b2 + b3 + c
    valor_final =print (f"O valor final de suas compras deu: {soma}")
    return valor_final


finish = total()