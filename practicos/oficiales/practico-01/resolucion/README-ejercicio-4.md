# Ejercicio 4

## Enunciado

Una maquina de Turing con **cinta doblemente infinita** es una MT cuya cinta es infinita tanto a la izquierda como a la derecha (las celdas estan indexadas por \(\mathbb Z\)). Mostrar que estas maquinas reconocen los mismos lenguajes que las maquinas de Turing estandar (Problema 3.11 de Sipser).

## Modelos involucrados

- **MT estandar (\(\TM_{\text{std}}\)):** una sola cinta infinita hacia la derecha, con extremo izquierdo. Si el cabezal intenta cruzar el extremo izquierdo, se queda en su lugar (Sipser, pag. 168).
- **MT doblemente infinita (\(\TM_{2}\)):** una sola cinta indexada por \(\mathbb Z\), sin extremo izquierdo. Inicialmente la entrada \(w=w_0\cdots w_{n-1}\) ocupa las celdas \(0,1,\dots,n-1\) y el resto contiene blancos.

## Teorema

\[
  \mathcal L(\TM_{\text{std}}) = \mathcal L(\TM_{2}).
\]

Demostramos las dos inclusiones por separado.

---

## (1) \(\mathcal L(\TM_{\text{std}}) \subseteq \mathcal L(\TM_{2})\)

Esta inclusion es trivial, pero damos una construccion explicita.

**Idea.** Sea \(M\in\TM_{\text{std}}\). Construimos \(N\in\TM_{2}\) que simula a \(M\) reservando un marcador de borde izquierdo \(\vdash\in\Gamma_N\setminus\Gamma_M\) en alguna celda fija (por ejemplo, la celda \(-1\)) y nunca permite que su cabezal cruce ese marcador hacia la izquierda.

**Construccion.**
\(N=\) "Con entrada \(w\):
1. Antes de comenzar la simulacion, escribir \(\vdash\) en la celda \(-1\).
2. Simular paso a paso a \(M\) sobre las celdas \(0,1,\dots\). Toda transicion de \(M\) se traslada literalmente a \(N\).
3. Si la simulacion intenta moverse a la izquierda y la celda actual contiene \(\vdash\), \(N\) se queda en su lugar (replicando el comportamiento de borde izquierdo de \(M\)).
4. Cuando \(M\) acepta o rechaza, \(N\) acepta o rechaza."

Cada paso de \(M\) se simula con un paso (o, en el caso del borde izquierdo, dos pasos contables) de \(N\). Por lo tanto:
\[
  L(N) = L(M).
\]
Asi todo lenguaje reconocible por una MT estandar lo es tambien por una MT doblemente infinita.

---

## (2) \(\mathcal L(\TM_{2}) \subseteq \mathcal L(\TM_{\text{std}})\)

Es la direccion no trivial. Sea
\[
  B = (Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}}) \in \TM_{2}.
\]
Construimos una MT estandar \(S\) que simula \(B\) "doblando" la cinta sobre si misma: las celdas con indice no negativo van en posiciones pares y las de indice negativo van en posiciones impares.

### 2.1. Codificacion de celdas

Definimos la biyeccion \(e:\mathbb Z\to\mathbb N\) por:
\[
  e(i) =
  \begin{cases}
    2i & \text{si } i\ge 0,\\
    -2i - 1 & \text{si } i<0.
  \end{cases}
\]
Es decir,
\[
  0\mapsto 0,\quad 1\mapsto 2,\quad 2\mapsto 4,\dots,\quad -1\mapsto 1,\quad -2\mapsto 3,\dots
\]
La funcion \(e\) es la misma usada en la teoria de la catedra (`Diag.pdf`) para enumerar \(\mathbb Z\) a partir de \(\mathbb N\).

En la cinta de \(S\), la celda \(e(i)\) contendra el simbolo que \(B\) tiene en la celda \(i\).

Para marcar la posicion del cabezal de \(B\) usamos un alfabeto de cinta extendido
\[
  \Gamma_S = \Gamma \cup \dot\Gamma,\quad \dot\Gamma=\{\dot a : a\in\Gamma\}.
\]
La celda de \(S\) cuyo contenido esta "punteado" indica donde esta posicionado el cabezal simulado de \(B\). Por construccion mantenemos la invariante:

> En todo momento, exactamente una celda de la cinta de \(S\) tiene un simbolo en \(\dot\Gamma\), y esa celda corresponde a la posicion del cabezal de \(B\).

### 2.2. Configuracion inicial

