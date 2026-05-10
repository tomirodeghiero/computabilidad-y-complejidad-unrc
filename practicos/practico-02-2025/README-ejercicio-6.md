# Ejercicio 6

## Enunciado

Usar el teorema de Rice, para demostrar la indecibilidad del siguiente lenguaje:

\[
All=\{\langle M\rangle \mid \mathcal L(M)=\Sigma^*\}.
\]

## Proposición

El lenguaje

\[
All=\{\langle M\rangle \mid L(M)=\Sigma^*\}
\]

es indecidible.

## Demostración (Teorema de Rice)

Consideremos la propiedad semántica de lenguajes reconocibles:

\[
P(L): \iff L=\Sigma^*.
\]

Verificamos las hipótesis de Rice:

1. **Propiedad de lenguaje (semántica):** depende sólo de \(L(M)\), no de la sintaxis de \(M\).
2. **No trivialidad:**  
   - Existe una MT \(M_{all}\) tal que \(L(M_{all})=\Sigma^*\) (por ejemplo, la máquina que acepta toda entrada).  
   - Existe una MT \(M_{\emptyset}\) tal que \(L(M_{\emptyset})=\emptyset\) (por ejemplo, la máquina que rechaza toda entrada).  
   Entonces la propiedad vale para algunos lenguajes reconocibles y falla para otros.

Por el Teorema de Rice, todo conjunto de descripciones de MT definido por una propiedad semántica no trivial es indecidible.

Aplicando Rice a \(P\), concluimos que \(All\) es indecidible.
