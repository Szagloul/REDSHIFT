# RedShift

A fast-paced, infinite survival dodger built with Python's Turtle graphics library. Players must navigate a minimalist arena, evading an ever-growing onslaught of red barriers that scale in speed and quantity as the score increases.

## Features

- **Dynamic Difficulty Scaling**:
  - Enemy speed increases based on your current score.
  - Additional enemies spawn at specific score milestones (20, 40, 60, 80, and 100+).
- **Visual Progression**:
  - Background colors shift through 6 distinct tiers (White, Pastel, Cyan, Lime, and Deep Slate) to signal increasing danger levels.
- **Physics & Collision**:
  - Custom-built AABB (Axis-Aligned Bounding Box) collision detection logic.
  - Procedural enemy spawning with randomized widths and heights from all four screen edges.
- **Responsive Controls**:
  - Smooth 4-way movement using boolean-based keyboard event listeners for fluid diagonal-like input.
- **Persistent Scoring**:
  - Real-time score tracking and High Score preservation across game resets.
- **Object-Oriented Architecture**:
  - Clean class structure using inheritance for Players, Enemies, and Game Items to ensure organized and extensible code.

## Usage

1. Ensure you have **Python 3.x** installed on your system.
2. Clone or download this repository.
3. Run the script via your terminal or IDE:
   ```bash
   python main.py
4. USE W,A,S,D for movement

## Technologies Used

- **Python 3.x**
- **Turtle Graphics Library** (Standard Library)
- **Random & Time modules** for procedural logic and frame timing.

## Skills Demonstrated

- **Object-Oriented Programming (OOP)**: Utilizing inheritance and class structures (Player and Enemy inheriting from GameItem) to manage game entities cleanly.
- **Game Loop Management**: Implementing `wn.update()` and `time.sleep()` for manual frame control and performance optimization.
- **Event-Driven Programming**: Mapping keyboard inputs to boolean states to allow for fluid, responsive movement.
- **Procedural Logic**: Randomizing enemy dimensions, entry points, and trajectories to ensure unique gameplay in every session.
- **Dynamic Difficulty Scaling**: Programming math-based speed increases and conditional logic to spawn more enemies as the player progresses.
- **State Management**: Handling game resets, score clearing, and environmental changes dynamically within a loop.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Created by Saif Zagloul*
