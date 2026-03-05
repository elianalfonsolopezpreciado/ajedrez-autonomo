# Ajedrez Autónomo (Autonomous Chess)

[Versión en Español](#ajedrez-autónomo-es) | [English Version](#autonomous-chess-en)

---

<a name="autonomous-chess-en"></a>
# Autonomous Chess (English)

A terminal-based chess simulator that explores multiple game branches in parallel, providing a tactical plan and real-time ASCII visualization of potential scenarios.

## 🚀 Overview

This project implements a practical approach to chess strategy using **Minimax search with Alpha-Beta pruning**. It doesn't just suggest a single move; it generates a comprehensive tactical playbook, predicting opponent responses and suggesting counters for each branch.

## ✨ Key Features

- **Multi-Branch Simulation**: Simulate several independent game lines simultaneously.
- **Tactical Playbook**: Detailed plans showing:
  - Recommended move.
  - Top predicted opponent responses.
  - Suggested counter-moves for each response.
- **Side-by-Side ASCII Rendering**: Visual "card" format for boards to compare scenarios easily.
- **Customizable Search**: Control depth, branch count, and simulation length via CLI.
- **FEN Support**: Start simulations from any valid Forsyth-Edwards Notation position.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: This project currently has no external dependencies.*

## 🕹️ Usage

Run the main script with customizable parameters:

```bash
python main.py --depth 3 --branches 3 --plies 12 --responses 3
```

### Parameters:
- `--depth`: Minimax search depth (higher is more accurate but slower).
- `--branches`: Number of initial parallel scenarios to explore.
- `--plies`: Maximum half-moves to simulate per scenario.
- `--responses`: Number of opponent responses to consider in the tactical plan.
- `--fen`: Custom starting position in FEN format.

### Example with FEN:
```bash
python main.py --fen "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3"
```

## 🏗️ Architecture

- `main.py`: CLI entry point and simulation flow controller.
- `ajedrez_autonomo/`
  - `chess_core.py`: Core logic (board representation, move generation, FEN parser).
  - `engine.py`: Search engine (Minimax, Alpha-Beta pruning, heuristics).
  - `simulation.py`: Scenario coordination and tactical plan generation.
  - `renderer.py`: ASCII board rendering and playbook formatting.

## 🧠 Technical Details

- **Algorithm**: Minimax with Alpha-Beta pruning to optimize search space.
- **Heuristic Evaluation**:
  - **Material**: Piece values (P=100, N=320, B=330, R=500, Q=900, K=20000).
  - **Mobility**: Bonus for the number of legal moves available.
  - **Terminal States**: Immediate win/loss evaluation for checkmate or king capture.

## 🗺️ Roadmap

- [ ] Implement full FIDE rules (Castling, En Passant, 50-move rule).
- [ ] Add Transposition Tables (Zobrist Hashing) for faster search.
- [ ] Interactive mode for manual branch exploration.
- [ ] Integration with UCI engines (e.g., Stockfish).

---

<a name="ajedrez-autónomo-es"></a>
# Ajedrez Autónomo (Español)

Un simulador de ajedrez basado en terminal que explora múltiples ramas de juego en paralelo, proporcionando un plan táctico y visualización ASCII en tiempo real de escenarios potenciales.

## 🚀 Descripción General

Este proyecto implementa una aproximación práctica a la estrategia de ajedrez utilizando **búsqueda Minimax con poda Alpha-Beta**. No solo sugiere un único movimiento; genera un "playbook" táctico completo, prediciendo las respuestas del oponente y sugiriendo contra-jugadas para cada rama.

## ✨ Características Principales

- **Simulación Multi-Rama**: Simula varias líneas de juego independientes simultáneamente.
- **Plan Táctico Detallado**:
  - Jugada recomendada.
  - Principales respuestas predichas del oponente.
  - Contra-jugadas sugeridas para cada respuesta.
- **Renderizado ASCII Lado a Lado**: Formato de "tarjetas" visuales para comparar tableros fácilmente.
- **Búsqueda Personalizable**: Controla la profundidad, el número de ramas y la duración de la simulación mediante CLI.
- **Soporte FEN**: Inicia simulaciones desde cualquier posición válida en Notación Forsyth-Edwards.

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd <directorio-del-repositorio>
   ```

2. **Configurar un entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   *Nota: Este proyecto actualmente no tiene dependencias externas.*

## 🕹️ Uso

Ejecuta el script principal con parámetros personalizables:

```bash
python main.py --depth 3 --branches 3 --plies 12 --responses 3
```

### Parámetros:
- `--depth`: Profundidad de búsqueda Minimax (más alto es más preciso pero más lento).
- `--branches`: Número de escenarios iniciales paralelos a explorar.
- `--plies`: Máximo de medios movimientos (plies) a simular por escenario.
- `--responses`: Cantidad de respuestas del rival a considerar en el plan táctico.
- `--fen`: Posición inicial personalizada en formato FEN.

### Ejemplo con FEN:
```bash
python main.py --fen "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3"
```

## 🏗️ Arquitectura

- `main.py`: Punto de entrada CLI y controlador del flujo de simulación.
- `ajedrez_autonomo/`
  - `chess_core.py`: Lógica central (representación del tablero, generación de movimientos, parser FEN).
  - `engine.py`: Motor de búsqueda (Minimax, poda Alpha-Beta, heurísticas).
  - `simulation.py`: Coordinación de escenarios y generación de planes tácticos.
  - `renderer.py`: Renderizado ASCII de tableros y formateo del plan de juego.

## 🧠 Detalles Técnicos

- **Algoritmo**: Minimax con poda Alpha-Beta para optimizar el espacio de búsqueda.
- **Evaluación Heurística**:
  - **Material**: Valores de piezas (P=100, N=320, B=330, R=500, Q=900, K=20000).
  - **Movilidad**: Bonificación por el número de movimientos legales disponibles.
  - **Estados Terminales**: Evaluación inmediata de victoria/derrota por jaque mate o captura de rey.

## 🗺️ Próximas Mejoras

- [ ] Implementar reglas FIDE completas (Enroque, Al paso, regla de 50 movimientos).
- [ ] Añadir Tablas de Transposición (Zobrist Hashing) para búsquedas más rápidas.
- [ ] Modo interactivo para exploración manual de ramas.
- [ ] Integración con motores UCI (ej. Stockfish).
