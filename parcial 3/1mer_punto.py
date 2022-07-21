from datetime import date
from datetime import datetime
from datetime import datetime
from datetime import timedelta

import sqlite3
import time

biblioteca=sqlite3.connect('biblioteca.db')
cursor=biblioteca.cursor()
cursor.execute("create table if not exists libros(nombre varchar,autor varchar,paginas integer,codigo integer,precio integer,uso varchar, fechaR varchar, fechaE varchar)")
cursor.execute("create table if not exists admin(usuario VARCHAR,contraseña integer)")
cursor.execute("create table if not exists usuarios(usuario varchar,contraseña integer)")

#cursor.execute("insert into admin (usuario,contraseña) values ('%s','%s')"%("felipe",121))
#cursor.execute("insert into usuarios (usuario,contraseña) values ('%s','%s')"%("herrera",11))

biblioteca.commit() 
                    

print('TABLAS CREADAS CON EXITO (👍≖‿‿≖)👍')

cursor.close()


class bibliotecauis ():
    def __init__ (self):
        #self.libros=[{'nombre':'calculo','autor':'nn','numero de paginas':1,'codigo':1,'precio':1,'uso':'','fecha R':'','fecha E':''}]
        #self.a=[{'usuario':'felipe','contraseña':'121'}]
        #self.estudiantes=[{'usuario':'herrera','contraseña':'1','libros':[]}]
        self.gcod=0

#ESTUDIANTE------------------------------------------------------------------------------------------------------

    def estd(self):
        self.usuario=input('ingrese su usuario:\n')
        self.contraseña=input('ingrese su contraseña:\n')
        biblioteca=sqlite3.connect('biblioteca.db')
        cursor=biblioteca.cursor()
        cursor.execute("SELECT * FROM usuarios")
        lista_usuarios = cursor.fetchall()
        cursor.close()
        biblioteca.close()
        for i in lista_usuarios:
            
            if self.usuario==i[0] and int(self.contraseña)==i[1]:
                print('BIENVENIDO',self.usuario,' (👍≖‿‿≖)👍')
                self.mestd()

        else:
            print('USUARIO O CONTRASEÑA INCORRECTO,INGRESE NUEVAMENTE (͠◉_◉᷅)')
            self.estd()
                
    def mestd(self):
        print('1.sacar libro\n2.devolver libro\n3.libros prestados\n4.salir')

        opp=int(input('ingrese su eleccion:\n'))
        if opp== 1:
            self.slibro()
        elif opp== 2:
            self.elibros()
        elif opp== 3:
            self.librosp()
        elif opp== 4:
            self.menp()
        
        else:
            print('error')
            
        self.mestd()

    def slibro(self):
        biblioteca=sqlite3.connect('biblioteca.db')
        cursor=biblioteca.cursor()
        cursor.execute("SELECT * FROM libros")
        libros=cursor.fetchall()

        a=1
        nombre=input('ingrese el nombre del libro\n')
        for i in libros:
            if nombre==i[0] and i[5]==' ':

                now=date.today()
                print('\nOPERACION EXITOSA(👍≖‿‿≖)👍\nLIBRO ENTREGADO EN LA FECHA:  ',now,'\n')
                
                new_date = now + timedelta(days=15)
                cursor.execute("UPDATE  libros SET uso=?, fechaR=?, fechaE=? WHERE codigo=?",( self.usuario,now ,new_date , i[3]))
                a=0
                            
            else:
                print('EL LIBRO',nombre,'NO ESTA DISPONIBLE (͠◉_◉᷅)')
            if a==0:
                break

        biblioteca.commit()
        cursor.close()
        biblioteca.close()        

    def librosp(self):
        print ("LIBROS PRESTADOS")


        biblioteca = sqlite3.connect("biblioteca.db")
        cursor = biblioteca.cursor()
        cursor.execute("SELECT * FROM libros WHERE uso=?",(self.usuario, ))
        ver = cursor.fetchall()
        if len(ver)>0:
            for i in ver:
                print(i)

        else:
            print('NO TIENE NINGUN LIBRO PRESTADO (͠◉_◉᷅)')

    def elibros(self):
        biblioteca=sqlite3.connect('biblioteca.db')
        cursor=biblioteca.cursor()
        cursor.execute("SELECT * FROM libros")
        libros=cursor.fetchall()

        a=1
        nombre=input('ingrese el nombre del libro\n')
        for i in libros:
            if nombre==i[0] and i[5]==self.usuario:

                now=date.today()
                print('\nOPERACION EXITOSA(👍≖‿‿≖)👍\nLIBRO DEVUELTO EN LA FECHA:  ',now,'\n')
                
                cursor.execute("UPDATE  libros SET uso=?, fechaR=?, fechaE=? WHERE codigo=?",( ' ',' ' ,' ', i[3]))
                a=0
                            
            else:
                print('UD NO HA SACADO EL LIBRO',nombre,'PRESTADO (͠◉_◉᷅)')
            if a==0:
                break

        biblioteca.commit()
        cursor.close()
        biblioteca.close()        
         





       

                    
                        
        
