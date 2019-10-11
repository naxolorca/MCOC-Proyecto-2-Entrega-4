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
**Simulacíon 1**

![Grafico_01](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/simulacion-1/Grafico_10.png)

**Simulacíon 2**

![Grafico_02](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/simulacion-2/Grafico_05.png)

**Simulacíon 3**

![Grafico_03](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/simulacion-3/Grafico_02.png)

**Simulacíon 4**

![Grafico_05](https://raw.githubusercontent.com/naxolorca/MCOC-Proyecto-2-Entrega-4/master/simulacion-4/Grafico_20.png)



## Discusión

	Utilizando el codigo con integración mejorada, se puede notar que python integra de forma 
	veloz cada particula por separado, pero se puede notar un claro cuello de botella en la 
	parte del codigo responsable de encontrar y aplicar un choque entre particulas. Este codigo 
	se compone de 2 recorridos for, por lo que se comprueba que cada particula por separado no 
	choque con las demas, es por esto que aumento de forma exponencia el tiempo necesario para
	recorrer estos ciclos y resolver de forma adecuada el programa.

