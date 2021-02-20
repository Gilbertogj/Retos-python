def format(numero):
    if not isinstance(numero,int):    
      return None, 'No es numero entero'
    elif numero<=0:                   
      return None, 'No es numero entero'
    n=str(numero)
    n=list(n)
    i=len(n)-1
    c=0
    f=[]
    while i>=0:
      c=c+1
      f.append(n[i])
      if c==3 and i>0:
        f.append(',')
        c=0
      i-=1
    n="".join(f)
    n=n[::-1]
    return(n)
      
print(format(100000)) 





