# Ajedrez Autónomo en Terminal (Python)

Proyecto para simular **múltiples partidas de ajedrez en paralelo** en terminal y, además, generar un **plan exacto de jugadas recomendadas**: qué mover, qué podría responder el oponente y qué deberías hacer en cada caso.

> ⚠️ Importante: no existe un algoritmo conocido que garantice *“siempre ganar”* en ajedrez desde la posición inicial contra un oponente perfecto. Este proyecto implementa una **aproximación práctica** con minimax + poda alpha-beta para elegir jugadas robustas y preparar respuestas por ramas.
Proyecto para simular **múltiples partidas de ajedrez en paralelo** en terminal usando tableros ASCII.

> ⚠️ Importante: no existe un algoritmo conocido que garantice *“siempre ganar”* en ajedrez desde la posición inicial contra un oponente perfecto. Este proyecto implementa una **aproximación práctica** con minimax + poda alpha-beta para elegir jugadas fuertes y explorar escenarios alternativos.

## Características

- Simulación de varias ramas de juego en paralelo.
- Plan de juego detallado:
  - Jugada recomendada.
  - Posibles respuestas del rival.
  - Respuesta sugerida para cada respuesta rival.
- Evaluación heurística (material + movilidad).
- Búsqueda minimax con poda alpha-beta.
- Render ASCII mejorado con tableros en formato “tarjeta” lado a lado.
- Evaluación heurística (material + movilidad).
- Búsqueda minimax con poda alpha-beta.
- Render de tableros ASCII lado a lado.
- Soporte para iniciar desde una posición FEN.

## Requisitos

- Python 3.10+
- Dependencias de `requirements.txt` (sin librerías externas obligatorias)
- Dependencias de `requirements.txt`

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py --depth 3 --branches 3 --plies 12 --responses 3
python main.py --depth 3 --branches 3 --plies 12
```

### Parámetros

- `--depth`: profundidad minimax (más alto = más preciso, más lento)
- `--branches`: número de planes/escenarios iniciales
- `--plies`: máximo de medios movimientos por escenario simulado
- `--responses`: cantidad de respuestas candidatas del rival por cada plan
- `--branches`: número de escenarios paralelos a visualizar
- `--plies`: máximo de medios movimientos por escenario
- `--fen`: posición inicial personalizada

Ejemplo con FEN:

```bash
python main.py --fen "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" --responses 4
```

## Qué muestra la salida

1. **Plan de juego recomendado**:
   - `PLAN N: juega ...`
   - `Si rival juega X, responde con Y`
2. **Simulación ASCII de escenarios**:
   - Tarjetas con turno, score, estado, tablero y último movimiento.

## Arquitectura

- `main.py`: CLI, plan táctico y simulación.
- `ajedrez_autonomo/chess_core.py`: núcleo de ajedrez (tablero y movimientos).
- `ajedrez_autonomo/engine.py`: minimax + poda alpha-beta + evaluación.
- `ajedrez_autonomo/simulation.py`: generación de planes y escenarios paralelos.
- `ajedrez_autonomo/renderer.py`: render ASCII de tableros y plan táctico.
python main.py --fen "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
```

## Arquitectura

- `main.py`: CLI y flujo principal.
- `ajedrez_autonomo/engine.py`: motor de evaluación y búsqueda.
- `ajedrez_autonomo/simulation.py`: coordinación de escenarios paralelos.
- `ajedrez_autonomo/renderer.py`: representación ASCII lado a lado.

## Cómo interpretar la salida

Cada escenario muestra:
- Nombre del escenario
- Turno actual
- Score estimado (positivo favorece blancas, negativo negras)
- Estado (en juego/finalizada)
- Tablero ASCII
- Último movimiento

## Limitaciones

- La evaluación es heurística (no “resuelve” ajedrez).
- El núcleo no implementa todas las reglas avanzadas oficiales (enroque, al paso, etc.).
- Profundidades pequeñas no capturan táctica profunda.
- Profundidades pequeñas no capturan táctica profunda.
- El sistema modela al oponente como racional según minimax.

## Próximas mejoras sugeridas

- Ordenamiento de jugadas y tablas transposición.
- Reglas completas de ajedrez (enroque, al paso, 50 movimientos, etc.).
- Evaluación posicional avanzada.
- Integración opcional con motor UCI (Stockfish).
- Evaluación posicional avanzada (estructura de peones, rey, etc.).
- Integración con motor UCI (Stockfish) para análisis más fuerte.
- Interfaz interactiva en tiempo real (curses/Textual).
