# Definición de variables de diferentes tipos primitivos
edad = 42
Indice = 87.35
cadena = "Los datos son:"
booleano = True

# Concatenación de variables con conversión adecuada
resultado_concatenacion = cadena+ "edad: " + str(edad) + " promedio: " + str(Indice) + " Valor: " + str(booleano)

# Impresión del resultado de la concatenación
print(resultado_concatenacion)

""" En Python 3, los enteros no tienen un límite fijo. Python utiliza la representación 
nativa del hardware para enteros largos (long integers). Esto significa que los enteros 
pueden crecer tanto como la memoria disponible en el sistema. No hay un límite teórico, 
pero en la práctica, el límite estará determinado por la cantidad de memoria RAM en tu máquina."""

""" Los números de punto flotante en Python siguen el estándar IEEE 754, que define varios
 formatos de representación de punto flotante con diferentes niveles de precisión. En Python, 
 los flotantes se implementan como float de 64 bits (doble precisión), que es el formato más 
 comúnmente utilizado."""

 #El rango y precisión de los flotantes de 64 bits en Python es aproximadamente:
 #-Mayor número positivo: alrededor de 1.8 x 10^308
 #-Mayor número negativo: alrededor de -1.8 x 10^308
 #-Más cercano a cero positivo: alrededor de 2.2 x 10^-308
 #-Más cercano a cero negativo: alrededor de -2.2 x 10^-308

 #**************************************************************************************

 #La fórmula para calcular la suma de los primeros n números pares es: Suma = n * (n + 1)

n = 5

suma_pares = n * (n + 1)

print("La suma de los primeros", n, "números pares es:", suma_pares)


