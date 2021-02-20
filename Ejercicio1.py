

# def number_length(numero):
#     if(number.isdigit() and numero>=0):
#         n=str (numero)
#         length=0
#         for i in n:
#             length=length+1
#     else:
#         return None, 'No es numero entero'
#     return length


    

# print(number_length(20))


# def number_length(numero):
#     n=str(numero)
#     length=0
#     for i in n:
#       if i.isdigit() and int(n)>=0:
#         length=length+1
#       else:
#         return None, 'No es numero entero'
#     return length

# print(number_length(-1))


def number_length(numero):
    if not isinstance(numero,int):    #Validamos que sea un entero
      return None, 'No es numero entero'
    elif numero<=0:                   #Validamos que no sea negativo
      return None, 'No es numero entero'
    n=str(numero)                     #Volvemos el numero un string
    length=0                          #Variable contador
    for i in n:                       #Recorremos nuestro string 
      length=length+1                 #Cada iteración sumamos a nuestro contador 
    return length                     #Regresamos el valor final del contador 

print(number_length(31))