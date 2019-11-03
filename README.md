# MCOC-Proyecto-2
Proyecto 2 Métodos computacionales para Obras Civiles

Para una simulación con un dt de 0.001 segundos, un t max de 0.5 segundos y un diametro de particulas de 5.6 mm se obtuvieron los siguientes resultados.

## Especificaciones del computador

	S.O Ubuntu 18.04
	CPU i7-6560u @ 2.20 GHz Turbo 3.20 GHz
	Ram 16gb LPDDR3 1867 MHz

## Tiempo de simulación

	Para la simulación 1:   547.0s
	Para la simulación 2:   52.0s
	Para la simulación 3:   5.1s
	Para la simulación 4:   --s
	
## Graficos
**Simulación 1**

![Grafico_01](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/simulacion-1/Grafico_10.png)

**Simulación 2**

![Grafico_02](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/simulacion-2/Grafico_05.png)

**Simulación 3**

![Grafico_03](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/simulacion-3/Grafico_02.png)

**Simulación 4**

![Grafico_05](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/simulacion-4/Grafico_20.png)



## Discusión

	Utilizando el codigo con integración mejorada, se puede notar que python integra de forma 
	veloz cada particula por separado, pero se puede notar un claro cuello de botella en la 
	parte del codigo responsable de encontrar y aplicar un choque entre particulas. Este codigo 
	se compone de 2 recorridos for, por lo que se comprueba que cada particula por separado no 
	choque con las demas, es por esto que aumento de forma exponencia el tiempo necesario para
	recorrer estos ciclos y resolver de forma adecuada el programa.

**Entrega 6 mejorada**
## Tiempo de simulación y Numero de particulas

	Para la simulación  1:   3.01s  	N = 1
	Para la simulación  2:   7.34s  	N = 3
	Para la simulación  3:   20.09s 	N = 10
	Para la simulación  4:   30.29s 	N = 15
	Para la simulación  5:   39.3s 		N = 20
	Para la simulación  6:   60.53s 	N = 30
	Para la simulación  7:   91.71s 	N = 45
	Para la simulación  8:   161.23s 	N = 70
	Para la simulación  9:   257s 		N = 100
	Para la simulación 10:   334.62s 	N = 120
	Para la simulación 11:   433.89s 	N = 150

**Simulación 1**

![Grafico_1](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/1.png)

**Simulación 2**

![Grafico_2](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/3.png)

**Simulación 3**

![Grafico_3](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/10.png)

**Simulación 4**

![Grafico_4](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/15.png)

**Simulación 5**

![Grafico_5](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/20.png)

**Simulación 6**

![Grafico_6](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/30.png)

**Simulación 7**

![Grafico_7](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/45.png)

**Simulación 8**

![Grafico_8](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/70.png)

**Simulación 9**

![Grafico_9](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/100.png)

**Simulación 10**

![Grafico_10](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/120.png)

**Simulación 11**

![Grafico_11](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico/150.png)

**Grafico N particulas vs Tiempo**

![Grafico_11](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/Mejorado/grafico.png)


## Discusión

	Utilizando este codigo podemos apreciar en el ultimo
	grafico, que el tiempo que se demora en ejecutar
	aumenta de forma lineal al aumentar la cantidad de
	partculas.
