# Librerias
# ---------------------------------
import matplotlib.pyplot as plt
import numpy as np

## Funciones
# ---------------------------------

def Leer_img(image_file):
	# Esta funcion recibe un string (image_file)
	# y con el comando de matplotlib plt.imread
	# lee la imagen y devuelve un arreglo bidimensional
	# para imagenes en escala de grises o un conjunto
	# de 3 arreglos bidimensionales si es rgb.
	I = plt.imread(image_file)
	return I

def RGB2Grey(I):
	# Esta funcion recibe un arreglo de una imagen rgb
	# la descompone en sus canales y recorre pixel por
	# pixel de cada canal promediando los que estan en
	# la misma posicion y albergando este promedio en 
	# un arreglo bidimensional denominado I_gray.
	Ir = I[:,:,0] # red
	Ig = I[:,:,1] # green
	Ib = I[:,:,2] # blue
	# obtener no. filas y columnas:
	nf,nc = Ir.shape 
	# pre-alocar la salida con ceros:
	I_gray = np.zeros((nf,nc))
	# Recorrer cada canal y promediar:
	for i in range(nf):
		for j  in range(nc):
			pixel_gray = (int(Ir[i,j]) + int(Ig[i,j]) + int(Ib[i,j]))/3 
			I_gray[i,j] = pixel_gray
	return I_gray

def Mostrar_img(I):
	# Esta funcion toma un conjunto de arreglos bidimensionales
	# y si tiene 1 canal lo muestra la imagen que representa en
	# escala de grises y si tiene 3 canales la muestra
	# a color.
	fig, ax = plt.subplots()
	if len(I.shape) == 2:
		im = ax.imshow(I,cmap='gray', vmin=0, vmax=255)
	else:
		im = ax.imshow(I)
	ax.axis('off')
	plt.show()

def Rotar_90_img(I):
	# Esta funcion recibe un arreglo bidimensional de 1 canal
	# y genera un nuevo arreglo I_new el cual tiene
	# rotados sus pixeles 90° en el sentido horario.

	# obtener no. filas y columnas:
	nf,nc = I.shape
	# Si la imagen es rectangular hacer esto:
	if nf > nc or nc > nf:
		nf_new = nc
		nc_new = nf
	# Si es cuadrada hacer esto:	
	else:
		nf_new = nf
		nc_new = nc
	# Numero para operar la resta:
	N = nc_new
	# pre-alocacion de la salida:
	I_new = np.zeros((nf_new,nc_new))
	# Rotar:
	for i in range(nf):
		for j in range(nc):
			I_new[j,N-1-i] = I[i,j]
	return I_new

def Rotar_n(I,n):
	# Esta funcion rota n veces 90°
	# un arreglo en el sentido horario. 
	for i in range(n):
		I = Rotar_90_img(I)
	return I

def Deflec_x(I):
	# Esta funcion recibe un arreglo bidimensional de un canal
	# y realiza una reflexion de esta con respecto al eje x.

	# obtener no. filas y columnas:
	nf,nc = I.shape
	# pre-alocacion de la salida:
	I_new = np.zeros((nf,nc))
	# Relejo x:
	for i in range(nf):
		for j in range(nc):
			I_new[nf-1-i,j] = I[i,j]
	return I_new

def Deflec_y(I):
	# Esta funcion recibe un arreglo bidimensional de un canal
	# y realiza una reflexion de esta con respecto al eje y.

	# obtener no. filas y columnas:
	nf,nc = I.shape
	# pre-alocacion de la salida:
	I_new = np.zeros((nf,nc))
	# Relejo y:
	for i in range(nf):
		for j in range(nc):
			I_new[i,nc-1-j] = I[i,j]
	return I_new

def menu():
	# Esta funcion devuelve un string, el cual
	# reprecenta el menu de opciones del programa.
	txt = """

		MI EDITOR DE IMAGEN - MENÚ DE OPCIONES
		========================================
		Seleccione una opción del siguiente menu 
		
		1. Cargar imagen.
		2. Convertir a escala de grises.
		3. Rotar n veces 90° en sentido horario.
		4. Reflectar en el eje x.
		5. Reflectar en el eje y.
		6. Guardar y terminar.

	"""
	return txt
	
# Main
# ----------------------------------


I = np.array([0])
while True:
    print(menu())
    opt = input('>> ')
    if opt == '1':
        try:
            image_file = input('Ingresar nombre de la imagen: ')
            I = Leer_img(image_file)
            Mostrar_img(I)
            print('Dimenciones = ')
            print(I.shape)
        except FileNotFoundError:
            print('Archivo no encontrado, rectificar direccion.')

    elif opt == '2':
        if len(I.shape) == 3:
            I = RGB2Grey(I)
            Mostrar_img(I)
        else:
            print('Para convetir imagen debe ser RGB')
    elif opt == '3':
        if len(I.shape) == 2:
            n = int(input('Ingrese un entero: '))
            I =  Rotar_n(I,n)
            Mostrar_img(I)
        else:
            print('Solo se pueden rotar imagenes en escala de grises')
    elif opt == '4':
        if len(I.shape) == 2:
            I = Deflec_x(I)
            Mostrar_img(I)
        else:
            print('Solo se pueden deflectar imagenes en escala de grises')
    elif opt == '5':
        if len(I.shape) == 2:
            I = Deflec_y(I)
            Mostrar_img(I)
        else:
            print('Solo se pueden deflectar imagenes en escala de grises')
    elif opt == '6':
        print('¿Desea guardar?')
        opt2 = input('y/n : ')
        if opt2 == 'y':
            file_save = input('Nombre de Archivo: ')
            plt.imsave(file_save, I, cmap='gray')
            print('GRACIAS POR USAR EL PROGRAMA')
            break
        elif opt2 == 'n':
            print('GRACIAS POR USAR EL PROGRAMA')
            break
        else:
            print('No es una opcion valida intente nuevamente')
    else:
        print('Opcion no valida')
