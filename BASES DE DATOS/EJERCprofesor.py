#ejercicio3
##Guardando datos en la base de datos
import sqlite3
import time

hector=sqlite3.connect("hector.db")
cursor=hector.cursor()
cursor.execute("create table if not exists estudiantes(codigo integer primary key, apellidoynombre text, nota real, correo text)")
cursor.execute("""
create table if not exists comida(codigo integer primary key, nombre text, precio integer)
""")
cursor.execute("""
create table if not exists bebidas(codigo integer primary key, nombre text, precio integer)
""")

print ("Se han creado las tres tablas correctamente")

cursor.close()

def agregar():

    print ("----------------")
    print ("Agregar dato")
    print ("----------------")
    hector = sqlite3.connect("hector.db")
    cursor = hector.cursor()
    tabla=int(input('''ingrese:
            1 para tabla estudiantes
            2 para tabla comida
            3 para tabla bebidas\n'''))
    if tabla==1:
        codigo=int(input('ingrese su código de estudiante\n'))
        apellidoynombre=input('escriba su apellido y nombre\n')
        nota=float(input('ingrese su nota definitiva del semestre'))
        correo=input('escriba su correo electronico')
        cursor.execute("insert into estudiantes (codigo, apellidoynombre, nota, correo) values ('%s','%s','%s','%s')"%(codigo,apellidoynombre,nota,correo))
        hector.commit()
        print ("Los datos fueron agregados con éxito")
        cursor.close()
        time.sleep(2) #espera

    elif tabla==2:
        codigo=int(input('ingrese su código de producto\n'))
        nombre=input('escriba nombre producto\n')
        precio=float(input('ingrese precio unitario producto'))
        
        cursor.execute("insert into comida (codigo, nombre, precio) values ('%s','%s','%s')"%(codigo,nombre,precio))
        hector.commit()
        print ("Los datos fueron agregados con éxito")
        cursor.close()
        time.sleep(2) #espera

    ##falta la tabla 3
    
    main()

def listar():

    #Muestra todos los datos contenidos en la base de datos, tenga en cuenta mostrar todas las tablas
    print ("------------------")
    print ("TABLAS EXISTENTES")
    print ("------------------")
    hector = sqlite3.connect("hector.db") #siempre que se quiera trabajar sobre la base debe conectarse
    cursor = hector.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    ver = cursor.fetchall()
    print('Tabla ESTUDIANTES')
    for i in ver:
        print ("%s %s %s %s" % (i[0],i[1],i[2],i[3]))

    cursor.execute("SELECT * FROM comida")
    ver = cursor.fetchall()
    print('Tabla COMIDA')
    for i in ver:
        print ("%s %s %s" % (i[0],i[1],i[2]))

    cursor.execute("SELECT * FROM bebidas")
    ver = cursor.fetchall()
    print('Tabla BEBIDAS')
    for i in ver:
        print ("%s %s %s" % (i[0],i[1],i[2]))
    

    cursor.close()
 
    print (" ----------------- ")
    input("Presione una tecla para continuar...")
 
    main()

def buscar():
    
    #Busca datos en las tablas existentes/en proceso
    pass
    print ("---------------")
    print ("Buscar contacto")
    print ("---------------")
 
 
    hector = sqlite3.connect("hector.db")
    cursor = hector.cursor()

##    tabla=int(input('seleccione la tabla a buscar 1. estudiantes, 2. comida, 3 bebidas\n'))
##    if tabla==1:
    buscar = input("Nombre a buscar: ")
    cursor.execute ("SELECT * FROM estudiantes WHERE apellidoynombre = '%s'" %(buscar))
    x = cursor.fetchall()
 
    print ("-----------------")
 
    for i in x:
         print ("codigo:", i[0])
         print ("Apellido y Nombre:", i[1])
         print ("Nota:", i[2])
         print ("Correo:", i[3])
            
         print ("----------------")
         
    cursor.close()
 
    print ("------------------")
    input("Presione una tecla para continuar...")
 
    main()

def main():

    #Funcion principal del programa...

    print ("       ------------------------------------------")
    print ("        BASES DE DATOS PRUEBA UIS PROGRAMACIÓN 2        ")
    print ("       ------------------------------------------")
    print ("""
    [1] Ingresar datos
    [2] Listar datos
    [3] Buscar dato
    [4] Editar dato
    [0] Salir
    """)
     
    opcion = input("Ingresa una opcion: ")
 
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "0":
        print ("Opcion incorrecta")
        input("Presione una tecla para continuar...")
        main()
    elif opcion == "1":
        agregar()
    elif opcion == "2":
        listar()
    elif opcion == "3":
        pass
        buscar()
    elif opcion == "4":
        pass
        editar()
    elif  opcion == "0":
        print ("_-------------------------------------------")
        print ("Gracias.... hasta pronto")
        print ("--------------------------------------------")
        
        time.sleep(3)
        exit()
      
main()
