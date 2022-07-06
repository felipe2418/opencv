from datetime import date
from datetime import datetime
from datetime import datetime
from datetime import timedelta
class bibliotecauis ():
    def __init__ (self):
        self.libros=[{'nombre':'calculo','autor':'nn','codigo':1,'precio':1,'uso':'','fecha R':'','fecha E':''}]
        self.a=[{'usuario':'felipe','contraseña':'121'}]
        self.estudiantes=[{'usuario':'herrera','contraseña':'1','libros':[]}]
        self.gcod=1

#ESTUDIANTE------------------------------------------------------------------------------------------------------

    def estd(self):
        self.usuario=input('ingrese su usuario:\n')
        self.contraseña=input('ingrese su contraseña:\n')

        for i in range(len(self.estudiantes)):
            if self.usuario==self.estudiantes[i]['usuario']:
                if self.contraseña==self.estudiantes[i]['contraseña']:
                    self.mestd()

        else:
            print('USUARIO O CONTRASEÑA INCORRECTO,INGRESE NUEVAMENTE (͠◉_◉᷅)')
            self.estd()





    def mestd(self):
        print('1.sacar libro\n2.libros prestados\n3.salir')

        opp=int(input('ingrese su eleccion:\n'))
        if opp== 1:
            self.slibro()
        elif opp== 2:
            self.librosp()
        elif opp== 3:
            self.menp()
        
        else:
            print('error')
            
        self.mestd()

    def slibro(self):
        a=1
        nombre=input('ingrese el nombre del libro\n')
        for i in range(len(self.libros)):
            if nombre==self.libros[i]['nombre'] and self.libros[i]['uso']=='':
                self.libros[i]['uso']='prestado'
                for j in range(len(self.estudiantes)):
                    if self.usuario==self.estudiantes[j]['usuario']:
                        if self.contraseña==self.estudiantes[j]['contraseña']:
                            self.estudiantes[j]['libros'].append(self.libros[i])
                            now=date.today()
                            print('\nEntregado el dia ',now,'\n')
                            self.libros[i]['fecha R']=now
                            new_date = now + timedelta(days=15)
                            self.libros[i]['fecha E']=new_date
                            a=0
                            
            else:
                print('EL LIBRO',nombre,'NO ESTA DISPONIBLE (͠◉_◉᷅)')
            if a==0:
                break

   
    def librosp(self):
        for j in range(len(self.estudiantes)):
            if self.usuario==self.estudiantes[j]['usuario']:
                if self.contraseña==self.estudiantes[j]['contraseña']:
                    for i in range(len(self.estudiantes[j]['libros'])):
                        print(self.estudiantes[j]['libros'][i])
##            else:
##                print("NO TIENE LIBROS PRESTADOS (͠◉_◉᷅)")
                    
                        
        
#ADMINISTRADOR-------------------------------------------------------------------------------------------

    def nlibro(self):
        nombre=input('ingrese el nombre del libro:\n')
        autor=input('ingrese el autor del libro:\n')
        precio=int(input('ingrese el precio del libro:\n'))
        self.cantidad=input('ingrese la cantidad de libros:\n')
        self.vercanti()
        for i in range(self.cantidad):
            self.gcod=self.gcod+1
            self.libros.append({'nombre':nombre,'autor':autor,'codigo':self.gcod,'precio':precio,'uso':'','fecha R':'','fecha E':''})
            print('SE HA GUARDADO SU NUEVO LIBRO CON EXITO (👍≖‿‿≖)👍 ')

            
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
        self.estudiantes.append({'usuario':u,'contraseña':c, 'libros':[]})
        print('SE HA GUARDADO EL NUEVO ESTUDIANTE CON EXITO (👍≖‿‿≖)👍 ')

    def inventario(self):
        print('LIBROS ALMACENADOS')
        for i in range (len(self.libros)):
            print ('->',self.libros[i])

        print('ESTUDIANTES RESTRADO')
        for i in range (len(self.estudiantes)):
            print ('->',self.estudiantes[i])
    
        
    
    def menuadmi(self):
        
        print('1.nuevo libro\n2.nuevo estudiante\n3.mostrar inventario\n4.salir')

        opp=int(input('ingrese su eleccion:\n'))
        if opp== 1:
            self.nlibro()
        elif opp== 2:
            self.nestudiante()
        elif opp== 3:
            self.inventario()
        elif opp== 4:
            self.menp()
        else:
            print('error')
            
        self.menuadmi()



    def admi(self):
        self.usuario=input('ingrese su usuario:\n')
        self.contraseña=input('ingrese su contraseña:\n')

        for i in range(len(self.a)):
            if self.usuario==self.a[i]['usuario']:
                if self.contraseña==self.a[i]['contraseña']:
                    self.menuadmi()

        else:
            print('USUARIO O CONTRASEÑA INCORRECTO,INGRESE NUEVAMENTE (͠◉_◉᷅)')
            self.admi()



#MENU PRINCIPAL------------------------------------------------------------------------------------------------


    def menp (self):
        print('1.Administrador\n2.Estudiante\n3.Salir')
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
    


