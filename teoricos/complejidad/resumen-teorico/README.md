# Resumen Teórico: Complejidad Computacional

**Computabilidad y Complejidad — UNRC**
*Basado en el material de Pablo Castro (`Complejidad.pdf`)*

---

## Índice

1. [Introducción: del problema "¿se puede?" al problema "¿se puede rápido?"](#1-introducción-del-problema-se-puede-al-problema-se-puede-rápido)
2. [Tiempo de ejecución y notaciones asintóticas](#2-tiempo-de-ejecución-y-notaciones-asintóticas)
3. [Análisis de tiempo: un ejemplo guía](#3-análisis-de-tiempo-un-ejemplo-guía)
4. [Clases de complejidad temporal](#4-clases-de-complejidad-temporal)
5. [Modelos de computación y la Tesis de Church–Turing Extendida](#5-modelos-de-computación-y-la-tesis-de-churchturing-extendida)
6. [Máquinas no deterministas y su simulación](#6-máquinas-no-deterministas-y-su-simulación)
7. [La clase P y ejemplos](#7-la-clase-p-y-ejemplos)
8. [La clase NP](#8-la-clase-np)
9. [Verificadores y certificados](#9-verificadores-y-certificados)
10. [Ejemplos de problemas en NP](#10-ejemplos-de-problemas-en-np)
11. [P vs NP](#11-p-vs-np)
12. [Reducibilidad polinomial](#12-reducibilidad-polinomial)
13. [NP-completitud](#13-np-completitud)
14. [SAT, 3-SAT y el Teorema de Cook–Levin](#14-sat-3-sat-y-el-teorema-de-cookhlevin)
15. [Reducciones clásicas: 3-SAT a Clique, Vertex-Cover, HAMPATH](#15-reducciones-clásicas-3-sat-a-clique-vertex-cover-hampath)
16. [Complejidad espacial](#16-complejidad-espacial)
17. [El Teorema de Savitch](#17-el-teorema-de-savitch)
18. [Jerarquía P ⊆ NP ⊆ PSPACE ⊆ EXPTIME y PSPACE-Completitud](#18-jerarquía-p--np--pspace--exptime-y-pspace-completitud)
19. [Ideas clave para repasar](#19-ideas-clave-para-repasar)
20. [Preguntas típicas de examen](#20-preguntas-típicas-de-examen)
21. [Resumen ultra breve](#21-resumen-ultra-breve)

---

## 1. Introducción: del problema "¿se puede?" al problema "¿se puede rápido?"

En **computabilidad** la pregunta central es:

> Dado un problema $P$, ¿es computable?

En **complejidad**, en cambio, ya partimos de problemas computables. La pregunta cambia a:

> ¿Existen **algoritmos eficientes** para resolver $P$?

Surge entonces un interrogante metodológico: **¿qué modelo de cómputo elegimos para evaluar si un algoritmo es eficiente o no?** Esta cuestión es crucial y la respuesta —vía la **Tesis de Church–Turing Extendida**— justificará usar máquinas de Turing como modelo de referencia.

> **Intuición.** Computabilidad pregunta "¿hay algoritmo?". Complejidad pregunta "¿hay algoritmo cuyo tiempo crezca razonablemente con el tamaño de la entrada?". Ambas preguntas son matemáticas, pero la segunda introduce un parámetro adicional: el tamaño $n$ de la entrada y una función $T(n)$ que mide cuánto trabajo se realiza.

---

## 2. Tiempo de ejecución y notaciones asintóticas

### 2.1. Tiempo de ejecución como función

Dado un algoritmo (una MT) $M$, su tiempo de ejecución se modela mediante una función

$$T_M : \mathbb{N} \to \mathbb{R}^{\geq 0}$$

que asigna, a cada $n$, la cantidad de pasos que $M$ realiza sobre alguna entrada de tamaño $n$. Convenciones estándar:

- En general $T$ se asume **monótona**.
- $M$ es una MT que **termina en todas sus entradas**.
- El análisis se hace en el **peor caso**.
- Nos interesa cómo crece $T$ cuando $n$ se hace grande (comportamiento asintótico).

### 2.2. Notación $O$ (big-oh)

La notación $O$ permite ignorar constantes multiplicativas y términos de menor orden.

**Definición.**

$$f(n) \in O(g(n)) \iff \exists\, c, n_0 > 0 : \forall n \geq n_0 : f(n) \leq c \cdot g(n).$$

> **Intuición.** Para entradas grandes, $g$ crece **igual o más rápido** que $f$ módulo constantes multiplicativas. Es una cota superior asintótica.

### 2.3. Notación $o$ (little-oh)

Es una versión estricta de $O$.

**Definición.**

$$f(n) \in o(g(n)) \iff \exists\, c, n_0 > 0 : \forall n \geq n_0 : f(n) < c \cdot g(n).$$

Equivalentemente:

$$\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0 \iff f(n) \in o(g(n)).$$

> **Observación.** $g$ crece **estrictamente** más rápido que $f$. En particular, **nunca** ocurre $f(n) \in o(f(n))$.

### 2.4. Notación $\Omega$ (omega)

Sirve para **cotas por abajo**:

$$f(n) \in \Omega(g(n)) \iff \exists\, c, n_0 > 0 : \forall n \geq n_0 : f(n) \geq c \cdot g(n).$$

> **Intuición.** Para entradas grandes, $f$ crece **igual o más rápido** que $g$ módulo constantes.

### 2.5. Notación $\Theta$ (theta)

Indica que dos funciones crecen "de la misma forma":

$$f(n) \in \Theta(g(n)) \iff f(n) \in O(g(n)) \text{ y } f(n) \in \Omega(g(n)).$$

> **Intuición.** $f$ y $g$ crecen igual módulo constantes multiplicativas.

### 2.6. Relación entre notaciones

| Notación | Significado | Tipo de cota |
|---|---|---|
| $f \in O(g)$ | $f$ crece a lo sumo como $g$ | Superior (no estricta) |
| $f \in o(g)$ | $f$ crece estrictamente menos que $g$ | Superior estricta |
| $f \in \Omega(g)$ | $f$ crece al menos como $g$ | Inferior |
| $f \in \Theta(g)$ | $f$ y $g$ crecen al mismo ritmo | Ajustada |

---

## 3. Análisis de tiempo: un ejemplo guía

Trabajemos sobre el lenguaje:

$$A = \{ 0^k 1^k \mid k \geq 0 \}.$$

### 3.1. Primer algoritmo ($O(n^2)$)

Dado el input $w$:

1. Se recorre la cinta; si se encuentra `10`, se rechaza.
2. Se vuelve al principio, se tacha el primer `0` y se busca el primer `1` y se tacha.
3. Se repite el paso 2 hasta que:
   - No queden 0s ni 1s → **acepta**.
   - Queden solo 0s o solo 1s → **rechaza**.

**Análisis:**

- Paso 1: $O(n)$.
- Paso 2: cada pasada consume tiempo $O(n)$.
- Paso 3: se repite $\sim n/2$ veces.
- **Total:** $O(n) + O(n/2 \cdot n) \in O(n^2)$.

### 3.2. Segundo algoritmo ($O(n \log n)$)

Una idea más astuta: usar la paridad.

1. Recorrer la cinta; si se encuentra `10`, rechazar.
2. Repetir mientras haya 0s o 1s:
   - Contar la cantidad de 0s y 1s; si alguna es impar, rechazar.
   - Cada dos 0s, tachar uno (alternando), y lo mismo para los 1s.
3. Si no quedan 0s ni 1s, **acepta**; sino **rechaza**.

> **Ejemplo de corrida.** Con $w = 0^{25} 1^{25}$: la cantidad es par; tras tachar la mitad nos quedan 12 ceros y 12 unos; luego 6 y 6; luego 3 y 3; etc. En cada iteración el número se **divide por 2**, por lo que hay $O(\log n)$ iteraciones, cada una de costo $O(n)$. Total: $O(n \log n)$.

### 3.3. Tercer algoritmo: dos cintas ($O(n)$)

Con una MT de **dos cintas**:

1. Recorrer la cinta; si encuentra `10`, rechazar.
2. Recorrer la cinta y copiar los ceros a la segunda cinta.
3. Recorrer la cinta otra vez; cada vez que aparezca un `1`, tachar un cero en la segunda cinta. Si no hay más ceros, rechazar.
4. Si todos los ceros de la segunda cinta fueron tachados, **acepta**; sino rechaza.

Total: **$O(n)$** (cuatro fases lineales).

> **Idea clave.** El mismo problema admite algoritmos de tiempo muy diferente según el modelo y la astucia: $O(n^2)$, $O(n \log n)$, $O(n)$. Esto motiva preguntas finas: ¿cuál es el **mínimo** tiempo posible? ¿el modelo importa?

---

## 4. Clases de complejidad temporal

Las clases de complejidad permiten clasificar problemas por cotas superiores:

$$\mathrm{TIME}(t(n)) = \{ L \mid L \text{ se puede decidir con una MT en } O(t(n)) \text{ pasos}\}.$$

Por ejemplo, $\mathrm{TIME}(O(n^2))$ contiene los problemas para los cuales existe un algoritmo que, en el peor caso, realiza $c \cdot n^2$ pasos.

### Preguntas centrales de complejidad

- Dado un problema, ¿pertenece a $\mathrm{TIME}(O(t(n)))$?
- ¿Hay problemas en $\mathrm{TIME}(O(t(n)))$ pero **no** en $\mathrm{TIME}(O(t'(n)))$? (Jerarquías de complejidad.)

### Tabla del crecimiento (motivación: la clase P es "tratable")

| | $n=10$ | $n=20$ | $n=30$ | $n=40$ | $n=50$ |
|---|---|---|---|---|---|
| $n$ | 0.00001 s | 0.00002 s | 0.00003 s | 0.00004 s | 0.00005 s |
| $n^2$ | 0.0002 s | 0.0004 s | 0.0009 s | 0.0016 s | 0.0025 s |
| $n^3$ | 0.1 s | 3.2 s | 24.3 s | 1.7 min | 15.2 min |
| $2^n$ | 0.001 s | 1.0 s | 17.9 min | 12.7 días | 35.6 años |

> **Idea clave.** La diferencia entre **polinomial** y **exponencial** no es estética: para $n=50$ el algoritmo $n^3$ tarda 15 minutos y el $2^n$ tarda 35 años. Por eso se considera que los problemas con algoritmo en $O(n^k)$ son **tratables**.

### Definición de la clase P

$$\boxed{\;\mathrm{P} = \bigcup_{k > 0} \mathrm{TIME}(O(n^k)).\;}$$

Es decir, $\mathrm{P}$ son los problemas para los cuales existe un algoritmo polinomial que los resuelve.

**Propiedades clave:**

- $\mathrm{P}$ es **invariante** respecto a los modelos deterministas razonables de cómputo.
- Si un problema tiene solución polinomial, los avances en hardware se traducen en mejoras significativas en la práctica.

---

## 5. Modelos de computación y la Tesis de Church–Turing Extendida

### 5.1. Modelos vistos en la materia

- Máquinas de Turing deterministas con **una sola cinta**.
- Máquinas de Turing deterministas con **varias cintas**.
- Máquinas de Turing deterministas con cinta **infinita en ambos lados**.
- Máquinas de Turing **no deterministas**.

> Las primeras tres se pueden simular entre sí en **tiempo polinomial**. La clase $\mathrm{TIME}$ solo toma como referencia las máquinas deterministas.

### 5.2. MT multicinta vs MT de una cinta

**Teorema.** Cualquier MT con muchas cintas que hace $O(t(n))$ pasos puede ser traducida a una MT de una cinta que la simula en $O(t(n)^2)$ pasos.

**Idea de la simulación.** Se concatenan las $k$ cintas en una sola, separadas con un símbolo `#`, y se utilizan símbolos especiales para marcar dónde están las cabezas. Para cada paso de la MT multicinta se recorre la cinta de la MT simuladora (a lo sumo $k \cdot t(n)$ símbolos), realizando $O(t(n))$ pasos. Como hay $t(n)$ pasos a simular, el total es $O(t(n)^2)$.

### 5.3. Tesis de Church–Turing Extendida

Recordemos la **Tesis de Church–Turing** clásica:

> *Si un problema es computable por algún modelo razonable de computación, entonces es computable en todos los otros.*

La versión **extendida** agrega la dimensión temporal:

> *Si un problema es decidible en tiempo $O(t(n))$ por algún modelo razonable de computación (**determinista**), entonces es decidible en $O(t(n)^k)$ en cualquier otro modelo razonable de computación (**determinista**).*

> **Idea clave.** La tesis extendida justifica usar las MT deterministas como modelo de referencia: si un problema tiene un algoritmo polinomial en cualquier modelo razonable, tiene un algoritmo polinomial en MT. Por eso $\mathrm{P}$ es robusta.

---

## 6. Máquinas no deterministas y su simulación

### 6.1. Tiempo en una MT no determinista

En máquinas **deterministas**, la única ejecución debe terminar en a lo sumo $t(n)$ pasos.

En máquinas **no deterministas**, hay un **árbol** de cómputo: para cada entrada, todas las ramas deben terminar en a lo sumo $t(n)$ pasos. Esto es: el tiempo de una MT no determinista es la longitud de la **rama más larga** del árbol.

### 6.2. Simulación de una MT no determinista

**Teorema.** Cualquier MT no determinista que hace $O(t(n))$ pasos puede ser simulada por una MT determinista que hace $2^{O(t(n))}$ pasos.

**Idea de la prueba.**

- Como la MT no determinista termina, su árbol tiene a lo sumo $|b|^{t(n)}$ nodos (donde $b$ es el branching factor: cantidad máxima de transiciones por configuración).
- En el peor caso hay que recorrerlos todos (haciendo BFS por niveles para evitar perderse en una rama infinita).
- $|b|^{t(n)} \leq (2^c)^{t(n)} = 2^{c \cdot t(n)} \in 2^{O(t(n))}$.

> **Idea clave.** El no determinismo permite "adivinar" decisiones, pero simularlo deterministamente cuesta una **explosión exponencial**. La pregunta $\mathrm{P} \overset{?}{=} \mathrm{NP}$ es exactamente la pregunta: ¿es realmente necesaria esa explosión?

---

## 7. La clase P y ejemplos

### 7.1. PATH

$$\mathrm{Path} = \{ \langle G, v, w \rangle \mid G \text{ es un grafo con un camino de } v \text{ a } w\}.$$

**Algoritmo ineficiente.** Dado un grafo codificado con matriz de adyacencia: para $i = 1, 2, \dots, |V|$, generar todos los posibles caminos de longitud $i$ que empiezan en $v$ y terminan en $w$, y aceptar si alguno está en el grafo. Esto es $O(n!)$ (con $n = |V|$).

**Algoritmo eficiente (búsqueda en anchura).**

1. Marcar $v$.
2. Mientras haya nodos sin marcar:
   - Recorrer los arcos de $G$; para cada arco $(a, b)$ con $a$ marcado y $b$ no, marcar $b$.
   - Si se marca $w$, aceptar.
3. Si no se llegó, rechazar.

Tiempo: se recorren todos los nodos, y por cada uno a lo sumo todas las aristas. **Costo:** $O(|V| \cdot |E|)$ → **polinomial**.

### 7.2. Coprimos

$$\mathrm{Coprimos} = \{ \langle x, y \rangle \mid x \text{ y } y \text{ son coprimos} \}.$$

**Algoritmo ineficiente.** Para todo $z$ con $1 < z \leq \min(x, y)$, chequear si $z \mid x$ y $z \mid y$. Como los números vienen en **binario**, si tienen $n$ bits hay que hacer hasta $2^n$ pasos: **exponencial**.

**Algoritmo eficiente (Euclides).** Dados $x, y$ en binario:

- Repetir hasta que $y = 0$: $x \leftarrow x \bmod y$; intercambiar $x$ e $y$.
- Si $x = 1$, aceptar; sino rechazar.

**Análisis.** En cada paso $x$ se divide al menos por 2, así que con $n$ bits se hacen $n$ iteraciones. Cada división se computa en tiempo polinomial $p(n)$. **Total: $n \cdot p(n)$ → polinomial.**

> **Cuidado con la codificación.** El tamaño de la entrada para un número $x$ es $\log_2 x$. Un algoritmo que itera "hasta $x$" no es polinomial en el tamaño de la entrada.

### 7.3. Gramáticas Libres de Contexto

$$\mathrm{GLC} = \{ \langle G, w \rangle \mid w \text{ es generado por la gramática libre de contexto } G\}.$$

Usando **programación dinámica** y la **forma normal de Chomsky** (producciones $A \to BC$, $A \to a$, $A \to \varepsilon$), el algoritmo de **CYK** llena una matriz $M[i][j]$ con los no-terminales que generan $w_i \cdots w_j$:

```
D = "Sobre input w = w_1 ... w_n:
  1. Si w = ε, aceptar sii S → ε es una regla.
  2. Para i = 1 hasta n:                  [substrings de longitud 1]
  3.   Para cada variable A:
  4.     Si A → b es regla con b = w_i, poner A en table(i, i).
  5. Para l = 2 hasta n:                   [l = longitud del substring]
  6.   Para i = 1 hasta n - l + 1:
  7.     j = i + l - 1.
  8.     Para k = i hasta j - 1:           [k = posición de corte]
  9.       Para cada regla A → BC:
 10.         Si table(i, k) contiene B y table(k+1, j) contiene C, poner A en table(i, j).
 11. Si S está en table(1, n), aceptar; sino rechazar."
```

**Complejidad:** $O(|v| \cdot n^3)$ aproximadamente (donde $|v|$ es la cantidad de variables). Es polinomial → **GLC ∈ P**.

---

## 8. La clase NP

Al igual que con $\mathrm{P}$, usamos MT no deterministas para definir una nueva clase:

$$\mathrm{NTIME}(t(n)) = \{ L \mid L \text{ es un lenguaje decidido por una MT no determinista en } t(n) \text{ pasos}\}.$$

$$\boxed{\;\mathrm{NP} = \bigcup_{k > 0} \mathrm{NTIME}(n^k).\;}$$

Es decir, $\mathrm{NP}$ son los problemas resolubles por una MT **no determinista** en **tiempo polinomial**.

> **Intuición.** Una MT no determinista en tiempo polinomial es "mágica": en cada paso elige entre varias transiciones y acepta si **alguna** rama lleva a un estado de aceptación. Equivale a tener un oráculo que adivina la respuesta y luego solo hay que verificarla.

---

## 9. Verificadores y certificados

Para entender mejor $\mathrm{NP}$, conviene introducir un punto de vista alternativo: el de **verificadores**.

### 9.1. Caminos Hamiltonianos como ejemplo guía

**Definición.** Dado un grafo dirigido $G = (V, E)$, un **camino Hamiltoniano** es un camino que pasa exactamente una vez por cada nodo.

$$\mathrm{HAMPATH} = \{ \langle G, s, t \rangle \mid G \text{ tiene un camino Hamiltoniano de } s \text{ a } t\}.$$

### 9.2. Solución no determinista para HAMPATH

Dado un grafo $G = \langle V, E\rangle$ en la cinta de entrada:

1. **Adivinar.** Escribir, de forma no determinista, $|V|$ nodos.
2. **Verificar.** Comprobar que esos nodos están todos conectados consecutivamente, son todos distintos, empiezan en $s$ y terminan en $t$. Aceptar si es así, rechazar en caso contrario.

> **Idea clave.** El patrón general para problemas en $\mathrm{NP}$:
> - **Etapa 1 (adivinanza):** se adivina no deterministamente una posible solución (candidato).
> - **Etapa 2 (verificación):** se verifica deterministamente, en tiempo polinomial, si efectivamente resuelve el problema.

### 9.3. Verificabilidad Polinomial

Decimos que una cadena $c$ es un **certificado** (o testigo) de un problema si, junto con la entrada, permite verificar la solución.

El problema HAMPATH tiene dos características importantes:

1. **Certificados cortos:** un camino Hamiltoniano se puede describir en menos espacio que el grafo.
2. **Verificación rápida:** dado un camino, podemos verificar en tiempo lineal si es solución o no.

> Los problemas que están en $\mathrm{NP}$ son **exactamente** los que poseen certificados polinomiales que se pueden verificar polinomialmente.

### 9.4. Verificadores formalmente

**Definición.** Dado un lenguaje $A$, un **verificador** para $A$ es una MT $V$ tal que

$$A = \{ w \mid \exists\, c : V \text{ acepta } (w, c)\}.$$

Intuitivamente, $V$ verifica que $c$ certifica una solución al problema $w$.

**Definición (verificador polinomial).** Un verificador $V$ se dice **polinomial** si:

1. $V$ corre en tiempo $O(n^k)$ (con $n = |w|$).
2. Los certificados son polinomialmente acotados:

$$A = \{ w \mid \exists\, c : |c| \leq |w|^k \text{ y } V \text{ acepta } (w, c)\}.$$

### 9.5. Definición alternativa de NP

**Propiedad.** $L \in \mathrm{NP}$ si y solo si $L$ tiene un verificador polinomial.

**Idea de la prueba.**

- **Si $L$ tiene un verificador $V$:** se construye una MT no determinista $N$ que, sobre la entrada $w$, adivina no deterministamente un certificado $c$ con $|c| \leq |w|^k$ y simula $V(w, c)$.
- **Si $L$ es decidido por una MT no determinista $N$:** se construye un verificador $V$ que recibe $(w, c)$ donde $c$ codifica una rama de cómputo de $N$. $V$ usa $c$ para guiar la simulación y acepta si la rama acepta.

> **Idea clave.** Tenemos dos visiones equivalentes de $\mathrm{NP}$:
> - **Operacional:** problemas decidibles en tiempo polinomial por una MT **no determinista**.
> - **Declarativa:** problemas cuyas instancias positivas admiten una **prueba corta** verificable polinomialmente.
>
> La visión declarativa es la más útil en la práctica: probar que un problema está en $\mathrm{NP}$ significa exhibir un certificado natural.

---

## 10. Ejemplos de problemas en NP

### 10.1. HAMPATH

Ya analizado. Certificado: el propio camino Hamiltoniano. Verificación: recorrer aristas. **HAMPATH ∈ NP.**

### 10.2. COMP (números compuestos)

$$\mathrm{COMP} = \{ x \mid \exists\, p, q > 1 : x = p \cdot q\}.$$

**Certificado.** Un par $(p, q)$ con $p, q > 1$ y $p \cdot q = x$.
**Verificador.** Chequea $p, q > 1$ y computa $p \cdot q$ (multiplicación polinomial en cantidad de bits) comparando con $x$. Como $p, q$ tienen menos bits que $x$, el certificado es polinomial. **COMP ∈ NP.**

### 10.3. CLIQUE

**Definición.** Dado un grafo no dirigido $G$, un **clique** es un subgrafo en el cual cada par de nodos está conectado. Un **$k$-clique** es un clique con $k$ nodos.

$$\mathrm{CLIQUE} = \{ \langle G, k \rangle \mid G \text{ tiene un } k\text{-clique}\}.$$

**Certificado.** Un subconjunto $c \subseteq V$.
**Verificador.** Dado $\langle G, c \rangle$:
- Controlar que los nodos de $c$ estén en $G$.
- Controlar que todos los pares de nodos en $c$ estén conectados.
- Aceptar si ambas condiciones se cumplen.

Tamaño del certificado: $|c| \leq |V|$. Tiempo: polinomial. **CLIQUE ∈ NP.**

### 10.4. SUBSET-SUM

$$\mathrm{SUBSET\text{-}SUM} = \{ \langle S, t \rangle \mid \exists\, S' \subseteq S : \textstyle\sum S' = t\}.$$

**Ejemplo.** $\langle \{4, 11, 16, 21, 27\}, 25 \rangle \in \mathrm{SUBSET\text{-}SUM}$ porque $4 + 21 = 25$.

**Certificado.** El subconjunto $S' \subseteq S$.
**Verificador.** Sumar los elementos de $S'$ y comparar con $t$. **SUBSET-SUM ∈ NP.**

### 10.5. Problemas **afuera** de NP

No todo problema tiene un certificado obvio. Por ejemplo:

$$\overline{\mathrm{HAMPATH}} = \{ w \mid w \notin \mathrm{HAMPATH}\}, \qquad \overline{\mathrm{CLIQUE}} = \{ w \mid w \notin \mathrm{CLIQUE}\}.$$

Para mostrar que un grafo **tiene** un camino Hamiltoniano basta exhibir uno; pero para mostrar que **no** tiene ninguno, no se conoce un certificado polinomial natural. Análogamente para CLIQUE. Estos problemas son los típicos representantes de la clase $\mathrm{coNP}$, y no se sabe si $\mathrm{NP} = \mathrm{coNP}$.

---

## 11. P vs NP

Podemos resumir:

- $\mathrm{P}$: lenguajes que pueden ser **decididos** rápidamente.
- $\mathrm{NP}$: lenguajes cuya pertenencia puede ser **verificada** rápidamente.

**Proposición.** $\mathrm{P} \subseteq \mathrm{NP}$.

*Demostración.* Si $L \in \mathrm{P}$, hay una MT determinista $M$ que decide $L$ en tiempo polinomial. Definimos un verificador $V$ que ignora el certificado y simula $M(w)$. Es polinomial, así que $L \in \mathrm{NP}$.

> **La pregunta abierta $\mathrm{P} \overset{?}{=} \mathrm{NP}$.** ¿Es $\mathrm{P} = \mathrm{NP}$? Es decir, ¿todo problema cuya solución se puede **verificar** rápidamente se puede también **resolver** rápidamente? Es uno de los grandes problemas no resueltos de la computación. *A priori* la verificabilidad polinomial parece más potente que la decidibilidad polinomial, pero nadie ha logrado probarlo.

```
+----------------------+
|        NP            |
|   +-------+          |
|   |   P   |          |
|   +-------+          |
+----------------------+
```

---

## 12. Reducibilidad polinomial

Para comparar la dificultad relativa de dos problemas se introduce una noción de **reducción** análoga a las de computabilidad, pero con la exigencia de eficiencia.

**Definición (función polinomialmente computable).** Una función $f : \Sigma^* \to \Sigma^*$ es **polinomialmente computable** si existe una MT que la computa en tiempo polinomial.

**Definición (reducibilidad polinomial).** Un lenguaje $A$ es **polinomialmente reducible** a $B$, notado $A \leq_P B$, si existe una función polinomialmente computable $f : \Sigma^* \to \Sigma^*$ tal que

$$\forall\, w : \quad w \in A \iff f(w) \in B.$$

> **Intuición.** $A \leq_P B$ significa que "resolver $A$ no es sustancialmente más difícil que resolver $B$, módulo un trabajo polinomial". Si sabemos resolver $B$, podemos resolver $A$ traduciendo cada instancia de $A$ a una de $B$ y usando el algoritmo de $B$.

### 12.1. Propiedad fundamental

**Proposición.** Si $A \leq_P B$ y $B \in \mathrm{P}$, entonces $A \in \mathrm{P}$.

*Demostración.* Sea $M$ una MT que computa $f$ en tiempo $O(n^k)$ y $M_B$ una MT que decide $B$ en tiempo $O(n^{k'})$. Construyamos una MT $N$ que decide $A$:

1. Sobre entrada $w$, ejecutar $M(w)$ y obtener $f(w)$.
2. Ejecutar $M_B(f(w))$; aceptar si $M_B$ acepta, rechazar si rechaza.

Como $M$ corre en $O(|w|^k)$ pasos, $|f(w)| \leq |w|^k$. El paso 2 tarda $O((|w|^k)^{k'}) = O(|w|^{k \cdot k'})$. Total: $O(|w|^k) + O(|w|^{k \cdot k'})$, polinomial. $\blacksquare$

> Análogamente: si $A \leq_P B$ y $B \in \mathrm{NP}$, entonces $A \in \mathrm{NP}$.

### 12.2. Transitividad

**Proposición.** Si $A \leq_P B$ y $B \leq_P C$, entonces $A \leq_P C$.

(La composición de funciones polinomialmente computables es polinomialmente computable.)

---

## 13. NP-completitud

Dentro de $\mathrm{NP}$ hay problemas que son los **más difíciles**: si alguien encontrara un algoritmo polinomial para alguno de ellos, automáticamente tendría algoritmos polinomiales para todos los problemas de $\mathrm{NP}$.

**Definición (NP-completitud).** Un lenguaje $L$ es **NP-completo** si:

1. $L \in \mathrm{NP}$.
2. Para todo $A \in \mathrm{NP}$, se cumple $A \leq_P L$ (esto se llama ser **NP-difícil** o **NP-hard**).

### Consecuencia central

**Proposición.** Si algún problema NP-completo está en $\mathrm{P}$, entonces $\mathrm{P} = \mathrm{NP}$.

*Demostración.* Sea $L$ NP-completo con $L \in \mathrm{P}$. Para cualquier $A \in \mathrm{NP}$, $A \leq_P L$. Por la propiedad anterior, $A \in \mathrm{P}$. Por lo tanto $\mathrm{NP} \subseteq \mathrm{P}$, y como ya teníamos $\mathrm{P} \subseteq \mathrm{NP}$, concluimos $\mathrm{P} = \mathrm{NP}$. $\blacksquare$

> **Idea clave.** Los NP-completos son el "centro nervioso" de $\mathrm{NP}$. Probar $\mathrm{P} = \mathrm{NP}$ se reduce a encontrar **un** algoritmo polinomial para **cualquiera** de ellos. Recíprocamente, probar $\mathrm{P} \neq \mathrm{NP}$ se reduce a mostrar que **ninguno** de ellos admite uno.

```
+----------------------+
|        NP            |
|   +-------------+    |
|   | NP-Completo |    |
|   +-------------+    |
+----------------------+
```

---

## 14. SAT, 3-SAT y el Teorema de Cook–Levin

### 14.1. Fórmulas booleanas

Sea $X = \{x, y, z, \dots\}$ un conjunto numerable de variables. Las **fórmulas booleanas** se generan con la gramática

$$\phi, \psi \;::=\; X \mid \neg\phi \mid \phi \land \psi \mid \phi \lor \psi.$$

Su semántica viene dada por **asignaciones** $v : X \to \{0, 1\}$ (funciones a valores de verdad).

Una fórmula $\phi$ es **satisfacible** si existe una asignación $v$ que la hace verdadera (notado $v \models \phi$).

### 14.2. El lenguaje SAT

$$\mathrm{SAT} = \{ \langle \phi \rangle \mid \phi \text{ es una fórmula booleana satisfacible}\}.$$

### 14.3. CNF y 3-CNF

Una **cláusula** es una disyunción de literales:

$$(\ell_1 \lor \ell_2 \lor \dots \lor \ell_n).$$

Una fórmula está en **CNF** (Conjunctive Normal Form) si es una conjunción de cláusulas:

$$c_0 \land c_1 \land \dots \land c_m.$$

> **Observación.** Toda fórmula booleana se puede escribir en CNF.

Una fórmula está en **3-CNF** si está en CNF y cada cláusula tiene exactamente **3 literales**. Por ejemplo:

$$(x_0 \lor x_1 \lor x_3) \land (\neg x_0 \lor \neg x_1 \lor x_2).$$

El lenguaje **3-SAT** es el problema de satisfacibilidad restringido a fórmulas en 3-CNF.

### 14.4. Teorema de Cook–Levin

> **Teorema (Cook–Levin).** $\mathrm{SAT}$ es **NP-completo**.

Si algún problema NP-completo está en $\mathrm{P}$, entonces $\mathrm{NP} = \mathrm{P}$. SAT fue el **primer problema NP-completo** encontrado.

Para probar el teorema hay que ver:

1. $\mathrm{SAT} \in \mathrm{NP}$.
2. Para todo $A \in \mathrm{NP}$, $A \leq_P \mathrm{SAT}$.

**Parte 1: $\mathrm{SAT} \in \mathrm{NP}$.** El certificado es una asignación $v$ a las variables de $\phi$. El verificador evalúa $\phi$ bajo $v$ en tiempo polinomial.

**Parte 2: todo $A \in \mathrm{NP}$ se reduce a $\mathrm{SAT}$.** Esta es la parte más difícil. La idea: dado un lenguaje $A \in \mathrm{NP}$ decidido por una MT no determinista $N$ en tiempo $n^k$, hay que construir, **en tiempo polinomial**, una fórmula $\phi_w$ tal que

$$w \in A \iff \phi_w \text{ es satisfacible}.$$

### 14.5. Idea de la reducción: la tabla de cómputo

Consideramos una matriz de $n^k \times n^k$ celdas que representa una rama del cómputo de $N$:

- Cada **fila** representa una configuración (cinta + estado + cabezal) en un instante de tiempo.
- Cada celda contiene un símbolo de $C = \Gamma \cup \Sigma \cup Q \cup \{\#\}$ (alfabeto de cinta ∪ alfabeto de entrada ∪ estados ∪ delimitador).
- Se pasa de la fila $i$ a la fila $i+1$ si, del estado en la fila $i$, existe una ejecución que llega a la fila $i+1$.

### 14.6. Variables proposicionales

Para cada celda $(i, j)$ y cada símbolo $s \in C$, introducimos la variable

$$x_{i,j,s} \text{ que es verdadera} \iff cell[i][j] = s.$$

Cantidad de variables: $|C| \cdot n^{2k} = O(n^{2k})$, **polinomial**.

### 14.7. Estructura de la fórmula $\phi$

$$\phi \;=\; \phi_{\text{cell}} \;\land\; \phi_{\text{start}} \;\land\; \phi_{\text{move}} \;\land\; \phi_{\text{accept}}.$$

Cada componente describe un aspecto del cómputo:

**$\phi_{\text{cell}}$ — Cada celda contiene exactamente un símbolo.**

$$\phi_{\text{cell}} = \bigwedge_{1 \leq i, j \leq n^k} \left[ \Big(\bigvee_{s \in C} x_{i,j,s}\Big) \land \Big( \bigwedge_{\substack{s, t \in C \\ s \neq t}} (\neg x_{i,j,s} \lor \neg x_{i,j,t}) \Big) \right].$$

Primera parte: hay al menos un símbolo. Segunda parte: no hay dos símbolos a la vez. Tamaño: $O(n^{2k})$.

**$\phi_{\text{start}}$ — La primera fila es la configuración inicial.**

$$\phi_{\text{start}} = x_{1,1,\#} \land x_{1,2,q_0} \land x_{1,3,w_1} \land \dots \land x_{1,n+2,w_n} \land x_{1,n+3,\sqcup} \land \dots \land x_{1,n^k-1,\sqcup} \land x_{1,n^k,\#}.$$

Tamaño: $O(n^k)$.

**$\phi_{\text{accept}}$ — Alguna fila contiene el estado de aceptación.**

$$\phi_{\text{accept}} = \bigvee_{1 \leq i, j \leq n^k} x_{i, j, q_{\text{accept}}}.$$

Tamaño: $O(n^{2k})$.

**$\phi_{\text{move}}$ — Cada paso es una transición válida.**

$$\phi_{\text{move}} = \bigwedge_{0 < i, j < n^k} (\text{la ventana centrada en } (i, j) \text{ es legal}).$$

Cada **ventana de $2 \times 3$ celdas** captura el contexto local de una transición. Una ventana es **legal** si su contenido es compatible con alguna transición de $N$ (incluyendo el caso de celdas que no cambian porque están lejos del cabezal). Como son 6 celdas, cada cláusula tiene tamaño constante. Tamaño total: $O(n^{2k})$.

> **Teorema clave.** Si **todas** las ventanas $2 \times 3$ son legales, entonces la matriz describe una rama de cómputo válida de $N$.
>
> *Intuición.* Si un símbolo está en el centro de una ventana sin ser adyacente a un estado, debe mantenerse igual en la próxima fila. Para celdas con estado en el centro, la fila inferior queda restringida a las que corresponden a alguna transición $\delta(q, a)$.

**Ejemplo de ventanas legales.** Si $\delta(q_1, a) = \{(q_1, b, R)\}$ y $\delta(q_1, b) = \{(q_2, c, L), (q_2, a, R)\}$, las siguientes son ventanas legales:

```
| a   q1  b |   | a   q1  b |   | a   a   q1 |
| q2  a   c |   | a   a   q2|   | a   a   b  |
```

### 14.8. Tamaño total y correctitud

$$|\phi_{\text{cell}}| = O(n^{2k}), \;\; |\phi_{\text{start}}| = O(n^k), \;\; |\phi_{\text{accept}}| = O(n^{2k}), \;\; |\phi_{\text{move}}| = O(n^{2k}).$$

Total: $O(n^{2k})$, **polinomial**. La construcción es polinomialmente computable.

**Correctitud.**

- Si $N$ acepta $w$, existe una rama aceptante; la matriz correspondiente da una asignación que satisface $\phi$.
- Si $\phi$ es satisfacible, la asignación describe una matriz donde se cumple la configuración inicial, las transiciones son legales y se alcanza el estado de aceptación → $N$ acepta $w$.

> **Idea clave.** Una vez probado Cook–Levin, demostrar que un nuevo problema $L$ es NP-completo no requiere repetir el argumento. Basta:
> 1. Mostrar $L \in \mathrm{NP}$.
> 2. Reducir polinomialmente algún problema NP-completo conocido a $L$.
>
> La transitividad de la reducción cierra el círculo automáticamente.

### 14.9. 3-SAT es NP-completo

**Teorema.** $\mathrm{3\text{-}SAT}$ es NP-completo.

*Idea.*

1. $\mathrm{3\text{-}SAT} \in \mathrm{NP}$: idéntico al caso SAT (certificado = asignación).
2. $\mathrm{SAT} \leq_P \mathrm{3\text{-}SAT}$: dada una fórmula en CNF, reescribir cada cláusula como conjunción de cláusulas con exactamente 3 literales.

**Reducción SAT → 3-SAT.** Para una cláusula

$$(x_0 \lor x_1 \lor \dots \lor x_{n-1})$$

de tamaño $n$, introducimos $n - 2$ variables auxiliares $z_1, \dots, z_{n-2}$ y la reescribimos como:

$$(x_0 \lor x_1 \lor z_1) \land (\neg z_1 \lor x_2 \lor z_2) \land (\neg z_2 \lor x_3 \lor z_3) \land \dots \land (\neg z_{n-2} \lor x_{n-2} \lor x_{n-1}).$$

Esto da $n - 2$ cláusulas y $n - 2$ variables nuevas. La fórmula resultante es **equisatisfacible** con la original:

- Si la cláusula original es satisfecha por algún $x_i$ verdadero, podemos asignar adecuadamente los $z_j$.
- Recíprocamente, si las nuevas cláusulas se satisfacen, por inducción a lo largo de la cadena de $z$s, alguna de las $x_i$ debe ser verdadera.

**Tamaño y tiempo.** Si $\phi$ tiene tamaño $N$, $\phi'$ tiene tamaño $O(N)$ y se computa en tiempo polinomial. Por transitividad: como SAT es NP-completo y SAT $\leq_P$ 3-SAT con 3-SAT $\in \mathrm{NP}$, se concluye **3-SAT NP-completo**.

---

## 15. Reducciones clásicas: 3-SAT a Clique, Vertex-Cover, HAMPATH

### 15.1. 3-SAT $\leq_P$ CLIQUE

Dada una fórmula $\phi = (a_1 \lor b_1 \lor c_1) \land (a_2 \lor b_2 \lor c_2) \land \dots \land (a_k \lor b_k \lor c_k)$ en 3-CNF, construimos un grafo $G_\phi$ y elegimos el número $k$ (cantidad de cláusulas):

- Por cada cláusula generamos un **grupo de 3 nodos**, uno por literal.
- Conectamos cada par de nodos con un arco **excepto** si:
  - Pertenecen a la misma cláusula (mismo grupo), o
  - Son contradictorios (uno es $x$ y el otro $\neg x$).

**Teorema.** $\phi$ es satisfacible si y solo si $G_\phi$ tiene un $k$-clique.

*Idea de la prueba.*

- ($\Rightarrow$) Si hay una asignación satisfaciente, en cada cláusula hay al menos un literal verdadero; tomando uno por cláusula obtenemos $k$ nodos en grupos distintos sin literales contradictorios → forman un $k$-clique.
- ($\Leftarrow$) Si hay un $k$-clique, este debe tener uno por cada grupo (no pueden estar dos del mismo grupo) y ningún par contradictorio → asignando True a esos literales se satisface $\phi$.

**Construcción polinomial:** $G_\phi$ tiene $3k$ nodos y $O(k^2)$ aristas.

> **Conclusión.** Como CLIQUE ∈ NP y 3-SAT $\leq_P$ CLIQUE → **CLIQUE es NP-completo**.

### 15.2. 3-SAT $\leq_P$ VERTEX-COVER

**Definición.** Dado un grafo no dirigido $G = (V, E)$ y un entero $k \leq |V|$, un **cubrimiento de vértices** de tamaño $k$ es un $V' \subseteq V$ con $|V'| = k$ tal que **cada arco de $G$ tiene al menos un extremo en $V'$**.

$$\mathrm{VERTEX\text{-}COVER} = \{ \langle G, k \rangle \mid G \text{ tiene un cubrimiento de tamaño } k\}.$$

**Verificador.** El certificado es $V'$; verificar que $|V'| = k$ y que cada arista toca algún nodo de $V'$. Polinomial → **VC ∈ NP**.

**Reducción 3-SAT → VC.** Dada $\phi$ con $m$ variables y $\ell$ cláusulas, construimos $G_\phi$ con dos tipos de **gadgets**:

- **Gadget de variable.** Por cada variable $x$, dos nodos $x$ y $\overline{x}$ conectados por una arista.
- **Gadget de cláusula.** Por cada cláusula, un triángulo con 3 nodos (uno por literal).
- **Conexiones.** Cada nodo de un triángulo se conecta con el nodo de variable con el mismo label.

Buscamos un cubrimiento de tamaño $k = m + 2\ell$.

**Teorema.** $\phi$ es satisfacible $\iff$ $G_\phi$ tiene un cubrimiento de tamaño $m + 2\ell$.

*Idea.*

- ($\Rightarrow$) Dada una asignación satisfaciente, tomamos el nodo del literal verdadero en cada par de variable ($m$ nodos), y en cada triángulo tomamos los dos correspondientes a los literales falsos ($2\ell$ nodos).
- ($\Leftarrow$) Un cubrimiento de tamaño mínimo $m + 2\ell$ debe tener exactamente 1 por par y 2 por triángulo. Asignamos True a las variables del cubrimiento: cada cláusula queda satisfecha porque el literal "no cubierto" del triángulo se conecta con un literal verdadero en el cubrimiento de variable.

> **Conclusión.** Como VC ∈ NP y 3-SAT $\leq_P$ VC → **VERTEX-COVER es NP-completo**.

### 15.3. 3-SAT $\leq_P$ HAMPATH

Sabemos que HAMPATH ∈ NP. Para mostrar NP-completitud se reduce polinomialmente 3-SAT a HAMPATH: dada una fórmula $\phi$ en 3-CNF se construye un grafo $G_\phi$ con un camino Hamiltoniano de $s$ a $t$ si y solo si $\phi$ es satisfacible. La construcción usa gadgets de variable (que codifican la asignación) y gadgets de cláusula (que fuerzan al camino a satisfacer cada cláusula). El resultado: **HAMPATH es NP-completo**.

### 15.4. Otros NP-completos clásicos

- **LPATH:** $\{\langle G, a, b, k \rangle \mid G \text{ contiene un camino simple de longitud} \geq k \text{ de } a \text{ a } b\}$ — NP-completo.
- **3-COLOR:** $\{\langle G \rangle \mid G \text{ es coloreable con 3 colores}\}$ — NP-completo.
- **SUBSET-SUM:** NP-completo (se reduce 3-SAT).
- **ISO** (isomorfismo de grafos): está en NP. Su status de NP-completitud es un problema abierto (existen algoritmos cuasi-polinomiales pero no se sabe si es NP-completo ni si está en P).

---

## 16. Complejidad espacial

Cuando analizamos algoritmos hay **dos dimensiones** importantes:

- **Tiempo:** cantidad de instrucciones básicas que se realizan.
- **Espacio:** cantidad de memoria que necesita el algoritmo para resolver el problema.

Siempre trabajamos con MT. La memoria se mide como la **cantidad de celdas de cinta** que usa la MT.

### 16.1. Definición formal

Sea $M$ una MT que siempre termina. La **complejidad espacial** de $M$ es la función $f : \mathbb{N} \to \mathbb{N}$ donde

$$f(n) = \text{cantidad máxima de celdas que } M \text{ inspecciona para cualquier entrada de longitud } n.$$

Si $M$ es **no determinista**, $f(n)$ es la cantidad máxima de celdas inspeccionadas en **cualquier rama** del árbol de cómputo.

### 16.2. Clases de complejidad espacial

$$\mathrm{SPACE}(f(n)) = \{ L \mid L \text{ es decidido por una MT en espacio } O(f(n))\}.$$

$$\mathrm{NSPACE}(f(n)) = \{ L \mid L \text{ es decidido por una MT no determinista en espacio } O(f(n))\}.$$

Análogamente a $\mathrm{P}$, definimos las clases polinomiales:

$$\boxed{\;\mathrm{PSPACE} = \bigcup_{k \geq 1} \mathrm{SPACE}(O(n^k)) \qquad \mathrm{NPSPACE} = \bigcup_{k \geq 1} \mathrm{NSPACE}(O(n^k)).\;}$$

### 16.3. Ejemplo: SAT ∈ PSPACE

Veamos que SAT está en PSPACE. Sea $M$ la MT que, dado el input $\phi$:

1. Para cada asignación de valores de verdad de $\phi$:
2. Evaluar $\phi$ bajo la asignación.
   - Si se evalúa a True → **aceptar**.
   - Si no, limpiar la porción de memoria usada y continuar.
3. **Rechazar.**

> **Idea clave.** Los algoritmos pueden **reusar espacio** pero no pueden reusar tiempo. SAT solo necesita una cantidad **lineal de espacio** porque, aunque haya exponencialmente muchas asignaciones, las recorre una por una reusando la misma porción de memoria.

### 16.4. Ejemplo: $\overline{\mathrm{ALL}_{\mathrm{NFA}}} \in$ NPSPACE

NPSPACE es el análogo no determinista a PSPACE. Hagamos una MT no determinista que decida

$$\overline{\mathrm{ALL}_{\mathrm{NFA}}} = \{\langle A \rangle \mid A \text{ es un NFA y } L(A) \neq \Sigma^*\}.$$

$N$ sobre input $\langle M \rangle$ con $M$ un NFA:

1. Poner una marca en el estado inicial.
2. Repetir $2^Q$ veces ($Q$ = cantidad de estados):
   - No deterministamente elegir un símbolo, y cambiar las marcas para simular $M$.
3. Si no se marcaron estados de aceptación, **aceptar**; sino rechazar.

> **Justificación.** Si hay una cadena que $A$ no acepta, hay una cadena de longitud a lo sumo $2^Q$ no aceptada. Solo necesita una cantidad **lineal de espacio** (las marcas).

---

## 17. El Teorema de Savitch

> **Teorema (Savitch).** $\mathrm{NSPACE}(f(n)) \subseteq \mathrm{SPACE}(f(n)^2)$.

**Lectura.** Toda MT no determinista que usa $f(n)$ espacio puede simularse por una MT determinista que usa a lo sumo $f(n)^2$ espacio.

> **Por qué no se puede simular ingenuamente el árbol.** Cada rama del árbol de cómputo no determinista puede tener longitud exponencial ($f(n) \cdot 2^{O(f(n))}$ pasos), así que recorrer el árbol directamente requeriría espacio exponencial.

**Propiedad útil.** Una MT que usa $O(f(n))$ espacio puede realizar a lo sumo $f(n) \cdot 2^{O(f(n))}$ pasos antes de empezar a repetir configuraciones.

### 17.1. Idea de la prueba: el algoritmo `canyield`

La prueba consiste en definir un programa recursivo:

```
canyield(c1, c2, t)
```

que dice: **¿se puede ir de la configuración `c1` a la configuración `c2` en a lo sumo `t` pasos, usando poco espacio?**

**Algoritmo.**

```
canyield(c1, c2, t):
  1. Si t = 1, verificar si c1 = c2 o si en un paso se llega de c1 a c2.
     Aceptar o rechazar de acuerdo a esto.
  2. Si t > 1, para cada configuración cm:
       3. Ejecutar canyield(c1, cm, t/2)
       4. Ejecutar canyield(cm, c2, t/2)
       5. Si los pasos 3 y 4 aceptan, aceptar.
  6. Si no se aceptó para ninguna, rechazar.
```

### 17.2. Análisis del algoritmo

Corremos `canyield(c_0, accept, 2^{d \cdot f(n)})` para alguna constante $d$.

- La MT original puede realizar a lo sumo $2^{O(f(n))}$ pasos, por lo cual si acepta el algoritmo aceptará.
- La pila de recursión solo puede tener tamaño **logarítmico** (porque $t$ se divide por 2 en cada llamada recursiva): $\log 2^{d \cdot f(n)} = d \cdot f(n) \in O(f(n))$.
- En cada llamada utilizamos $O(f(n))$ celdas para la configuración.
- Espacio total: configuraciones $\times$ pila de recursión = $O(f(n)) \times O(f(n)) = O(f(n)^2)$.

### 17.3. Consecuencia inmediata

**Corolario.** $\mathrm{NPSPACE} = \mathrm{PSPACE}$.

*Demostración.* Si $L \in \mathrm{NPSPACE}$, entonces $L \in \mathrm{NSPACE}(O(n^k))$ para algún $k$. Por Savitch, $L \in \mathrm{SPACE}(O(n^{2k})) \subseteq \mathrm{PSPACE}$. Y obviamente $\mathrm{PSPACE} \subseteq \mathrm{NPSPACE}$. $\blacksquare$

> **Idea clave.** Para el **espacio** polinomial, el no determinismo no ayuda. Esto contrasta con el caso del **tiempo**, donde no se sabe si $\mathrm{P} = \mathrm{NP}$.

---

## 18. Jerarquía P ⊆ NP ⊆ PSPACE ⊆ EXPTIME y PSPACE-Completitud

### 18.1. La cadena de inclusiones

A partir de los resultados vistos:

$$\boxed{\;\mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{PSPACE} = \mathrm{NPSPACE} \subseteq \mathrm{EXPTIME}.\;}$$

- $\mathrm{P} \subseteq \mathrm{NP}$: ya visto.
- $\mathrm{NP} \subseteq \mathrm{PSPACE}$: una MT no determinista en tiempo polinomial usa solo espacio polinomial; pero también podemos simular cada certificado posible reusando espacio (ejemplo SAT).
- $\mathrm{PSPACE} = \mathrm{NPSPACE}$: Teorema de Savitch.
- $\mathrm{NPSPACE} \subseteq \mathrm{EXPTIME}$: una MT que usa $O(f(n))$ espacio realiza a lo sumo $f(n) \cdot 2^{O(f(n))}$ pasos antes de repetir configuración. Si $f$ es polinomial, esto da tiempo exponencial.

No se sabe cuáles de las inclusiones son estrictas; en particular el famoso $\mathrm{P} \overset{?}{=} \mathrm{NP}$ y también $\mathrm{NP} \overset{?}{=} \mathrm{PSPACE}$ son problemas abiertos.

### 18.2. PSPACE-Completitud

Al igual que en NP-completitud, podemos definir problemas PSPACE-completos:

**Definición.** Un problema $B$ se dice **PSPACE-completo** si:

1. $B \in \mathrm{PSPACE}$.
2. Para todo $A \in \mathrm{PSPACE}$, $A \leq_P B$.

> **Observación.** También usamos **reducibilidad polinomial** (no espacial) aquí, porque si tenemos un procedimiento polinomial en tiempo, también corre en espacio polinomial. Así, las reducciones polinomiales son lo suficientemente finas para distinguir dentro de PSPACE.

---

## 19. Ideas clave para repasar

1. **Big-Oh y compañía.** $O$, $o$, $\Omega$, $\Theta$ son herramientas para hablar de crecimiento asintótico módulo constantes. $o$ es estricto, $\Theta$ es ajustada. Útiles para clasificar tiempo y espacio.

2. **Análisis comparativo de algoritmos.** El mismo problema ($0^k 1^k$) admite algoritmos de tiempo muy distinto: $O(n^2)$, $O(n \log n)$, $O(n)$ con dos cintas. La elección del modelo y del algoritmo importa.

3. **La clase $\mathrm{P}$.** $\mathrm{P} = \bigcup_k \mathrm{TIME}(O(n^k))$. Es robusta: el modelo determinista razonable no cambia $\mathrm{P}$ (Tesis de Church–Turing Extendida). Los problemas en $\mathrm{P}$ se consideran **tratables**.

4. **MT multicinta vs MT de una cinta.** Cualquier MT multicinta que hace $O(t(n))$ pasos se simula con una MT de una cinta en $O(t(n)^2)$ → polinomial preservado.

5. **No determinismo: tiempo de la rama más larga.** Una MT no determinista acepta si **alguna** rama lleva a un estado de aceptación. Simularla deterministamente cuesta $2^{O(t(n))}$.

6. **Patrón "adivinar + verificar".** Para mostrar $L \in \mathrm{NP}$ basta exhibir un certificado polinomial y un algoritmo de verificación polinomial. Esta es la **definición declarativa** de NP y es la más útil en la práctica.

7. **NP por verificadores ≡ NP por MT no determinista.** Ambas definiciones son equivalentes; la equivalencia se construye explícitamente.

8. **$\mathrm{P} \subseteq \mathrm{NP}$.** Trivial (verificador que ignora el certificado). La pregunta $\mathrm{P} \overset{?}{=} \mathrm{NP}$ está abierta.

9. **Reducibilidad polinomial $\leq_P$.** Es **transitiva**. Si $A \leq_P B$ y $B \in \mathrm{P}$ (resp. $\mathrm{NP}$), entonces $A \in \mathrm{P}$ (resp. $\mathrm{NP}$).

10. **NP-Completitud.** $L$ es NP-completo si $L \in \mathrm{NP}$ y todo $A \in \mathrm{NP}$ se reduce a $L$. Si **un** NP-completo está en $\mathrm{P}$, entonces $\mathrm{P} = \mathrm{NP}$.

11. **Cook–Levin.** SAT es el primer problema NP-completo. La prueba codifica la ejecución de una MT no determinista en una fórmula booleana usando variables $x_{i,j,s}$ y una tabla de cómputo de $n^k \times n^k$. La fórmula tiene tamaño $O(n^{2k})$ y consta de:
    - $\phi_{\text{cell}}$ (cada celda tiene un único símbolo),
    - $\phi_{\text{start}}$ (configuración inicial),
    - $\phi_{\text{move}}$ (transiciones legales vía ventanas $2 \times 3$),
    - $\phi_{\text{accept}}$ (alguna fila tiene estado de aceptación).

12. **Cadena de reducciones.** $\mathrm{SAT} \leq_P \mathrm{3\text{-}SAT} \leq_P \mathrm{CLIQUE}, \mathrm{VERTEX\text{-}COVER}, \mathrm{HAMPATH}, \dots$ Cada nueva reducción agrega un NP-completo al catálogo.

13. **Método estándar para NP-completitud.** Para probar que $L$ es NP-completo:
    1. Mostrar $L \in \mathrm{NP}$ (verificador).
    2. Reducir polinomialmente algún NP-completo conocido a $L$.

14. **Complejidad espacial.** Cuenta celdas (no pasos). El espacio puede **reusarse**, el tiempo no. SAT ∈ PSPACE aunque sea exponencial en tiempo (en el peor caso conocido).

15. **Teorema de Savitch.** $\mathrm{NSPACE}(f(n)) \subseteq \mathrm{SPACE}(f(n)^2)$. En particular $\mathrm{NPSPACE} = \mathrm{PSPACE}$. Prueba vía algoritmo recursivo `canyield(c1, c2, t)` con pila logarítmica.

16. **La jerarquía:** $\mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{PSPACE} = \mathrm{NPSPACE} \subseteq \mathrm{EXPTIME}$. Ninguna inclusión se sabe estricta.

---

## 20. Preguntas típicas de examen

### Q1. Decir cuáles son verdaderas y cuáles falsas.

| | Afirmación | Resp. | Justificación breve |
|---|---|---|---|
| a | $2n \in O(n)$ | **V** | Con $c = 2$, $n_0 = 1$. |
| b | $n^2 \in O(n)$ | **F** | $n^2 / n = n \to \infty$. |
| c | $n^2 \in O(n \log^2 n)$ | **F** | $n^2 / (n \log^2 n) = n / \log^2 n \to \infty$. |
| d | $3^n \in 2^{O(n)}$ | **V** | $3^n = 2^{n \log_2 3} = 2^{O(n)}$. |
| e | $2^n \in o(3^n)$ | **V** | $2^n / 3^n = (2/3)^n \to 0$. |
| f | $1 \in o(1/n)$ | **F** | $1 / (1/n) = n \to \infty$, no $\to 0$. |

### Q2. ¿Por qué el algoritmo ingenuo para Coprimos no es polinomial?

Porque los números vienen en binario: el tamaño de la entrada es $\log_2 x$ (la cantidad de bits). Recorrer hasta $\min(x, y)$ son $2^n$ pasos si $n$ es el tamaño en bits → **exponencial**. El algoritmo eficiente (Euclides) divide por 2 en cada paso, dando $O(n \cdot p(n))$ con $p$ polinomio para la división.

### Q3. ¿Es $\mathrm{P}$ cerrada bajo unión, intersección, concatenación y complemento?

**Sí.**
- **Unión:** $L_1 \cup L_2$ se decide ejecutando los dos algoritmos polinomiales y aceptando si alguno acepta.
- **Intersección:** ídem, aceptando si ambos aceptan.
- **Concatenación:** dada $w$, probar las $|w|+1$ formas de partir $w$ en $w = uv$ y verificar $u \in L_1$ y $v \in L_2$. Polinomial.
- **Complemento:** simular el algoritmo y aceptar cuando rechaza (y viceversa). Polinomial.

### Q4. Mostrar que NP es cerrada bajo unión y concatenación.

- **Unión:** verificador para $L_1 \cup L_2$ es la disyunción de los verificadores. Certificado polinomial.
- **Concatenación:** verificador adivina el punto de corte y los dos certificados; verifica que las dos mitades pertenezcan a $L_1$ y $L_2$. Polinomial.

> Si NP es cerrada bajo **complemento** es una pregunta abierta: equivale a si $\mathrm{NP} = \mathrm{coNP}$.

### Q5. ¿Por qué $\mathrm{P} \subseteq \mathrm{NP}$?

Si $L \in \mathrm{P}$, hay una MT determinista polinomial $M$ que decide $L$. Definimos un verificador $V$ que ignora el certificado y simula $M(w)$. Es polinomial → $L \in \mathrm{NP}$.

### Q6. ¿Por qué CLIQUE está en NP?

Certificado: un subconjunto $c$ de nodos. Verificador: chequear $|c| = k$, $c \subseteq V$, y que cada par de nodos en $c$ esté conectado. Todo polinomial.

### Q7. Si un problema NP-completo está en P, ¿qué se concluye?

Que $\mathrm{P} = \mathrm{NP}$. Porque si $L$ es NP-completo y $L \in \mathrm{P}$, para todo $A \in \mathrm{NP}$ se tiene $A \leq_P L$, y por la propiedad de reducción, $A \in \mathrm{P}$ → $\mathrm{NP} \subseteq \mathrm{P}$.

### Q8. Idea de la reducción $\mathrm{SAT} \leq_P \mathrm{3\text{-}SAT}$.

Cada cláusula de tamaño $n$ se reescribe usando $n-2$ variables nuevas $z_1, \dots, z_{n-2}$:

$$(x_0 \lor x_1 \lor z_1) \land (\neg z_1 \lor x_2 \lor z_2) \land \dots \land (\neg z_{n-2} \lor x_{n-2} \lor x_{n-1}).$$

Las fórmulas son equisatisfacibles y la construcción es polinomial.

### Q9. ¿Qué es una "ventana legal" en la prueba de Cook–Levin?

Una ventana de $2 \times 3$ celdas (3 celdas en la fila $i$ y 3 en la fila $i+1$) es **legal** si su contenido es consistente con alguna transición posible de la MT no determinista $N$. Si todas las ventanas son legales, la tabla describe una rama válida de $N$.

### Q10. Enunciar el Teorema de Savitch y su consecuencia.

**Teorema.** $\mathrm{NSPACE}(f(n)) \subseteq \mathrm{SPACE}(f(n)^2)$.

**Consecuencia.** $\mathrm{PSPACE} = \mathrm{NPSPACE}$.

**Prueba (idea).** Algoritmo recursivo `canyield(c1, c2, t)` que parte $t$ a la mitad probando configuraciones intermedias; la pila de recursión es logarítmica en $t = 2^{d \cdot f(n)}$, por ende $O(f(n))$. Cada configuración ocupa $O(f(n))$. Total: $O(f(n)^2)$.

### Q11. ¿Por qué SAT está en PSPACE?

Porque podemos recorrer todas las asignaciones una por una, **reusando** el mismo bloque de memoria cada vez. Solo se necesita espacio lineal para representar una asignación.

### Q12. ¿Qué dice la Tesis de Church–Turing Extendida?

Que cualquier modelo razonable de cómputo determinista que decida un problema en $O(t(n))$ pasos es simulable en $O(t(n)^k)$ pasos por cualquier otro modelo razonable determinista. Justifica usar MT como modelo de referencia para complejidad.

---

## 21. Resumen ultra breve

> **Tres páginas resumidas en seis líneas.**

- **Complejidad** estudia la cantidad de **tiempo** y **espacio** que requieren los algoritmos. Notaciones: $O, o, \Omega, \Theta$ describen crecimiento asintótico módulo constantes.

- **Clase P:** problemas decidibles en tiempo polinomial por una MT determinista. Considerada la clase de los problemas **tratables**. Es invariante respecto a modelos deterministas razonables (Tesis Church–Turing Extendida).

- **Clase NP:** problemas decidibles en tiempo polinomial por una MT **no determinista** $\equiv$ problemas con un **verificador polinomial** (certificado corto, verificación rápida). Patrón "adivinar + verificar". Ejemplos: HAMPATH, CLIQUE, SUBSET-SUM, COMP.

- **Reducibilidad polinomial $A \leq_P B$:** existe $f$ polinomial con $w \in A \iff f(w) \in B$. Transitiva. Preserva $\mathrm{P}$ y $\mathrm{NP}$.

- **NP-completos:** los problemas más difíciles dentro de NP. **Cook–Levin:** $\mathrm{SAT}$ es NP-completo. Reducciones clásicas: $\mathrm{SAT} \leq_P \mathrm{3\text{-}SAT} \leq_P \mathrm{CLIQUE}, \mathrm{VERTEX\text{-}COVER}, \mathrm{HAMPATH}$.

- **Espacio:** se puede **reusar**, el tiempo no. $\mathrm{PSPACE}$ = decidibles en espacio polinomial. **Savitch:** $\mathrm{NSPACE}(f) \subseteq \mathrm{SPACE}(f^2)$, por lo cual $\mathrm{PSPACE} = \mathrm{NPSPACE}$.

- **Jerarquía:** $\mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{PSPACE} = \mathrm{NPSPACE} \subseteq \mathrm{EXPTIME}$. Las inclusiones intermedias **se conjeturan estrictas** (en particular $\mathrm{P} \neq \mathrm{NP}$), pero ninguna se ha demostrado.
