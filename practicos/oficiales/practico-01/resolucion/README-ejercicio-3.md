# Ejercicio 3

## Enunciado

Dar definiciones de maquinas de Turing para decidir los siguientes lenguajes:

(a) \(L_1 = \{w\in\{0,1\}^* \mid \#_0(w)=\#_1(w)\}\)

(b) \(L_2 = \{w\in\{0,1\}^* \mid \#_0(w) = 2\cdot \#_1(w)\}\)

donde \(\#_a(w)\) denota la cantidad de apariciones del simbolo \(a\) en \(w\).

## Convenciones

Usamos el alfabeto de cinta \(\Gamma=\{0,1,x,y,\sqcup\}\), donde:

- \(\sqcup\) es el blanco;
- \(x\) marca un \(0\) "ya emparejado";
- \(y\) marca un \(1\) "ya emparejado".

La estrategia general es la de los Ejemplos 3.9 (\(M_1\), lenguaje \(\{w\#w\}\)) y 3.11 (\(M_3\), lenguaje \(\{a^ib^jc^k:i\cdot j=k\}\)) del libro: "marcar y emparejar". En cada iteracion se elige un simbolo no marcado y se busca su contraparte para marcarlos en bloque; al agotar la cadena, si todos quedaron marcados consistentemente, se acepta.

---

## (a) MT que decide \(L_1\)

### Descripcion a nivel implementacion (estilo Sipser)

\(M_{eq} =\) "Con entrada \(w\):

1. Volver al inicio de la cinta.
2. Recorrer la cinta hacia la derecha hasta encontrar el primer simbolo no marcado (\(0\) o \(1\)).
3. Si no hay ninguno (solo \(x\), \(y\) y blancos), aceptar.
4. Si el simbolo es \(0\), marcarlo como \(x\) y buscar a su derecha el primer \(1\) no marcado. Si lo encuentra, marcarlo como \(y\) y volver a (2). Si llega a un blanco sin encontrar \(1\), rechazar.
5. Si el simbolo es \(1\), marcarlo como \(y\) y buscar a su derecha el primer \(0\) no marcado. Si lo encuentra, marcarlo como \(x\) y volver a (2). Si llega a un blanco sin encontrar \(0\), rechazar.
"

### Descripcion formal (7-tupla)

\[
  M_{eq} = (Q, \Sigma, \Gamma, \delta, q_{\text{seek}}, q_{\text{accept}}, q_{\text{reject}}),
\]

con \(\Sigma=\{0,1\}\), \(\Gamma=\{0,1,x,y,\sqcup\}\) y

\[
  Q = \{q_{\text{seek}}, q_{\text{find1}}, q_{\text{find0}}, q_{\text{back}}, q_{\text{accept}}, q_{\text{reject}}\}.
\]

#### Funcion de transicion

**1) Busqueda inicial** (\(q_{\text{seek}}\)):
\[
\begin{aligned}
\delta(q_{\text{seek}},x) &= (q_{\text{seek}},x,R), &
\delta(q_{\text{seek}},y) &= (q_{\text{seek}},y,R),\\
\delta(q_{\text{seek}},0) &= (q_{\text{find1}},x,R), &
\delta(q_{\text{seek}},1) &= (q_{\text{find0}},y,R),\\
\delta(q_{\text{seek}},\sqcup) &= (q_{\text{accept}},\sqcup,R). & &
\end{aligned}
\]

**2) Buscar un \(1\) que empareje al \(0\) recien marcado** (\(q_{\text{find1}}\)):
\[
\begin{aligned}
\delta(q_{\text{find1}},0) &= (q_{\text{find1}},0,R),\\
\delta(q_{\text{find1}},x) &= (q_{\text{find1}},x,R),\\
\delta(q_{\text{find1}},y) &= (q_{\text{find1}},y,R),\\
\delta(q_{\text{find1}},1) &= (q_{\text{back}},y,L),\\
\delta(q_{\text{find1}},\sqcup) &= (q_{\text{reject}},\sqcup,R).
\end{aligned}
\]

**3) Buscar un \(0\) que empareje al \(1\) recien marcado** (\(q_{\text{find0}}\)):
\[
\begin{aligned}
\delta(q_{\text{find0}},1) &= (q_{\text{find0}},1,R),\\
\delta(q_{\text{find0}},x) &= (q_{\text{find0}},x,R),\\
\delta(q_{\text{find0}},y) &= (q_{\text{find0}},y,R),\\
\delta(q_{\text{find0}},0) &= (q_{\text{back}},x,L),\\
\delta(q_{\text{find0}},\sqcup) &= (q_{\text{reject}},\sqcup,R).
\end{aligned}
\]

**4) Volver al extremo izquierdo** (\(q_{\text{back}}\)):
\[
\begin{aligned}
\delta(q_{\text{back}},a) &= (q_{\text{back}},a,L) \quad\text{para } a\in\{0,1,x,y\},\\
\delta(q_{\text{back}},\sqcup) &= (q_{\text{seek}},\sqcup,R).
\end{aligned}
\]

### Correctitud

**Si \(M_{eq}\) acepta:** En cada iteracion completa se marcaron exactamente un \(0\) (como \(x\)) y un \(1\) (como \(y\)). La maquina acepta cuando \(q_{\text{seek}}\) lee un blanco, lo que significa que ya no quedan \(0\)s ni \(1\)s sin marcar. Como en cada iteracion se marcan en pareja, \(\#_0(w)=\#_1(w)\).

**Si \(\#_0(w)=\#_1(w)\):** En cada iteracion al elegir un simbolo no marcado, por igualdad de cantidades siempre existe la contraparte para emparejarlo. Asi \(M_{eq}\) nunca cae en \(q_{\text{reject}}\) y termina aceptando al consumir todos los simbolos.

### Terminacion

Cada iteracion completa marca al menos dos simbolos nuevos. Como \(|w|<\infty\), tras \(\lfloor|w|/2\rfloor\) iteraciones la maquina ya no encuentra simbolos sin marcar y se detiene. \(M_{eq}\) **decide** \(L_1\).

---

## (b) MT que decide \(L_2\)

La idea es analoga, pero ahora cada iteracion debe emparejar **un \(1\) con dos \(0\)s**.

### Descripcion a nivel implementacion

\(M_{2{:}1} =\) "Con entrada \(w\):

1. Volver al inicio de la cinta.
2. Buscar de izquierda a derecha el primer \(1\) no marcado.
3. Si no hay \(1\) sin marcar, pasar a la fase de verificacion final:
   - recorrer la cinta y comprobar que tampoco quede ningun \(0\) sin marcar;
   - si no queda ninguno, aceptar; si queda alguno, rechazar.
4. Si se encontro un \(1\), marcarlo como \(y\).
5. Volver al inicio y buscar el primer \(0\) sin marcar; si no existe, rechazar; en caso contrario, marcarlo como \(x\).
6. Continuar a la derecha y buscar un segundo \(0\) sin marcar; si no existe, rechazar; en caso contrario, marcarlo como \(x\).
7. Volver al inicio y volver a (2).
"

### Descripcion formal (7-tupla)

\[
  M_{2{:}1} = (Q, \Sigma, \Gamma, \delta, q_{\text{scan1}}, q_{\text{accept}}, q_{\text{reject}}),
\]

con \(\Sigma=\{0,1\}\), \(\Gamma=\{0,1,x,y,\sqcup\}\) y

\[
  Q = \{q_{\text{scan1}}, q_{\text{back1}}, q_{\text{find0a}}, q_{\text{find0b}}, q_{\text{back}}, q_{\text{backf}}, q_{\text{check0}}, q_{\text{accept}}, q_{\text{reject}}\}.
\]

Intuicion de cada estado:

- \(q_{\text{scan1}}\): busca un \(1\) no marcado.
- \(q_{\text{back1}}\): retrocede al inicio luego de marcar un \(1\).
- \(q_{\text{find0a}}\), \(q_{\text{find0b}}\): buscan el primer y el segundo \(0\) no marcados respectivamente.
- \(q_{\text{back}}\): retrocede para reiniciar el ciclo.
- \(q_{\text{backf}}\), \(q_{\text{check0}}\): fase final de verificacion (ya no quedan \(1\)).

#### Funcion de transicion

**1) Buscar un \(1\) sin marcar** (\(q_{\text{scan1}}\)):
\[
\begin{aligned}
\delta(q_{\text{scan1}},0) &= (q_{\text{scan1}},0,R),\\
\delta(q_{\text{scan1}},x) &= (q_{\text{scan1}},x,R),\\
\delta(q_{\text{scan1}},y) &= (q_{\text{scan1}},y,R),\\
\delta(q_{\text{scan1}},1) &= (q_{\text{back1}},y,L),\\
\delta(q_{\text{scan1}},\sqcup) &= (q_{\text{backf}},\sqcup,L).
\end{aligned}
\]

**2) Volver al inicio luego de marcar un \(1\)** (\(q_{\text{back1}}\)):
\[
\delta(q_{\text{back1}},a) = (q_{\text{back1}},a,L)\ \text{para } a\in\{0,1,x,y\},\quad
\delta(q_{\text{back1}},\sqcup) = (q_{\text{find0a}},\sqcup,R).
\]

**3) Primer \(0\) sin marcar** (\(q_{\text{find0a}}\)):
\[
\begin{aligned}
\delta(q_{\text{find0a}},1) &= (q_{\text{find0a}},1,R),\\
\delta(q_{\text{find0a}},x) &= (q_{\text{find0a}},x,R),\\
\delta(q_{\text{find0a}},y) &= (q_{\text{find0a}},y,R),\\
\delta(q_{\text{find0a}},0) &= (q_{\text{find0b}},x,R),\\
\delta(q_{\text{find0a}},\sqcup) &= (q_{\text{reject}},\sqcup,R).
\end{aligned}
\]

**4) Segundo \(0\) sin marcar** (\(q_{\text{find0b}}\)):
\[
\begin{aligned}
\delta(q_{\text{find0b}},1) &= (q_{\text{find0b}},1,R),\\
\delta(q_{\text{find0b}},x) &= (q_{\text{find0b}},x,R),\\
\delta(q_{\text{find0b}},y) &= (q_{\text{find0b}},y,R),\\
\delta(q_{\text{find0b}},0) &= (q_{\text{back}},x,L),\\
\delta(q_{\text{find0b}},\sqcup) &= (q_{\text{reject}},\sqcup,R).
\end{aligned}
\]

**5) Volver al inicio para reiniciar ciclo** (\(q_{\text{back}}\)):
\[
\delta(q_{\text{back}},a) = (q_{\text{back}},a,L)\ \text{para } a\in\{0,1,x,y\},\quad
\delta(q_{\text{back}},\sqcup) = (q_{\text{scan1}},\sqcup,R).
\]

**6) Fase final** (\(q_{\text{backf}},q_{\text{check0}}\)):
\[
\begin{aligned}
\delta(q_{\text{backf}},a) &= (q_{\text{backf}},a,L)\ \text{para } a\in\{0,1,x,y\},\\
\delta(q_{\text{backf}},\sqcup) &= (q_{\text{check0}},\sqcup,R),\\
\delta(q_{\text{check0}},x) &= (q_{\text{check0}},x,R),\\
\delta(q_{\text{check0}},y) &= (q_{\text{check0}},y,R),\\
\delta(q_{\text{check0}},0) &= (q_{\text{reject}},0,R),\\
\delta(q_{\text{check0}},1) &= (q_{\text{reject}},1,R),\\
\delta(q_{\text{check0}},\sqcup) &= (q_{\text{accept}},\sqcup,R).
\end{aligned}
\]

