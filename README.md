# propagacion-gusano

Se da una red re computadoras y en el tiempo de enlaces entre ellas, sabiendo el momento en que se infectaron determinadas computadoras, se determina donde se originó el problema.

---

DESCRIPCION DEL PROBLEMA

---

Un virus del tipo “gusano” infecta redes de computadoras. Este virus, una vez que
llega a una computadora, se retransmite a todas las computadoras vecinas. La figura
muestra el mapa de la red, detallando las computadoras, los enlaces bidireccionales
de telecomunicaciones, y el tiempo que demanda la transmisión completa del gusano
por cada enlace de la red. Los tiempos de retransmisión del gusano en cada
computadora son despreciables.

---

SE PIDE

---

-- Tome como entrada el mapa de la red y una lista de pares (computadora, hora) que indica la hora en segundos en la que el gusano llegó por primera vez a dicha computadora.

-- Indique el/las computadora(s) donde se puede haber originado el gusano.

---

DATOS DE ENTRADA

---

-- La cantidad de enlaces de la red (menor o igual a 30000)

-- Una línea por cada enlace de la red, formada por el número de la computadora origen (entre 1 y 1000), el tiempo que demanda la transmisión del gusano por el enlace (entre 1 y 50), y el número de la computadora destino (entre 1 y 1000)

-- La cantidad de pares (computadora, hora) de llegada del gusano (menor o igual a 100)

-- una línea por cada par (computadora, hora), formada por el número de la computadora y la hora a la que arribó el gusano a dicha computadora (en segundos, menor o igual a 20000)

---

DATOS DE SALIDA

---

Se deberá grabar un archivo gusano.out que contendrá una línea con cada computadora donde se puede haber generado el gusano.

---

EJEMPLO

---

Dado el input:

17<br />
1 2 3<br />
1 3 2<br />
3 2 4<br />
2 4 5<br />
4 4 5<br />
11 2 10<br />
12 3 10<br />
10 1 5<br />
5 2 6<br />
6 3 15<br />
6 3 8<br />
5 1 8<br />
10 4 13<br />
8 1 7<br />
8 2 9<br />
8 1 14<br />
13 2 14<br />
4<br />
7 2<br />
1 7<br />
15 5<br />
12 4<br />

El resultado esperado es:

5
