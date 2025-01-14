# ESCRIBE UN PROGRAMA QUE ALMACENE UN NÚMERO Y PIDA AL USUARIO ADIVINARLO...

# OBJETIVO: INTRODUCIR EL CONCEPTO DE ENTRADA DE USUARIO Y CONDICIONALES...

secret_number = 7
guess = int(input("GUESS THE NUMBER: "))

if guess == secret_number:
    print("SUCCESS!!!!!!")

else:
    print("TRY AGAIN!")