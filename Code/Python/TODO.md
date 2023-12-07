
## Retrieve
### ¿Cómo representamos al usuario?

#### Representación caso
- identificador del cas
- fecha
- derivació del cas??
- descripció del problema (vector atribut-valor)
- diagnòstic/s del problema??
- solució del problema
- evaluació de la solució (èxit/fracàs)
- mesura d’utilitat

#### Organización casos
- Estructuradas 
    - Jerárquicas
        - Arbres/Grafs de característiques compartides
        - Arbres/Grafs Discriminants
        - Arbres/Grafs Redundants Discriminants
        - k-d trees
    - Organitzacions Orientades a Objectes
    - Bases de casos múltiples
- Mixtas
- Desestructuradas

En las estructuradas se usa la similitud?

La recuperación puede ser:
- BD: Concordancia absoluta
- CBR: Concordancia parcial

Podemos hacer un sistema que para las primeras variable sea como un árbol (para las variables más importantes) y luego use la similitud.
- Habrá que tener en cuenta el número de casos que tenemos para ver como hacemos el árbol

Los pasos serían:
- Indexació: cercar dins l'estructura de la biblioteca de casos un conjunt de "casos prometedors”
-  Valoració de Similitud: determinar el valor exacte de similitud per a cadascun dels casos cercats

Debemos estudiar más medidas de similitud.

#### Preprocessing
Debemos discretizar variables. ¿Qué método seleccionamos?
¿Qué hacemos con los valores que faltan?
- Eliminarlos
- No tener en cuenta en el calculo de la similitud los valores que faltan
    - No tener en cuenta en el individuo?
    - O si en una columna falta un valor, no tenerla en cuenta?
    - Si la estructuración es jerárquica y ese valor está en dentro de la jerárquia?
- Imputarlo
- Lazy: Si se desconoce uno de los valores, la disimilitud en ese valor es máxima, si se desconocen los dos es mínima.


## Adapt
¿Si el caso seleccionado no coincide perfectamente con el caso nuevo?
- Adaptació nul·la (PLEXUS)
- Adaptació ponderada (knn)
- Adaptació estructural
    - Mètodes de substitució
        - Ajustament de paràmetres (HYPO, PERSUADER, JUDGE) (Creo que no se puede en nuestro dominio porque la solución no es númerica)
        - Mètodes d’abstracció/re-especialització (CHEF, JULIANA, SWALE, PLEXUS, CYRUS) (Utilizar conocimiento del dominio y aplicar restricciones)
        - Mètodes de substitució basats en casos (CLAVIER, JULIA, CELIA) (utilizar un caso diferencia para completar) (en nuestro dominio no me cuadra)
    - Mètodes de transformació (CASEY, JULIA, KRITIK) (usar reglas, añadir cosas o eliminarlas) (usar sentido común)
    - Adaptació a un propòsit especial (PERSUADER, CHEF, JULIA) (usar conocimiento experto para crear reglas?)
- Adaptació derivativa (ARIES, PRODIGY/ANALOGY, JULIA, MEDIATOR) (no reutilizar el caso más similar sino su derivación)


## Evaluar el modelo
- En el mundo real
- Expertos
- Simulación

## Aprendizaje
- Aprenentatge per observació
    - Seeding del casos inicials de la Biblioteca de Casos
    - Aprenentatge d'un nou cas/experiència donat per un expert
- Aprenentatge per experiència
    - Aprenent dels èxits
    - Aprenent dels fracasos

![Alt text](image.png)







--------------------------------------------------------------------

# Características dominio
- Es dinámico
- Complejo
- Información qualitativa
- Certesa
- Bien estructurado?





--------------------------------------------------------------------------
# Profe tips
1. Fases de CBR (Cuatro R's) -> Proceso
2. Definición y representación de caso -> No usar tupla, usar clase, el caso viene de la ontologia, no guardamos libros, guardamos casos (modificar libros).
Si tu nunca has recomendado un libro, nunca lo vas a recomendar xd Métodos hibrido
3. Organización de la biblioteca de casos
    - No hacer organización plana => Objetivo un sistema escalable en escalabilidad y calidad, no se ha de degradar con el número de casos
    - Cluster: no siempre va a tener que explorar toda la base de datos. Métodos númericos valen. Abstracción usando experto. Consejo ideas sencillas xd. Usar red neuronal? No tenemos datos
    - Árbol
4. Persistencia. Guardar los casos en una base de datos
5. Que es un caso redundante o inútil. Hay que explicar que es un caso reduntante y qué es un caso inútil. Un inútil puede servir para saber que no hacer
6. Generar casos. Fuente de datos legal. A mano (encuestas, es una mierda). Sistema de recomendación externa. Aleatorio, como evaluas la calidad de la recomendación.
- Qué consideramos una recomendación de calidad?

. Experimentos!!!!

Punto estrella de esta práctica es la validación