# Ejercicio 10

## Enunciado

Usar el Teorema de Rice para demostrar la indecibilidad del siguiente lenguaje:

\[
All=\{\langle M\rangle \mid L(M)=\Sigma^*\}.
\]

(El enunciado original tiene una pequeña errata, escribiendo \(\mathcal M=\Sigma^*\) en lugar de \(\mathcal L(M)=\Sigma^*\). Se trabaja con la lectura corregida.)

## Recordatorio: Teorema de Rice

**Teorema de Rice** (Problema 5.28 de Sipser; ver tambien las laminas en `Reducibilidad.pdf`).

Sea \(P\subseteq\{\langle M\rangle \mid M \text{ es una MT}\}\) un conjunto de descripciones de MT que cumple las dos siguientes propiedades:

1. **Es una propiedad de lenguajes (semantica):** si \(L(M_1)=L(M_2)\), entonces \(\langle M_1\rangle\in P \iff \langle M_2\rangle\in P\). En palabras: \(P\) depende solo del lenguaje reconocido por \(M\), no de la sintaxis o estructura interna de \(M\).
2. **Es no trivial:**
   - \(P\neq\emptyset\), es decir, existe alguna MT \(M_1\) con \(\langle M_1\rangle\in P\).
   - \(P\neq\{\langle M\rangle\mid M \text{ es MT}\}\), es decir, existe alguna MT \(M_2\) con \(\langle M_2\rangle\notin P\).

Entonces \(P\) es **indecidible**.

La idea de la prueba (registrada en la teoria) es construir, dado un decisor hipotetico \(M_P\) para \(P\), un decisor para \(A_{TM}\), llegando a una contradiccion. Esto se logra disenando una MT \(M_w\) (a partir de \(\langle M,w\rangle\)) cuyo lenguaje sea \(L(T)\) si \(M\) acepta \(w\), y \(\emptyset\) en caso contrario, donde \(T\) es un testigo apropiado.

## Aplicacion del Teorema de Rice a \(All\)

Definimos la propiedad asociada a \(All\):

\[
P(L) \iff L=\Sigma^*.
\]

Es decir, \(\langle M\rangle\in All\) si y solo si \(L(M)=\Sigma^*\).

Verificamos las hipotesis del Teorema de Rice.

### 1. \(All\) es una propiedad semantica

Supongamos que \(M_1\) y \(M_2\) son dos MT con \(L(M_1)=L(M_2)\). Entonces

\[
\langle M_1\rangle\in All \iff L(M_1)=\Sigma^* \iff L(M_2)=\Sigma^* \iff \langle M_2\rangle\in All.
\]

Por lo tanto, la pertenencia a \(All\) depende exclusivamente del lenguaje reconocido por la MT, y no de su sintaxis o estructura. Esto satisface la condicion de propiedad semantica.

### 2. \(All\) es no trivial

Necesitamos exhibir dos MT, una en \(All\) y otra fuera de \(All\).

- **Una MT en \(All\):** sea \(M_{\Sigma^*}\) la MT que en cualquier entrada va al estado de aceptacion (por ejemplo, \(M_{\Sigma^*}\) lee el primer simbolo y acepta inmediatamente). Entonces \(L(M_{\Sigma^*})=\Sigma^*\), y \(\langle M_{\Sigma^*}\rangle\in All\). Esto muestra que \(All\neq\emptyset\).
- **Una MT fuera de \(All\):** sea \(M_\emptyset\) la MT que en cualquier entrada va al estado de rechazo (por ejemplo, \(M_\emptyset\) rechaza inmediatamente sin leer la cinta). Entonces \(L(M_\emptyset)=\emptyset\neq\Sigma^*\) (pues \(\Sigma^*\) contiene al menos la cadena vacia, y mas si \(\Sigma\neq\emptyset\)), y \(\langle M_\emptyset\rangle\notin All\). Esto muestra que \(All\) no contiene a todas las descripciones de MT.

(El razonamiento de no trivialidad solo requiere \(\Sigma\neq\emptyset\), lo cual asumimos siempre para alfabetos en este curso.)

### Aplicacion del teorema

Hemos verificado:

- \(All\) es una propiedad semantica.
- \(All\) es no trivial (existen MT con \(L(M)=\Sigma^*\) y otras con \(L(M)\neq\Sigma^*\)).

Por el Teorema de Rice, \(All\) es indecidible.

\[
\boxed{All=\{\langle M\rangle\mid L(M)=\Sigma^*\} \text{ es indecidible.}}
\]

## Comentario sobre la conexion con el resto del capitulo

El lenguaje \(All\) es el problema *complementario* (en cierto sentido) a \(E_{TM}=\{\langle M\rangle\mid L(M)=\emptyset\}\): mientras que \(E_{TM}\) pregunta si \(M\) **no** acepta nada, \(All\) pregunta si \(M\) acepta **todo**. Sipser prueba la indecibilidad de \(E_{TM}\) directamente (Teorema 5.2) por reduccion desde \(A_{TM}\); aqui aprovechamos que el Teorema de Rice generaliza esos argumentos para cualquier propiedad semantica no trivial, ahorrandonos la construccion explicita de la reduccion.

Vale aclarar que existe tambien una demostracion directa por reduccion: dado \(\langle M,w\rangle\) podemos construir una MT \(M_w\) que ignore su entrada, simule \(M\) sobre \(w\) y acepte si \(M\) acepta. Asi:

- Si \(M\) acepta \(w\): \(L(M_w)=\Sigma^*\), por lo que \(\langle M_w\rangle\in All\).
- Si \(M\) no acepta \(w\): \(L(M_w)=\emptyset\) o, dependiendo del comportamiento, no contiene a alguna cadena, por lo que \(\langle M_w\rangle\notin All\).

Esto da \(A_{TM}\le_m All\), demostrando la indecibilidad de \(All\) sin invocar Rice. Pero el camino via Rice, como pide el enunciado, es mucho mas conciso una vez verificadas las dos condiciones.
