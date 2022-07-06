

class Agenda():
    def __init__(self):
        self.lista=[]
        
    def añadir(self):
        
        a=input("INGRESE EL NOMBRE\n->")
        b=input("INGRESE EL APELLIDO\n->")
        c=int(input("INGRESE EL NUMERO TELEFONICO\n->"))
        d=input("INGRESE EL CORREO ELECTRONICO\n->")
        self.lista.append({"NOMBRE": a, "APELLIDO":b,"NUMERO":c, "CORREO ELECTRONICO":d})
        print('SE HA GUARDADO SU NUEVO CONTACTO CON EXITO (👍≖‿‿≖)👍 ')

        self.menu()



#_____________________________________________________________________________________________        
    def listar(self):
        if len(self.lista)==0:
            print("NO HAY NINGUN CONTACTO ALMACENADO(͠◉_◉᷅)")
            
        else:
            print('CONTACTOS GUARDADOS EN LA AGENDA')
            for i in range (len(self.lista)):
##                print('CONTACTOS GUARDADOS EN LA AGENDA')
                print ('->',self.lista[i]["NOMBRE"],self.lista[i]["APELLIDO"])
                       
        self.menu()

    

#_____________________________________________________________________________________________
    def buscar(self):
        
        noesta=False
        a=int(input('''BUSCAR CONTACTO POR:
        1-NOMBRE
        2-APELLIDO \n->'''))
        if a==1:
        
            dato=input('INGRESE EL NOMBRE DEL CONTACTO A BUSCAR\n->')
            s=len(self.lista)
            for i in range(s):
                if(dato==self.lista[i]["NOMBRE"]):
                    noesta=True
                    print('->NOMBRE:',self.lista[i]["NOMBRE"],'\n'"->APELLIDO:",self.lista[i]["APELLIDO"],'\n'"->NUMERO:",self.lista[i]["NUMERO"],'\n'"->CORREO ELECTRONICO:",self.lista[i]["CORREO ELECTRONICO"])
                    
            if noesta==False:
                print("EL CONTACTO CON NOMBRE:",dato,",NO EXISTE (͠◉_◉᷅)")

        if a==2:
            
            dato=input('INGRESE EL APELLIDO DEL CONTACTO A BUSCAR\n->')
            s=len(self.lista)
            for i in range(s):
                if(dato==self.lista[i]["APELLIDO"]):
                    noesta=True
                    print('->NOMBRE:',self.lista[i]["NOMBRE"],'\n'"->APELLIDO:",self.lista[i]["APELLIDO"],'\n'"->NUMERO:",self.lista[i]["NUMERO"],'\n'"->CORREO ELECTRONICO:",self.lista[i]["CORREO ELECTRONICO"])
            
            if noesta==False:
                
                print("EL CONTACTO CON APELLIDO:",dato,",NO EXISTE (͠◉_◉᷅)")
            


        self.menu()
        
        
        
