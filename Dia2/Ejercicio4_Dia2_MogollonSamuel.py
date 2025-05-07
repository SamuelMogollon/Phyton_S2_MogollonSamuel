# Ejercicio4_Dia2_MogollonSamuel
# ###########################
# ###### Clase Dia 2 ######
# ###########################
#VERIFICAR SI NUMERO ES PRIMO

print('Bienvenido al portal para verificar si un numero es primo ')

numVerificar=int(input('ingrese el numero que desea verificar '))
cantidadDivisores= 0

for i in range (1,numVerificar + 1):
    if numVerificar % i == 0:
      cantidadDivisores += 1

if cantidadDivisores == 2:
    print("el numero es primo")
else:
    print ('el numero no es primo')
 
  #Desarrollado Por Samuel Enrique Mogollon Janne T.I. - 1096202198
  
