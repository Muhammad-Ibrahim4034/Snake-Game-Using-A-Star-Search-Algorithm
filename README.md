# Snake-Game-Using-A-Star-Search-Algorithm
In this project me any my team created snake game with both manual and A* search algorithm to illustrate the difference between an Ai algorithm and human.


Absolutely! Here's a polished and detailed `README.md` file for your **Snake Game with Manual & A* AI Modes** project:

---

# 🐍 Snake Game: Manual Play vs. A* AI Search

## 💡 Project Overview

This project is a classic **Snake Game** that supports two modes of gameplay:
1. **Manual Mode** – controlled by a human player using keyboard input.
2. **AI Mode** – powered by the **A* Search Algorithm** to demonstrate pathfinding and decision-making.

The aim of the project is to visually **compare human behavior vs. AI behavior** and showcase how an algorithm like **A*** navigates the snake efficiently toward the food while avoiding collisions.

## 👥 Team Members

- [Your Name]
- [Teammate 1]
- [Teammate 2]
- [Teammate 3]  
*(Update with actual names)*

## 🎯 Objectives

- Build a fun and interactive snake game.
- Implement the **A* Search Algorithm** for automated gameplay.
- Compare AI decision-making with human input.
- Help beginners understand AI search techniques through visualization.

## 🛠️ Technologies Used

- **Python** with **Pygame** (for game development)
- **A* Search Algorithm** (for AI navigation logic)
- Basic **Data Structures** (queues, priority queues, graphs)

## 🚀 How It Works

### 🕹️ Manual Mode
- Player controls the snake using arrow keys.
- The goal is to eat as much food as possible without hitting the walls or itself.

### 🤖 AI Mode (A* Search)
- The snake is controlled by an A* algorithm.
- A path is calculated in real-time from the snake’s head to the food.
- The snake follows the optimal path while avoiding collisions.
- If no valid path exists, the game ends.

## 📁 Folder Structure

```
snake-ai-game/
│
├── snake_game.py           # Main game loop and logic
├── ai.py                   # A* pathfinding logic
├── game_objects.py         # Snake, food, and grid components
├── assets/                 # (Optional) images/sounds
└── README.md               # Project documentation
```

## 🎮 Controls (Manual Mode)

- **Arrow Keys** – Move the snake: ↑ ↓ ← →
- **M Key** – Switch to Manual Mode
- **A Key** – Switch to AI Mode
- **R Key** – Restart the game
- **Q Key** – Quit the game

## 🔍 A* Algorithm: How It Works

- Treats the game grid as a graph.
- Uses **heuristics** (Manhattan Distance) to estimate cost from the snake to the food.
- Prioritizes paths that are shortest and safest.
- Continuously recalculates the best path after each move.

## 📊 Comparison: Human vs AI

| Feature         | Manual Mode | AI Mode (A*)      |
|----------------|-------------|-------------------|
| Reaction Time   | Slower (Human) | Instant (AI)   |
| Decision Making | Based on skill | Based on algorithm |
| Mistakes        | Possible       | Rare (unless no valid path) |
| Path            | Varies         | Always optimal (if path exists) |

## 📸 Screenshots

*(You can add screenshots here to show gameplay in both modes)*

## 🧪 How to Run

### 🐍 Requirements
- Python 3.x
- Pygame  
  Install using:  
  ```
  pip install pygame
  ```

### ▶️ Start the Game
```bash
python snake_game.py
```

## 🔮 Future Improvements

- Add other AI algorithms (BFS, DFS, Dijkstra) for comparison.
- Add increasing difficulty levels.
- Add score tracking and high score saving.
- Deploy a web version using JavaScript or WebAssembly.

## ❤️ Acknowledgements

- Pygame Library
- A* Search Algorithm Theory
- Open-source snake game inspirations

---

Let me know if you want help writing the actual Python files for the game, including A* logic and manual controls — happy to help you build the full project step-by-step!
