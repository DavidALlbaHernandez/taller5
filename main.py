frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
#Entradas:
lista-->list-->list
elemento->str-->elemento
#Salidas
lista-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
#Realizar una funcion que retorne la copia de una lista que pasa por parametro 
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista

def copia_lista(lista):
  return lista.copy()
"""
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
  
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux
"""    
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista

def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista

""" 
#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""
""""
def letra(lista,elemento):
  auxiliar=[]
  for x in lista:
    if(x[0]=="M"):
      print(x)
      auxiliar.append(x)
  return auxiliar  


"""
#Realizar una funcion que retorne el tamaño de una lista   

"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamano
"""
"""
def tamano_lista(lista):
  aux=[]
  for i in lista:
    print (len(lista))
    return aux
"""

#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamano

def tamano_lista(lista):
  aux=[]
  for i in lista:
    print (len(lista))
    return aux
"""
#Retornar una lista con los numero negativos  
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
def numeros_negativos(lista):
  aux=[]
  for i in lista:
    if(float(i)<=0):
      aux.append(i)
  return aux

pass

"""

#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Entradas:
lista-list-->lista
lista-str-->elemento
Salidas
lista-list-->lista

def posicion_elemento(lista , elemento):
    lista_posiciones = []
    for i in list(range(0,len(lista))):
        if str(lista[i]) == str(elemento): 
            lista_posiciones.append(i)
    return lista_posiciones
  

"""
#realizar una funcion que agregue al final de archivo frutas una
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista

def frutas_nueva(lista,elemento):
  lista.append(elemento)
  return lista
"""

#Realizar una funcion que cuente el numero de veces que se repite un elemento 
""" 
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""
"""
def repetir(lista , elemento):
    aux = []
    for i in list(range(0,len(lista))):
        if str(lista[i]) == str(elemento): 
            aux.append(i)
    return len(aux)
"""  
#if __name__ == "__main__":
"""
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  print(nueva)

"""
"""
if __name__ == "__main__":
  print(copia_lista(lista_frutas))
  print(copia_lista(lista_numeros))
"""
"""
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  nueva_dos=numeros_pares(nueva)
  print(nueva_dos)
"""
"""
if __name__ == "__main__":
	nueva=eliminar_un_caracter(lista_numeros,"\n")
	nueva_tres=numeros_negativos(nueva)
	print(nueva_tres)
"""
"""
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  print(elimina_elemento_lista(nueva,"10"))
"""
"""
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  print("Ingrese la nueva fruta: ")
  elemento=input()
  nueva_fruta = frutas(nueva, elemento)
  print(nueva_fruta)
"""
"""
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=letra(nueva,"a")
  print(nueva_dos)
"""
""" 
  if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=tamano_lista(nueva)
  print(nueva_dos)
  print(type(lista_frutas))
"""
"""
if __name__ == "__main__":
	nueva=eliminar_un_caracter(lista_frutas,"\n")
  print("elemento:")
  elemento = input()
  repetir = repetir(nueva, elemento)
  print(repetir)
"""
"""
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  print("numero:")
  elemento = input() 
  posiciones = posicion_elemento(nueva, elemento)
  print("posicion: ", posiciones)
"""
"""
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=letra(nueva,"")
  print(nueva_dos)
"""