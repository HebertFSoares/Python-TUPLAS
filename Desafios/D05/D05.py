tupla = ("aprender", "programar","trabalhar")

for p in tupla:
    print(f"\nna Palavra {p.upper()} temos", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
    