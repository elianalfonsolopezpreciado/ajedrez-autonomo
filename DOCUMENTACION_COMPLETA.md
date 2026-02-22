# Documentación completa

## 1. Objetivo del sistema

Construir un sistema de terminal que:

1. Calcule jugadas recomendadas con búsqueda adversarial.
2. Liste posibles respuestas del oponente.
3. Indique la respuesta concreta sugerida para cada situación.
4. Muestre múltiples escenarios de juego en paralelo con visual ASCII clara.

## 2. Aclaración teórica importante

La meta de “siempre ganar” en ajedrez no está garantizada desde la posición inicial. Este software se enfoca en **maximizar robustez de decisiones** contra respuestas racionales del rival.

## 3. Diseño técnico

### 3.1 Núcleo de ajedrez (`chess_core.py`)

- Representación de tablero 8x8.
- Estructura `Move` con notación UCI.
- Parser FEN básico.
- Generación de movimientos por tipo de pieza.
- Filtrado de legalidad para no dejar el rey en jaque.

### 3.2 Motor de búsqueda (`engine.py`)

- Algoritmo: Minimax.
- Optimización: poda alpha-beta.
- Heurística:
  - Material.
  - Movilidad.
- API principal:
  - `best_move(board)`
  - `top_candidate_moves(board, count)`

### 3.3 Plan táctico (`simulation.py`)

`build_strategy_playbook(...)` genera, por cada plan inicial:

- **Jugada recomendada**.
- **Top respuestas del rival**.
- **Respuesta sugerida** a cada respuesta rival.

Estructuras:

- `StrategyPlan`
- `OpponentLine`

### 3.4 Simulación paralela (`simulation.py`)

`run(...)` crea escenarios independientes desde las mejores jugadas iniciales y los avanza hasta `max_plies` o fin de juego.

### 3.5 Visualización ASCII (`renderer.py`)

- Tableros en formato tarjeta con bordes.
- Piezas renderizadas en dos caracteres (`WK`, `BP`, etc.).
- Render lado a lado para comparar ramas.
- Sección textual de plan de juego con condicionales tipo:
  - “Si rival juega X, responde Y”.
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
│   ├── chess_core.py
│   ├── engine.py
│   ├── renderer.py
│   └── simulation.py
├── DOCUMENTACION_COMPLETA.md
├── README.md
├── main.py
└── requirements.txt
```

## 5. Instalación
## 5. Instalación paso a paso

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 6. Ejecución

### 6.1 Flujo principal

```bash
python main.py --depth 3 --branches 3 --plies 12 --responses 3
```

### 6.2 Parámetros

- `--depth`: profundidad de búsqueda.
- `--branches`: cantidad de planes/ramas iniciales.
- `--plies`: duración máxima por escenario simulado.
- `--responses`: respuestas rivales consideradas por plan.
- `--fen`: posición inicial en FEN.

## 7. Interpretación de resultados

### 7.1 Plan de juego recomendado

Cada bloque `PLAN` indica:

- Movimiento inicial sugerido.
- Escenarios probables de respuesta rival.
- Movimiento recomendado de continuación.

### 7.2 Simulación ASCII

Cada tarjeta de escenario indica:

- Turno.
- Score estimado.
- Estado.
- Tablero completo.
- Último movimiento.

## 8. Validación rápida

```bash
python -m compileall .
python main.py --depth 2 --branches 2 --plies 4 --responses 2
```

## 9. Limitaciones actuales

- No hay garantías matemáticas de victoria forzada universal.
- Reglas de ajedrez implementadas parcialmente.
- Precisión dependiente de profundidad y tiempo de cómputo.

## 10. Recomendaciones de mejora

- Implementar reglas completas (enroque, al paso, etc.).
- Añadir tabla de transposición.
- Mejorar heurística con factores posicionales.
- Modo interactivo para explorar ramas manualmente.
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
