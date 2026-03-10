Algoritmo geometric_areas
	
	Definir piValor Como Real
	piValor <- 3.1416
	
	Definir lado, baseRect, alturaRect, baseTri, alturaTri, radio Como Real
	Definir areaCuadrado, areaRectangulo, areaTriangulo, areaCirculo, totalAreas Como Real
	
	Escribir "Ingrese el lado del cuadrado:"
	Leer lado
	areaCuadrado <- lado * lado
	
	Escribir "Ingrese la base del rectangulo:"
	Leer baseRect
	Escribir "Ingrese la altura del rectangulo:"
	Leer alturaRect
	areaRectangulo <- baseRect * alturaRect
	
	Escribir "Ingrese la base del triangulo:"
	Leer baseTri
	Escribir "Ingrese la altura del triangulo:"
	Leer alturaTri
	areaTriangulo <- (baseTri * alturaTri) / 2
	
	Escribir "Ingrese el radio del circulo:"
	Leer radio
	areaCirculo <- piValor * radio * radio
	
	totalAreas <- areaCuadrado + areaRectangulo + areaTriangulo + areaCirculo
	
	Escribir "Total de todas las areas: ", totalAreas
	
FinAlgoritmo
