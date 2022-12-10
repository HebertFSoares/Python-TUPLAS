tupla = ("zero","um","dois","três","quatro","cinco"
         "seis","sete","oito","nove","dez","onze","doze","treze",
         "quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
while True:
    while True:
        a = int(input("Digite um numero entre 0 a 20> "))
        if 0<= a <= 20:
            break
        print("Tente Novamente", end="")
    print(f"Você Digitou o Numero {tupla[a]}")
    b = str(input("Quer Continuar? (s/n)")).upper().strip()
    if b == "N":
        break
    print("Programa Encerrado!")