# ---------------------------------------------------------------
# Título del trabajo: Seguimiento #1 Python "LISTAS"
# Nombre: [Jerónimo Vallejo Quintero]
# Fecha de creación: 17/11/2024
# Descripción:  Ejercicios prácticos para 
#              aprender a manipular listas en Python.
# ---------------------------------------------------------------

# ======================================================
# Ejercicio 1:
# Crear una lista con los nombres de 5 frutas colombianas favoritas
# y mostrarla por pantalla.
# ======================================================
# Creamos una lista con nombres de frutas.
frutas = ["Guanábana", "Lulo", "Maracuyá", "Borojó", "Chontaduro"]
print("Lista de frutas colombianas favoritas:", frutas)

# ======================================================
# Ejercicio 2:
# Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
# ======================================================
# Imprimimos el segundo y cuarto elemento usando índices.
print("Segundo elemento:", frutas[1])
print("Cuarto elemento:", frutas[3])

# ======================================================
# Ejercicio 3:
# Crear una lista con los números del 1 al 10 y mostrar su longitud.
# ======================================================
# Usamos range para crear la lista de números y len para obtener su longitud.
numeros = list(range(1, 11))
print("Lista de números:", numeros)
print("Longitud de la lista de números:", len(numeros))

# ======================================================
# Ejercicio 4:
# Concatenar las dos listas creadas en los ejercicios 1 y 3.
# ======================================================
# Concatenamos las listas frutas y numeros.
lista_concatenada = frutas + numeros
print("Lista concatenada:", lista_concatenada)

# ======================================================
# Ejercicio 5:
# Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
# ======================================================
# Reemplazamos el tercer elemento por 100.
lista_concatenada[2] = 100
print("Lista modificada:", lista_concatenada)

# ======================================================
# Ejercicio 6:
# Borrar el último elemento de la lista del ejercicio 4.
# ======================================================
# Usamos pop para eliminar el último elemento de la lista.
lista_concatenada.pop()
print("Lista después de eliminar el último elemento:", lista_concatenada)

# ======================================================
# Ejercicio 7:
# Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
# ======================================================
# Creamos una lista y multiplicamos cada elemento por 5 usando una comprensión de listas.
numeros_3 = [2, 4, 6]
multiplicados = [x * 5 for x in numeros_3]
print("Lista original:", numeros_3)
print("Lista con elementos multiplicados por 5:", multiplicados)

# ======================================================
# Ejercicio 8:
# Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
# ======================================================
# Creamos dos listas y multiplicamos sus elementos usando zip y una comprensión de listas.
lista_a = [1, 2, 3, 4, 5]
lista_b = [10, 20, 30, 40, 50]
producto = [a * b for a, b in zip(lista_a, lista_b)]
print("Lista A:", lista_a)
print("Lista B:", lista_b)
print("Producto de elementos correspondientes:", producto)

# ======================================================
# Ejercicio 9:
# Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
# ======================================================
# Creamos una lista de listas.
listas_anidadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
segundo_elemento = listas_anidadas[1][1]
print("Lista anidada:", listas_anidadas)
print("Segundo elemento de la segunda lista:", segundo_elemento)

# ======================================================
# Ejercicio 10:
# Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
# ======================================================
# Usamos slicing para tomar los elementos del índice 2 al 6.
sublista = numeros[2:7]
print("Sublista del índice 2 al 6:", sublista)

# ======================================================
# Ejercicio 11:
# Usar el método `.append()` para agregar un nuevo elemento
# al final de la lista del ejercicio 1.
# ======================================================
# Agregamos una nueva fruta a la lista.
frutas.append("Mango")
print("Lista después de agregar una fruta:", frutas)

# ======================================================
# Ejercicio 12:
# Usar el método `.insert()` para agregar un nuevo elemento
# en la posición 2 de la lista del ejercicio 3.
# ======================================================
# Insertamos un número en la posición 2 de la lista.
numeros.insert(2, 99)
print("Lista después de la inserción:", numeros)

# ======================================================
# Ejercicio 13:
# Usar el método `.remove()` para eliminar un elemento
# específico de la lista del ejercicio 7.
# ======================================================
# Eliminamos un número específico de la lista.
multiplicados.remove(10)
print("Lista después de eliminar el elemento 10:", multiplicados)

