try:
    string = input("Digite uma frase apenas com letras maiusculas: ")

    if not string.isupper():
        raise ValueError
    
    print(string)
except ValueError:
    print("A frase deve conter apenas letras maiusculas")