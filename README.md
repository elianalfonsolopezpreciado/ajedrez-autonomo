# Ajedrez Autónomo en Terminal (Python)

Proyecto para simular **múltiples partidas de ajedrez en paralelo** en terminal usando tableros ASCII.

> ⚠️ Importante: no existe un algoritmo conocido que garantice *“siempre ganar”* en ajedrez desde la posición inicial contra un oponente perfecto. Este proyecto implementa una **aproximación práctica** con minimax + poda alpha-beta para elegir jugadas fuertes y explorar escenarios alternativos.

## Características

- Simulación de varias ramas de juego en paralelo.
- Evaluación heurística (material + movilidad).
- Búsqueda minimax con poda alpha-beta.
- Render de tableros ASCII lado a lado.
- Soporte para iniciar desde una posición FEN.

## Requisitos

- Python 3.10+
- Dependencias de `requirements.txt`

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py --depth 3 --branches 3 --plies 12
```

### Parámetros

- `--depth`: profundidad minimax (más alto = más preciso, más lento)
- `--branches`: número de escenarios paralelos a visualizar
- `--plies`: máximo de medios movimientos por escenario
- `--fen`: posición inicial personalizada

Ejemplo con FEN:

```bash
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
- Profundidades pequeñas no capturan táctica profunda.
- El sistema modela al oponente como racional según minimax.

## Próximas mejoras sugeridas

- Ordenamiento de jugadas y tablas transposición.
- Evaluación posicional avanzada (estructura de peones, rey, etc.).
- Integración con motor UCI (Stockfish) para análisis más fuerte.
- Interfaz interactiva en tiempo real (curses/Textual).
