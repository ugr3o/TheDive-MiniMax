 Juego del Gato y el Ratón 
📌 Descripción
Este proyecto consiste en un código que simula un juego del gato y el ratón de la forma más simple posible.
El jugador controla al gato, mientras que el ratón es controlado por la IA usando el algoritmo Minimax, que le permite tomar decisiones óptimas para escapar hacia la salida.

✅ ¿Qué creé?

Un programa en Python que simula el juego del gato y el ratón en un tablero de 7x7.
El jugador controla al gato con las teclas W/A/S/D e intenta atrapar al ratón antes de que llegue a la salida 🚪.
El ratón es controlado por el algoritmo Minimax con una heurística que prioriza escapar hacia la salida y alejarse del gato.


👍 ¿Qué funcionó?

Los movimientos del gato (jugador) funcionaron sin problemas, incluyendo la detección de límites del tablero.
La implementación del algoritmo Minimax para el ratón, logrando que tome decisiones inteligentes en cada turno.
La interacción básica del jugador con el juego es clara y funcional.

💥 ¿Qué fue un desastre?

El tablero del juego, debido a:

Las diferentes formas posibles de resolver el desafío.
La dificultad para ordenar el código en secciones claras.
El esfuerzo extra para dejar el código prolijo y entender correctamente cómo funciona el algoritmo Minimax.
Bugs visuales al moverse sobre la salida y al limpiar posiciones anteriores de los personajes.

💡 Mi mejor "¡ajá!"

Comprender cómo representar el tablero del juego y visualizar su estructura correctamente.
Entender que en Minimax el ratón es el maximizador y el gato es el minimizador, y cómo eso se traduce en código real.

▶️ Cómo probar / usar el proyecto en Python

Cloná este repositorio:

git clone git@github.com:ugr3o/TheDive-MiniMax.git

Entrá a la carpeta del proyecto:

bash   cd TheDive-MiniMax

Ejecutá el archivo:

bash   python minimax.py

Usá W/A/S/D para mover al gato y Q para salir.