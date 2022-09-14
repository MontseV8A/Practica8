'''
Tema: Entrada y Salida
Fecha: 12 de septiembre del 2022
Autor: Montserrat Valdovinos Ochoa

'''

# Python soporta múltiples formas de formatear una cadena de caracteres. A continuación se describen:
# 1. Formateo %. operador de interpolación
# 2. format(). devuelve una versión formateada de una cadena de caracteres, usando substituciones desde argumentos
# 3. formateo avanzado. Este método soporta muchas técnicas de formateo
# 4. formateo por tipo


# 1. Formateo %. operador de interpolación
# operacion="potencia"
# num = 10
# x = 10**2
#print("La %s del número es: %d es %f" %(operacion, num, x))

#Mostrar el valor de num en octal y hexadecimal
#print("El valor de: %d en octal es: %o y en hexadecimal es: %x" %(num, num, num))

# formato con salida %.2(dos decimales)
#print("La %s del número es: %d es %.2f" %(operacion, num, x))


#    Con esta sintaxis hay que determinar el tipo del objeto:

#    %c = str, simple carácter.
#    %s = str, cadena de carácter.


#    %d = int, enteros.
#    %f = float, coma flotante.
#    %o = octal.
#    %x = hexadecimal.

estudiante={
    "Control": 1000,
    "Nombre":"José Ramon Flores",
    "Sexo": "M",
    "Materias":[
        {"Clave":10, "Nombre":"Base de datos","Promedio":80.98},
        {"Clave": 20, "Nombre": "Programación", "Promedio": 80.8},
        {"Clave": 30, "Nombre": "Moviles", "Promedio": 80.0}
        ],
    "Altura":1.79
}

#print("Control: %d Nombre del estudiante: %s tiene una altura %.2f"%(estudiante["Control"],estudiante["Nombre"],estudiante["Altura"]))
#print("Estudiante: %s con promedio en la materia %s de: %f"%(estudiante["Nombre"],estudiante["Materias"][0]["Nombre"]))

# 2. format(). devuelve una versión formateada de una cadena de caracteres,
#     usando substituciones desde argumentos
operacion="potencia"
num = 10
x = 10**2
#print("La {} de {} es {}".format(operacion,num,x))
#print(f"La {operacion} de {num} es {x}")

# 3. fromateo avanzado. Este método soporta muchas técnicas de formateo
#    A) Alinear una cadena de caracteres a la derecha en 30 caracteres
#print("{:>90}".format("Esta es la cadena"))
#print("{:0}".format("Esta es la cadena"))
#    B) Alinear una cadena de caracteres a la izquierda en 30 caracteres
#        (crea espacios a la derecha), con la siguiente sentencia


#    C) Alinear una cadena de caracteres al centro en 30 caracteres.
#print("{:^80}".format("Cadena"))

#    D) Truncamiento a 9 caracteres.
cadena="Cadena"
#print("{:.5}".format(cadena))

# 4. Formateo por tipo //rellena con espacios
#    s para cadenas de caracteres (tipo str).
#    d para números enteros (tipo int).
#    f para números de coma flotante (tipo float).
#print("{:8d}".format(10))
# Formateo de numeros enteros rellenados con espacios
#print("{:08d}".format(10))
#print("{:08f}".format(1.1243453465))
# Formateo de numeros rellenados con ceros


# Formateo de números flotantes, rellenados con espacios


'''
# Carrito de compra:
#    nombre_producto
#    precio
#    cantidad
#    descuento


#    NOMBRE PRODUCTO     PRECIO      CANTIDAD        SUBTOTAL

carrito = {1:['Monitor Samsumng 27 pulgadas     ', 4589.98, 1, 3],
           2:['Tableta 10 pulgadas marca X      ', 2500.9, 1, 3],
           3:['Mouse gamer 3d                   ', 3400.5, 1, 3],
           4:['Computadora de escritorio lenovo ', 1589.98, 1, 3],
           5:['Renovación Antivirus X           ', 1057, 2, 3]
           }

1. Mostrar el contenido del carrito alineado
2. Eliminar un producto del carrito
3. Regresar un JSON con una bandera si el carrito tiene productos
'''

carrito = {1:['Monitor Samsumng 27 pulgadas     ', 4589.98, 1, 3],
           2:['Tableta 10 pulgadas marca X      ', 2500.9, 1, 3],
           3:['Mouse gamer 3d                   ', 3400.5, 1, 3],
           4:['Computadora de escritorio lenovo ', 1589.98, 1, 3],
           5:['Renovación Antivirus X           ', 1057, 2, 3]
           }
#Mostrar alineado

def Mostrar():
    for i in carrito:
        print(carrito[i][0], "{:8.2f}".format(carrito[i][1]), "{:8d}".format(carrito[i][2]),"{:8}".format(carrito[i][3]))
Mostrar()

# def eliminar():
#     op=int(input("Dame el numero de producto a eliminar:"))
#     if(op==1):
#         del carrito[1]
#     elif(op==2):
#         del carrito[2]
#     elif (op == 3):
#         del carrito[3]
#     elif (op == 4):
#         del carrito[4]
#     print("Eliminado")
#     Mostrar()

#eliminar()
def archivo_carrito():
    productos = open("productos.txt", "w")
    for i in carrito:
        llenar_carrito=carrito[i][0] + " "+ "{:8.2f}".format(carrito[i][1])+" "+ "{:8d}".format(carrito[i][2])+" "+" "+"{:8}".format(carrito[i][3]) + "\n"
        productos.write(llenar_carrito)
    print("archivo generado")

archivo_carrito()

import json



#
# json.dump(informacion, mJson)









def bandera():
    bandera={}
    archivo=open("productos.txt", 'r')
    mJson = open("productos.json", mode='w')
    prod= archivo.read().split("\n")
    if len(prod)>0:
        for i in carrito:
            bandera = {"Nombre_producto": carrito[i][0],"Precio": "{:8.2f}".format(carrito[i][1]),"Cantidad": "{:8d}".format(carrito[i][2]), "Subtotal": str(carrito[i][1]*carrito[i][2])}
            json.dump(bandera, mJson)
    else :
        print("Carrito vacio")

bandera()