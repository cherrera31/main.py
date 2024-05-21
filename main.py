import math
'''

primer_nombre = "Carolina"
print(primer_nombre)
apellido = "Herrera"
print (apellido)
print (primer_nombre + apellido)

print (type(primer_nombre))

nombre_completo = primer_nombre + " " + apellido 

print ("Hola mi nombre es:" + nombre_completo)
edad = 24
#edad = 24 + 1
edad += 1
print (edad)

print ("Hola mi edad es:" +str (edad))

altura = 1.63

print (altura)

print(type(altura))

print ("Hola mi altura es:"+str (altura))

humano = False
print (humano)
print(type(humano))

nombre = "carolina"
edad = 24
atractivo = True

nombre,edad,atractivo = "carolina", 24, True

print(nombre)
print(edad)
print(atractivo)

bobesponja = 30
arenita = 30
patricio = 30
calamardo = 30

print(bobesponja)
print(arenita)
print (patricio)
print(calamardo)

x = float(input("Ingrese un numero:"))
print(x)
y = float(input("Ingrese segundo numero:"))
print(y)

suma = x + y
print ("El resultado es :"+ str (suma))


a = float(input("Ingrese el primer numero:"))
b = float(input("Ingrese el segundo numero:"))
c = float(input("Ingrese el tercer numero:"))

s = (a + b + c) / 2
print(s)

Area = math.sqrt (s * (s - a) * (s -b) * (s-c)) 
print ("El area es:"+ str (Area))


funciones #no lleva indentacion 
def sumar(x, y):
    if (x==y):
        print (f'Los argumentos son {x} y {y} y su suma es:')
        return x + y
    elif (x>y):
        return 'x es mayor a y'
    else:
        return False
    
print (sumar (1,1))
print (sumar (2,1))
print (sumar (1,2))

#base times height of a square
def cuadrito(x):
    return x*x

print (cuadrito(5))



import math #Teoria de Heron pero con una funcion
def triangle_area (a,b,c):
 s = (a + b + c) / 2
 Area = math.sqrt (s * (s - a) * (s -b) * (s-c)) 
 return Area

lol = triangle_area (2,2,2)
print ("The area of the triangle is:", lol)


 nombre = "carolina"

 print(len(nombre))
 print(())
 

#75  para arriba Boomer
#18 para arriba adulto
#menos de 18 nino


def edad(x):
    if (x >= 75):
        print ('Eres un Boomer')
        return x
    elif (x >= 18):
        print ('Eres un adulto')
        return x
    else:
        print('Eres pequeno')

print (edad(100))

name = ""

while len(name)==0:
     name = input("Introduzca su nombre:")

print ("Me sali")


for i in range(10):
    print(i)

aprobadas = []
calificaciones = []


Materias = ("matematicas" , "quimica" , "historia" , "fisica" , "lenguas")
print (Materias)
name = ""
while len(name)==0:
    name = input ("Ingresa tu nombre: " )

for i in Materias:
    calificacion = input("Que sacaste en " + "" + i )
    if int (calificacion) >= 70:
        

#def atrapado_en_bucle (name): 

i = 250
while len(str(i)) > 72: #i se convierte en un caratcter de 3 digitos
    i *= 2  # variable izquierdo se multiplica por 2 asi que la funcion no se cumple
else:
    i //=2 # variable i se divide entre 2
print (i)


n = 0
while n < 4 :
    n += 1
    print (n,end= " ") #asi salen horizontal, space entre las comillas hace que se separen los numeros
    
val = 1
val2 = 0
val = val ^ val2
val2 = val ^ val2
val = val ^ val2
print (val)

Lista = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print (Lista)
def par_impar(x): 
  if (x % 2) == 0:
        print ('numero par')
        return x
  else:
        print('numero impar')

print (par_impar(20))

#Asi lo hizo el profe
Lista = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

for i in list:
     if i % 2 ==0:
          print (f'{i} es par')
     else:
        print(f'{i} es impar')
        
#Diccionarios
#Diccionario = {"a":10, "b":20, "c":30}
capitales_paises = {"Mexico":"CDMX","Italia":"Roma","USA":"Washington D.C.", "Russia":"Moscu", "Peru":"Lima", "Australia":"Canberra"}
for pais in capitales_paises:
    print(pais)

for capitales in capitales_paises:
    capital = capitales_paises[capitales]
    print(capital)
    '''
tipos_archivos = {".txt":"Archivo de texto", ".pdf": "Documento PDF", "jpg":"Iamgen jpg"}
print()