# ======================================================
# Ejercicio 14:
# Usar el método `.reverse()` para invertir el orden
# de la lista del ejercicio 4.
# ======================================================
# Invertimos el orden de la lista concatenada.
lista_concatenada.reverse()
print("Lista invertida:", lista_concatenada)

# ======================================================
# Ejercicio 15:
# Usar el método `.sort()` para ordenar de forma ascendente
# la lista del ejercicio 7.
# ======================================================
# Ordenamos la lista en forma ascendente.
multiplicados.sort()
print("Lista ordenada:", multiplicados)

# ======================================================
# Ejercicio 16:
# Usar el método `.pop()` para eliminar y obtener el último
# elemento de la lista del ejercicio 4.
# ======================================================
# Eliminamos y obtenemos el último elemento.
ultimo_elemento = lista_concatenada.pop()
print("Último elemento eliminado:", ultimo_elemento)
print("Lista después de usar pop:", lista_concatenada)

# ======================================================
# Ejercicio 17:
# Usar el método `.count()` para contar cuántas veces aparece
# un elemento específico en la lista del ejercicio 7.
# ======================================================
# Contamos cuántas veces aparece el número 15.
cantidad = multiplicados.count(15)
print("El número 15 aparece", cantidad, "veces en la lista.")

# ======================================================
# Ejercicio 18:
# Usar el método `.index()` para obtener el índice de un elemento
# específico en la lista del ejercicio 4.
# ======================================================
# Obtenemos el índice de un elemento específico.
if 100 in lista_concatenada:
    indice = lista_concatenada.index(100)
    print("El índice del elemento 100 es:", indice)
else:
    print("El elemento 100 no está en la lista.")

# ======================================================
# Ejercicio 19:
# Usar el método `.clear()` para eliminar todos los elementos
# de la lista del ejercicio 1.
# ======================================================
# Limpiamos la lista de frutas.
frutas.clear()
print("Lista de frutas después de usar clear:", frutas)

# ======================================================
# Ejercicio 20:
# Crear una lista vacía y utilizar un bucle `for` para agregar
# los números del 1 al 10.
# ======================================================
# Creamos una lista vacía y agregamos números con un bucle for.
lista_vacia = []
for i in range(1, 11):
    lista_vacia.append(i)
print("Lista llena con números del 1 al 10:", lista_vacia)

# ======================================================
# Ejercicio 21:
# Crear una lista de números enteros y utilizar un bucle `while`
# para eliminar los elementos impares.
# ======================================================
# Creamos una lista y eliminamos los números impares usando while.
numeros_enteros = list(range(1, 11))
i = 0
while i < len(numeros_enteros):
    if numeros_enteros[i] % 2 != 0:
        numeros_enteros.pop(i)
    else:
        i += 1
print("Lista después de eliminar impares:", numeros_enteros)

# ======================================================
# Ejercicio 22:
# Crear una lista con los nombres de 5 materias favoritas y
# ordenarlas alfabéticamente.
# ======================================================
# Creamos y ordenamos una lista de materias.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Química"]
materias.sort()
print("Materias ordenadas alfabéticamente:", materias)

# ======================================================
# Ejercicio 23:
# Crear una lista con los números del 1 al 15 y mostrar
# solo los múltiplos de 3.
# ======================================================
# Creamos una lista y usamos una comprensión para obtener los múltiplos de 3.
numeros_15 = list(range(1, 16))
multiplos_3 = [x for x in numeros_15 if x % 3 == 0]
print("Múltiplos de 3:", multiplos_3)

# ======================================================
# Ejercicio 24:
# Crear una lista con los nombres de 10 artistas favoritos y
# utilizar un bucle `for` para imprimir cada nombre en mayúsculas.
# ======================================================
# Creamos una lista de artistas y los imprimimos en mayúsculas.
artistas = ["Shakira", "J Balvin", "Maluma", "Carlos Vives", "Juanes",
            "Karol G", "Andrés Cepeda", "Fonseca", "Camilo", "Sebastián Yatra"]
print("Artistas en mayúsculas:")
for artista in artistas:
    print(artista.upper())

# ======================================================
# Ejercicio 25:
# Crear una lista con los números del 1 al 20 y utilizar
# una comprensión de listas para crear una nueva lista con
# solo los números pares.
# ======================================================
# Creamos una lista con números pares usando una comprensión.
pares = [x for x in range(1, 21) if x % 2 == 0]
print("Números pares:", pares)

