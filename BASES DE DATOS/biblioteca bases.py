import sqlite3
import time

biblioteca=sqlite3.connect('biblioteca.db')
cursor=biblioteca.cursor()
cursor.execute("create table if not exists libros(nombre varchar,autor varchar,paginas interger,codigo integer,precio interger,uso varchar, fechaR varchar, fechaE varchar)")
cursor.execute("create table if not exists admin(usuario varchar,contraseña interger)")
cursor.execute("create table if not exists usuarios(usuario varchar,contraseña interger)")

cursor.execute("insert into admin (usuario,contraseña) values ('%s','%s')"%("felipe",121))
cursor.execute("insert into usuarios (usuario,contraseña) values ('%s','%s')"%("herrera",11))
#cursor.execute("insert into libros (nombre,autor) values ('%s','%s')"%("a","yo"))
biblioteca.commit()
				    

print('TABLAS CREADAS CON EXITO (👍≖‿‿≖)👍')

cursor.close()

def nlibro():
    biblioteca=sqlite3.connect('biblioteca.db')
    cursor=biblioteca.cursor()
    #gcod=0
    nombre=input('ingrese el nombre del libro:\n')
    autor=input('ingrese el autor del libro:\n')
    npaginas=input('ingrese el numero de paginas del libro:\n')
    precio=int(input('ingrese el precio del libro:\n'))
    #cantidad=input('ingrese la cantidad de libros:\n')
##    vercanti()
##    for i in range(cantidad):
    #gcod=gcod+1
    cursor.execute("insert into libros (nombre, autor, paginas, precio,) values ('%s','%s','%s','%s','%s')"%(nombre,autor,npaginas,precio))
    biblioteca.commit()
    print('SE HA GUARDADO SU NUEVO LIBRO CON EXITO (👍≖‿‿≖)👍 ')
    cursor.close()
    menuadmi()
    

##def vercanti():
##    if cantidad.isdigit()==True:
##        if int(cantidad)>0:
##            cantidad=int(cantidad)
##    else:
##        cantidad=input('ingrese la cantidad de libros\n')
##        vercanti()
##
##
##

def nusuario():
    biblioteca=sqlite3.connect('biblioteca.db')
    cursor=biblioteca.cursor()
    usuario=input('ingrse el nuevo usuario\n')
    contraseña=int(input('ingrese la contraseña'))
        
    cursor.execute("insert into usuarios (usuario, contraseña) values ('%s','%s')"%(usuario,contraseña))
    biblioteca.commit()
    print('SE HA GUARDADO EL NUEVO USUARIO CON EXITO (👍≖‿‿≖)👍 ')
    cursor.close()

    menuadmi()
    

    
def menuadmi():
    print('-----------------------')
    print('BIENVENIDO ADMINISTRADOR')
    print('1.nuevo libro\n2.nuevo estudiante\n3.editar libros\n4.mostrar inventario\n5.salir')
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

    
    
        
def menp ():
    
    print('1.Administrador\n2.Usuario\n3.Salir')
    opp=int(input('ingrese su eleccion:\n'))
    
    if opp==1:
        admi()
            
    elif opp==2:
        estd()
            
    elif opp==3:
        exit()
    else :
        print('error de ingreso, seleccione una opcione de menu correcta')
        menp()
        
        
menp()


        


    




