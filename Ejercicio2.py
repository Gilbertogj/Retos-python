# def multiplos(num,length):
#     lista=[]                  
#      #Creamos una lista vacía
#     if not isinstance(num,int) or not isinstance(length,int) :    
#         # Validamos que sean numeros
#       return None, 'Debes ingresar numeros enteros'
#     elif num<=0 or length<=0:
#         #Validamos que sean enteros 
#       return None, 'Debes ingresar numeros enteros'
#     for i in range(length):    
#         # Recorremos de 0 a la longitud dada por el usuario 
#       lista.append(num*(i+1))  
#       #agregamos a la lista nueva el numero multiplicado por cada valor de 1 a la longitud
#     return lista               
#     #retornamos la lista 

# print(multiplos('hola',4))

def multiplos(num,length):
    if not isinstance(num,int) or not isinstance(length,int) :    
        #Validamos que sean numeros
      return None, 'Debes ingresar numeros enteros'
    elif num<=0 or length<=0:
      #Validamos que sean enteros 
      return None, 'Debes ingresar numeros enteros'
    lista=[num*(i+1) for i in range (length)]
    return lista 
print(multiplos(-0,5))