#_____________________________________________________________________________________________

    def editar(self):
        noesta=False
        a=int(input('''BUSCAR CONTACTO A EDITAR POR:
        1-NOMBRE
        2-APELLIDO \n->'''))
        if a==1:
        
            dato=input('INGRESE EL NOMBRE DEL CONTACTO A EDITAR\n->')
            s=len(self.lista)
            for i in range(s):
                if(dato==self.lista[i]["NOMBRE"]):
                    
                    noesta=True
                    print('->NOMBRE:',self.lista[i]["NOMBRE"],'\n'"->APELLIDO:",self.lista[i]["APELLIDO"],'\n'"->NUMERO:",self.lista[i]["NUMERO"],'\n'"->CORREO ELECTRONICO:",self.lista[i]["CORREO ELECTRONICO"])
                    e=int(input('''EDITAR CONTACTO:
                    1-NOMBRE
                    2-APELLIDO
                    3.TELEFONO
                    4.CORREO
                    5.TODO EL CONTACTO\n->'''))
                    
                    if e==1:
                        f=input('INGRESE EL NUEVO NOMBRE\n->')
                        self.lista[i].update({"NOMBRE":f})
                        print('MODIFICACION EXITOSA (👍≖‿‿≖)👍')
                        self.menu()
                        
                    if e==2:
                         
                         g=input('INGRESE EL NUEVO APELLIDO\n->')
                         self.lista[i].update({"APELLIDO":g})
                         print('MODIFICACION EXITOSA')
                         self.menu()
                    if e==3:
                         
                         h=int(input('INGRESE EL NUEVO TELEFONO\n->'))
                         self.lista[i].update({"TELEFONO":h})
                         print('MODIFICACION EXITOSA (👍≖‿‿≖)👍')
                         self.menu()     
                    
                    if e==4:
                         
                         j=input('INGRESE EL NUEVO CORREO ELECTRONICO\n->')
                         self.lista[i].update({"CORREO ELECTRONICO":j})
                         print('MODIFICACION EXITOSA (👍≖‿‿≖)👍')
                         self.menu()
                         
                    if e==5:
                         
                         f=input('INGRESE EL NUEVO NOMBRE\n->')
                         g=input('INGRESE EL NUEVO APELLIDO\n->')
                         h=int(input('INGRESE EL NUEVO TELEFONO\n->'))
                         j=input('INGRESE EL NUEVO CORREO ELECTRONICO\n->')
                         self.lista[i].update({"NOMBRE":f,"APELLIDO":g,"TELEFONO":h,"CORREO ELECTRONICO":j})
                         print('MODIFICACION EXITOSA')
                         self.menu()
                
            if noesta==False:
                print("EL CONTACTO CON NOMBRE:",dato,",NO EXISTE (͠◉_◉᷅)")

        if a==2:
            
            dato=input('INGRESE EL APELLIDO DEL CONTACTO A BUSCAR\n->')
            s=len(self.lista)
            for i in range(s):
                if(dato==self.lista[i]["APELLIDO"]):
                    noesta=True
                    print('->NOMBRE:',self.lista[i]["NOMBRE"],'\n'"->APELLIDO:",self.lista[i]["APELLIDO"],'\n'"->NUMERO:",self.lista[i]["NUMERO"],'\n'"->CORREO ELECTRONICO:",self.lista[i]["CORREO ELECTRONICO"])
                    e=int(input('''EDITAR CONTACTO:
                    1-NOMBRE
                    2-APELLIDO
                    3.TELEFONO
                    4.CORREO
                    5.TODO EL CONTACTO\n->'''))
                    
                    if e==1:
                        f=input('INGRESE EL NUEVO NOMBRE\n->')
                        self.lista[i].update({"NOMBRE":f})
                        print('MODIFICACION EXITOSA (👍≖‿‿≖)👍')
                        self.menu()
                        
                    if e==2:
                         
                         g=input('INGRESE EL NUEVO APELLIDO\n->')
                         self.lista[i].update({"APELLIDO":g})
                         print('MODIFICACION EXITOSA')
                         self.menu()
                    if e==3:
                         
                         h=int(input('INGRESE EL NUEVO TELEFONO\n->'))
                         self.lista[i].update({"TELEFONO":h})
                         print('MODIFICACION EXITOSA (👍≖‿‿≖)👍')
                         self.menu()     
                    
                    if e==4:
                         
                         j=input('INGRESE EL NUEVO CORREO ELECTRONICO\n->')
                         self.lista[i].update({"CORREO ELECTRONICO":j})
                         print('MODIFICACION EXITOSA (👍≖‿‿≖)👍')
                         self.menu()
                         
                    if e==5:
                         
                         f=input('INGRESE EL NUEVO NOMBRE\n->')
                         g=input('INGRESE EL NUEVO APELLIDO\n->')
                         h=int(input('INGRESE EL NUEVO TELEFONO\n->'))
                         j=input('INGRESE EL NUEVO CORREO ELECTRONICO\n->')
                         self.lista[i].update({"NOMBRE":f,"APELLIDO":g,"TELEFONO":h,"CORREO ELECTRONICO":j})
                         print('MODIFICACION EXITOSA')
                         self.menu()
            if noesta==False:
                
                print("EL CONTACTO CON APELLIDO:",dato,",NO EXISTE (͠◉_◉᷅)")
            


        self.menu()






        
#_____________________________________________________________________________________________
        
    def eliminar(self):
        noesta=False
        a=int(input('''ELIMINAR CONTACTO POR:
        1.NOMBRE
        2.APELLIDO \n->'''))
        if a==1:
            
            dato=input('INGRESE EL NOMBRE DEL CONTACTO A BORRAR\n->')
            s=len(self.lista)
            for i in range(s):
                if(dato==self.lista[i]["NOMBRE"]):
                    self.lista.remove(self.lista[i])
                    noesta=True
                    print("CONTACTO ELIMINADO CON EXITO (͠≖ ͜ʖ͠≖)👌")
                    break
            if noesta==False:
                print("EL CONTACTO CON NOMBRE:",dato,",NO EXISTE (͠◉_◉᷅)")

        if a==2:
            
            
            dato=input('INGRESE EL APELLIDO DEL CONTACTO A BORRAR\n->')
            s=len(self.lista)
            for i in range(s):
                if(dato==self.lista[i]["APELLIDO"]):
                    self.lista.remove(self.lista[i])
                    noesta=True
                    
                    print("CONTACTO ELIMINADO CON EXITO (͠≖ ͜ʖ͠≖)👌")
                    break
            if noesta==False:
                
                print("EL CONTACTO CON APELLIDO:",dato,",NO EXISTE (͠◉_◉᷅)")
            


        self.menu()    
#_____________________________________________________________________________________________


    def menu(self):
        
        print ('''AGENDA TELEFONICA

    1.AÑADIR
    2.LISTAR
    3.BUSCAR
    4.EDITAR
    5.ELIMINAR
    6.CERRAR
    ''')
        op=1
        while op!=6:
            
            op=int(input('DIJITE SU ELECCION:\n'))
            
            
            if op==1:
                
                self.añadir()
                
            elif op==2:
                self.listar()
                
            elif op==3:
                
                self.buscar()
                
            elif op==4:
                self.editar()    
                
            elif op==5:
                self.eliminar()

            elif op==6:
                exit()
            else:
                print('error en ingreso, seleccione menu correcto')
                

#programa principal
agenda=Agenda()
agenda.menu()
        
