# FreeCell Solver

This project is a simulation of the FreeCell card game, designed to demonstrate the solving process of the game using Python. 

## Overview

FreeCell is a solitaire card game played with a standard 52-card deck. The objective is to move all cards to the foundation piles, following specific rules for moving cards between tableau columns, free cells, and foundation piles. This project implements the game logic and provides a solver to find solutions to various FreeCell scenarios.

## Project Structure

- `src/main.py`: Entry point of the application that initializes the game and starts the simulation.
- `src/game/board.py`: Contains the `Board` class that manages the game state and operations on the board.
- `src/game/card.py`: Defines the `Card` class representing individual playing cards.
- `src/game/solver.py`: Implements the `Solver` class that contains the logic for solving the FreeCell game.
- `tests/`: Directory containing unit tests for the game components.

## Requirements

To run this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Simulation

To start the FreeCell simulation, run the following command:

```
python src/main.py
```

## Running Tests

To run the unit tests for this project, use the following command:

```
python tests/test_<target>.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.