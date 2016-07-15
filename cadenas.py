lista = []

elemento = raw_input("Elemento: ")

while elemento != "":
  lista.append (elemento)
  elemento = raw_input("elemento siguiente ")
  
print lista


while True:

  print ""
  print ""

  print "Selecciona una opción"

  print "1.- Cadena a la cero"
  print "2.- Cadena a la uno"
  print "3.- Cadena a la dos"
  print "4.- Cadena a la tres"
  print "5.- Cadena a la cuatro"
  print "6.- Cadena  ala cinco"
  print "7.- Salir"
  
  
  print ""


  opcionMenu = raw_input("inserta un numero valor >> ")

  if opcionMenu=="1":
    		print ""
    		raw_input("Cadena potencia cero...\npulsa una tecla para continuar")
                print ""
                print "E Epsilon"
                
  elif opcionMenu=="2":
		print ""
		raw_input("Cadena potencia uno...\npulsa una tecla para continuar")
                print ""
                print lista
                print ""
  elif opcionMenu=="3":
		print ""
		raw_input("Cadena potencia dos...\npulsa una tecla para continuar")
                print ""
                lista2 = []
                for i in lista:
                   for j in lista:
                      lista2.append(i + j)
                      
                print lista2


  elif opcionMenu=="4":
		print ""
		raw_input("Cadena potencia tres...\npulsa una tecla para continuar")
                print ""
                lista2 = []
                lista3 = []
                for i in lista:
                   for j in lista:
                      lista2.append(i + j)
                      
                
                
                for f in lista:
                   for c in lista2:
                      lista3.append(f + c)
                      
                print lista3 


  elif opcionMenu=="5":
		print ""
		raw_input("Cadena potencia cuatro...\npulsa una tecla para continuar")
                print ""
                lista2 = []
                lista3 = []
                lista4 = []
                for i in lista:
                   for j in lista:
                      lista2.append(i + j)
                      
                
                
                for f in lista:
                   for c in lista2:
                      lista3.append(f + c)
                      
                
                for d in lista:
                   for j in lista3:
                      lista4.append(d + j)
                      
                print lista4
                

  elif opcionMenu=="6":
		print ""
		raw_input("Cadena potencia cinco...\npulsa una tecla para salir del programa")
                print ""
                lista2 = []
                lista3 = []
                lista4 = []
                lista5 = []
                for i in lista:
                   for j in lista:
                      lista2.append(i + j)
                      
                
                
                for f in lista:
                   for c in lista2:
                      lista3.append(f + c)
                      
                
                for d in lista:
                   for j in lista3:
                      lista4.append(d + j)
                      
                for o in lista:
                   for p in lista4:
                      lista5.append(o + p)
                      
                print lista5
              
  elif opcionMenu=="7":
		print ""
		raw_input("Esta apunto de salir...\npulsa una tecla para salir del programa")
                break

  else:
		print ""
		raw_input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