# ======================================================
# Ejercicio 26:
# Crear una lista con los nombres de los municipios de Arauca
# y utilizar un bucle `for` para imprimir cada nombre en orden inverso.
# ======================================================
municipios = ["Arauca", "Tame", "Saravena", "Fortul", "Arauquita", "Cravo Norte", "Puerto Rondón"]
print("Municipios en orden inverso:")
for municipio in municipios:
    print(municipio[::-1])

# ======================================================
# Ejercicio 27:
# Crear una lista con los números del 1 al 12 y utilizar una comprensión
# de listas para crear una nueva lista con los cuadrados de cada número.
# ======================================================
numeros_12 = list(range(1, 13))
cuadrados = [x**2 for x in numeros_12]
print("Cuadrados de los números:", cuadrados)

# ======================================================
# Ejercicio 28:
# Crear una lista con los meses del año y utilizar el método `.index()`
# para obtener el índice del mes "Junio".
# ======================================================
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
indice_junio = meses.index("Junio")
print("El índice de 'Junio' es:", indice_junio)

# ======================================================
# Ejercicio 29:
# Crear una lista con los nombres de 6 mascotas y utilizar el método `.remove()`
# para eliminar una mascota de la lista.
# ======================================================
mascotas = ["Luna", "Max", "Bella", "Simba", "Rocky", "Milo"]
mascotas.remove("Simba")
print("Lista de mascotas después de eliminar 'Simba':", mascotas)

# ======================================================
# Ejercicio 30:
# Crear una lista con los números del 1 al 20 y utilizar el método
# `.sort(reverse=True)` para ordenarla de forma descendente.
# ======================================================
numeros_20 = list(range(1, 21))
numeros_20.sort(reverse=True)
print("Lista ordenada de forma descendente:", numeros_20)

# ======================================================
# Ejercicio 31:
# Crear una lista con los nombres de 4 libros favoritos y utilizar el método
# `.append()` para agregar un nuevo libro al final de la lista.
# ======================================================
libros = ["Cien años de soledad", "El amor en los tiempos del cólera", 
          "La ciudad y los perros", "Crónica de una muerte anunciada"]
libros.append("Rayuela")
print("Lista de libros después de agregar uno:", libros)

# ======================================================
# Ejercicio 32:
# Crear una lista con los números del 1 al 15 y utilizar una comprensión
# de listas para crear una nueva lista con los números impares.
# ======================================================
numeros_impares = [x for x in range(1, 16) if x % 2 != 0]
print("Números impares:", numeros_impares)

# ======================================================
# Ejercicio 33:
# Crear una lista con los nombres de 7 comidas favoritas y utilizar el método
# `.insert()` para agregar una nueva comida en la posición 3.
# ======================================================
comidas = ["Pizza", "Hamburguesa", "Arepa", "Bandeja Paisa", "Sancocho", "Tacos", "Ceviche"]
comidas.insert(3, "Empanada")
print("Lista de comidas después de la inserción:", comidas)

# ======================================================
# Ejercicio 34:
# Crear una lista con los números del 1 al 10 y utilizar el método `.extend()`
# para agregar una segunda lista con los números del 11 al 15.
# ======================================================
numeros_10 = list(range(1, 11))
numeros_11_15 = list(range(11, 16))
numeros_10.extend(numeros_11_15)
print("Lista extendida:", numeros_10)

# ======================================================
# Ejercicio 35:
# Crear una lista con los nombres de 6 compañeros y utilizar el método `.count()`
# para contar cuántas veces aparece un nombre específico en la lista.
# ======================================================
companeros = ["Juan", "María", "Pedro", "Ana", "Juan", "Lucía"]
cantidad_juan = companeros.count("Juan")
print("El nombre 'Juan' aparece", cantidad_juan, "veces en la lista.")

# ======================================================
# Ejercicio 36:
# Crear una lista con los números del 1 al 12 y utilizar una comprensión
# de listas para crear una nueva lista con los números divisibles por 3.
# ======================================================
divisibles_3 = [x for x in range(1, 13) if x % 3 == 0]
print("Números divisibles por 3:", divisibles_3)

# ======================================================
# Ejercicio 37:
# Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar
# el método `.reverse()` para invertir el orden de la lista.
# ======================================================
artistas_musicales = ["Shakira", "J Balvin", "Maluma", "Juanes", "Karol G"]
artistas_musicales.reverse()
print("Lista de artistas en orden inverso:", artistas_musicales)

