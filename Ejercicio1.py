

def number_length(numero):
    if(numero>=0):
        n=str (numero)
        length=0
        for i in n:
            length=length+1
    else:
        return None, 'No es numero entero'
    return length


    

number_length(20)
