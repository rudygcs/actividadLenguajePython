# Pedir al usuario que ingrese los tres textos
texto1 = input("Ingresa el primer texto: ")
texto2 = input("Ingresa el segundo texto: ")
texto3 = input("Ingresa el tercer texto: ")

# Calcular la longitud de cada texto
longitud_texto1 = len(texto1)
longitud_texto2 = len(texto2)
longitud_texto3 = len(texto3)

# Calcular el promedio de las longitudes
promedio_longitudes = (longitud_texto1 + longitud_texto2 + longitud_texto3) / 3

# Concatenar los textos
texto_concatenado = texto1 + texto2 + texto3

# Verificar la longitud de la concatenación
longitud_concatenacion = len(texto_concatenado)
resultado_longitud = ""

if longitud_concatenacion > 15:
    resultado_longitud = "mayor"
elif longitud_concatenacion < 15:
    resultado_longitud = "menor"
else:
    resultado_longitud = "igual"

# Encontrar el texto más largo
texto_mas_largo = max(texto1, texto2, texto3, key=len)

# Contar los caracteres numéricos en la concatenación
caracteres_numericos = sum(1 for caracter in texto_concatenado if caracter.isdigit())

# Mostrar los resultados
print(f"El promedio de las longitudes de los textos es: {promedio_longitudes}")
print(f"La longitud de la concatenación es {resultado_longitud} a 15.")
print(f"El texto más largo es: {texto_mas_largo}")
print(f"La cantidad de caracteres numéricos en la concatenación es: {caracteres_numericos}")
