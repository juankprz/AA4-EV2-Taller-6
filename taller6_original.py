#TALLER 6 PYTHON 
#AUTOR(A): JUAN CAMILO PEREZ
# FECHA: 20-OCTUBRE-2022
from datetime import date
hoy =date.today()	#fecha actual
print("Hoy es el dia: ", hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1=int(input("digite un numero:"))
print("*** Ciclo controlado por contador")
i=1
while i <= num1:
   print(i)
   i+=1
print("fin del ciclo")
print()
print("*** Ciclo controlado por evento")
i=1
numero1=5
numero2=int(input("Digite un número de 1 a 10:"))
while numero2 != numero1:
   i += 1
   numero2=int(input("Digite un número de 1 a 10:"))
print("Acertaste en el intento N°",i)
print("fin del ciclo")
print()
print("*** Ciclo abortado con la sentencia break")
amistad=input("digite el nombre de una amistad:")
amistad=amistad.upper()
for character in amistad:
   print(character)
   if character=="A":
      break
print("Fin del ciclo") 
print()
print("FIN")     