#ADMINISTRADOR-------------------------------------------------------------------------------------------

    def nlibro(self):


        nombre=input('ingrese el nombre del libro:\n')
        autor=input('ingrese el autor del libro:\n')
        npaginas=input('ingrese el numero de paginas del libro:\n') 
        precio=int(input('ingrese el precio del libro:\n'))
        self.cantidad=input('ingrese la cantidad de libros:\n')
        self.vercanti()

        for i in range(self.cantidad):
            self.gcod=self.gcod+1
            biblioteca=sqlite3.connect('biblioteca.db')
            cursor=biblioteca.cursor()
            cursor.execute("INSERT INTO libros VALUES (?,?,?,?,?,?,?,?)",(nombre , autor, npaginas, self.gcod , precio,' ',' ',' ' ))
            biblioteca.commit()
            cursor.close()
            biblioteca.close()


            
            print('SE HA GUARDADO EL LIBRO ',nombre,'CON EXITO (👍≖‿‿≖)👍 ')

            
    def vercanti(self):
        if self.cantidad.isdigit()==True:
            if int(self.cantidad)>0:
                self.cantidad=int(self.cantidad)
        else:
            self.cantidad=input('ingrese la cantidad de libros\n')
            self.vercanti()
            
            
    def nestudiante(self):
        u=input('ingrese el usuario:\n')
        c=input('ingrese la contraseña:\n')
        biblioteca=sqlite3.connect('biblioteca.db')
        cursor=biblioteca.cursor()
        cursor.execute("INSERT INTO usuarios VALUES (?,?)",(u,c))
        biblioteca.commit()
        cursor.close()
        biblioteca.close()
        print('SE HA GUARDADO A',u,'COMO NUEVO USUARIO CON EXITO (👍≖‿‿≖)👍 ')


    def editar(self):
        print('MENU EDITAR')
        print('1.editar libros\n3.salir')

        opp=int(input('ingrese su eleccion:\n'))
        if opp== 1:
            pass
            ##self.editarl()
        elif opp==3:
            exit()
        else :
            print('error de ingreso, seleccione una opcione de menu correcta')
            self.editar()


    def inventario(self):
        print ("DATOS ALMACENADOS")

    
        biblioteca = sqlite3.connect("biblioteca.db")
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
            print ("%s %s %s %s %s %s %s %s" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        
        print('--------------------------')
        cursor.close()

        self.menuadmi()
        
    
        
    
    def menuadmi(self):

        print('MENU ADMINISTRADOR')
        print('1.nuevo libro\n2.nuevo usuario\n3.editar libros\n4.mostrar libros y usuarios registrados\n5.salir')

        opp=int(input('ingrese su eleccion:\n'))
        if opp== 1:
            self.nlibro()
        elif opp== 2:
            self.nestudiante()
        elif opp==3:
            self.editar()
            
            
        elif opp== 4:
            self.inventario()
        elif opp== 5:
            self.menp()
        else:
            print('error')
            
        self.menuadmi()



    def admi(self):
        self.usuario=input('ingrese su usuario:\n')
        self.contraseña=input('ingrese su contraseña:\n')
        biblioteca=sqlite3.connect('biblioteca.db')
        cursor=biblioteca.cursor()
        cursor.execute("SELECT * FROM admin")
        lista_usuarios = cursor.fetchall()
        cursor.close()
        biblioteca.close()
        for i in lista_usuarios:
            
            if self.usuario==i[0] and int(self.contraseña)==i[1]:
                print('BIENVENIDO ADMINISTRADOR (👍≖‿‿≖)👍')
                self.menuadmi()

        else:
            
            print('USUARIO O CONTRASEÑA INCORRECTO,INGRESE NUEVAMENTE (͠◉_◉᷅)')
            self.admi()



#MENU PRINCIPAL------------------------------------------------------------------------------------------------


    def menp (self):
        print('MENU PRINCIPAL')
        print('1.Administrador\n2.Usuario\n3.Salir')
        opp=int(input('ingrese su eleccion:\n'))
        if opp==1:
            self.admi()
            
        elif opp==2:
            self.estd()
            
        elif opp==3:
            exit()
        else :
            print('error de ingreso, seleccione una opcione de menu correcta')
            self.menp()
 



bibliotecauis().menp()
    

