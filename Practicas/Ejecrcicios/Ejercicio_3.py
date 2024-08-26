
# texto y las letras al usuario
texto = input("Ingrese un texto: ").lower()
letras = input("Ingrese tres letras: ").lower()

# Análisis 1: Contamos las letras
letras_lista = list(letras)
conteo_letras = [texto.count(letra) for letra in letras_lista]
print("Frecuencia de cada letra:", dict(zip(letras_lista, conteo_letras)))

# Análisis 2: Contamos las palabras
palabras = texto.split()
print("Número de palabras:", len(palabras))

# Análisis 3: Primera y última letra
print("Primera letra:", texto[0])
print("Última letra:", texto[-1])

# Análisis 4: Invertimos el orden de las palabras
palabras_invertidas = palabras[::-1]
texto_invertido = " ".join(palabras_invertidas)
print("Texto con palabras invertidas:", texto_invertido)

# Análisis 5: Buscamos la palabra "Python"
python_en_texto = "python" in texto
print("¿Se encuentra 'Python' en el texto?", python_en_texto)

# Este código utiliza métodos de strings como lower(), count(), split(), join() y slicing para realizar los análisis solicitados. También utiliza listas y diccionarios para almacenar y mostrar los resultados. ¡Espero que te guste!