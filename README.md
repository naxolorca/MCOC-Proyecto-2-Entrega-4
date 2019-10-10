# MCOC-Proyecto-2
Proyecto 2 Métodos computacionales para Obras Civiles

Para una simulación con un dt de 0.001 segundos, un t max de 0.5 segundos y un diametro de particulas de 5.6 mm se obtuvieron los siguientes resultados.

## Especificaciones del computador

	S.O Ubuntu 18.04
	CPU i7-6560u @ 2.20 GHz Turbo 3.20 GHz
	Ram 16gb LPDDR3 1867 MHz

## Tiempo de simulación

	Para 1 particula:   0.8s
	Para 2 particulas:  2.0s
	Para 3 particulas:  3.5s
	Para 5 particulas:  8.6s
	Para 8 particulas:  48.3s
	Para 10 particulas: 80.8s
	Para 12 particulas: 151.6s
	
## Graficos
	1 particula

(https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/ruta/al/asset/Grafico_01.png)

	2 particulas

(https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/ruta/al/asset/Grafico 02.png)

	3 particulas

(https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/ruta/al/asset/Grafico 03.png)

	5 particulas

(https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/ruta/al/asset/Grafico 05.png)

	8 particulas

(https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/ruta/al/asset/Grafico 08.png)

	10 particulas

(https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/ruta/al/asset/Grafico 10.png)

	12 particulas

(https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/ruta/al/asset/Grafico 12.png)

## Discución

	Utilizando el codigo con integración mejorada, se puede notar que python integra de forma 
	veloz cada particula por separado, pero se puede notar un claro cuello de botella en la 
	parte del codigo responsable de encontrar y aplicar un choque entre particulas. Este codigo 
	se compone de 2 recorridos for, por lo que se comprueba que cada particula por separado no 
	choque con las demas, es por esto que aumento de forma exponencia el tiempo necesario para
	recorrer estos ciclos y resolver de forma adecuada el programa.

