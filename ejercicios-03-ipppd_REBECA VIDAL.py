# EJERCICIO 1


def codifica_descodifica(fichero1,fichero2):
    f=open(fichero1)
    texto=f.read()
    lista=texto.split()
    listanueva=[]
    for palabra in lista:
        pl=list(palabra)
        npl=[]
        for x in pl:
            nx=155-ord(x)
            x=chr(nx)
            npl.append(x)
        palabra2="".join(npl)
        listanueva.append(palabra2)
    texto2=" ".join(listanueva)

    fichero2=open(fichero2,"w")
    fichero2.write(texto2)
    return fichero2.close()


# EJERCICIO 2       

           
def mi_grep(cadena,fichero):
    f=open(fichero)
    n=0
    for line in f:
        n+=1
        texto=f.readline()
        if cadena in texto:
           print("Línea",n,":",texto)
           if n<10:pos=texto.index(cadena)+9
           else:pos=texto.index(cadena)+10
           print(" "*pos,"^"*len(cadena))


#ejercicio 3
#ejercicio 4
           
