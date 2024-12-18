# Snake Game 🐍

This project is a classic **Snake Game** implemented in Python using the `turtle` module. It is part of the [100 Days of Python](https://www.udemy.com/course/100-days-of-code/) course by Angela Yu on Udemy. The game showcases core programming concepts like Object-Oriented Programming (OOP), modularization, and event handling.

## Features 🚀
- **Responsive Controls**: Navigate the snake using arrow keys (`Up`, `Down`, `Left`, `Right`).
- **Dynamic Gameplay**: The snake grows as it eats food, and the score updates in real time.
- **Collision Detection**: Game ends if the snake hits a wall or its own body.
- **Score Display**: Shows current score and game-over message.

## Gameplay Instructions 🎮
1. Run the `main.py` script.
2. Use the arrow keys to control the snake.
3. Avoid hitting the walls or the snake's body.
4. Eat the red food to increase your score.

## Project Structure 📂
- **`main.py`**: Handles the game loop, collision detection, and interactions between components.
- **`snake.py`**: Contains the `Snake` class to manage the snake's movement, growth, and controls.
- **`food.py`**: Defines the `Food` class to generate food at random locations.
- **`scoreboard.py`**: Implements the `ScoreBoard` class to manage and display the score and game-over messages.

## How to Run 💻
1. Ensure Python is installed on your system.
2. Clone this repository or download the files.
3. Navigate to the project directory.
4. Run the game:
   ```bash
   python main.py
