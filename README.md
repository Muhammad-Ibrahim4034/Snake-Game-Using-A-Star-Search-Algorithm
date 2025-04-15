# Snake-Game-Using-A-Star-Search-Algorithm
In this project me any my team created snake game with both manual and A* search algorithm to illustrate the difference between an Ai algorithm and human.


# 🐍 Snake Game: Manual Play vs. A* AI Search

## 💡 Project Overview

This project is a classic **Snake Game** that supports two modes of gameplay:
1. **Manual Mode** – controlled by a human player using keyboard input.
2. **AI Mode** – powered by the **A* Search Algorithm** to demonstrate pathfinding and decision-making.

The aim of the project is to visually **compare human behavior vs. AI behavior** and showcase how an algorithm like **A*** navigates the snake efficiently toward the food while avoiding collisions.

## 👥 Team Members

- Muhammad Ibrahim
- Muhammad Hamza Nawaz
- Rameela Hassan


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


## 🔮 Future Improvements

- Add other AI algorithms (BFS, DFS, Dijkstra) for comparison.
- Add increasing difficulty levels.
- Add score tracking and high score saving.
- Deploy a web version using JavaScript or WebAssembly.

## ❤️ Acknowledgements

- Pygame Library
- A* Search Algorithm Theory