Si la entrada es \(w=w_0w_1\cdots w_{n-1}\), \(B\) la dispone en las celdas \(0,1,\dots,n-1\). Bajo la codificacion \(e\), eso corresponde a las celdas \(0,2,4,\dots,2(n-1)\) de \(S\). El resto de la cinta, en particular las celdas impares \(1,3,5,\dots\) (que codifican posiciones negativas), debe contener blancos.

\(S\) realiza, antes de la simulacion, una fase de inicializacion: en una pasada finita reorganiza \(w\) en las posiciones pares e intercala blancos en las impares. Luego marca la celda \(0\) como \(\dot w_0\) (el cabezal de \(B\) esta inicialmente en la celda \(0\)).

### 2.3. Simulacion de un paso

Supongamos que \(S\) esta simulando el estado \(q\) de \(B\) y lee \(\dot a\) en la posicion codificada \(k=e(h)\), donde \(h\) es la posicion actual del cabezal de \(B\). Si
\[
  \delta(q,a) = (p,b,D),\qquad D\in\{L,R\},
\]
entonces \(S\) hace:

1. reemplazar \(\dot a\) por \(b\) (sin marca) en la celda \(k\);
2. calcular \(k'=e(h')\) donde \(h'=h\pm 1\) segun \(D\);
3. marcar la celda \(k'\) escribiendo \(\dot{c}\), siendo \(c\) el simbolo que ya estaba alli;
4. actualizar el estado simulado a \(p\).

Las formulas explicitas para \(k'\) se obtienen examinando los casos de paridad de \(k\):

**Caso \(D=R\)** (de \(h\) a \(h+1\)):
\[
  k' =
  \begin{cases}
    k+2 & \text{si } k\text{ es par } (h\ge 0,\ h'=h+1\ge 0),\\
    0   & \text{si } k=1 \quad (h=-1,\ h'=0),\\
    k-2 & \text{si } k>1\text{ impar} \quad (h\le -2,\ h'=h+1<0).
  \end{cases}
\]

**Caso \(D=L\)** (de \(h\) a \(h-1\)):
\[
  k' =
  \begin{cases}
    1   & \text{si } k=0 \quad (h=0,\ h'=-1),\\
    k-2 & \text{si } k>0\text{ par} \quad (h\ge 1,\ h'=h-1\ge 0),\\
    k+2 & \text{si } k\text{ es impar} \quad (h\le -1,\ h'=h-1<0).
  \end{cases}
\]

En todos los casos, \(S\) solo necesita moverse a lo sumo dos celdas (en su cinta fisica) para reubicar la marca, lo cual es operacion estandar de una MT.

### 2.4. Correctitud

**Invariante de simulacion:** despues de simular el paso \(t\)-esimo, la cinta de \(S\) contiene en la celda \(e(i)\) exactamente el simbolo que \(B\) tiene en la celda \(i\) tras \(t\) pasos, y la unica celda con simbolo punteado coincide con la posicion del cabezal de \(B\).

Probamos el invariante por induccion en \(t\).

- **Base (\(t=0\)):** se cumple por la inicializacion descrita en 2.2.
- **Paso inductivo:** las reglas 2.3 reflejan exactamente la transicion de \(B\). En particular, las formulas de \(k'\) se derivan algebraicamente de \(e\) y respetan \(h\to h\pm 1\). Por lo tanto, despues de simular el paso \(t+1\) el invariante sigue siendo valido.

**Aceptacion.** \(S\) acepta sii \(B\) entra en \(q_{\text{accept}}\); analogamente para rechazo. Como \(B\) y \(S\) realizan computos paso a paso equivalentes, recorren los mismos estados (modulo la simulacion). En particular,
\[
  L(S) = L(B).
\]

Esto demuestra \(\mathcal L(\TM_{2})\subseteq \mathcal L(\TM_{\text{std}})\).

---

## Conclusion

Combinando ambas inclusiones:
\[
  \mathcal L(\TM_{\text{std}}) = \mathcal L(\TM_{2}).
\]

Las MT con cinta doblemente infinita reconocen exactamente los mismos lenguajes que las MT estandar.

## Comentario

El fenomeno aqui ilustrado es lo que Sipser llama **robustez** del modelo de MT (pag. 176): pequeñas variaciones en la definicion (cinta de un lado o de dos lados, una o varias cintas, deterministica o no, etc.) no cambian la clase de lenguajes reconocibles. La codificacion \(e\) es la misma idea que la biyeccion \(\mathbb N\cong\mathbb Z\) usada en la teoria de la catedra para argumentos de cardinalidad; aqui la usamos como tecnica de simulacion concreta.