# ======================================================
# Ejercicio 38:
# Crear una lista con los números del 1 al 20 y utilizar una función lambda y el
# método `.sort()` para ordenar la lista de forma descendente.
# ======================================================
numeros_20_lambda = list(range(1, 21))
numeros_20_lambda.sort(key=lambda x: -x)
print("Lista ordenada con lambda de forma descendente:", numeros_20_lambda)

# ======================================================
# Ejercicio 39:
# Crear una lista con las materias de la universidad y utilizar el método `.pop()`
# para eliminar y obtener el último elemento de la lista.
# ======================================================
materias_universidad = ["Cálculo", "Física", "Programación", "Álgebra", "Estadística"]
ultima_materia = materias_universidad.pop()
print("Última materia eliminada:", ultima_materia)
print("Lista después de eliminar la última materia:", materias_universidad)

# ======================================================
# Ejercicio 40:
# Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas
# para crear una nueva lista con los números múltiplos de 5.
# ======================================================
multiplos_5 = [x for x in range(1, 26) if x % 5 == 0]
print("Números múltiplos de 5:", multiplos_5)

# ======================================================
# Ejercicio 41:
# Crear una lista con los nombres de 8 deportes y utilizar una función 
# anónima y el método `.sort()` para ordenar la lista.
# ======================================================
deportes = ["Fútbol", "Baloncesto", "Voleibol", "Natación", 
            "Atletismo", "Ciclismo", "Boxeo", "Tenis"]
deportes.sort(key=lambda deporte: deporte)
print("Deportes ordenados alfabéticamente:", deportes)

# ---------------------------------------------------------------
# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
# ---------------------------------------------------------------
lista_a_limpiar = list(range(1, 16))
lista_a_limpiar.clear()
print("Lista después de usar clear():", lista_a_limpiar)

# ---------------------------------------------------------------
# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
# ---------------------------------------------------------------
paises = ["Colombia", "Brasil", "Argentina", "Chile", "México", "Perú"]
for pais in paises:
    print(pais.lower())

# ---------------------------------------------------------------
# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
# ---------------------------------------------------------------
cuadrados_pares = [n**2 for n in range(1, 21) if n % 2 == 0]
print("Cuadrados de los números pares:", cuadrados_pares)

# ---------------------------------------------------------------
# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
# ---------------------------------------------------------------
videojuegos = ["Minecraft", "Fortnite", "GTA V", "Call of Duty", "FIFA", "Among Us", "Valorant", "PUBG", "Roblox", "League of Legends"]
indice_fifa = videojuegos.index("FIFA")
print("El índice del juego 'FIFA' es:", indice_fifa)

# ---------------------------------------------------------------
# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
# ---------------------------------------------------------------
numeros_1_12 = list(range(1, 13))
numeros_1_12.remove(8)
print("Lista después de eliminar el número 8:", numeros_1_12)

# ---------------------------------------------------------------
# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
# ---------------------------------------------------------------
monumentos = ["Santuario de Las Lajas", "Castillo de San Felipe", "Parque Tayrona", "Ciudad Perdida", "Catedral de Sal", "La Piedra del Peñol", "Caño Cristales"]
monumentos.sort(key=lambda x: len(x))
print("Monumentos ordenados por longitud:", monumentos)

# ---------------------------------------------------------------
# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
# ---------------------------------------------------------------
multiplos_3_5 = [n for n in range(1, 19) if n % 3 == 0 and n % 5 == 0]
print("Múltiplos de 3 y 5:", multiplos_3_5)

# ---------------------------------------------------------------
# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
# ---------------------------------------------------------------
asignaturas_interesantes = ["Inteligencia Artificial", "Redes", "Ciberseguridad", "Bases de Datos", "Programación Avanzada", "Análisis de Datos"]
asignaturas_interesantes.append("Sistemas Embebidos")
print("Lista de asignaturas después de agregar una nueva:", asignaturas_interesantes)

# ---------------------------------------------------------------
# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
# ---------------------------------------------------------------
numeros_1_25 = list(range(1, 26))
elemento_eliminado = numeros_1_25.pop(7)
print("Elemento eliminado en la posición 7:", elemento_eliminado)
print("Lista después de eliminar el elemento:", numeros_1_25)


