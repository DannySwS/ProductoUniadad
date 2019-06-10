import numpy as np
from io import StringIO

pfile=open('productos.txt','r')
data=pfile.read()
productos=data
pfile.close()
data=np.genfro
print (productos, "\n")

Codigo = int(input("Ingrese el código del producto: "))

if Codigo<=filas:
    for aux in range(filas):
        if int(data[aux,0])==Codigo:
            print ("\nSu producto cuesta: $",data[aux,2])
            Precio = float(data[aux,2])
            Dinero = float(input("\nIngrese la cantidad de dinero: "))
                while Dinero<Precio:
                    print("\nCantidad insuficiente")
                    Suma = float(input("\nIngrese más dinero: "))
                    Dinero = Dinero+Suma     
                Vuelto = round(float(Dinero-Precio),2)
                Vuelto = round(Vuelto,2)
                print ("\nSu cambio es de $",Vuelto)
            else:
                Vuelto = float(Dinero-Precio)
                Vuelto = round(Vuelto,2)
                print ("\nSu cambio es de $",Vuelto)
                print ("\nGracias por su compra :))")    
else:
    print ("Código incorrecto")