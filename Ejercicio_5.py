class vehiculo():
	
	def __init__(self, modelo, pintura , peso , largo):
		self.modelo= modelo
		self.pintura=pintura
		self.peso=peso
		self.largo=largo

	def descripcion(self):
		print('modelo : ',self.modelo,
			'\npintura : ',self.pintura,
			'\npeso: ',self.peso,
			'\nlargo: ',self.largo)

class automovil(vehiculo):
	
	def __init__(self, numero_llantas , chasis , motor ,modelo, pintura , peso , largo):
		super().__init__(modelo, pintura , peso , largo)
		self.numero_llantas=numero_llantas
		self.chasis=chasis
		self.motor=motor
		self.tipo='automovil'

	def descripcion(self):
		super().descripcion()
		print('numero de llantas: ',self.numero_llantas,
			'\nchasis: ',self.chasis,
			'\nmotor: ',self.motor,
			'\nTipo: ',self.tipo)

class camioneta(vehiculo):
	
	def __init__(self, numero_llantas , chasis , motor ,modelo, pintura , peso , largo, x4x4x):
		super().__init__(modelo, pintura , peso , largo)
		self.numero_llantas=numero_llantas
		self.chasis=chasis
		self.motor=motor
		self.x4x4x=x4x4x
		self.tipo='camioneta'

	def descripcion(self):
		super().descripcion()
		print('numero de llantas: ',self.numero_llantas,
			'\nchasis: ',self.chasis,
			'\nmotor: ',self.motor,
			'\n4x4: ',self.x4x4x,
			'\nTipo:',self.tipo)


class camion(vehiculo):

	def __init__(self, numero_llantas , chasis , motor ,modelo, pintura , peso , largo, carga):
		super().__init__(modelo, pintura , peso , largo)
		self.numero_llantas=numero_llantas
		self.chasis=chasis
		self.motor=motor
		self.carga=carga
		self.tipo='camion'

	def descripcion(self):
		super().descripcion()
		print('numero de llantas: ',self.numero_llantas,
			'\nchasis: ',self.chasis,
			'\nmotor: ',self.motor,
			'\ncarga ',self.carga,
			'\nTipo: ',self.tipo)

inventario=list()
while True:
	print('1 para añadir \n2 para ver inventario \n3 salir')
	opcion=str(input('opcion: '))
	if opcion=='1':
		print('1 para añadir automovil',
			'\n2 para añadir camioneta',
			'\n3 para añadir camion')
		opcion2=str(input('opcion: '))
		if opcion2=='1':
			numero_llantas=input('Numero de llantas: ')  
			chasis= input('chasis')  
			motor = input('motor: ')
			modelo =input('modelo: ') 
			pintura =input('pintura')
			peso=input('peso')
			largo=input('largo')
			inventario.append(automovil(numero_llantas , chasis , motor ,modelo, pintura , peso , largo))
		elif opcion2=='2':
			numero_llantas=input('Numero de llantas: ')  
			chasis= input('chasis')  
			motor = input('motor: ')
			modelo =input('modelo: ') 
			pintura =input('pintura ')
			peso=input('peso ')
			largo=input('largo ')
			x4x4x =input('4x4: ')
			inventario.append(camioneta(numero_llantas , chasis , motor ,modelo, pintura , peso , largo, x4x4x))
		elif opcion2=='3':
			numero_llantas=input('Numero de llantas: ')  
			chasis= input('chasis')  
			motor = input('motor: ')
			modelo =input('modelo: ') 
			pintura =input('pintura ')
			peso=input('peso ')
			largo=input('largo ')
			carga =input('carga: ')
			inventario.append(camion(numero_llantas , chasis , motor ,modelo, pintura , peso , largo, carga))
		else:
			print('opcion invalida')
	elif opcion=='2':
		numero_inventario=len(inventario)
		print('-------------------------')
		for i in range(numero_inventario):
			inventario[i].descripcion()
			print('-------------------------')
	elif opcion=='3':
		break
	else:
		print('opcion invalida')