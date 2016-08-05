lista = []

elemento = raw_input("Elemento: ")

while elemento != "":
  lista.append (elemento)
  elemento = raw_input("elemento siguiente ")
  
print lista

a = "a"
b = "b"

conta = 0;



cantidad = len(lista)
cont = 0
#print cantidad
print 

#for i in lista:
if lista[0] == a:
  for o in lista:
    if o == a:
      cont +=1;
    
    
    elif o == b:
      break
  if cont == cantidad:
    print "nola"
    
      

  
  l = lista[cont:cantidad]
   
  
    
  
  contadorsito = 1;
  for k in l:
      if k == a:
       contadorsito +=1;
       
  if contadorsito >= 2:
    print("lista no permitida")

  elif contadorsito == 1:
    print ("lista permitida")
    
  

  
 
 
    
    
elif lista[0] == b:
    contador = 1;
    for i in lista:
      if i == a:
       contador +=1;
       
if contador >= 2:

  print("lista no permitida")
  
elif contador == 1:
  print ("lista permitida")