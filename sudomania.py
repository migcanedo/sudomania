"""
Titulo: sudomania.py 

Descripcion: Este Programa es uno de los clasicos juegos de todos los tiempos, un Sudoku.

Autores: Miguel C. Canedo R. 13-10214

Ultima Actualizacion: 01/04/16
"""

#####################################################
#Funciones
#####################################################
#----------------------------------------------------------------------

#----------------------------------------------------------------------
#Descripcion: Esta Funcion lee un archivo de texto y crea la Matriz Solicion para el Sudoku a realizar.
#Parametros:
#	Entrada:
#		arch : str // representa el nombre del Archivo donde estara el tablero Solucion.
#	Salida:
#		tableroSol : list // Matriz que representara el Tablero Solucion del Juego.
def obtenerTableroSolucion(arch: str) -> list:
	#PRECONDICION:
	assert(True)
	
	with open(arch, 'r') as f:
		lineas = f.readlines()
		
	tableroSol = []
		
	for linea in lineas:
		linea = linea.split()
		tableroSol.append(linea)
	
	#POSTCONDICION:
	assert((len(tableroSol) == 9 and all((len(tableroSol[i]) == 9) for i in range(9))) \
			or (len(tableroSol) == 6 and all((len(tableroSol[i]) == 6) for i in range(6))))
	
	return tableroSol


#----------------------------------------------------------------------
#Descripcion: Esta Funcion borra todos aquellos numero que no tengan un asterisco(Si lo tienen significan que son pistas para el Sudoku a realizar). 
#Parametros:
#	Entrada:
#		tableroSol : list // Matriz que representara el Tablero Solucion del Juego.
#	Salida:
#		tableroJuego : list // Matriz que representara al Tablero donde se Jugara.
def inicializarTablero(tableroS: list) -> list:
	#PRECONDICION:
	assert(True)
	
	tableroJuego = tableroS
	
	for fila in tableroJuego:
		for numero in fila:
			fi = tableroJuego.index(fila)
			num = tableroJuego[fi].index(numero)
				
			if not('*' in numero):
				tableroJuego[fi][num] = " "
	
	#POSTCONDICION			
	assert((len(tableroJuego) == 9 and all((len(tableroJuego[i]) == 9) for i in range(9))) \
			or (len(tableroJuego) == 6 and all((len(tableroJuego[i]) == 6) for i in range(6))))
	
	return tableroJuego

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#DIBUJAR EN PANTALLA PYGAME
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#----------------------------------------------------------------------
#Descripcion: Esta Funcion Crea un Boton en la Pantalla.
#Parametros:
#	screen : Screen // Es la ventana del Juego.
#	fontE : Font // Fuente de usos Varios para textos que aparezcan en la Ventana.
#	mensaje : str // Mensaje que aparecera dentro del Boton q se crea.
#	x : int // Posicion en X donde se ubicara el Boton en pantalla.
#	y : int // Posicion en Y donde se ubicara el Boton en pantalla. 
#	largo : int // Largo que tendra el Boton en pantalla.
#	alto : int // Ancho que tendra el Boton en pantalla.
#	ci : (int, int, int) // Color que tendra el Boton mientras este Inactivo.
#	ca : (int, int, int) // Color que tendra el Boton mientras este Activo.

def boton(screen, fontE, mensaje: str, x: int, y: int, largo: int, alto: int, ci: (int, int,int), ca: (int, int, int)) -> 'void':
	#PRECONDICION:
	assert(True)
	
	xMouse, yMouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x < xMouse < x + largo and y < yMouse < y + alto:
		pygame.draw.rect(screen, ca,((x, y),(largo, alto)))
		
	
	else:
		pygame.draw.rect(screen, ci, ((x, y),(largo, alto)))
		
	textoSuperf = fontE.render(mensaje, True, (255,255,255))
	textoRect = textoSuperf.get_rect()
	textoRect.center = (x + (largo/2), y + (alto/2))
	screen.blit(textoSuperf, textoRect)
	
	#POSTCONDICION
	assert(True)
		
