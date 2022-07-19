import sqlite3
import time
from datetime import datetime
from datetime import datetime
from datetime import timedelta

biblioteca=sqlite3.connect('biblioteca.db')
cursor=biblioteca.cursor()
cursor.execute("create table if not exists libros(nombre varchar,autor varchar,paginas interger,codigo integer,precio interger)")
cursor.execute("create table if not exists admin(usuario varchar,contraseña interger)")
cursor.execute("create table if not exists usuarios(usuario varchar,contraseña interger)")

#cursor.execute("insert into admin (usuario,contraseña) values ('%s','%s')"%("felipe",121))
#cursor.execute("insert into usuarios (usuario,contraseña) values ('%s','%s')"%("herrera",11))
#cursor.execute("insert into libros (nombre,autor) values ('%s','%s')"%("calculo","nn",125,1,12000))
biblioteca.commit()
				    

print('TABLAS CREADAS CON EXITO (👍≖‿‿≖)👍')

cursor.close()

def menusuario():
        print('1.sacar libro\n2.libros prestados\n3.salir')

        opp=int(input('ingrese su eleccion:\n'))
        if opp== 1:
            slibro()
            pass
        elif opp== 2:   
            librosp()
            pass
        elif opp== 3:
            menp()
        
        else:
            print('error')
            
        menusuario()





def usuario():
    biblioteca =sqlite3.connect('biblioteca.db')
    usuario=input('ingrese su usuario:')
    contraseña=input('ingrese su contraseña:')
    cursor = biblioteca.execute("select * from usuarios where usuario ='%s'"%(usuario))
    cursor = biblioteca.execute("select * from usuarios where contraseña ='%s'"%(contraseña))

    x = cursor.fetchall()
    for i in x:
        menusuario()
        break
    else:
        print('error de ingreso')
        admi()
    biblioteca.close()



#ADMINISTRADOR---------------------------------------------------------------------------------------------

def inventario():
    print ("DATOS ALMACENADFOS")
    
    biblioteca = sqlite3.connect("biblioteca.db") #siempre que se quiera trabajar sobre la base debe conectarse
    cursor = biblioteca.cursor()
    cursor.execute("SELECT * FROM usuarios")
    ver = cursor.fetchall()
    print('USUARIOS REGISTRADOS')
    for i in ver:
        print ("%s %s" % (i[0],i[1]))

    cursor.execute("SELECT * FROM libros")
    ver = cursor.fetchall()
    print('LIBROS ALMACENADOS')
    for i in ver:
        print ("%s %s %s %s %s" % (i[0],i[1],i[2],i[3],i[4]))

    cursor.close()

    menuadmi()
    
    


def nlibro():
    biblioteca=sqlite3.connect('biblioteca.db')
    cursor=biblioteca.cursor()
    nombre=input('ingrese el nombre del libro:\n')
    autor=input('ingrese el autor del libro:\n')
    paginas=input('ingrese el numero de paginas del libro:\n')
    codigo=int(input('ingrese el codigo del libro:\n'))
    precio=int(input('ingrese el precio del libro:\n'))

    cursor.execute("insert into libros (nombre, autor, paginas, codigo, precio) values ('%s','%s','%s','%s','%s')"%(nombre,autor,paginas,codigo,precio))
    biblioteca.commit()
    print('SE HA GUARDADO SU NUEVO LIBRO CON EXITO (👍≖‿‿≖)👍 ')
    cursor.close()
    menuadmi()
    

def nusuario():
    biblioteca=sqlite3.connect('biblioteca.db')
    cursor=biblioteca.cursor()
    usuario=input('ingrese el nuevo usuario\n')
    contraseña=int(input('ingrese la contraseña\n'))
        
    cursor.execute("insert into usuarios (usuario, contraseña) values ('%s','%s')"%(usuario,contraseña))
    biblioteca.commit()
    print('SE HA GUARDADO EL NUEVO USUARIO CON EXITO (👍≖‿‿≖)👍 ')
    cursor.close()

    menuadmi()
    

    
def menuadmi():
    print('-----------------------')
    print('BIENVENIDO ADMINISTRADOR')
    print('1.nuevo libro\n2.nuevo estudiante\n3.editar libros\n4.mostrar libros y usuarios registrados\n5.salir')
    opp=int(input('ingrese su eleccion:\n'))

    if opp== 1:
        nlibro()

    elif opp== 2:
        nusuario()

    elif opp==3:
        pass

            
            
    elif opp== 4:
        inventario()

    elif opp== 5:
        menp()

    else:
        print('error')
            
        menuadmi()

def admi():
    biblioteca =sqlite3.connect('biblioteca.db')
    usuario=input('ingrese su usuario:')
    contraseña=input('ingrese su contraseña:')
    cursor = biblioteca.execute("select * from admin where usuario ='%s'"%(usuario))
    cursor = biblioteca.execute("select * from admin where contraseña ='%s'"%(contraseña))

    x = cursor.fetchall()
    for i in x:
        menuadmi()
        break
    else:
        print('error de ingreso')
        admi()
    biblioteca.close()

    
#MENU PRINCIPAL------------------------------------------------------
        
def menp ():
    
    print('1.Administrador\n2.Usuario\n3.Salir')
    opp=int(input('ingrese su eleccion:\n'))
    
    if opp==1:
        admi()
            
    elif opp==2:
        usuario()
            
    elif opp==3:
        exit()
    else :
        print('error de ingreso, seleccione una opcione de menu correcta')
        menp()
        
        
menp()


        


    



