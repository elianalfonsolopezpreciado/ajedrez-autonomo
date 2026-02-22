# Documentación completa

## 1. Objetivo del sistema

Construir un sistema en terminal que ejecute múltiples juegos de ajedrez en paralelo para comparar líneas de juego y aproximar decisiones robustas.

## 2. Aclaración teórica importante

La meta de “siempre ganar” en ajedrez no está garantizada desde la posición inicial. Este software adopta un enfoque de **optimización local con búsqueda adversarial**: elige movimientos que maximizan el resultado esperado contra respuestas fuertes del rival.

## 3. Diseño técnico

### 3.1 Motor de búsqueda (`engine.py`)

- Algoritmo base: Minimax.
- Optimización: poda alpha-beta.
- Evaluación:
  - Material por tipo de pieza.
  - Movilidad (cantidad de jugadas legales).
  - Condiciones terminales (mate/tablas).

### 3.2 Simulación paralela (`simulation.py`)

1. Desde el tablero base, se eligen N jugadas candidatas (`branches`).
2. Cada candidata crea un escenario independiente.
3. Cada escenario avanza con el mejor movimiento según minimax hasta `plies` o fin de partida.

### 3.3 Render ASCII (`renderer.py`)

- Convierte la matriz interna del tablero a caracteres ASCII.
- Imprime múltiples tableros lado a lado para comparación visual.

## 4. Estructura del proyecto

```text
.
├── ajedrez_autonomo/
│   ├── __init__.py
│   ├── engine.py
│   ├── renderer.py
│   └── simulation.py
├── DOCUMENTACION_COMPLETA.md
├── README.md
├── main.py
└── requirements.txt
```

## 5. Instalación paso a paso

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 6. Uso operativo

### 6.1 Ejecución básica

```bash
python main.py --depth 3 --branches 3 --plies 12
```

### 6.2 Ajustes recomendados

- CPU limitada: `--depth 2 --branches 2`
- Mayor calidad: `--depth 4 --branches 4`

### 6.3 Posición específica

```bash
python main.py --fen "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3"
```

## 7. Validación

Comandos recomendados:

```bash
python -m compileall .
python main.py --depth 2 --branches 2 --plies 4
```

## 8. Extensión futura hacia “juego casi perfecto”

Para acercarse a un rendimiento más fuerte:

- Iterative deepening.
- Quiescence search.
- Transposition tables (Zobrist hashing).
- Evaluación entrenada (NNUE/ML).
- Endgame tablebases.

## 9. Solución de problemas

- Error de ejecución por versión de Python:
  - Usar Python 3.10 o superior.
- Rendimiento bajo:
  - Bajar `--depth` o `--branches`.
- Salida muy ancha:
  - Reducir número de escenarios paralelos.

## 10. Licencia y uso

Se entrega como base técnica educativa para análisis de búsqueda adversarial en ajedrez.
