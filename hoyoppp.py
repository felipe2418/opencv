class superuis():
    def __init__ (self):
        self.idd=input('ingrese id de producto: ')
        self.descripcion=input('ingrese el nombre del producto: ')
        self.cantidad=int(input('ingrese la cantidad del producto: '))
        self.marca=input('ingrese marca del producto: ')
        self.precio=float(input('ingres precio de producto: '))

    def etiqueta(self):
        print('su producto tiene las siguientes caracteristicas:\n')
        return self.idd, self.descripcion, self.cantidad, self.marca, self.precio
    
class eledome(superuis):
    def __init__(self):
        super().__init__()
        self.modelo=input('ingrese el modelo del producto: ')
        self.consumo=float(input('ingrese el consumo en watt: '))
        self.color=input('ingrese el color: ')
        
    def etiqueta(self):#polimorfismo y sobre carga de metodos
        return super().etiqueta()+(self.modelo, self.consumo, self.color)
        
class perecederos(superuis):
    def __init__(self):
        super().__init__()
        self.fvenci=input('ingrese fecha de vencimiento del producto: ')
        self.tipo=input('ingrese el tipo de producto: ')
        self.peso=float(input('ingrese el peso: '))
        
    def etiqueta(self):#polimorfismo y sobre carga de metodos
        return super().etiqueta()+(self.fvenci, self.tipo, self.peso)

class textil(superuis):
    def __init__(self):
        super().__init__()
        self.tipotela=input('ingrese el tipo de tela: ')
        self.talla=input('ingrese la talla de la prenda: ')
        self.prenda=input('ingrese si la prenda es masculina o femenina: ')
        
    def etiqueta(self):#polimorfismo y sobre carga de metodos
        return super().etiqueta()+(self.tipotela, self.talla, self.prenda)

class electronicos(superuis):
    def __init__(self):
        super().__init__()
        self.espacio=input('ingrese la capacidad de almacenamiento: ')
        self.consumo=input('ingrese el consumo en watt: ')
        self.color=input('ingrese el color : ')
        
    def etiqueta(self):#polimorfismo y sobre carga de metodos
        return super().etiqueta()+(self.espacio, self.consumo, self.color)
    
    
           
        
    ###### averiguar sobrecarga de metodos
        
    
                                                  