#----------------------------------------------------------------------
#Descripcion: Esta Funcion Siver para tener el cronometro en la pantalla del Juego y asi ontener el tiempo final.
#Parametros:
#	Entrada:	
#		screen : Screen // Es la ventana del Juego.
#		myfont : Font // Fuente de usos Varios para textos que aparezcan en la Ventana.
# 		reloj : Clock // Variable que guarda la funcion pygame.time.Clock()
#		contadorReloj : int // Variable que va contando cuanto tiempo transcurre en la partida.
#		rate : int // Ritmo al que se actualizara el Reloj.
#	Salida:
#		minutos : int // Minutos transcurridos de la partida jugada.
#		segundos : int // Segundos transcurridos de la partida jugada.
def crono(screen, reloj, myfont, contadorReloj: int, rate: int) -> (int, int):
	#PRECONDICION:
	assert(contadorReloj >= 0 and rate >= 0)
	
	segundosT = contadorReloj // rate
	
	minutos = segundosT // 60
	segundos = segundosT % 60
	crono = "Tiempo: {0:02}:{1:02}".format(minutos, segundos)
	
	timer = myfont.render(crono, True, (0, 0, 0))
	screen.blit(timer, (10, 50))
	
	reloj.tick(rate)
	
	#POSTCONDICION
	assert(minutos == segundosT // 60 and segundos == segundosT % 60)
	
	return (minutos, segundos)
	
	
#----------------------------------------------------------------------
#Descripcion: Esta Funcion dibuja lineas en la Interfaz de Pygame de forma que crea el esqueleto del Tablero de Sudoku.
#Parametros:
#	s : Screen // Pantalla del juego.
#	tablero : list // Matriz del Juego la cual se trae para saber su tamaño.
def dibujarTablero(s, tablero: list) -> 'void':
	#PRECONDICION:
	assert(True)
	
	if len(tablero) == 9:
		#Cuadro Grande
		pygame.draw.line(s, (0, 0, 0), (95, 125), (95, 575), 6)
		pygame.draw.line(s, (0, 0, 0), (95, 575), (545, 575), 6)
		pygame.draw.line(s, (0, 0, 0), (545, 575), (545, 125), 6)
		pygame.draw.line(s, (0, 0, 0), (545, 125), (95, 125), 6)
		
		#Horizontales 
		pygame.draw.line(s, (0, 0, 0), (95, 175), (545, 175), 1)
		pygame.draw.line(s, (0, 0, 0), (95, 225), (545, 225), 1)
		pygame.draw.line(s, (0, 0, 0), (95, 275), (545, 275), 6)
		
		pygame.draw.line(s, (0, 0, 0), (95, 325), (545, 325), 1)
		pygame.draw.line(s, (0, 0, 0), (95, 375), (545, 375), 1)
		pygame.draw.line(s, (0, 0, 0), (95, 425), (545, 425), 6)
		
		pygame.draw.line(s, (0, 0, 0), (95, 475), (545, 475), 1)
		pygame.draw.line(s, (0, 0, 0), (95, 525), (545, 525), 1)
		
		#Verticales
		pygame.draw.line(s, (0, 0, 0), (145, 125), (145, 575), 1)
		pygame.draw.line(s, (0, 0, 0), (195, 125), (195, 575), 1)
		pygame.draw.line(s, (0, 0, 0), (245, 125), (245, 575), 6)
		
		pygame.draw.line(s, (0, 0, 0), (295, 125), (295, 575), 1)
		pygame.draw.line(s, (0, 0, 0), (345, 125), (345, 575), 1)
		pygame.draw.line(s, (0, 0, 0), (395, 125), (395, 575), 6)
		
		pygame.draw.line(s, (0, 0, 0), (445, 125), (445, 575), 1)
		pygame.draw.line(s, (0, 0, 0), (495, 125), (495, 575), 1)
	
	elif len(tablero) == 6:
		#Cuadro Grande
		pygame.draw.line(s, (0, 0, 0), (95, 125), (95, 575), 6)
		pygame.draw.line(s, (0, 0, 0), (95, 575), (545, 575), 6)
		pygame.draw.line(s, (0, 0, 0), (545, 575), (545, 125), 6)
		pygame.draw.line(s, (0, 0, 0), (545, 125), (95, 125), 6)
		
		#Horizontales 
		pygame.draw.line(s, (0, 0, 0), (95, 200), (545, 200), 1)
		pygame.draw.line(s, (0, 0, 0), (95, 275), (545, 275), 6)
		pygame.draw.line(s, (0, 0, 0), (95, 350), (545, 350), 1)
		
		pygame.draw.line(s, (0, 0, 0), (95, 425), (545, 425), 6)
		pygame.draw.line(s, (0, 0, 0), (95, 500), (545, 500), 1)
		
		
		#Verticales
		pygame.draw.line(s, (0, 0, 0), (170, 125), (170, 575), 1)
		pygame.draw.line(s, (0, 0, 0), (245, 125), (245, 575), 1)
		pygame.draw.line(s, (0, 0, 0), (320, 125), (320, 575), 6)
	
		
		pygame.draw.line(s, (0, 0, 0), (395, 125), (395, 575), 1)
		pygame.draw.line(s, (0, 0, 0), (470, 125), (470, 575), 1)

	#POSTCONDICION
	assert(True)
	
#----------------------------------------------------------------------
#Descripcion: Esta funcion Dibuja en la Interfaz de Pygame los numero que pertecen al tablero de Sudoku, y al final llama a una funcion extra que se explicara mas adelante que realiza. Tambien esta Funcion si se requiere devulve las posiciones de donde se encuentran las Pistas del Tablero.
#Parametros:
# 	Entrada:
#		screen : Screen // Pantalla del Juego.
#		font : Font // Fuente usada para los numeros que apareceran en la Pantalla.
#		tablero : list // Matriz que hace de Tablero en el cual se esta rellenando enm el juego.

#		poniendoPistas : bool // Parametro de la funcion resaltarCoincidencias.
#		n : int // Parametro de la funcion resaltarCoincidencias.
#		dificultad : str // Parametro de la funcion resaltarCoincidencias.
#		estaFila : bool // Parametro de la funcion resaltarCoincidencias.
#		posCoincidenciaF : (int, int) // Parametro de la funcion resaltarCoincidencias.
#		estaColumna : bool // Parametro de la funcion resaltarCoincidencias.
#		posCoincidenciaC : (int, int) // Parametro de la funcion resaltarCoincidencias.
#		estaRegion : bool // Parametro de la funcion resaltarCoincidencias.
#		posCoincidenciaR : (int, int) // Parametro de la funcion resaltarCoincidencias.
#	Salida:
#		pistas : list // Lista de las Coordenadas donde se encuentran las pistas del tablero. 
def escribirMatriz(screen, font, tablero: list, poniendoPistas: bool, n: int, dificultad: str, estaFila: bool, \
			posCoincidenciaF: (int, int), estaColumna: bool, posCoincidenciaC: (int, int), \
				estaRegion: bool, posCoincidenciaR: (int, int)) -> 'void' or list:

	
	#PRECONDICION:
	assert((len(tablero)== 9 and 0 <= posCoincidenciaF[0] < 9 and 0 <= posCoincidenciaC[0] < 9 \
		and 0 <= posCoincidenciaR[0] < 9 and 0 <= posCoincidenciaF[1] < 9 and 0 <= posCoincidenciaC[1] < 9\
		 and 0 <= posCoincidenciaR[1] < 9) or (len(tablero) == 6 and 0 <= posCoincidenciaF[0] < 6 \
		 and 0 <= posCoincidenciaC[0] < 6 and 0 <= posCoincidenciaR[0] < 6 and 0 <= posCoincidenciaF[1] < 6 \
		 and 0 <= posCoincidenciaC[1] < 6 and 0 <= posCoincidenciaR[1] < 6))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0
			sys.exit()
	
	pistas = [] # :list // Esta Lista tendra guardada las posiciones donde se encuentran los numeros con '*'
	
	#---------------------
	#Para Tablero 9x9
	if len(tablero) == 9:
	
		fi = 0 # :int // Variable Iterable
		while fi < 9:
			num = 0# :int // Variable Iterable
			while num < 9:
				#Tomando las Coordenadas de las Pistas.
				if "*" in tablero[fi][num] and poniendoPistas:
					pistas.append((fi, num))
				
				if len(tablero[fi][num]) == 2:
					numero = font.render(tablero[fi][num][1], True, (20,20,20))
					screen.blit(numero, (110 + 50*num, 140 + 50*fi))
				else:
					numero = font.render(tablero[fi][num], True, (20,20,20))
					screen.blit(numero, (110 + 50*num, 140 + 50*fi))

				num += 1
			fi += 1
	
	
	
	#---------------------
	#Para Tablero 6x6
	elif len(tablero) == 6:
		fi = 0# :int // Variable Iterable
		while fi < 6:
			num = 0# :int // Variable Iterable
			while num < 6:
				#Tomando las Coordenadas de las Pistas.
				if "*" in tablero[fi][num] and poniendoPistas:
					pistas.append((fi, num))
				
				if len(tablero[fi][num]) == 2:
					numero = font.render(tablero[fi][num][1], True, (20,20,20))
					screen.blit(numero, (125 + 75*num, 152 + 75*fi))
				else:
					numero = font.render(tablero[fi][num], True, (20,20,20))
					screen.blit(numero, (125 + 75*num, 152 + 75*fi))

				num += 1
			fi += 1
	
	
	resaltarCoincidencias(screen, font, tablero, n, dificultad, estaFila, posCoincidenciaF, \
				 estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR) #Funcion Explicada mas Abajo.

	
	dibujarTablero(screen, tablero) #Explicada Previamente.
	
	#POSCONDICION
	assert((len(tablero) == 9 and all((all((0 <= pistas[par][i] < 9) for i in range(2))) for par in range(len(pistas)))) or\
		((len(tablero) == 6 and all((all((0 <= pistas[par][i] < 6) for i in range(2))) for par in range(len(pistas))))))
	
	return pistas

		
#----------------------------------------------------------------------
#Descripcion: Esta Funcion dibuja en la Interfaz de Pygame el fondo de las Casillas Pistas del Tablero.
#Parametros:
#	screen : Screen // Pantalla del Juego.
#	pistas : list // Lista que guarda las Coordenadas donde se encuentran las pistas.
#	tablero : list // Matriz que hace de Tablero en el cual se esta rellenando en el juego.
def rellenoCasPista(screen, pistas: list, tablero: list) -> 'void' :
	
	#PRECONDICION:
	assert(True)
	
	#-----------------
	#Para Tablero 9x9
	if len(tablero) == 9:
		for i in pistas:
			pygame.draw.rect(screen, (175,175,175, 85),((95 + 50*i[1], 125 + 50*i[0]),(50, 50)))
	
	#-----------------
	#Para Tablero 6x6
	elif len(tablero) == 6:
		for i in pistas:
			pygame.draw.rect(screen, (175,175,175, 85),((95 + 75*i[1], 125 + 75*i[0]),(75, 75)))
			
	
	#POSTCONDICION:
	assert(True)
			
#----------------------------------------------------------------------
#Descripcion: Esta Funcion devuelve las coordenadas de una casilla del tablero en donde el usuario haya hecho CLICK.
#Parametros:
#	Entrada:
#		tablero : list // Matriz que representa el tablero donde se esta jugando.
#
#		screen : Screen // Parametro de la funcion menuGuardarPartida.
#		fondo : Surface // Parametro de la funcion menuGuardarPartida.
#		fontTit : Font // Parametro de la funcion menuGuardarPartida.
#		fontE : Font // Parametro de la funcion menuGuardarPartida.
#		myfont : Font // Parametro de la funcion menuGuardarPartida.
#		usuario : str // Parametro de la funcion menuGuardarPartida.
#		contadorReloj : int // Parametro de la funcion menuGuardarPartida.
#		dificultad : str // Parametro de la funcion menuGuardarPartida.
#		cantidadPistas : int // Parametro de la funcion menuGuardarPartida.
#		puntajeTotal : int // Parametro de la funcion menuGuardarPartida.
#		factorCobertura : int // Parametro de la funcion menuGuardarPartida.
#		factorJugada : int // Parametro de la funcion menuGuardarPartida.
#		errores : int // Parametro de la funcion menuGuardarPartida.
#		contadorJugadas : int // Parametro de la funcion menuGuardarPartida.
#		contadorAumentado : int // Parametro de la funcion menuGuardarPartida.
#		presionar : int // Parametro de la funcion menuGuardarPartida.
#		tableroS : list // Parametro de la funcion menuGuardarPartida.
#	Salida:
#		casilla : (int, int) // Coordenadas que representan cual casilla fue clickeada por el Jugador.
def resaltarCasilla(screen, fondo, fontTit, fontE, myfont, usuario: str, contadorReloj: int,\
			dificultad: str, cantidadPistas: int, puntajeTotal: int, factorCobertura: int,\
			  factorJugada: int, errores: int, contadorJugadas: int, contadorAumento: int, presionar: int,\
			     tablero: list, tableroS: str) -> (int, int):
	
	#PRECONDICION:
	assert(True)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			menuGuardarPartida(screen, fondo, fontTit, fontE, myfont, usuario, \
						contadorReloj, dificultad, cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
								tablero, tableroS)
	
	casilla = None	
		
	estado = pygame.mouse.get_pressed()# : (bool, bool,bool) // Variable que guarda el estado de los botones del Mouse
	
	if estado[0]:
		x, y = pygame.mouse.get_pos() # : (float, float) // Coordenas donde se encuentre el Mouse.
		
		#-----------------
		#Para Tablero 9x9
		if len(tablero) == 9:
			fi = 0# :int // Variable Iterable
			while fi < 9:
				cas = 0# :int // Variable Iterable
				while cas < 9:
					if (95 + 50*cas <= x <=  145 + 50*cas) and (125 + 50*fi <= y <= 175 + 50*fi):
						casilla = (fi, cas) # : (int, int) // Variable que guarda las coordenadas de la casilla Clickeada.
						break
						
					cas += 1
				fi += 1
		
		#-----------------
		#Para Tablero 6x6
		elif len(tablero) == 6:
			fi = 0# :int // Variable Iterable
			while fi < 6:
				cas = 0# :int // Variable Iterable
				while cas < 6:
					if (95 + 75*cas <= x <=  170 + 75*cas) and (125 + 75*fi <= y <= 200 + 75*fi):
						casilla = (fi, cas) # : (int, int) // Variable que guarda las coordenadas de la casilla Clickeada.
				
					cas += 1
				fi += 1			
			
	#POSTCONDICION:
	assert(estado[0] or(estado[0] and ((len(tablero) == 9 and 0 <= casilla[0] < 9 and 0 <= casilla[1] < 9)\
		or (len(tablero) == 6 and 0 <= casilla[0] < 6 and 0 <= casilla[0] < 6))) \
		  or (not(estado[0]) and casilla == None))
		
	return casilla
		
#----------------------------------------------------------------------
#Descripcion: Esta Funcion Dibuja Lineas en Pygame donde se vera resaltado en que fila y en que columna esta la casilla donde el Usuario haya hecho CLICK.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		casilla : (int, int) // Coordenadas que representan cual casilla fue clickeada por el Jugador.
#		tablero : list // Matriz que representa el tablero el cual se va rellenando en el Juego.
def resaltarFilaColumna(screen, casilla: (int, int), tablero: list) -> 'void':
	
	#PRECONDICION:
	assert((len(tablero) == 9 and 0 <= casilla[0] < 9 and 0 <= casilla[1] < 9)\
		or (len(tablero) == 6 and 0 <= casilla[0] < 6 and 0 <= casilla[0] < 6))
	
	
	fila, columna = casilla #:(int, int) // La Fila y La COlumna donde se Encuentra la Casilla clickeada.
	#-----------
	#Para el tablero 9x9
	if len(tablero) == 9:
		fi = 0 # :int // Variable Iterable
		while fi < 9:
			if fila == fi:
				pygame.draw.line(screen, (255, 0, 0), (95, 125 + 50*fi), (545, 125 + 50*fi), 6)
				pygame.draw.line(screen, (255, 0, 0), (95, 175 + 50*fi), (545, 175 + 50*fi), 6)


			fi += 1
		col = 0 # :int // Variable Iterable
		while col < 9:
			if columna == col:
				pygame.draw.line(screen, (255, 0, 0), (95 + 50*col, 125), (95 + 50*col, 575), 6)
				pygame.draw.line(screen, (255, 0, 0), (145 + 50*col, 125), (145 + 50*col, 575), 6) 	

			col += 1
	#-----------
	#Para el tablero 6x6
	if len(tablero) == 6:
		fi = 0# :int // Variable Iterable
		while fi < 6:
			if fila == fi:
				pygame.draw.line(screen, (255, 0, 0), (95, 125 + 75*fi), (545, 125 + 75*fi), 6)
				
				pygame.draw.line(screen, (255, 0, 0), (95, 200 + 75*fi), (545, 200 + 75*fi), 6)
			
			
			fi += 1
		
		col = 0# :int // Variable Iterable
		while col < 6:
			if columna == col:
				pygame.draw.line(screen, (255, 0, 0), (95 + 75*col, 125), (95 + 75*col, 575), 6)
				pygame.draw.line(screen, (255, 0, 0), (170 + 75*col, 125), (170 + 75*col, 575), 6) 	
			 
			col += 1
			
	#POSTCONDICION:
	assert(True)
	
	
#----------------------------------------------------------------------
#Descripcion: Esta Funcion introduce un numero dado en una casilla dada de una matriz dada 6x6 o 9x9.
#Parametros:
#	Entrada:
#		casilla : (int, int) // Coordenadas que representan cual casilla fue clickeada por el Jugador.
#		numero : str // Numero que sera introducido en el Tablero donde se esta Jugando.
#		tablero : list // Matriz que representa el Tablero donde se esta Jugando.
def escribirNumero(casilla: (int, int), numero: str, tablero: list) -> 'void':
	fila, columna = casilla # : (int, int) // Variable que guarda las coordenadas de la casilla Clickeada.
	
	#PRECONDICION:
	assert(((len(tablero) == 9 and 0 <= casilla[0] < 9 and 0 <= casilla[1] < 9)\
		or (len(tablero) == 6 and 0 <= casilla[0] < 6 and 0 <= casilla[0] < 6)) \
		 and ('1'<= numero <= '9' or numero == ' '))

	fi = 0# :int // Variable Iterable
	while fi < len(tablero):
		cas = 0# :int // Variable Iterable
		while cas < len(tablero):
			if fi == fila and cas == columna:
				if "*" in tablero[fi][cas]:
					tablero[fi][cas] = tablero[fi][cas]
				else:
					tablero[fi][cas] = numero
			
			cas += 1
		fi += 1
	
	#POSTCONDICION
	assert((("*" in tablero[casilla[0]][casilla[1]]) and tablero[casilla[0]][casilla[1]] == tablero[casilla[0]][casilla[1]])\
			or (not("*" in tablero[casilla[0]][casilla[1]]) and tablero[casilla[0]][casilla[1]] == numero))

	
#----------------------------------------------------------------------
#Descripcion: Esta Funcion retornara el numero que el Usuario meta por el Teclado, y borrara en caso q asi lo desee
#Descripcion: Esta Funcion se encargaba de devolver cual numero introducia el usuario por el teclado para luego colocarlo en el Tablero donde se estaba Jugando. Tambien devuelve el contadorReloj para que asi el tiempo siga corriendo mientras el usuario se decide cual numero escoger.
#Parametros:
#	Entrada:
#		contadorReloj : int // Variable que va contando cuanto tiempo va pasando en todo el juego y guarda cuanto tiempo transcurre en esta funcion. Ademas de ser Parametro de la funcion menuGuardarPartida y de la funcion crono.
#		screen : Screen // Parametro de la funcion menuGuardarPartida.
#		fondo : Surface // Parametro de la funcion menuGuardarPartida.
#		fontTit : Font // Parametro de la funcion menuGuardarPartida.
#		fontE : Font // Parametro de la funcion menuGuardarPartida.
#		myfont : Font // Parametro de la funcion menuGuardarPartida.
#		nombre : str // Parametro de la funcion menuGuardarPartida.
#		dificultad : str // Parametro de la funcion menuGuardarPartida.
#		tableroJuego : list // Parametro de la funcion menuGuardarPartida.
#		tableroS : list // Parametro de la funcion menuGuardarPartida.
#		cantidadPistas : int // Parametro de la funcion menuGuardarPartida.
#		puntajeTotal : int // Parametro de la funcion menuGuardarPartida.
#		factorCobertura : int // Parametro de la funcion menuGuardarPartida.
#		factorJugada : int // Parametro de la funcion menuGuardarPartida.
#		errores : int // Parametro de la funcion menuGuardarPartida.
#		contadorJugadas : int // Parametro de la funcion menuGuardarPartida.
#		contadorAumentado : int // Parametro de la funcion menuGuardarPartida.
#		presionar : int // Parametro de la funcion menuGuardarPartida.
#
# 		reloj : Clock // Variable que guarda la funcion pygame.time.Clock()
#		rate : int // Ritmo al que se actualizara el Reloj.
#	Salida:
#		contadorReloj : int // Variable que va contando cuanto tiempo transcurre en la partida y al ser este un ciclo sin fin hasta q el usuario meta un numero, entonces esta variable seguira contando aqui dentro y actualizara el reloj de la pantalla del juego al salir.
#		numero : str // Variable que representara cual numero el Usuario ha introducido por el teclado.		
def introducirNumero(screen, fondo, fontTit, fontE, myfont, nombre: str, contadorReloj: int, dificultad: str, \
			cantidadPistas: int, puntajeTotal: int, factorCobertura: int, factorJugada: int, \
			  errores: int, contadorJugadas: int, contadorAumento: int, presionar: int, tableroJuego: list, \
			    tableroS: list, reloj: int, rate: int) -> (str, int) or (None, int):
	
	#PRECONDICION:
	assert(True)
	
	while True:
		event = pygame.event.poll() 		
		if event.type == pygame.QUIT:
			menuGuardarPartida(screen, fondo, fontTit, fontE, myfont, nombre, \
						contadorReloj, dificultad, cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar, \
								tableroJuego, tableroS)
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				return ("1", contadorReloj)
			elif event.key == pygame.K_2:
				return ("2", contadorReloj)
			elif event.key == pygame.K_3:
				return ("3", contadorReloj)
			elif event.key == pygame.K_4:
				return ("4", contadorReloj)
			elif event.key == pygame.K_5:
				return ("5", contadorReloj)
			elif event.key == pygame.K_6:
				return ("6", contadorReloj)
			elif event.key == pygame.K_BACKSPACE:
				return (" ", contadorReloj)
			elif event.key == pygame.K_SPACE:
				return (" ", contadorReloj)
			if len(tableroJuego) > 6:
				if event.key == pygame.K_7:
					return ("7", contadorReloj)
				elif event.key == pygame.K_8:
					return ("8", contadorReloj)
				elif event.key == pygame.K_9:
					return ("9", contadorReloj)
				
			else:
				return(None, contadorReloj)
	
		elif event.type == pygame.MOUSEBUTTONDOWN:
			return (None, contadorReloj)
	
		else:
			pass
		
		
		crono(screen, reloj, myfont, contadorReloj, rate)
		contadorReloj += 2
		reloj.tick(rate)
	
	#POSTCONDICION:
	assert(True)

#----------------------------------------------------------------------
#Descripcion: Esta Funcion resaltara de verde todas aquellas coincidencias que conciga en el tablero del numero que se encuentre en la casilla clickeada por el usuario.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fontNum : Font // Fuente de Texto que se utiliza para los numero en el tablero.
#		casilla : (int, int) // Coordenadas que representan cual casilla fue clickeada por el Jugador.
#		tablero : list // Matriz que representa el tablero en el cula se esta Jugando.
def resaltarNumerosCorrectos(screen, fontNum, casilla: (int, int), tablero: list) -> 'void':
	
	#PRECONDICION:
	assert((len(tablero) == 9 and 0 <= casilla[0] < 9 and 0 <= casilla[1] < 9)\
		or (len(tablero) == 6 and 0 <= casilla[0] < 6 and 0 <= casilla[0] < 6))
	
	fila, columna = casilla # : (int, int) // Variable que guarda las coordenadas de la casilla Clickeada.
	
	
	if tablero[fila][columna] != " ":
		numeroCasilla = tablero[fila][columna].replace('*', '')
		
		#------------------------
		#Para la Matriz 9x9
		if len(tablero) == 9:
			fi = 0# :int // Variable Iterable
			while fi < 9:
				col = 0# :int // Variable Iterable
				while col < 9:
					num = tablero[fi][col].replace('*', '')
					
					if num == numeroCasilla:
						numero = fontNum.render(num, True, (0, 200, 0))
						screen.blit(numero, (110 + 50*col, 140 + 50*fi))
					
					col += 1
				
				fi += 1
				
		#-----------------------
		#Para la Matriz 6x6
		elif len(tablero) == 6:
			fi = 0# :int // Variable Iterable
			while fi < 6:
				col = 0# :int // Variable Iterable
				while col < 6:
					num = tablero[fi][col].replace('*', '')
				
					if num == numeroCasilla:
						numero = fontNum.render(num, True, (0, 130, 0))
						screen.blit(numero, (125 + 75*col, 152 + 75*fi))
				
					col += 1
				
				fi += 1

	#POSTCONDICION:
	assert(True)



#------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion resalta la Casilla donde este colocado el Indicador del Mouse y al darle click devolvera cual fue la Casilla clickeada, la cual sera resuelta por el Juego posteriormente.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego. Ademas Parametro de la Funcion Escribir Matriz.
#		tableroJuego : list // Matriz que representa el tablero que se esta jugando. Ademas Parametro de la Funcion Escribir Matriz.
#		
#		fontNum : Font // Parametro de la Funcion Escribir Matriz.
#		poniendoListas : bool // Parametro de la Funcion Escribir Matriz.
#		n : int // Parametro de la Funcion Escribir Matriz.
#		dificultad : str // Parametro de la Funcion Escribir Matriz.
#		estaFila : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaF : (int, int) // Parametro de la Funcion Escribir Matriz.
#		estaColumna : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaC : (int, int) // Parametro de la Funcion Escribir Matriz.
#		estaRegion : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaR : (int, int) // Parametro de la Funcion Escribir Matriz.
#	Salida:
#		fi : int // Representa cual fue la Fila que selecciono el Usuario dandole click.
def selecCasillaAyuda(screen, fontNum, tableroJuego: list, poniendoPistas: bool, n: int, dificultad: str, estaFila: bool, \
		    posCoincidenciaF: (int, int), estaColumna: bool, posCoincidenciaC: (int, int), \
		      estaRegion: bool, posCoincidenciaR: (int, int)) -> int:
	
	if len(tableroJuego) == 9:
		while True:
			screen.blit(fondo, (0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()

			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
	
			for fi in range(9):
				for col in range(9):
					if 95 + 50*col < xMouse < 145 + 50*col and 125 + 50*fi < yMouse < 175 + 50*fi:
						pygame.draw.rect(screen, (255, 255, 0, 90),((95 + 50*col, 125+50*fi),(50, 50)))
		 			
		

			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
					posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)


			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			fi = 0
			while fi < 9:
				col = 0
				while col < 9:
					if 95 + 50*col < xMouse < 145 + 50*col and 125 + 50*fi < yMouse < 175 + 50*fi \
														and click[0]:
						#POSTCONDICION:
						assert((len(tableroJuego) == 9 and 0 <= fi < 9 and 0 <= col < 9))
			
						return fi, col
					 
					col += 1
				fi += 1		
			pygame.display.update()

	
	elif len(tableroJuego) == 6:
		while True:
			screen.blit(fondo, (0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()

			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
	
			for fi in range(6):
				for col in range(6):
					if 95 + 75*col < xMouse < 170 + 75*col and 125 + 75*fi < yMouse < 200 + 75*fi:
						pygame.draw.rect(screen, (255, 255, 0, 90),((95 + 75*col, 125+75*fi),(75, 75)))
		 			
		

			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
					posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)


			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			fi = 0
			while fi < 6:
				col = 0
				while col< 6:
					if 95 + 75*col < xMouse < 170 + 75*col and 125 + 75*fi < yMouse < 200 + 75*fi \
														and click[0]:
						#POSTCONDICION:
						assert((len(tableroJuego) == 6 and 0 <= fi < 6 and 0 <= col < 6))
			
						return fi, col
					 
					col += 1
				fi += 1		
			pygame.display.update()


#------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion resalta la Fila donde este colocado el Indicador del Mouse y al darle click devolvera cual fue la Fila clickeada, la cual sera resuelta por el Juego postriormente.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego. Ademas Parametro de la Funcion Escribir Matriz.
#		tableroJuego : list // Matriz que representa el tablero que se esta jugando. Ademas Parametro de la Funcion Escribir Matriz.
#		
#		fontNum : Font // Parametro de la Funcion Escribir Matriz.
#		poniendoListas : bool // Parametro de la Funcion Escribir Matriz.
#		n : int // Parametro de la Funcion Escribir Matriz.
#		dificultad : str // Parametro de la Funcion Escribir Matriz.
#		estaFila : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaF : (int, int) // Parametro de la Funcion Escribir Matriz.
#		estaColumna : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaC : (int, int) // Parametro de la Funcion Escribir Matriz.
#		estaRegion : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaR : (int, int) // Parametro de la Funcion Escribir Matriz.
#	Salida:
#		fi : int // Representa cual fue la Fila que selecciono el Usuario dandole click.
def selecFilaAyuda(screen, fontNum, tableroJuego: list, poniendoPistas: bool, n: int, dificultad: str, estaFila: bool, \
		    posCoincidenciaF: (int, int), estaColumna: bool, posCoincidenciaC: (int, int), \
		      estaRegion: bool, posCoincidenciaR: (int, int)) -> int:
	
	#PRECONDICION:
	assert(len(tableroJuego) == 9 or len(tableroJuego) == 6)
	
	#------------------------------
	#Para Tablero 9x9
	if len(tableroJuego) == 9:
		while True:
			screen.blit(fondo, (0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()

			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
		
			for fi in range(9):
				if 95 < xMouse < 545 and 125 + 50*fi < yMouse < 175 + 50*fi:
					pygame.draw.rect(screen, (255, 255, 0, 90),((95, 125+50*fi),(450, 50)))
		 			
			

			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
					posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)


			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			fi = 0
			while fi < 9:
				if 95 < xMouse < 545 and 125 + 50*fi < yMouse < 175 + 50*fi and click[0]:
					#POSTCONDICION:
					assert((len(tableroJuego) == 9 and 0 <= fi < 9))
		
					return fi
					
				fi += 1		
				
			pygame.display.update()
			
			
	#------------------------------
	#Para Tablero 6x6
	elif len(tableroJuego) == 6:
		while True:
			screen.blit(fondo, (0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()

			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
		
			for fi in range(6):
				if 95 < xMouse < 545 and 125 + 75*fi < yMouse < 200 + 75*fi:
					pygame.draw.rect(screen, (255, 255, 0, 90),((95, 125+75*fi),(450, 75)))
		 			
			

			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
					posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)


			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			fi = 0
			while fi < 6:
				if 95 < xMouse < 545 and 125 + 75*fi < yMouse < 200 + 75*fi and click[0]:
					#POSTCONDICION:
					assert((len(tableroJuego) == 6 and 0 <= fi < 6))
				
					return fi
			
				fi += 1		
			pygame.display.update()
			
			

#------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion resalta la columna donde este colocado el Indicador del Mouse y al darle click devolvera cual fue la Columna clickeada, la cual sera resuelta por el Juego postriormente.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego. Ademas Parametro de la Funcion Escribir Matriz.
#		tableroJuego : list // Matriz que representa el tablero que se esta jugando. Ademas Parametro de la Funcion Escribir Matriz.
#		
#		fontNum : Font // Parametro de la Funcion Escribir Matriz.
#		poniendoListas : bool // Parametro de la Funcion Escribir Matriz.
#		n : int // Parametro de la Funcion Escribir Matriz.
#		dificultad : str // Parametro de la Funcion Escribir Matriz.
#		estaFila : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaF : (int, int) // Parametro de la Funcion Escribir Matriz.
#		estaColumna : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaC : (int, int) // Parametro de la Funcion Escribir Matriz.
#		estaRegion : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaR : (int, int) // Parametro de la Funcion Escribir Matriz.
#	Salida:
#		col : int // Representa cual fue la Columna que selecciono el Usuario dandole click.
def selecColumnaAyuda(screen, fontNum, tableroJuego: list, poniendoPistas: bool, n: int, dificultad: str, estaFila: bool, \
			posCoincidenciaF: (int, int), estaColumna: bool, posCoincidenciaC: (int, int), \
			  estaRegion: bool, posCoincidenciaR: (int, int)) -> int:
	
	#PRECONDICION:
	assert(len(tableroJuego) == 9 or len(tableroJuego) == 6)
	
	if len(tableroJuego) == 9:
		while True:
			screen.blit(fondo, (0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()

			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
		
			for col in range(9):
				if 95 + 50*col < xMouse < 145 + 50*col and 125 < yMouse < 575:
					pygame.draw.rect(screen, (255, 255, 0, 90),((95+50*col, 125),(50, 450)))
		 			
			

			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
					posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)


			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			col = 0
			while col < 9:
				if 95+50*col < xMouse < 145+50*col and 125 < yMouse < 575 and click[0]:
					
					#POSTCONDICION:
					assert(0<= col < 9)

					return col
			
				col += 1		
		
			pygame.display.update()
	
	#------------------------------
	#Para Tablero 6x6
	elif len(tableroJuego) == 6:
		while True:
			screen.blit(fondo, (0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()

			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
		
			for col in range(6):
				if 95 + 75*col < xMouse < 170 + 75*col and 125 < yMouse < 575:
					pygame.draw.rect(screen, (255, 255, 0, 90),((95+75*col, 125),(75, 450)))
		 			
			

			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
					posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)


			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			col = 0
			while col < 6:
				if 95 + 75*col < xMouse < 170 + 75*col and 125 < yMouse < 575 and click[0]:
										
					#POSTCONDICION:
					assert(0<= col < 6)

					return col
			
				col += 1		
		
			pygame.display.update()

#------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion resalta la Region donde este colocado el Indicador del Mouse y al darle click devolvera cual fue la Region clickeada, la cual sera resuelta por el Juego postriormente.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego. Ademas Parametro de la Funcion Escribir Matriz.
#		tableroJuego : list // Matriz que representa el tablero que se esta jugando. Ademas Parametro de la Funcion Escribir Matriz.
#		
#		fontNum : Font // Parametro de la Funcion Escribir Matriz.
#		poniendoListas : bool // Parametro de la Funcion Escribir Matriz.
#		n : int // Parametro de la Funcion Escribir Matriz.
#		dificultad : str // Parametro de la Funcion Escribir Matriz.
#		estaFila : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaF : (int, int) // Parametro de la Funcion Escribir Matriz.
#		estaColumna : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaC : (int, int) // Parametro de la Funcion Escribir Matriz.
#		estaRegion : bool // Parametro de la Funcion Escribir Matriz.
#		posCoincidenciaR : (int, int) // Parametro de la Funcion Escribir Matriz.
#	Salida:
#		region : int // Representa cual fue la Region que selecciono el Usuario dandole click.
def selecRegionAyuda(screen, fontNum, tableroJuego: list, poniendoPistas: bool, n: int, dificultad: str, \
			estaFila: bool, posCoincidenciaF: (int, int), estaColumna: bool,\
			  posCoincidenciaC: (int, int), estaRegion: bool, posCoincidenciaR: (int, int)) -> int:
	
	#PRECONDICION:
	assert(len(tableroJuego) == 9 or len(tableroJuego) == 6)
	
	#--------------------------
	#Para Tablero 9x9
	if len(tableroJuego) == 9:
		while True:
			screen.blit(fondo, (0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()

			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
		
			for fi in range(3):
				for col in range(3):
					if 95+150*col < xMouse < 245 + 150*col and 125 + 150*fi < yMouse < 275 + 150*fi:
						pygame.draw.rect(screen, (255, 255, 0, 90),((95+150*col, 125+150*fi),(150, 150)))
			 			
			

			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila,\
					 posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)


			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			fi = 0
			while fi < 3:
				col = 0
				while col < 3:
					if 95+150*col < xMouse < 245 + 150*col and \
						125 + 150*fi < yMouse < 275 + 150*fi and click[0]:
						region = col + fi*3
						
						#POSTCONDICION:
						assert(0 <= region < 9)

						return region
			
					col += 1		
				fi += 1
				
			pygame.display.update()
		
	#--------------------------
	#Para Tablero 6x6
	elif len(tableroJuego) == 6:
		while True:
			screen.blit(fondo, (0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()

			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
		
			for fi in range(3):
				for col in range(2):
					if 95+225*col < xMouse < 320 + 225*col and 125 + 150*fi < yMouse < 275 + 150*fi:
						pygame.draw.rect(screen, (255, 255, 0, 90),((95+225*col, 125+150*fi),(225, 150)))
			 			
			

			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila,\
					 posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)


			xMouse, yMouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			fi = 0
			while fi < 3:
				col = 0
				while col < 2:
					if 95+225*col < xMouse < 320 + 225*col and 125 + 150*fi < yMouse < 275 + 150*fi \
														and click[0]:
						region = col + fi*2
						
						#POSTCONDICION:
						assert(0 <= region < 6)

						return region
			
					col += 1		
				fi += 1
				
			pygame.display.update()

#-------------------------------------------------------------------------------------------------		
#Descripcion: Esta Funcion resuelve una casilla que le jugador haya clickeado, copiando el elemento de esa casilla que esta en tableroS a tableroJ.
#Parametros:
#	Entrada:
#		casilla : (int, int) // Tupla que representa la casilla que se va a resolver.
#		tableroJ : list // Matriz que representa el tablero con el cual se esta jugando.
#		tableroS : list // Matriz que representa el tablero solucion.
def resolverCasilla(casilla: (int, int), tableroJ: list, tableroS: list) -> 'void':
	#PRECONDICION
	assert((len(tableroJ) == 9 and len(tableroS) == 9 and 0 <= casilla[0] < 9 and 0 <= casilla[1] < 9) or\
			(len(tableroJ) == 6 and len(tableroS) == 6 and 0 <= casilla[0] < 6 and 0 <= casilla[1] < 6 ))
			
	fila, columna = casilla
	
	tableroJ[fila][columna] = tableroS[fila][columna]
	
	#POSTCONDICION:
	assert(tableroJ[casilla[0]][casilla[1]] == tableroS[casilla[0]][casilla[1]])

#-------------------------------------------------------------------------------------------------		
#Descripcion: Esta Funcion resuelve la Fila que el usuario haya seleccionado, copiando los elementos del tablero Solucion de dicha fila al tablero del Juego.
#Parametros:
#	Entrada:
#		fila : int // Variable que representa la fila que se va a resolver.
#		tableroJ : list // Matriz que representa el tablero con el cual se esta jugando.
#		tableroS : list // Matriz que representa el tablero solucion.
def resolverFila(fila: int, tableroJ: list, tableroS: list) -> 'void':
	#PRECONDICION
	assert((len(tableroJ) == 9 and len(tableroS) == 9 and 0 <= fila < 9) \
		 or (len(tableroJ) == 6 and len(tableroS) == 6 and 0 <= fila < 6))
		
	for columna in range(len(tableroJ)):
		tableroJ[fila][columna] = tableroS[fila][columna]
		
	#POSTCONDICION:
	assert(all(tableroJ[fila][c] == tableroS[fila][c] for c in range(len(tableroJ))))
	
	
#-------------------------------------------------------------------------------------------------		
#Descripcion: Esta Funcion resuelve la Columna que el usuario haya seleccionado, copiando los elementos del tablero Solucion de dicha columna al tablero del Juego.
#Parametros:
#	Entrada:
#		columna : int // Variable que representa la columna que se va a resolver.
#		tableroJ : list // Matriz que representa el tablero con el cual se esta jugando.
#		tableroS : list // Matriz que representa el tablero solucion.
def resolverColumna(columna: list, tableroJ: list, tableroS: list) -> 'void':
	#PRECONDICION
	assert((len(tableroJ) == 9 and len(tableroS) == 9 and 0 <= columna < 9) \
		 or (len(tableroJ) == 6 and len(tableroS) == 6 and 0 <= columna < 6))
	
	for fila in range(len(tableroJ)):
		tableroJ[fila][columna] = tableroS[fila][columna]

	#POSTCONDICION:
	assert(all(tableroJ[f][columna] == tableroS[f][columna] for f in range(len(tableroJ))))

		
#-------------------------------------------------------------------------------------------------		
#Descripcion: Esta Funcion resuelve la Region que el usuario haya seleccionado, copiando los elementos del tablero Solucion de dicha region al tablero del Juego.
#Parametros:
#	Entrada:
#		region : int // Variable que representa la region que se va a resolver.
#		tableroJ : list // Matriz que representa el tablero con el cual se esta jugando.
#		tableroS : list // Matriz que representa el tablero solucion.
def resolverRegion(region: int, tableroJ: list, tableroS: list) ->'void':
	#PRECONDICION
	assert((len(tableroJ) == 9 and len(tableroS) == 9 and 0 <= region < 9) \
		 or (len(tableroJ) == 6 and len(tableroS) == 6 and 0 <= region < 6))

	#----------------------------
	#Para Tablero 9x9	
	if len(tableroJ) == 9:
		for filaR in range(3):
			for columnaR in range(3):
				if region == filaR*3 + columnaR:
				
					fi = 0 + 3*filaR
					while fi <= 2 + 3*filaR:
						col = 0 + 3*columnaR
						while col <= 2 + 3*columnaR:
							tableroJ[fi][col] = tableroS[fi][col]
						
							col += 1
						fi += 1 

	#----------------------------
	#Para Tablero 6x6
	elif len(tableroJ) == 6:
		for filaR in range(3):
			for columnaR in range(2):
				if region == filaR*2 + columnaR:
				
					fi = 0 + 2*filaR
					while fi <= 1 + 2*filaR:
						col = 0 + 3*columnaR
						while col <= 2 + 3*columnaR:
							tableroJ[fi][col] = tableroS[fi][col]
						
							col += 1
						fi += 1
	
	#POSTCONDICION
	#Todos los elementos de l tablero Juego pertenecientes a la region seleccionada, seran igual a los elementos de dicha region en el tablero Solucion.(Disculpa por ponerlo en palabras, pero no consegui otra forma.)


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#Verificaciones
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-------------------------------------------------------------------------------------------------		
#Descripcion: Esta Funcion Verifica si el numero Introducido por el usuario se repite en la Fila donde se encuentre la casilla Seleccionada.
#Parametros:
#	Entrada:
#		numero : str // Variable que representa el numero que le Jugador introdujo.
#		posicion : (int, int) // Tupla que guarda las coodenadas, en (fila, columna), de la casilla donde se introdujo numero.
#		tablero : list // Matriz que representa el tablero donde se esta Jugando.
#	Salida:
#		esta : bool // Representa si existe un numero igual a 'numero' en la fila a evaluar.
#		fila : int // Representa la fila donde se encuentra el numero repetido, en caso de que exista. 
#		columna : int // Representa la columna donde se encuentra el numero repetido, en caso de que exista.
def verificarFila(numero: str, posicion: (int, int), tablero: list) -> (bool, (int, int)):
	#PRECONDICION
	assert((len(tablero) == 9 and 0 <= posicion[0] < 9 and 0 <= posicion[1] < 9)\
		 or (len(tablero) == 6 and 0 <= posicion[0] < 6 and 0 <= posicion[1] < 6))

	
	esta = False # : bool // Variable que me indicara si el numero deseado esta repetido o no en la fila deseada.
	fila = posicion[0] # :int // Fila a evaluar a ver si se repite el numero.
	col = 0 # :int // ES un entero que tendra guardada la columna donde se repite, si es el caso, el numero a evaluar(Sera None al principio para que retorne vacio en caso de no repertise el numero a evaluar)
	 
	for columna in range(len(tablero)):
		n = tablero[fila][columna].replace('*', '')
		
		if n == numero:
			esta = True # : bool // Variable que me indicara si el numero deseado esta repetido o no en la fila deseada.
			col = columna# :int // Es un entero que tendra guardada la columna donde se repite, si es el caso, el numero a evaluar.
			break
	
	
	#POSTCONDICION:
	assert(True)
	
	return (esta, (fila, col))


#-------------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion Verifica si el numero Introducido por el usuario se repite en la Columna donde se encuentre la casilla Seleccionada.
#Parametros:
#	Entrada:
#		numero : str // Variable que representa el numero que le Jugador introdujo.
#		posicion : (int, int) // Tupla que guarda las coodenadas, en (fila, columna), de la casilla donde se introdujo numero.
#		tablero : list // Matriz que representa el tablero donde se esta Jugando.
#	Salida:
#		esta : bool // Representa si existe un numero igual a 'numero' en la columna a evaluar.
#		fila : int // Representa la fila donde se encuentra el numero repetido, en caso de que exista. 
#		columna : int // Representa la columna donde se encuentra el numero repetido, en caso de que exista.
def verificarColumna(numero: str, posicion: (int, int), tablero: list) -> (bool, (int, int)):
	
	#PRECONDICION
	assert((len(tablero) == 9 and 0 <= posicion[0] < 9 and 0 <= posicion[1] < 9)\
		 or (len(tablero) == 6 and 0 <= posicion[0] < 6 and 0 <= posicion[1] < 6))

	
	esta = False # : bool // Variable que me indicara si el numero deseado esta repetido o no en la columna deseada.
	columna = posicion[1] # :int // Columna a evaluar a ver si se repite el numero.
	fi = 0 # :int // Es un entero que tendra guardada la columna donde se repite, si es el caso, el numero a evaluar.


	for fila in range(len(tablero)):
		n = tablero[fila][columna].replace('*', '')
		
		if n == numero:
			esta = True
			fi = fila # :int // ES un entero que tendra guardada la fila donde se repite, si es el caso, el numero a evaluar.
			break
			
	#POSTCONDICION:
	assert(True)
			
	return (esta, (fi, columna))
#-----------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion Verifica si el numero Introducido por el usuario se repite en la Region donde se encuentre la casilla Seleccionada.
#Parametros:
#	Entrada:
#		numero : str // Variable que representa el numero que le Jugador introdujo.
#		posicion : (int, int) // Tupla que guarda las coodenadas, en (fila, columna), de la casilla donde se introdujo numero.
#		tablero : list // Matriz que representa el tablero donde se esta Jugando.
#	Salida:
#		esta : bool // Representa si existe un numero igual a 'numero' en la columna a evaluar.
#		fila : int // Representa la fila donde se encuentra el numero repetido, en caso de que exista. 
#		columna : int // Representa la columna donde se encuentra el numero repetido, en caso de que exista.
def verificarRegion(numero: str, posicion: (int, int), tablero: list) -> (bool, (int, int)):

	#PRECONDICION
	assert((len(tablero) == 9 and 0 <= posicion[0] < 9 and 0 <= posicion[1] < 9)\
		 or (len(tablero) == 6 and 0 <= posicion[0] < 6 and 0 <= posicion[1] < 6))

	
	esta = False
	filaEsta, columnaEsta = 0, 0
	
	
	fila, columna = posicion
	if len(tablero) == 9:
		for regionF in range(3):
			for regionC in range(3):
				if 0 + 3*regionF <= fila <= 2 + 3*regionF and 0 +3*regionC <= columna <= 2 + 3*regionC:
					regionFila = regionF
				
					regionColumna = regionC
	
		fi = 0 + 3*regionFila
		while fi <= 2 + 3*regionFila:
			col = 0 + 3*regionColumna
			while col <= 2 + 3*regionColumna:
				num = tablero[fi][col].replace('*', '') 
			
				if numero == num:
					esta = True
					filaEsta = fi
					columnaEsta = col
					break
				
				col += 1
			fi += 1 
		
		#POSTCONDICION:
		assert(True)
		
		return (esta, (filaEsta, columnaEsta))


	#----------------------------
	#Para Tablero 6x6
	elif len(tablero) == 6:
		for regionF in range(3):
			for regionC in range(2):
				if 0 + 2*regionF <= fila <= 1 + 2*regionF and 0 + 3*regionC <= columna <= 2 + 3*regionC:
					regionFila = regionF
				
					regionColumna = regionC
	
		fi = 0 + 2*regionFila
		while fi <= 1+ 2*regionFila:
			col = 0 + 3*regionColumna
			while col <= 2 + 3*regionColumna:
				num = tablero[fi][col].replace('*', '') 
			
				if numero == num:
					esta = True
					filaEsta = fi
					columnaEsta = col
					break
					
				col += 1
			fi += 1 
		
		#POSTCONDICION:
		assert(True)
		
		return (esta, (filaEsta, columnaEsta))
#-----------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion verifica si se llena una fila con la ultima casilla llenada. 
#Parametros:
#	Entrada:
#		casilla : (int, int) // Tupla que representa las coordenadas de la ultima casilla lenada.
#		tablerJ : list // Matriz que represnta el tablero con el que se esta jugando.
#		tableroS : list // Matrzi que representa el tablero solucion del tablero con el que se juega.
#	Salida:
#		: bool // Variable que nos dira si se lleno una fila.
def fullFila(casilla: (int, int), tableroJ: list, tableroS: list)-> bool:
	#PRECONDICION
	assert((len(tableroJ) == 9 and len(tableroS) == 9 and 0 <= casilla[0] < 9 and 0 <= casilla[1] < 9)\
		 or (len(tableroJ) == 6 and len(tableroS) == 6 and 0 <= casilla[0] < 6 and 0 <= casilla[1] < 6))
		 	
	fila, columna = casilla
	full = True
	for col in range(len(tableroJ)):
		if (tableroS[fila][col] != tableroJ[fila][col]):
			full = False
			break
	
	#POSTCONDICION
	assert(full <= (all((tableroS[fila][col] == tableroJ[fila][col]) for col in range(len(tableroJ)))))
	
	
	return full
	
#-----------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion verifica si se llena una columna con la ultima casilla llenada.
#Parametros:
#	Entrada:
#		casilla : (int, int) // Tupla que representa las coordenadas de la ultima casilla lenada.
#		tablerJ : list // Matriz que represnta el tablero con el que se esta jugando.
#		tableroS : list // Matrzi que representa el tablero solucion del tablero con el que se juega.
#	Salida:
#		: bool // Variable que nos dira si se lleno una columna.
def fullColumna(casilla: (int, int), tableroJ: list, tableroS: list) -> bool:
	#PRECONDICION
	assert((len(tableroJ) == 9 and len(tableroS) == 9 and 0 <= casilla[0] < 9 and 0 <= casilla[1] < 9)\
		 or (len(tableroJ) == 6 and len(tableroS) == 6 and 0 <= casilla[0] < 6 and 0 <= casilla[1] < 6))
	
	fila, columna = casilla
	full = True
	for fi in range(len(tableroJ)):
		if (tableroS[fi][columna] != tableroJ[fi][columna]):
			full = False
			break
	
	#POSTCONDICION
	assert(full <= (all((tableroS[fi][columna] == tableroJ[fi][columna]) for fi in range(len(tableroJ)))))
		
	return full
	
	
#-----------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion verifica si se llena una fila con la ultima casilla llenada.
#Parametros:
#	Entrada:
#		casilla : (int, int) // Tupla que representa las coordenadas de la ultima casilla lenada.
#		tablerJ : list // Matriz que represnta el tablero con el que se esta jugando.
#		tableroS : list // Matrzi que representa el tablero solucion del tablero con el que se juega.
#	Salida:
#		: bool // Variable que nos dira si se lleno una region.
def fullRegion(casilla: (int, int), tableroJ: list, tableroS: list) -> bool:
	#PRECONDICION
	assert((len(tableroJ) == 9 and 0 <= casilla[0] < 9 and 0 <= casilla[1] < 9)\
		 or (len(tableroJ) == 6 and 0 <= casilla[0] < 6 and 0 <= casilla[1] < 6))

	
	fila, columna = casilla
	full = True
	
	if len(tableroJ) == 9:
		for regionF in range(3):
			for regionC in range(3):
				if 0 + 3*regionF <= fila <= 2 + 3*regionF and 0 +3*regionC <= columna <= 2 + 3*regionC:
					regionFila = regionF
					regionColumna = regionC
					break
	
		fi = 0 + 3*regionFila
		while fi <= 2 + 3*regionFila:
			col = 0 + 3*regionColumna
			while col <= 2 + 3*regionColumna:
				if (tableroS[fi][col] != tableroJ[fi][col]):
					full = False
					break
		
				
				col += 1
			fi += 1 
		
		#POSTCONDICION:
		assert(True)
		
		return full


	#----------------------------
	#Para Tablero 6x6
	elif len(tableroJ) == 6:
		for regionF in range(3):
			for regionC in range(2):
				if 0 + 2*regionF <= fila <= 1 + 2*regionF and 0 + 3*regionC <= columna <= 2 + 3*regionC:
					regionFila = regionF
					regionColumna = regionC
	
		fi = 0 + 2*regionFila
		while fi <= 1+ 2*regionFila:
			col = 0 + 3*regionColumna
			while col <= 2 + 3*regionColumna:
				if tableroJ[fi][col] != tableroS[fi][col]:
					full = False
					break
				col += 1
			fi += 1 
		
		#POSTCONDICION:
		assert(True)
		
		return full
#----------------------------------------------------------------------------------------------
#Descripcion: Esta funcion recorre el tablero entero y verifica si existe algun error.
#Parametros:
#	Entrada:
#		tableroJ : list // Matriz que representa el tablero con el que se esta jugando.
#		tableroS : list // Matriz que representa la solucion del tablero que se esta jugando.
#	Salida:
#		: bool // Variable que representara si hasta ahora el tablero esta llenado de forma correcta.
def comprobarSudoku(tableroJ: list, tableroS: list) -> bool:
	#PRECONDICION
	assert((len(tableroJ) == 9 and len(tableroS) == 9) or (len(tableroJ) == 6 and len(tableroS) == 6))
	
	check = True
	
	for fi in range(len(tableroJ)):
		for col in range(len(tableroJ)):
			if tableroJ[fi][col] != " ":
				if tableroJ[fi][col] != tableroS[fi][col]:
					check = False
	
	#POSTCONDICION
	assert(check <= (all((all(((tableroJ[fi][col] != " ") <= (tableroJ[fi][col] == tableroS[fi][col])) \
						for col in range(len(tableroJ))) for col in range(len(tableroJ))))))
	return check
#----------------------------------------------------------------------------------------------
#Descripcion: Esta funcion se encarga de colocar donde corresponde al nuevo Puntaje obtenido en la Tabla de Records.
#Parametros:
#	Entrada:
#		nombre : str // Variable que guarda el nombre del jugador
#		puntajeFinal : int // Variable que representa cual fue le puntaje final del jugador
#		dificultad : str // Variable que representa que dificultad fue jugada.
#	Salida:
#		: int // Variable que representa la posicion en la cual quedo posicionado el Usuario en la Tabla de Records
def actualizarTablaRecords(nombre: str, puntajeFinal: int, dificultad: str) -> int:
	#PRECONDICION
	assert(True)
	
	if dificultad == "Muy Dificil":
		dificultad = "MuyDificil"
		
	with open('records/records' + dificultad + '.txt', 'r') as f:
		arch = f.readlines()
		
	tabla = []
	
	for posicion in arch:
		posicion = posicion.split()
		posicion[1] = int(posicion[1])
		tabla.append(posicion)
		
	pos = 0
	while pos < len(tabla):
		if puntajeFinal > tabla[pos][1]:
			tabla.insert(pos, [nombre, puntajeFinal])
			break
		pos += 1
	
	if len(tabla) > 5:
		tabla = tabla[:-1]
		
		
	with open('records/records' + dificultad + '.txt', 'w') as h:
		for posicion in tabla:
			posicion[1] = str(posicion[1])
			posicion = " ".join(posicion)
			h.write(posicion + "\n")

	#POSTCONDICION
	assert(True)

	return pos	
		
		 
#-----------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion Resalta de verde todos aquellos numeros del Tablero Completo que sean sean iguales al de la casilla Clickeada por el Usuario.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego. Ademas Parametro de la Funcion Escribir Matriz.
#		fontNum : Font // Fuente de Texto usada para los numeros que se presentan en el tablero.
#		tablero : list // Matriz que representa el tablero que se esta jugando. Ademas Parametro de la Funcion Escribir Matriz.
#		n : int // Numero el cual introdujo el Jugador.
#		dificultad : str // Representa cual es el nivel de dificultad el cual se esta Jugando.
#		estaFila : bool // Representa si el numero se repite o no en la fila donde se coloco.
#		posCoincidenciaF : (int, int) // En caso de encontrarse uno igual en la fila, esta variable guardara la posicion de la coincidencia.
#		estaColumna : bool // Representa si el numero se repite o no en la columna donde se coloco.
#		posCoincidenciaC : (int, int) // En caso de encontrarse uno igual en la columna, esta variable guardara la posicion de la coincidencia.
#		estaRegion : bool // Representa si el numero se repite o no en la region donde se coloco.
#		posCoincidenciaR : (int, int) // En caso de encontrarse uno igual en la region, esta variable guardara la posicion de la coincidencia.
def resaltarCoincidencias(screen, fontNum, tablero: list, n: int, dificultad: str, estaFila: bool, \
			   posCoincidenciaF: (int, int), estaColumna: bool, posCoincidenciaC: (int, int), \
			     estaRegion: bool, posCoincidenciaR: (int, int)) -> 'void':
	#PRECONDICION
	assert((len(tablero)== 9 and 0 <= posCoincidenciaF[0] < 9 and 0 <= posCoincidenciaC[0] < 9 \
		and 0 <= posCoincidenciaR[0] < 9 and 0 <= posCoincidenciaF[1] < 9 and 0 <= posCoincidenciaC[1] < 9\
		 and 0 <= posCoincidenciaR[1] < 9) or (len(tablero)== 6 and 0 <= posCoincidenciaF[0] < 6 \
		 and 0 <= posCoincidenciaC[0] < 6 and 0 <= posCoincidenciaR[0] < 6 and 0 <= posCoincidenciaF[1] < 6 \
		 and 0 <= posCoincidenciaC[1] < 6 and 0 <= posCoincidenciaR[1] < 6))
	
	#----------------------------
	#Para Tablero 9x9
	if len(tablero) == 9:
		if estaFila and (("Entrenamiento" in dificultad) or dificultad == "Facil"):
			numero = fontNum.render(n, True, (200, 0, 0))
			screen.blit(numero, (110 + 50*posCoincidenciaF[1], 140 + 50*posCoincidenciaF[0]))
	
		if estaColumna and (("Entrenamiento" in dificultad) or dificultad == "Facil"):
			numero = fontNum.render(n, True, (200, 0, 0))
			screen.blit(numero, (110 + 50*posCoincidenciaC[1], 140 + 50*posCoincidenciaC[0]))
		
		
		if estaRegion and (("Entrenamiento" in dificultad) or dificultad == "Facil"):
			numero = fontNum.render(n, True, (200, 0, 0))
			screen.blit(numero, (110 + 50*posCoincidenciaR[1], 140 + 50*posCoincidenciaR[0]))
					
		if not(estaFila) and not(estaColumna) and not(estaRegion) and ("Entrenamiento" in dificultad):
			for fi in range(9):
				for col in range(9):
					num = tablero[fi][col].replace('*', '')
					
					if num == n:
						numero = fontNum.render(n, True, (0, 130, 0))
						screen.blit(numero, (110 + 50*col, 140 + 50*fi))
	
	
	
	elif len(tablero) == 6:
		
		if estaFila and (("Entrenamiento" in dificultad) or dificultad == "Facil"):
			numero = fontNum.render(n, True, (200, 0, 0))
			screen.blit(numero, (125 + 75*posCoincidenciaF[1], 152 + 75*posCoincidenciaF[0]))
	
		if estaColumna and (("Entrenamiento" in dificultad) or dificultad == "Facil"):
			numero = fontNum.render(n, True, (200, 0, 0))
			screen.blit(numero, (125 + 75*posCoincidenciaC[1], 152 + 75*posCoincidenciaC[0]))		
		
		if estaRegion and (("Entrenamiento" in dificultad) or dificultad == "Facil"):
			numero = fontNum.render(n, True, (200, 0, 0))
			screen.blit(numero, (125 + 75*posCoincidenciaR[1], 152 + 75*posCoincidenciaR[0]))
					
		if not(estaFila) and not(estaColumna) and not(estaRegion) and ("Entrenamiento" in dificultad):
			for fi in range(6):
				for col in range(6):
					num = tablero[fi][col].replace('*', '')
					
					if num == n:
						numero = fontNum.render(n, True, (0, 130, 0))
						screen.blit(numero, (125 + 75*col, 152 + 75*fi))	
	
	#POSTCONDICION:
	assert(True)

#--------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion comprueba y verifica cual es el nivel de perimos que tiene un jugador. Retorna dicho valor.
#Parametros:
#	Entrada:
#		nombre : str // Variable que representa el Nombre del Jugador.
#	Salida
#		: int // Variable que representa cual es el nivel de Permiso el cual le coloca al Jugador.
def comprobarPermisos(nombre: str) -> int:
	with open('admin/permisos.txt', 'r') as f:
		archivo = f.readlines()
	
	permisos = []

	for linea in archivo:
		linea = linea.split()
		linea[1] = int(linea[1])
		permisos.append(linea)
		
	for p in permisos:
		if p[0] == nombre:
			return p[1]
			
#--------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion se encarga de actualizar los permisos que obtiene un Jugador, dependiendo del Nivel que haya pasado.
#Parametros:
#	Entrada:
#		nombre : str // Variable que representa el Nombre del Jugador.
#		permisoConsedido : int // Variable que representa cual es el nivel de Permiso el cual le coloca al Jugador.
def actualizarPermisos(nombre: str, permisoConsedido: int) -> 'void': 
	with open('admin/permisos.txt', 'r') as f:
		archivo = f.readlines()
			
	permisos = []
	esta = False
	
	for linea in archivo:
		linea = linea.split()
		linea[1] = int(linea[1])
		permisos.append(linea)
		
	for p in permisos:
		if p[0] == nombre:
			esta = True
			if p[1] < permisoConsedido:
				p[1] = permisoConsedido
	
	if not(esta):
		permisos.append([nombre, permisoConsedido])
		
		
	with open('admin/permisos.txt', 'w') as h:
		for p in permisos:
			p[1] = str(p[1])
			p = " ".join(p)+"\n"
			h.write(p)
	

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#MENUS
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#----------------------------------------------------------------------
#Descripcion: Esta Funcion es la que presenta el Menu Principal en pantalla y devuelve la opcion que el usuario haya elegido.
#Parametros:
# 	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontTit : Font  // Fuente de Texto usada para los titulos.
#		fontE : Font // Fuente de Texto usada en varias ocasiones.
#	Salida:
#		: int // Representa la opcion que el Jugador metio medienate el teclado.
def menuPrincipal(screen, fondo, fontTit, fontE) -> int:
	#PRECONDICION
	assert(True)
	
	while True:
		screen.blit(fondo, (0,0))
		
		menuP = ["1. Crear Partida Nueva.", 
			 "2. Cargar Partida Guardada.", 
			 "3. Ver Tabla de Records.", 
			 "4. Mostrar Ayuda.", 
			 "5. SALIR."] # :list // Lista que guarad las Opciones del Menu Principal
	
		
		titulo = fontTit.render("BIENVENIDO A 'SUDOMANIA'!", True, (0, 0, 255))
		screen.blit(titulo, (5, 70))
	
		pregunta = fontE.render("Que desea Hacer?", True, (0, 0, 255))
		screen.blit(pregunta, (35, 180))
		
		imagen = pygame.image.load('admin/images.jpg')
		screen.blit(imagen, (390, 370))
		
		for opcion in menuP:
			texto = myfont.render(opcion, True, (0, 0, 255))
			screen.blit(texto, (100, 230+(25*menuP.index(opcion))))
	
		#Eventos realizados.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					return 1
				
				elif event.key == pygame.K_2:
					return 2
				
				elif event.key == pygame.K_3:
					return 3
				
				elif event.key == pygame.K_4:
					return 4
				
				elif event.key == pygame.K_5:
					running = 0
					sys.exit()
	
		pygame.display.update()
		
		#POSTCONDICION:
		assert(True)
		


#----------------------------------------------------------------------
#Descripcion: Esta Funcion presenta en pantalla el Menu de la Opcion de Crear Partida, en la cual el Usuario decide que dificultad quiere jugar, y devuelve dicha opcion seleccionada.
#Parametros:
# 	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontE : Font // Fuente de Texto usada en varias ocasiones.
#		myfont : Font // Fuente de Texto usada en varias ocasiones.
#	Salida:
#		: int // Representa la opcion que el Jugador metio medienate el teclado.
def opcionCrearPartida(screen, fondo, fontE, myfont)-> int:
	#PRECONDICION
	assert(True)
	
	while True:
		screen.blit(fondo, (0,0))
		
		menuCrearPartida = ["1. Entrenamiento.", 
				    "2. Facil.", 
				    "3. Dificil.", 
				    "4. Muy Dificil."] # : list // Lista que guarda las opciones del Menu de Crear Partida.
	
		pregunta = fontE.render("Que Dificultad Desea?", True, (0, 0, 255), 15)
		screen.blit(pregunta, (35, 180))	
	
		for opcion in menuCrearPartida:
			texto = myfont.render(opcion, True, (0, 0, 255))
			screen.blit(texto, (100, 230+(25*menuCrearPartida.index(opcion))))
		
		#Eventos Realizados.		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					return 1	
				elif event.key == pygame.K_2:
					return 2					
				elif event.key == pygame.K_3:
					return 3
				elif event.key == pygame.K_4:
					return 4				
		pygame.display.update()
		
		#POSTCONDICION:
		assert(True)
		


#----------------------------------------------------------------------
#Descripcion: Esta funcion presenta en pantalla un Menu en el cual el Usuario debera elegir el tamaño del tablero que quiere jugar, y devolvera dicha seleccion.
#Parametros:
# 	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontE : Font // Fuente de Texto usada en varias ocasiones.
#		myfont : Font // Fuente de Texto usada en varias ocasiones.
#	Salida:
#		: int // Representa la opcion que el Jugador metio medienate el teclado.
def crearEntrenamiento(screen, fondo, fontE, myfont) -> int:
	#PRECONDICION
	assert(True)
	
	while True:
		screen.blit(fondo, (0,0))
		
		tiposTablero = ["1. 6x6", 
				"2. 9x9"] # : list // Lista que guarda las opciones de los tipos de Tablero Jugables.
	
		pregunta = fontE.render("Elija Tipo de Tablero", True, (0, 0, 255), 15)
		screen.blit(pregunta, (35, 180))	
		
		for opcion in tiposTablero:
			texto = myfont.render(opcion, True, (0, 0, 255))
			screen.blit(texto, (100, 230+(25*tiposTablero.index(opcion))))
		
		#Eventos Realizados.
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit()
				
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						return 1
					elif event.key == pygame.K_2:
						return 2
						
		pygame.display.update()
		
		#POSTCONDICION:
		assert(True)
		
		
#-------------------------------------------------------------------------
#Descripcion: Esta Funcion presenta en pantalla cuantos tableros existen del nivel seleccionado por el Usuario y el debe elegir cual jugar. Devolvera la opcion seleccionada.
#Parametros:
# 	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontE : Font // Fuente de Texto usada en varias ocasiones.
#		myfont : Font // Fuente de Texto usada en varias ocasiones.
#	Salida:
#		: int // Representa la opcion que el Jugador metio medienate el teclado.
def elegirTablero(screen, fondo, fontE, myfont) -> int:
	#PRECONDICION
	assert(True)
	
	
	while True:
		screen.blit(fondo, (0,0))
		
		pregunta = fontE.render("Elija Tablero", True, (0, 0, 255))
		screen.blit(pregunta, (35, 180))
		
		opciones = myfont.render("DEL 1 AL 3", True, (0,0,255))	
		screen.blit(opciones, (60, 220))
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					return 1						
				elif event.key == pygame.K_2:
					return 2
				elif event.key == pygame.K_3:
					return 3
								
		pygame.display.update()
		
		#POSTCONDICION:
		assert(True)
		
		
#--------------------------------------------------------------------------------
#Descripcion: Esta Funcion presenta en pantalla el Menu de Ayuda del Nivel Entrenamiento, y el usuario elige que desea hacer.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego. Ademas Parametro de las Funciones resolverFilaAyuda, resolverColumnaAyuda, resolverRegionAyuda, selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontE : Font // Fuente de Texto usado en varias ocasiones.
#		myfont : Font // Fuente de Texto usado en varias ocasiones.
#
#		tableroJ : list // Parametro de las Funciones resolverFilaAyuda, resolverColumnaAyuda, resolverRegionAyuda, selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		tableroS : list // Parametro de las Funciones resolverFilaAyuda, resolverColumnaAyuda y resolverRegionAyuda.
#
#		fontNum : Font // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		poniendoListas : bool // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		n : int // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		dificultad : str // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		estaFila : bool // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		posCoincidenciaF : (int, int) // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		estaColumna : bool // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda..
#		posCoincidenciaC : (int, int) // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		estaRegion : bool // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		posCoincidenciaR : (int, int) // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
def menuAyudaEntrenamiento(screen, fondo, fontE, myfont, tableroJ: list, tableroS: list, poniendoPistas: bool, \
				n: int, dificultad: str, estaFila: bool, posCoincidenciaF: (int, int), estaColumna: bool, \
				posCoincidenciaC: (int, int), estaRegion: bool, posCoincidenciaR: (int, int)) -> 'void':
	
	#PRECONDICION
	assert(True)
	
	while True:
		screen.blit(fondo, (0,0))
		numero = 0
		
		menuAyuda = ["1. Resolver Casilla", 
			     "2. Resolver Fila.", 
			     "3. Resolver Columna.", 
			     "4. Resolver Region.", 
			     "5. ATRAS"] # : list // Lista que guarda las opciones del Menu de Crear Partida.
	
		pregunta = fontE.render("Que Desea Hacer?", True, (0, 0, 255), 15)
		screen.blit(pregunta, (35, 180))	
	
		for opcion in menuAyuda:
			texto = myfont.render(opcion, True, (0, 0, 255))
			screen.blit(texto, (100, 230+(25*menuAyuda.index(opcion))))
				
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					casilla = selecCasillaAyuda(screen, fontNum, tableroJ, poniendoPistas,\
									    n, dificultad, estaFila, posCoincidenciaF,\
									    estaColumna, posCoincidenciaC,\
									    estaRegion, posCoincidenciaR)
									    
					resolverCasilla(casilla, tableroJ, tableroS)

				elif event.key == pygame.K_2:
					fila = selecFilaAyuda(screen, fontNum, tableroJ, poniendoPistas, n, dificultad, \
							estaFila, posCoincidenciaF, estaColumna, posCoincidenciaC,\
							estaRegion, posCoincidenciaR)
					
					resolverFila(fila, tableroJ, tableroS)
					
					
										
				elif event.key == pygame.K_3:
					columna = selecColumnaAyuda(screen, fontNum, tableroJ, poniendoPistas, n, dificultad, \
								estaFila, posCoincidenciaF, estaColumna, posCoincidenciaC, \
								estaRegion, posCoincidenciaR)
					
					resolverColumna(columna, tableroJ, tableroS)
					
					
					
				elif event.key == pygame.K_4:
					region = selecRegionAyuda(screen, fontNum, tableroJ, poniendoPistas, n, dificultad, \
								estaFila, posCoincidenciaF, estaColumna, posCoincidenciaC,\
								estaRegion, posCoincidenciaR)
					
					resolverRegion(region, tableroJ, tableroS)
					
					
					
				elif event.key == pygame.K_5:
					numero = 4
			
		if numero == 4:
			break
		
		pygame.display.update()
		
		#POSTCONDICION:
		assert(True)
		
#--------------------------------------------------------------------------------
#Descripcion: Esta Funcion presenta en pantalla el Menu de Ayuda del Nivel Facil, y el usuario elige que desea hacer.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego. Ademas Parametro de las Funciones resolverFilaAyuda, resolverColumnaAyuda, resolverRegionAyuda, selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontE : Font // Fuente de Texto usado en varias ocasiones.
#		myfont : Font // Fuente de Texto usado en varias ocasiones.
#
#		tableroJ : list // Parametro de las Funciones resolverFilaAyuda, resolverColumnaAyuda, resolverRegionAyuda, selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		tableroS : list // Parametro de las Funciones resolverFilaAyuda, resolverColumnaAyuda y resolverRegionAyuda.
#		cantidadPistas : int // Variable que representa la cantidad de pistas que le quedan al Jugador.
#
#		fontNum : Font // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		poniendoListas : bool // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		n : int // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		dificultad : str // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		estaFila : bool // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		posCoincidenciaF : (int, int) // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		estaColumna : bool // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda..
#		posCoincidenciaC : (int, int) // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		estaRegion : bool // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#		posCoincidenciaR : (int, int) // Parametro de las Funciones selecFilaAyuda, selecColumnaAyuda y selecRegionAyuda.
#	Salida:
#		cantidadPistas : int // Variable que representa la cantidad de pistas que le quedan al Jugador.

def menuAyudaFacil(screen, fondo, fontE, myfont, tableroJ: list, tableroS: list, cantidadPistas: int, poniendoPistas: bool, \
				n: int, dificultad: str, estaFila: bool, posCoincidenciaF: (int, int), estaColumna: bool, \
				posCoincidenciaC: (int, int), estaRegion: bool, posCoincidenciaR: (int, int)) -> int:
	
	#PRECONDICION
	assert(True)
	
	while True:
		screen.blit(fondo, (0,0))
		numero = 0
		
		menuAyuda = ["1. Resolver una Casilla.", 
			     "2. ATRAS."] # : list // Lista que guarda las opciones del Menu de Crear Partida.
	
		if cantidadPistas > 0:
		
			pregunta = fontE.render("Que Desea Hacer?", True, (0, 0, 255))
			screen.blit(pregunta, (35, 180))
		
			texto = fontE.render("Le Quedan "+str(cantidadPistas)+ " Pistas Disponibles", True, (0, 0, 255))
			screen.blit(texto, (80, 215))
	
			for opcion in menuAyuda:
				texto = myfont.render(opcion, True, (0, 0, 255))
				screen.blit(texto, (110, 295+(25*menuAyuda.index(opcion))))
				
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit() 
			
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						
						casilla = selecCasillaAyuda(screen, fontNum, tableroJ, poniendoPistas,\
									    n, dificultad, estaFila, posCoincidenciaF,\
									    estaColumna, posCoincidenciaC,\
									    estaRegion, posCoincidenciaR)
									    
						resolverCasilla(casilla, tableroJ, tableroS)
						
						cantidadPistas -= 1
						 
						return cantidadPistas
					
		
					elif event.key == pygame.K_2:
						numero = 4
			
			if numero == 4:
				break
				
		
		else:
			texto = fontE.render("No le quedan Pistas Disponibles", True, (0, 0, 255))
			screen.blit(texto, (35, 180))
			
			texto2 = myfont.render("Presione Cualquier Tecla para Continuar.", True, (0, 0, 255))
			screen.blit(texto2, (95, 500))
			
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit() 
			
				elif event.type == pygame.KEYDOWN:
					numero = 4
			
			if numero == 4:
				break
				

		
		pygame.display.update()
		
		#POSTCONDICION:
		assert(True)
		

#----------------------------------------------------------------------------------------
#Descripcion: Esta Funcion Presenta en pantalla la pregunta si el Jugador desea guardar la partida en curso, en caso de ser la respuesta afirmativa creara un archivo en el cual se almacenaran: Nivel de Dificultad, Nombre del Jugador, Tiempo Transcurrido, Tablero Solucion y Tablero del Juego tal cual lo dejo el Jugador.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontTit : Font // Fuente de Texto que se usa para los Titulos.
#		fontE : Font // Fuente de Texto usada en varios casos.
#		myfont : Font // Fuente de Texto usada en varios casos.
#		usuario : str // VAriable que almacena el nombre del Jugador.
#		contadorReloj : int // Variable que va contando cuanto tiempo transcurre en la partida.
#		dificultad : str // Variable que almacena en que dificultad se esta Jugando.
#		cantidadPistas : int // Variable que guarda la cantidad de pistas que le quedan al jugador en el nivel facil.
#		puntajeTotal : int // Variable que representa el Puntaje Total acumulado por el jugador.
#		factorCobertura : int // Variable que representa en que valor quedo el Factor de Cobertura.
#		factorJugada : int // Variable que representa en que valor quedo el Factor de Jugada.
#		errores : int // variable que representa la cantidad de errores que ha cometido el JUgador.
#		contadorJugadas : int // Variable que guarda cuantas jugadas ha realizado el usuario.
#		contadorAumentado : int // Variable que representa cuantas veces se han aumentado los factores de Cobertura y Jugada
#		presionar : int // Variable que represnta cuantas veces el jugador uso el Boton CHECK
#		tableroJ : list // Matriz que representa el tablero el cual se va llenando.
#		tableroS : list // Matriz que representa el tablero Solucion del Juego.
def menuGuardarPartida(screen, fondo, fontTit, fontE, myfont, usuario: str, contadorReloj: int, dificultad: str, \
			cantidadPistas: int, puntajeTotal: int, factorCobertura: int, factorJugada: int, errores: int,\
			 contadorJugadas: int, contadorAumento: int, presionar: int, tableroJ: list, tableroS: list) -> 'void':
	#PRECONDICION
	assert(True)
	
	while True:
		screen.blit(fondo, (0,0))
		atras = False
		
		menuGuardar = ["1. Si", 
			       "2. No", 
			       "3. ATRAS"] # : list // Lista que guarda las opciones del Menu de Guardar Partida.
	
		pregunta = fontE.render("Desea Guardar la Partida?", True, (0, 0, 255), 15)
		screen.blit(pregunta, (35, 180))	
	
		for opcion in menuGuardar:
			texto = myfont.render(opcion, True, (0, 0, 255))
			screen.blit(texto, (100, 230+(25*menuGuardar.index(opcion))))
				
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					fecha = time.strftime("%d%m%y")
					tableroGuardar = []
					
					tableroGuardar.append(dificultad + "\n")
					tableroGuardar.append(nombre + "\n")
					tableroGuardar.append(str(contadorReloj) + "\n")

					for fi in range(len(tableroS)):
						for col in range(len(tableroS)):
							if not("*" in tableroS[fi][col]):
								tableroS[fi][col] = " "+tableroS[fi][col]

						fila = " ".join(tableroS[fi])
						
						tableroGuardar.append(fila+"\n")
						
					for fi in range(len(tableroJ)):
						for col in range(len(tableroJ)):
							if tableroJ[fi][col] == " ":
								tableroJ[fi][col] = " 0"
							
							elif not("*" in tableroJ[fi][col]):
								tableroJ[fi][col] = " "+tableroJ[fi][col]
								
						fila = " ".join(tableroJ[fi])
						tableroGuardar.append(fila+"\n")
					
					if cantidadPistas == None:
						cantidadPistas = 0
					
					tableroGuardar.append(str(cantidadPistas)+"\n")
					tableroGuardar.append(str(puntajeTotal)+"\n")
					tableroGuardar.append(str(factorCobertura)+"\n")
					tableroGuardar.append(str(factorJugada)+"\n")
					tableroGuardar.append(str(errores)+"\n")
					tableroGuardar.append(str(contadorJugadas)+"\n")
					tableroGuardar.append(str(contadorAumento)+"\n")
					tableroGuardar.append(str(presionar)+"\n")
					
					i = 1
					while True:
						if os.path.isfile("partidasGuardadas/tablero"+usuario + \
											fecha +"_"+str(i) + ".txt"):
							
							i += 1
						
						else:
							with open('partidasGuardadas/tablero'+ usuario + fecha + \
												"_"+str(i) + '.txt', 'w') as f:
								for fila in range(len(tableroGuardar)):
									f.write(tableroGuardar[fila])
							break
							
					while True:
						screen.blit(fondo, (0,0))
						
						texto1 = fontE.render("Partida Guardada", True, (0, 0, 255), 15)
						screen.blit(texto1, (35, 180))
						
						texto2 = myfont.render("Presione Cualquier Tecla para Salir.", \
									True, (0, 0, 255), 15)
						screen.blit(texto2, (95, 500))
						
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								running = 0
								sys.exit() 
					
							elif event.type == pygame.KEYDOWN:
								running = 0
								sys.exit()
											
						pygame.display.update()
							
							 
				elif event.key == pygame.K_2:
					running = 0
					sys.exit()
				
				elif event.key == pygame.K_3:
					atras = True
					
		if atras:
			break
			
		pygame.display.update()
		
		#POSTCONDICION:
		assert(True)
		
#---------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion presenta en pantalla las Tablas de Records divididas por dificultad.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontTit : Font // Fuente de Texto que se usa para los Titulos.
#		fontE : Font // Fuente de Texto usada en varios casos.
#		myfont : Font // Fuente de Texto usada en varios casos.
def menuTablaRecords(screen, fondo, fontTit, fontE, myfont) -> 'void':
	#PRECONDICION
	assert(True)
	
	while True:
		numero = 0
		
		screen.blit(fondo, (0,0))
		
		menuTabla = ["1. Facil", 
			     "2. Dificil", 
			     "3. Muy Dificil.",
			     "4. ATRAS"] # : list // Lista que guarda las opciones del Menu de Guardar Partida.
	
		pregunta = fontE.render("Cual Tabla Records desea ver?", True, (0, 0, 255), 15)
		screen.blit(pregunta, (35, 180))
	
		for opcion in menuTabla:
			texto = myfont.render(opcion, True, (0, 0, 255))
			screen.blit(texto, (100, 230+(25*menuTabla.index(opcion))))
				
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					with open("records/recordsFacil.txt", 'r') as f:
						arch = f.readlines()
						
					tabla = []
					
					for linea in arch:
						linea = linea.split()
						tabla.append(linea)
						
					while True:
						
						numero = 0
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								running = 0
								sys.exit()
							elif event.type == pygame.KEYDOWN:
								numero = 4

	
						screen.blit(fondo, (0,0))
	
						titulo = fontE.render("RECORDS: FACIL", True, (0, 0, 255), 15)
						screen.blit(titulo, (170, 80))
						
					
						for posicion in tabla:
							nombre, puntaje = posicion
						
							texto = myfont.render(nombre, True, (0, 0, 255))
							screen.blit(texto, (180, 200+(25*tabla.index(posicion))))
			
							texto1 = myfont.render(puntaje, True, (255, 0, 0))
							screen.blit(texto1, (380, 200+(25*tabla.index(posicion))))

						texto2 = myfont.render("Presione Cualquier Tecla para Continuar.", \
													True, (0, 0, 255))
						screen.blit(texto2, (95, 500))

						
						if numero == 4:
							break
							
						pygame.display.update()

							
				elif event.key == pygame.K_2:
					with open("records/recordsDificil.txt", 'r') as f:
						arch = f.readlines()
						
					tabla = []
					
					for linea in arch:
						linea = linea.split()
						tabla.append(linea)
						
					while True:
						
						numero = 0
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								running = 0
								sys.exit()
							elif event.type == pygame.KEYDOWN:
								numero = 4

	
						screen.blit(fondo, (0,0))
	
						titulo = fontE.render("RECORDS: DIFICIL", True, (0, 0, 255), 15)
						screen.blit(titulo, (170, 80))
						
					
						for posicion in tabla:
							nombre, puntaje = posicion
						
							texto = myfont.render(nombre, True, (0, 0, 255))
							screen.blit(texto, (180, 200+(25*tabla.index(posicion))))
			
							texto1 = myfont.render(puntaje, True, (255, 0, 0))
							screen.blit(texto1, (380, 200+(25*tabla.index(posicion))))

						texto2 = myfont.render("Presione Cualquier Tecla para Continuar.", \
													True, (0, 0, 255))
						screen.blit(texto2, (95, 500))

						
						if numero == 4:
							break
							
						pygame.display.update()

				elif event.key == pygame.K_3:
					with open("records/recordsMuyDificil.txt", 'r') as f:
						arch = f.readlines()
						
					tabla = []
					
					for linea in arch:
						linea = linea.split()
						tabla.append(linea)
						
					while True:
						
						numero = 0
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								running = 0
								sys.exit()
							elif event.type == pygame.KEYDOWN:
								numero = 4

	
						screen.blit(fondo, (0,0))
	
						titulo = fontE.render("RECORDS: MUY DIFICIL", True, (0, 0, 255), 15)
						screen.blit(titulo, (130, 80))
						
					
						for posicion in tabla:
							nombre, puntaje = posicion
						
							texto = myfont.render(nombre, True, (0, 0, 255))
							screen.blit(texto, (180, 200+(25*tabla.index(posicion))))
			
							texto1 = myfont.render(puntaje, True, (255, 0, 0))
							screen.blit(texto1, (380, 200+(25*tabla.index(posicion))))

						texto2 = myfont.render("Presione Cualquier Tecla para Continuar.", \
													True, (0, 0, 255))
						screen.blit(texto2, (95, 500))

						
						if numero == 4:
							break
							
						pygame.display.update()

				elif event.key == pygame.K_4:
					numero = 4
					
		if numero == 4:
			break
	
		pygame.display.update()
	
#----------------------------------------------------------------------------------------
#Descripcion: Funcion presenta una pantalla felicitando al Jugador por haber ganado la Partida, mostarndole a su vez su Nombre y su Tiempo Final.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontTit : Font // Fuente de Texto que se usa para los Titulos.
#		fontE : Font // Fuente de Texto usada en varios casos.
#		myfont : Font // Fuente de Texto usada en varios casos.
#		nombre : str // Variable que almacena el nombre del Jugador.
#		tiempo : (int, int) // Tupla que guarda el tiempo final, siendo su primer termino los minutos y el segundo los segundos.
#		puntajeTotal : int // Variable que representa el Puntaje q consiguio el Jugador en la partida.
#		errores : int // Variable que guardara la cantidad de errores que hizo el Jugador.
def pantallaVictoria(screen, fondo, fontTit, fontE, myfont, nombre: str, tiempo: (int, int), dificultad: str, \
			puntajeTotal: int, errores: int) -> 'void':
	#PRECONDICION
	assert(True)
	if not("Entrenamiento" in dificultad):
		posicion = actualizarTablaRecords(nombre, puntajeTotal, dificultad)
	
	while True:
		screen.blit(fondo, (0,0))
		
		texto1 = fontTit.render("VICTORIA!", True, (0, 0, 255))
		screen.blit(texto1, (30, 35))
		
		texto2 = fontE.render("Felicitaciones, " + nombre, True, (0,0,255))
		screen.blit(texto2, (30, 80))
		
		texto3 = fontE.render("Tiempo Final: {0:02}:{1:02}".format(tiempo[0], tiempo[1]), True, (0,0,255))
		screen.blit(texto3, (30, 115))
		
		fecha = time.strftime("%d/%m/%y")
		
		textof = fontE.render(fecha, True, (0,0,255))
		screen.blit(textof,(485, 0))
		

		
		if not("Entrenamiento" in dificultad):
			texto5 = fontE.render("Puntaje Final: " + str(puntajeTotal), True, (0, 0, 255))
			screen.blit(texto5, (140, 270))
			
			texto6 = fontE.render("N. de Errores: " + str(errores), True, (0, 0, 255))		
			screen.blit(texto6, (165, 315))
			
			texto0 = fontE.render("Posicion en la T. Records: " + str(posicion + 1), True, (0,0,255))
			screen.blit(texto0, (60, 360))
			
			
		texto4 = myfont.render("Presione Cualquier Tecla para Salir", True, (0, 0, 255), 15)
		screen.blit(texto4, (95, 500))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			elif event.type == pygame.KEYDOWN:
				running = 0
				sys.exit()
		
		pygame.display.update()
		
	#POSTCONDICION
	assert(True)



#----------------------------------------------------------------------------------------
#Descripcion: Funcion presenta una pantalla lamentandose por el Jugador por haber perdido la Partida, mostarndole a su vez su Nombre y su Tiempo Final.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontTit : Font // Fuente de Texto que se usa para los Titulos.
#		fontE : Font // Fuente de Texto usada en varios casos.
#		myfont : Font // Fuente de Texto usada en varios casos.
#		nombre : str // Variable que almacena el nombre del Jugador.
#		tiempo : (int, int) // Tupla que guarda el tiempo final, siendo su primer termino los minutos y el segundo los segundos.
#		errores : int // Variable que guarda la cantidad de veces que el usuario se equivoco.
def pantallaDerrota(screen, fondo, fontTit, fontE, myfont, nombre: str, tiempo: (int, int), \
								dificultad: str, errores: int) -> 'void':
	#PRECONDICION
	assert(True)
	
	while True:
		screen.blit(fondo, (0,0))
		
		texto1 = fontTit.render("DERROTA!", True, (255, 0, 0))
		screen.blit(texto1, (30, 35))
		
		texto2 = fontE.render("Lo siento, " + nombre, True, (255, 0, 0))
		screen.blit(texto2, (30, 80))
		
		texto3 = fontE.render("Tiempo Final: {0:02}:{1:02}".format(tiempo[0], tiempo[1]), True, (255, 0, 0))
		screen.blit(texto3, (30, 115))
		
		if not("Entrenamiento" in dificultad):
			texto5 = fontE.render("Sobrepaso la cantidad maxima ", True, (255, 0, 0))
			screen.blit(texto5, (20, 270))
			
			texto6 = fontE.render("permitida de Errores.", True, (255, 0, 0))
			screen.blit(texto6, (235, 305))
			
			texto7 = fontE.render("N. de Errores: "+ str(errores), True, (255, 0, 0))		
			screen.blit(texto7, (165, 350))
			
			
		texto4 = myfont.render("Presione Cualquier Tecla para Salir", True, (255, 0, 0))
		screen.blit(texto4, (85, 500))

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			elif event.type == pygame.KEYDOWN:
				running = 0
				sys.exit()
		
		pygame.display.update()
		
		#POSTCONDICION
		assert(True)
	

	
#-------------------------------------------------------------------------------------------------
#Descripcion: Esta recorre el Directorio donde se encuentran las Partidas Guardadas y seleccionara aquellas que Coincidan con el Nombre del jugador y la Fecha de cuand fue guardada, en caso de no existir coincidencias entrara en la funcion explicada mas Abajo. En el caso de existir coincidencia, mostrara en pantalla un Breve Menu para que el Usuario elija cual Partida desea Cargar y retorna dicha seleccion.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontTit : Font // Fuente de Texto que se usa para los Titulos.
#		fontE : Font // Fuente de Texto usada en varios casos.
#		myfont : Font // Fuente de Texto usada en varios casos.
#		nombre : str // Variable que almacena el nombre del Jugador.
#		fecha : str // Variable que almacena la fecha cuando fue guardada la partida.
#	Salida:
#		: int // Representa la opcion que selecciono el Usuario de la Partida Guardada que desea jugar.
def elegirPartidaGuardada(screen, fondo, fontE, myfont, nombre: str, fecha: str) -> int:

	
	#PRECONDICION
	assert(type(nombre) == str and type(fecha) == str)
	
	listaArchivos = [] # : list // Lista que Guardara los Archivos de Partidas Guardadas 
					#que coincidan con el Usuario y la Fecha dada.
	 
	listaDirectorio = os.walk('partidasGuardadas')   
	
	for root, directorios, archivos in listaDirectorio:
		for fichero in archivos:
			(nombreFichero, extension) = os.path.splitext(fichero)
			
			if(extension == ".txt") and (nombre in fichero) and (fecha in fichero):
				listaArchivos.append(nombreFichero+extension)
	
	if len(listaArchivos) == 0:
		noHayPartidasGuardadas(screen, fondo, fontE, myfont)
		
	else:
		while True:
		
			screen.blit(fondo, (0,0))
			
			pregunta = fontE.render("Cual Partida Desea Cargar?", True, (0, 0, 255))
			screen.blit(pregunta, (35, 180))
	
			k = 0
			while k < len(listaArchivos):
				texto = myfont.render(str(k+1) + ".  " + listaArchivos[k], True, (0, 0, 255))
				screen.blit(texto, (100, 230+(25*k)))
				
				k += 1
								
	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit() 
			
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						return listaArchivos[0]
				
					if len(listaArchivos) >= 2:			
						if event.key == pygame.K_2:
							return listaArchivos[1]
				
						if len(listaArchivos) >= 3:
							if event.key == pygame.K_3:
								return listaArchivos[2]
						
							if len(listaArchivos) >= 4:
								if event.key == pygame.K_4:
									return listaArchivos[3]
							
								if len(listaArchivos) >= 5:
									if event.key == pygame.K_5:
										return listaArchivos[4]
				
									if len(listaArchivos) >= 6:
										if event.key == pygame.K_6:
											return listaArchivos[5]
									
										if len(listaArchivos) >= 7:
											if event.key == pygame.K_7:
												return listaArchivos[6]
										
											if len(listaArchivos) >= 8:
												if event.key == pygame.K_8:
													return listaArchivos[7]
											
												if len(listaArchivos) == 9:
													if event.key\
														 == pygame.K_9:
														return\
														 listaArchivos[8]
				
								
			pygame.display.update()
			
			
		#POSTCONDICION
		assert(True)
	

#-------------------------------------------------------------------------------------------
#Descripcion: Esta Funcion escribe en la Pantalla el mensaje de que no se encontraron Coincidencias entra las Partidas Guardadas con los Datos suministrados por el Usuario.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontTit : Font // Fuente de Texto que se usa para los Titulos.
#		fontE : Font // Fuente de Texto usada en varios casos.
#		myfont : Font // Fuente de Texto usada en varios casos.
def noHayPartidasGuardadas(screen, fondo, fontE, myfont) -> 'void':
	
	#PRECONDICION
	assert(True)
	

	while True:
	
		screen.blit(fondo, (0,0))
		
		texto1 = fontE.render("No existen Coincidencias ", True, (0, 0, 255))
		screen.blit(texto1, (35, 180))
		
				
		texto1 = fontE.render("en las Partidas Guardadas.", True, (0, 0, 255))
		screen.blit(texto1, (60, 220))
		
		texto2 = myfont.render("Presione Cualquier Tecla para Salir.", True, (0, 0, 255))
		screen.blit(texto2, (95, 500))
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			
			elif event.type == pygame.KEYDOWN:
				running = 0
				sys.exit() 
			
								
		
		pygame.display.update()
		
		#POSTCONDICION
		assert(True)
	
#----------------------------------------------------------------------------------------
#Descripcion:
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontE : Font // Fuente de Texto usada en varios casos.
#		myfont : Font // Fuente de Texto usada en varios casos.
def pantallaFaltaPermiso(screen, fondo, fontE, myfont, fontNum) -> 'void':
	#PRECONDICION
	assert(True)
	

	while True:
		numero = 0
		screen.blit(fondo, (0,0))
		
		texto0 = fontE.render("Lo siento, "+ nombre, True, (0, 0, 255))
		screen.blit(texto0, (20, 120))

		texto1 = fontE.render("Debes ganar una Partida en el", True, (0, 0, 255))
		screen.blit(texto1, (45, 200))
		
				
		texto1 = fontE.render("Nivel anterior para Jugar", True, (0, 0, 255))
		screen.blit(texto1, (90, 240))
		
		texto3 = fontE.render("este Nivel.", True, (0, 0, 255))
		screen.blit(texto3, (200, 280))
		
		texto2 = myfont.render("Presione Cualquier Tecla para Continuar.", True, (0, 0, 255))
		screen.blit(texto2, (95, 500))
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
				sys.exit() 
			
			elif event.type == pygame.KEYDOWN:
				numero = 4
		
		if numero == 4:
			break
			
								
		
		pygame.display.update()
		
		#POSTCONDICION
		assert(True)
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#Pedir Datos
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#----------------------------------------------------------------------------------------
#Descripcion: Esta funcion Creara una pantalla donde le pedira al usuario que introduzca la fecha.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontE : Font // Fuente de Texto usada en varios casos.
def pedirFecha(screen, fondo, fontE) -> str:
	#PRECONDICION
	assert(True)
	
	fecha = [] # : list // Lista donde se guardara las letras que vaya metiendo el usuario para escribir su nombre.
	

	while True:
		screen.blit(fondo, (0, 0))
		
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit() 

		
		pregunta = fontE.render("Fecha (DDMMAA): "+ "".join(fecha), True, (0, 0, 255))
		screen.blit(pregunta, (105, 300))

		pygame.display.update()		
					
		letra = obtenerTecla()
		 
		if letra == pygame.K_BACKSPACE:
			fecha = fecha[0:-1]
		
		elif letra == pygame.K_RETURN:
			break
		
		elif 48 <= letra <= 57:
			fecha.append(chr(letra))
		
		pregunta = fontE.render("Fecha (DDMMAA): "+ "".join(fecha), True, (0, 0, 255))
		screen.blit(pregunta, (105, 300))
		
		pygame.display.update()
		
	#POSTCONDICION:
	assert(True)
	
	return "".join(fecha)

#--------------------------------------------------------------------------------
#Descripcion: Esta Funcion presenta en pantalla que nombre esta introduciendo el Usuario, y retorna dicho nombre para ser representado posteriormente.
#Parametros:
#	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontE : Font // Fuente de Texto usada en varios casos.
def pedirUsuario(screen, fondo, fontE) -> str:
	
	#PRECONDICION
	assert(True)
	
	nombre = [] # : list // Lista donde se guardara las letras que vaya metiendo el usuario para escribir su nombre.
	
	pregunta = fontE.render("Nombre: "+ "".join(nombre), True, (0, 0, 255))
	screen.blit(pregunta, (220, 300))
	

	
	while True:
		screen.blit(fondo, (0, 0))
		
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit() 

		
		pregunta = fontE.render("Nombre: "+ "".join(nombre), True, (0, 0, 255))
		screen.blit(pregunta, (190, 250))

		pygame.display.update()		
					
		letra = obtenerTecla()
		 
		if letra == pygame.K_BACKSPACE:
			nombre = nombre[0:-1]
		
		elif letra == pygame.K_RETURN:
			break
		
		elif letra == pygame.K_MINUS:
			nombre.append("-")
	
		elif letra <= 127:
			nombre.append(chr(letra))
		
		pregunta = fontE.render("Nombre: "+ "".join(nombre), True, (0, 0, 255))
		screen.blit(pregunta, (190, 250))
		
		pygame.display.update()
	
	#POSTCONDICION:
	assert(type("".join(nombre)) == str)

	return "".join(nombre)
#--------------------------------------------------------------------------------
#Descripcion: Esta Funcion retorna cual tecla introduce el Usuario.
#Parametros:
#	Entrada:
#		No tiene Parametrso de entrada.
#	Salida:
#		Devuleve la tecla que el Jugador haya presionado
def obtenerTecla():
	#PRECONDICION
	assert(True)
	
	while True:
		event = pygame.event.poll()
		if event.type == pygame.KEYDOWN:
			return event.key
		
		elif event.type == pygame.QUIT:
			running = 0
			sys.exit()

		else:
			pass

	#POSTCONDICION:
	assert(True)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#Juego
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#------------------------------------------------------------------------------------
#Descripcion: Esta Funcion reprensenta en pantalla la Pantalla de la Partida que se esta jugando. 
#Parametros:
# 	Entrada:
#		screen : Screen // Pantalla del Juego.
#		fondo : Surface // Fondo que se coloca en la pantalla para tapar lo que previamente aparecia en la Pantalla.
#		fontTit : Font  // Fuente de Texto usada para los titulos.
#		fontE : Font // Fuente de Texto usada en varias ocasiones.
#		myfont : Font // Fuente de Texto usada en varias ocasiones.
#		fontNum : Font // Fuente de Texto usada en los numeros dentro del tablero.
#		nombre : str // Variable que almacena el nombre del Jugador.
#		dificultad : str // Variable que almacena en que dificultad se esta Jugando.
#		cantidadPistas : int // Variable que guarda la cantidad de pistas que le quedan al jugador en el nivel facil.
#		puntajeTotal : int // Variable que representa el Puntaje Total acumulado por el jugador.
#		factorCobertura : int // Variable que representa en que valor quedo el Factor de Cobertura.
#		factorJugada : int // Variable que representa en que valor quedo el Factor de Jugada.
#		errores : int // variable que representa la cantidad de errores que ha cometido el JUgador.
#		contadorJugadas : int // Variable que guarda cuantas jugadas ha realizado el usuario.
#		contadorAumentado : int // Variable que representa cuantas veces se han aumentado los factores de Cobertura y Jugada
#		presionar : int // Variable que represnta cuantas veces el jugador uso el Boton CHECK
#		contadorReloj : int // Variable que va contando cuanto tiempo transcurre en la partida.
#		tableroJuego : list // Matriz que representa el tablero el cual se va llenando.
#		tableroSolucion : list // Matriz que representa el tablero Solucion del Juego.
def JUGAR(screen, fondo, fontE, myfont, fontNum, nombre: str, dificultad: str, cantidadPistas: int, puntajeTotal: int,\
		factorCobertura: int, factorJugada: int, errores: int, contadorJugadas: int, contadorAumento: int,\
			 presionar: int, contadorReloj: int, tableroJuego: list, tableroSolucion: list) -> 'void':
	
	#PRECONDICION:
	assert(True)

	reloj = pygame.time.Clock()
	
	
	puntajeJugada = 0
	puntajeCobertura = 0
		
	rate = 60
	
	
	poniendoPistas = True # :bool // Booleano que representa que si es la primera vez que se llama a la Funcion
				# escribirMatriz() para que sepa que debe guardar las posiciones donde se encuentran las pistas.
	
	estaFila, posCoincidenciaF = False, (0, 0) # :bool, (int, int) // Booleano que representa si el numero introducio por
						#el usuario se encuentra o no en la Fila a la que pertenece esa casilla. //
						#Posicion donde estara la Coincidencia si se repite el numero, en caso contrario
						#tentra valor None.
	estaColumna, posCoincidenciaC = False, (0, 0)# :bool, (int, int) // Booleano que representa si el numero introducio por
						#el usuario se encuentra o no en la Columna a la que pertenece esa casilla. //
						#Posicion donde estara la Coincidencia si se repite el numero, en caso contrario
						#tentra valor None.
	estaRegion, posCoincidenciaR = False, (0, 0)# :bool, (int, int) // Booleano que representa si el numero introducio por
						#el usuario se encuentra o no en la Region a la que pertenece esa casilla. //
						#Posicion donde estara la Coincidencia si se repite el numero, en caso contrario
						#tentra valor None.
	
	n = 0 # :int // Inicializacion del Numero que introucira el Usuario posteriormente.
	
		
	pistas = escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, posCoincidenciaF, \
				estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)
					 # :list // Lista que tendra guardada las posiciones odne se encuentran las pistas.
	acabar = False
	
	while (not acabar):
		
		screen.blit(fondo, (0,0))

		rellenoCasPista(screen, pistas, tableroJuego)	

		poniendoPistas = False
		
		
		tituloTablero = myfont.render(dificultad, True, (0, 0, 0))
		screen.blit(tituloTablero, (10, 10))
		
		usuario = myfont.render("Nombre: " + nombre, True, (255,0,0))
		screen.blit(usuario, (10, 30))
		
		
					
		escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
				posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)
		
		tiempo = crono(screen, reloj, myfont, contadorReloj, rate)
		contadorReloj += 2
		reloj.tick(rate)
		
		if not("Entrenamiento" in dificultad):
			puntajeJ = myfont.render("Puntaje Jugada: " + str(puntajeJugada), True, (0,0,0))
			screen.blit(puntajeJ, (375, 10))

			puntajeC = myfont.render("Puntaje Cobertura: " + str(puntajeCobertura), True, (0,0,0))
			screen.blit(puntajeC, (340, 30))
					
			puntajeT = myfont.render("Puntaje Total: " + str(puntajeTotal), True, (0,0,255))
			screen.blit(puntajeT, (389, 55))
			
			textoErrores = myfont.render("N. Errores: " + str(errores), True, (255,0,0))
			screen.blit(textoErrores, (400, 90))
			
			
						
		
					
		boton(screen, fontE, "SALIR", 0, 580, 100, 60, (0, 0, 255), (0, 255, 0)) #Creara el Boton de Salir en Pantalla.
				
		
		if not ("Dificil" in dificultad):
			boton(screen, fontE, "Ayuda", 540, 580, 100, 60, (0, 0, 255), (0, 255, 0)) # Creara el Boton de Ayuda en Pantalla.
		if dificultad == "Muy Dificil":
			boton(screen, fontE, "CHECK", 540, 580, 100, 60, (0, 0, 255), (0, 255, 0)) # Creara el Boton de Comprobar en Pantalla.
		
		xMouse, yMouse = pygame.mouse.get_pos() # int, int // Variables que guardaran las 
								     			# coordenadas x, y del Mouse.
		click = pygame.mouse.get_pressed() # : (bool, bool, bool) // Tupla que tendra el 
									#estado de los botones del Mouse.

		#Click Boton Comprobar.
		if 540 < xMouse < 640 and 580 < yMouse < 640 and click[0] and ("Muy Dificil" == dificultad):
			presionar += 1
			
			check = comprobarSudoku(tableroJuego, tableroSolucion)
			
			
			if check:
				if all((not(" " in tableroJuego[i])) for i in range(len(tableroJuego))):
					acabar = True
				else:
					error = fontE.render("NO HAY ERRORES!", True, (255, 0, 0))
					screen.blit(error, (190, 590))
					
	
			else:
				error = fontE.render("HAY ERRORES!", True, (255, 0, 0))
				screen.blit(error, (210, 590))	
			
		
			pygame.display.update()
				
		casilla = resaltarCasilla(screen, fondo, fontTit, fontE, myfont, usuario, contadorReloj, dificultad,\
						cantidadPistas, puntajeTotal, factorCobertura, factorJugada, errores,\
						contadorJugadas, contadorAumento, presionar, tableroJuego, tableroSolucion) 
				# :(int, int) // Las Coordenadas en fila, columna de la casilla seleccionada por el Usuario.
		
		
		if casilla != None:
				
			resaltarFilaColumna(screen, casilla, tableroJuego)
			
			if ("Entrenamiento" in dificultad):
				resaltarNumerosCorrectos(screen, fontNum, casilla, tableroJuego)

				
			pygame.display.update()
			
		
			n, contadorReloj = introducirNumero(screen, fondo, fontTit, fontE, myfont, \
								nombre, contadorReloj, dificultad, cantidadPistas,\
								 puntajeTotal, factorCobertura, factorJugada, errores,\
								  contadorJugadas, contadorAumento, presionar,\
								    tableroJuego, tableroSolucion, reloj, rate) 
		# : int, int // Numero que el usuario Introdujo por Teclado // Contador que se usa para llevar el tiempo.
			
			if n != None:
				contadorJugadas += 1
				
				#Verificaciones
				estaFila, posCoincidenciaF = verificarFila(n, casilla, tableroJuego) 
		
				estaColumna, posCoincidenciaC = verificarColumna(n, casilla, tableroJuego)
		
				estaRegion, posCoincidenciaR = verificarRegion(n, casilla, tableroJuego)
				
				
				#Descuento de los Factores
				if contadorJugadas%5 == 0 and contadorJugadas > 0 and factorJugada > 1 \
											and factorCobertura > 1:
					
					if dificultad == "Facil":
						factorJugada -= 1
						factorCobertura -= 2
					
					elif "Dificil" in dificultad:
						factorJugada -= 2
						factorCobertura -= 3

				#Aumento de los Factores
				if puntajeTotal >= 3000*contadorAumento and dificultad == "Facil":
					factorJugada += 5
					factorCobertura += 5
					
					contadorAumento += 1
					
				if puntajeTotal >= 4500*contadorAumento and ("Dificil" in dificultad):
					factorJugada += 5
					factorCobertura += 5
					
					contadorAumento += 1
	
					
				#Contando los Errores
				if (estaFila or estaColumna or estaRegion) and n != " ":
					errores += 1
					if dificultad == "Facil":
						puntajeTotal -= 50
					elif ("Dificil" in dificultad):
						puntajeTotal -= 100
				
				#Calculando el Puntaje Jugada
				else:
					if n != " ":
						g = int(n)
					else:
						g = 0
					
					puntajeJugada = g * factorJugada
					

				#Modificando la Matriz del Juego
				escribirNumero(casilla, n, tableroJuego)
				
				#Verificando si se llena correctamente una Fila, Columna o Region.
				fullF = fullFila(casilla, tableroJuego, tableroSolucion)
				fullC = fullColumna(casilla, tableroJuego, tableroSolucion)
				fullR = fullRegion(casilla, tableroJuego, tableroSolucion)
				
				
				puntajeCobertura = 0
				pC = 0
				
				#Calculo Puntaje Cobertura
				if fullF:
					pC += len(tableroJuego)
				if fullC:
					pC += len(tableroJuego)
				if fullR:
					pC += len(tableroJuego)
					
				puntajeCobertura += pC*factorCobertura

				puntajeTotal += puntajeJugada + puntajeCobertura

				
				
			
			tiempo = crono(screen, reloj, myfont, contadorReloj, rate)
			reloj.tick(rate)
			
			
						
			pygame.display.update()

		
		
		#Click Boton Salir.
		if 0 < xMouse < 100 and 580 < yMouse < 640 and click[0]:
			menuGuardarPartida(screen, fondo, fontTit, fontE, myfont, nombre, contadorReloj, \
						dificultad, cantidadPistas, puntajeTotal, factorCobertura,\
						factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
						tableroJuego, tableroSolucion)

		#Click Boton Ayuda Entrenamiento.
		if 540 < xMouse < 640 and 580 < yMouse < 640 and click[0] and ("Entrenamiento" in dificultad):
			menuAyudaEntrenamiento(screen, fondo, fontE, myfont, tableroJuego, tableroSolucion, \
						poniendoPistas, n, dificultad, estaFila, posCoincidenciaF, estaColumna,\
						posCoincidenciaC, estaRegion, posCoincidenciaR)
						
			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
					posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)

		
		#Click Boton Ayuda Facil.
		if 540 < xMouse < 640 and 580 < yMouse < 640 and click[0] and ("Fac" in dificultad):
			cantidadPistas = menuAyudaFacil(screen, fondo, fontE, myfont, tableroJuego, tableroSolucion,\
							cantidadPistas, poniendoPistas, n, dificultad, estaFila,\
							posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion,\
							posCoincidenciaR)
			
			escribirMatriz(screen, fontNum, tableroJuego, poniendoPistas, n, dificultad, estaFila, \
					posCoincidenciaF, estaColumna, posCoincidenciaC, estaRegion, posCoincidenciaR)
			
		

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				menuGuardarPartida(screen, fondo, fontTit, fontE, myfont, usuario, \
						    contadorReloj, dificultad, cantidadPistas, puntajeTotal,\
						  	factorCobertura, factorJugada, errores, contadorJugadas,\
							  contadorAumento, presionar,tableroJuego, tableroSolucion)
							  
		
		if all((not(" " in tableroJuego[i])) for i in range(len(tableroJuego))) and tableroJuego != tableroSolucion\
											and dificultad != "Muy Dificil":
			error = fontE.render("HAY ERRORES!", True, (255, 0, 0))
			screen.blit(error, (210, 590))

		
		elif all((not(" " in tableroJuego[i])) for i in range(len(tableroJuego))) and tableroJuego == tableroSolucion\
											and dificultad != "Muy Dificil":
			acabar = True
							  
		

		pygame.display.update()
			
	if "Entrenamiento" in dificultad:
		if tableroJuego == tableroSolucion:
			actualizarPermisos(nombre, 1)
			pantallaVictoria(screen, fondo, fontTit, fontE, myfont, nombre, tiempo, dificultad, \
												puntajeTotal, errores)
		
		
	if dificultad == "Facil":
		if errores < 6:
			actualizarPermisos(nombre, 2)
			pantallaVictoria(screen, fondo, fontTit, fontE, myfont, nombre, tiempo, dificultad, \
												puntajeTotal, errores)
		
		else:
			pantallaDerrota(screen, fondo, fontTit, fontE, myfont, nombre, tiempo, dificultad, errores)
			

	if dificultad == "Dificil":
		if errores < 4:
			actualizarPermisos(nombre, 3)
			
			pantallaVictoria(screen, fondo, fontTit, fontE, myfont, nombre, tiempo, dificultad, \
												puntajeTotal, errores)
		
		else:
			pantallaDerrota(screen, fondo, fontTit, fontE, myfont, nombre, tiempo, dificultad, errores)
			
	if dificultad == "Muy Dificil":
		if errores < 4 and presionar < 4:
			if presionar == 1:
				if errores == 0:
					puntajeTotal += 5000
				if 1 <= errores <= 3:
					puntajeTotal += 1500
			
			pantallaVictoria(screen, fondo, fontTit, fontE, myfont, nombre, tiempo, dificultad, \
												puntajeTotal, errores)
		
		else:
			pantallaDerrota(screen, fondo, fontTit, fontE, myfont, nombre, tiempo, dificultad, errores)
		
	
	#POSTCONDICION:
	assert(True)
	
					
######################################################
#Inicio de Programa
#######################################################

#Importando Librerias
import pygame, sys, time, os.path

#Inicio de Pygame
pygame.init()

#Ventana
screen = pygame.display.set_mode((640, 640)) #Ventana en Pygame para el Juego.
pygame.display.set_caption('SudoMania') #Titulo de la Ventana
running = 1

fondo = pygame.Surface((640,640)) #Fondo que se usara para tapar menus anteriores.
fondo.fill((230, 230, 230)) #Color que tendra dicho fondo.


#Fuentes de Texto de lo que se escribira en Pantalla
myfont = pygame.font.SysFont('monospace', 20)
fontTit = pygame.font.SysFont('monospace', 42, True, True)
fontE = pygame.font.SysFont('monospace', 30, True)
fontNum = pygame.font.SysFont('monospace', 25, True)

#Inicializando la Variables del Juego
errores = 0
puntajeTotal = 0
contadorAumento = 1
contadorJugadas = -1
factorJugada = 15
factorCobertura = 31
cantidadPistas = 3
presionar = 0

while True:
	#pygame.mixer.music.load('admin/sound.mp3')
	#pygame.mixer.music.play(-1, 0.0)

	#Color de Fondo de la Ventana
	screen.fill((230, 230, 230))
		
	
		
	opcionMenuP = menuPrincipal(screen, fondo, fontTit, fontE)
	
	#Opcion de Crear Partida Nueva
	if opcionMenuP == 1:
		opcion = opcionCrearPartida(screen, fondo, fontE, myfont)
		
		nombre = pedirUsuario(screen, fondo, fontE)
			
		#Opcion Partida Nueva de Entrenamiento
		if opcion == 1:
			opcion = crearEntrenamiento(screen, fondo, fontE, myfont)

			#-----------------------
			#Opcion Entrenamiento de tablero 6x6
			if opcion == 1:
				opcion = elegirTablero(screen, fondo, fontE, myfont)
				
				
				if opcion == 1:
					archivo = "tablerosIniciales/entrenamiento/6x6/tablero1E6x6.txt"
	
					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
					
					contadorReloj = 0
	
					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre,\
						"Entrenamiento 6x6", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar, \
								contadorReloj, tableroJuego, tableroSolucion)

				if opcion == 2:
					archivo = "tablerosIniciales/entrenamiento/6x6/tablero2E6x6.txt"

					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
					
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Entrenamiento 6x6", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar, \
								contadorReloj, tableroJuego, tableroSolucion)
						
				if opcion == 3:
					archivo = "tablerosIniciales/entrenamiento/6x6/tablero3E6x6.txt"

					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
					
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Entrenamiento 6x6", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
								contadorReloj, tableroJuego, tableroSolucion)

			#-----------------------
			#Opcion Entrenamiento de tablero 9x9
			elif opcion == 2:
				opcion = elegirTablero(screen, fondo, fontE, myfont)
				
				
				#----------------------
				#Tablero 1 de Entrenamiento 9x9
				if opcion == 1:
					archivo = "tablerosIniciales/entrenamiento/9x9/tablero1E9x9.txt"
					
					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
					
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Entrenamiento 9x9", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
								contadorReloj, tableroJuego, tableroSolucion)
					
					
				
				#----------------------
				#Tablero 2 de Entrenamiento 9x9		
				elif opcion == 2:
					archivo = "tablerosIniciales/entrenamiento/9x9/tablero2E9x9.txt"
					
					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
					
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Entrenamiento 9x9", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
								contadorReloj, tableroJuego, tableroSolucion)
					
				#----------------------
				#Tablero 3 de Entrenamiento 9x9					
				elif opcion == 3:
					archivo = "tablerosIniciales/entrenamiento/9x9/tablero3E9x9.txt"
				
					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
					
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Entrenamiento 9x9", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
								contadorReloj, tableroJuego, tableroSolucion)
					
		#Opcion Partida Nueva de Facil
		elif opcion == 2:
			opcion = elegirTablero(screen, fondo, fontE, myfont)
				
			
			if opcion == 1:
				archivo = "tablerosIniciales/facil/tablero1F.txt"

				aux = obtenerTableroSolucion(archivo)

				tableroJuego = inicializarTablero(aux)

				tableroSolucion = obtenerTableroSolucion(archivo)
				
				contadorReloj = 0

				JUGAR(screen, fondo, fontE, myfont, fontNum, nombre,\
					"Facil", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
								contadorReloj, tableroJuego, tableroSolucion)

			if opcion == 2:
				archivo = "tablerosIniciales/facil/tablero2F.txt"

				aux = obtenerTableroSolucion(archivo)

				tableroJuego = inicializarTablero(aux)

				tableroSolucion = obtenerTableroSolucion(archivo)
				
				contadorReloj = 0

				JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
					"Facil", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
								contadorReloj, tableroJuego, tableroSolucion)
					
			if opcion == 3:
				archivo = "tablerosIniciales/facil/tablero3F.txt"

				aux = obtenerTableroSolucion(archivo)

				tableroJuego = inicializarTablero(aux)

				tableroSolucion = obtenerTableroSolucion(archivo)
				
				contadorReloj = 0

				JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
					"Facil", cantidadPistas, puntajeTotal, factorCobertura,\
							factorJugada, errores, contadorJugadas, contadorAumento, presionar,\
								contadorReloj, tableroJuego, tableroSolucion)

			
		#Opcion Partida Nueva de Dificil	
		elif opcion == 3:
			nivelPermiso = comprobarPermisos(nombre)
			
			if nivelPermiso != None and nivelPermiso >= 2: 
				opcion = elegirTablero(screen, fondo, fontE, myfont)
				
				if opcion == 1:
					archivo = "tablerosIniciales/dificil/tablero1D.txt"

					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
				
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre,\
						"Dificil", cantidadPistas, puntajeTotal, factorCobertura,\
								factorJugada, errores, contadorJugadas, contadorAumento,\
								   presionar, contadorReloj, tableroJuego, tableroSolucion)

				if opcion == 2:
					archivo = "tablerosIniciales/dificil/tablero2D.txt"

					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
				
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Dificil", cantidadPistas, puntajeTotal, factorCobertura,\
								factorJugada, errores, contadorJugadas, contadorAumento,\
								  presionar, contadorReloj, tableroJuego, tableroSolucion)
					
				if opcion == 3:
					archivo = "tablerosIniciales/dificil/tablero3D.txt"

					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
				
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Dificil", cantidadPistas, puntajeTotal, factorCobertura,\
								factorJugada, errores, contadorJugadas, contadorAumento,\
									 presionar, contadorReloj, tableroJuego, tableroSolucion)
			
			else:
				pantallaFaltaPermiso(screen, fondo, fontE, myfont, fontNum)
					
		#Opcion Partida Nueva de Muy Dificil
		elif opcion == 4:
			nivelPermiso = comprobarPermisos(nombre)
			
			if nivelPermiso != None and nivelPermiso >= 3: 
				opcion = elegirTablero(screen, fondo, fontE, myfont)
				
				if opcion == 1:
					archivo = "tablerosIniciales/muyDificil/tablero1MD.txt"

					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
				
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre,\
						"Muy Dificil", cantidadPistas, puntajeTotal, factorCobertura,\
								factorJugada, errores, contadorJugadas, contadorAumento,\
									 presionar, contadorReloj, tableroJuego, tableroSolucion)

				if opcion == 2:
					archivo = "tablerosIniciales/muyDificil/tablero2MD.txt"

					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
				
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Muy Dificil", cantidadPistas, puntajeTotal, factorCobertura,\
								factorJugada, errores, contadorJugadas, contadorAumento,\
									 presionar, contadorReloj, tableroJuego, tableroSolucion)
					
				if opcion == 3:
					archivo = "tablerosIniciales/muyDificil/tablero3MD.txt"

					aux = obtenerTableroSolucion(archivo)

					tableroJuego = inicializarTablero(aux)

					tableroSolucion = obtenerTableroSolucion(archivo)
				
					contadorReloj = 0

					JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, \
						"Muy Dificil", cantidadPistas, puntajeTotal, factorCobertura,\
								factorJugada, errores, contadorJugadas, contadorAumento,\
									 presionar, contadorReloj, tableroJuego, tableroSolucion)
			
			else:
				pantallaFaltaPermiso(screen, fondo, fontE, myfont, fontNum)

			
	#Opcion Cargar Partida Guarada
	elif opcionMenuP == 2:
		nombre = pedirUsuario(screen, fondo, fontE)
		fecha = pedirFecha(screen, fondo, fontE)
		
		
		archivo = elegirPartidaGuardada(screen, fondo, fontE, myfont, nombre, fecha)
		
		
		with open('partidasGuardadas/' + archivo, 'r') as f:
			arch = f.readlines()
			
		dificultad = arch[0][:-1]
		nombre = arch[1][:-1]
		contadorReloj = int(arch[2][:-1])
			
		tableroSolucion = []
		tableroJuego = []
		
		
		if len(arch) == 23:
			linea = 3
			while linea <= 8:
				arch[linea] = arch[linea].split()
				tableroSolucion.append(arch[linea])
			
				linea += 1
		
			li = 9
			while li <= 14:
				arch[li] = arch[li].split()
			
				tableroJuego.append(arch[li])
			
				li += 1
				
			cantidadPistas = int(arch[15][:-1])
			puntajeTotal = int(arch[16][:-1])
			factorCobertura = int(arch[17][:-1])
			factorJugada = int(arch[18][:-1])
			errores = int(arch[19][:-1])
			contadorJugadas = int(arch[20][:-1])
			contadorAumento = int(arch[21][:-1])

		elif len(arch) == 29:
			 
			linea = 3
			while linea <= 11:
				arch[linea] = arch[linea].split()
				tableroSolucion.append(arch[linea])
			
				linea += 1
		
			li = 12
			while li <= 20:
				arch[li] = arch[li].split()
			
				tableroJuego.append(arch[li])
			
				li += 1
		
			cantidadPistas = int(arch[21][:-1])
			puntajeTotal = int(arch[22][:-1])
			factorCobertura = int(arch[23][:-1])
			factorJugada = int(arch[24][:-1])
			errores = int(arch[25][:-1])
			contadorJugadas = int(arch[26][:-1])
			contadorAumento = int(arch[27][:-1])
			presionar = int(arch[28][:-1])
			
		for fi in range(len(tableroJuego)):
			for col in range(len(tableroJuego)):
				if tableroJuego[fi][col] == "0":
					tableroJuego[fi][col] = " "
		
					
		
		JUGAR(screen, fondo, fontE, myfont, fontNum, nombre, dificultad, cantidadPistas, puntajeTotal, factorCobertura,\
			factorJugada, errores, contadorJugadas, contadorAumento,  presionar, contadorReloj, tableroJuego, tableroSolucion)
		

	#Opcion Tabla de Records
	elif opcionMenuP == 3:
		menuTablaRecords(screen, fondo, fontTit, fontE, myfont)
		
	#Opcion Ayuda
	elif opcionMenuP == 4:
		while True:
			numero = 0
			screen.blit(fondo, (0,0))
		
			texto0 = fontE.render("Como Jugar Sudoku: ", True, (0, 0, 255))
			screen.blit(texto0, (20, 50))

			
			texto1 = myfont.render("El Sudoku es un juego muy sencillo, es como un ", True, (0, 0, 255))
			screen.blit(texto1, (30, 100))
			
			texto1 = myfont.render("rompecabezas numérico. Se juega sobre cuadriculas de ", True, (0, 0, 255))
			screen.blit(texto1, (10, 120))
			
			texto1 = myfont.render("6x6 o 9x9 cuyos cuadros deben ser llenados con los ", True, (0, 0, 255))
			screen.blit(texto1, (10, 140))
			
			texto1 = myfont.render("números del 1 al 6 y del 1 al 9 respectivamente y de ", True, (0, 0, 255))
			screen.blit(texto1, (10, 160))
			
			texto1 = myfont.render("forma especifica para poder ganar.", True, (0, 0, 255))
			screen.blit(texto1, (10, 180))
			
			texto1 = myfont.render("El secreto es llenar todas las filas y todas las ", True, (0, 0, 255))
			screen.blit(texto1, (30, 220))
			
			texto1 = myfont.render("columnas con los números del 1 al 9 o los números  del ", True, (0, 0, 255))
			screen.blit(texto1, (5, 240))
			
			texto1 = myfont.render("1 al 6 sin repetirlos; es decir se deben llenar las ", True, (0, 0, 255))
			screen.blit(texto1, (5, 260))
			
			texto1 = myfont.render("filas con los números al igual que las columnas. ", True, (0, 0, 255))
			screen.blit(texto1, (5, 280))
			
			texto1 = myfont.render("Normalmente se colocan ya números previamente para ", True, (0, 0, 255))
			screen.blit(texto1, (5, 300))
			
			texto1 = myfont.render("darle mayor dificultad al juego. ", True, (0, 0, 255))
			screen.blit(texto1, (5, 320))
			
			texto1 = myfont.render("La ultima regla importante del Sudoku y que ", True, (0, 0, 255))
			screen.blit(texto1, (30, 360))
			
			texto1 = myfont.render("incrementa también la dificultad en la resolución del ", True, (0, 0, 255))
			screen.blit(texto1, (5, 380))
			
			texto1 = myfont.render("mismo, es que los tableros de 6x6 y 9x9 se subdividen ", True, (0, 0, 255))
			screen.blit(texto1, (5, 400))

			texto1 = myfont.render("en regiones. Los de 6x6 en regiones de 3x2 y los de ", True, (0, 0, 255))
			screen.blit(texto1, (5, 420))
			
			texto1 = myfont.render("9x9 en regiones de 3x3. Dentro de estas regiones los ", True, (0, 0, 255))
			screen.blit(texto1, (5, 440))
			
			texto1 = myfont.render("numeros tampoco pueden repetirse, sumado a que no se ", True, (0, 0, 255))
			screen.blit(texto1, (5, 460))
			
			texto1 = myfont.render("pueden repetir en las columnas ni en las filas. ", True, (0, 0, 255))
			screen.blit(texto1, (5, 480))
			
						
			texto2 = myfont.render("Presione Cualquier Tecla para Continuar.", True, (255, 0, 0))
			screen.blit(texto2, (85, 600))
		
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = 0
					sys.exit() 
			
				elif event.type == pygame.KEYDOWN:
					numero = 4
		
			if numero == 4:
				break
			
								
		
			pygame.display.update()

	pygame.display.update()
