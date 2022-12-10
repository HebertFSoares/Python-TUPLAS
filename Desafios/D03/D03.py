tupla = ()
a = (int(input("Digite Um Numero: ")), 
     int(input("Digite Outro Numero: ")), 
     int(input("Digite Mais Um Numero: ")), 
     int(input("Digite o Ultimo Numero: ")), )
print(f"Você digitou {a}")
print(f"O valor 9 apareceu {a.count(9)} vezes")
if 3 in a:
    print(f"o valor 3 foi digitado {a.index(3)+1}")
else:
    print("O valor 3 não foi digitado")
print("OS valores pares digitados foram", end="")
for n in a:
    if n % 2 == 0:
        print(n, end=" ")

    