### Correctitud

**Si \(M_{2{:}1}\) acepta:** En cada ciclo se marco exactamente un \(1\) y dos \(0\)s. Al llegar a la fase final, no queda ningun \(1\) y la verificacion confirma que tampoco queda ningun \(0\). Por lo tanto, llamando \(k\) al numero de ciclos completados, \(\#_1(w)=k\) y \(\#_0(w)=2k\), de donde \(\#_0(w)=2\,\#_1(w)\).

**Si \(\#_0(w)=2\,\#_1(w)\):** En cada ciclo, al marcar un \(1\) restan \(2\,(\#_1(w)-i)\) ceros sin marcar (donde \(i\) es el numero de ciclos previos). Como \(\#_1(w)-i\ge 1\), siempre existen al menos dos \(0\)s sin marcar para emparejar al \(1\). Despues de \(\#_1(w)\) ciclos no quedan \(1\)s ni \(0\)s sin marcar, y la fase final acepta.

### Terminacion

Cada ciclo marca **un \(1\)** y **dos \(0\)s**, o bien rechaza. Como \(|w|<\infty\), tras \(\#_1(w)\) ciclos (o antes, si se rechaza) la maquina llega a la fase final. \(M_{2{:}1}\) **decide** \(L_2\).

---

## Conclusion

Hemos exhibido deciders explicitos:

- \(M_{eq}\) decide \(L_1\).
- \(M_{2{:}1}\) decide \(L_2\).

Por lo tanto, ambos lenguajes son **decidibles**.

## Observacion sobre la implementacion

La parte de programacion del practico (`ejercicio4_mt_teorico.py`) implementa estas dos maquinas y verifica su comportamiento sobre baterias de pruebas, contrastando el resultado con el predicado matematico correspondiente. La equivalencia entre la descripcion formal de \(\delta\) y el codigo es directa: cada celda de la tabla de transicion se traduce en una entrada del diccionario de Python.
