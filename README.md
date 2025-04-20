# Extreme Obby 2D Platformer

A simple side-scrolling platformer game built with Pygame. Designed for easy understanding and extension—perfect for learning and coding together!

## Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## How to Run

1. Make sure you have Python 3 installed.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the game:
   ```
   python main.py
   ```

## File Structure

- `main.py` — Game entry point, setup, and main loop
- `movement.py` — Player movement functions (`up()`, `down()`, etc.)
- `player.py` — Player class and logic
- `level.py` — Level layout, platforms, and obstacles
- `ui.py` — User interface (name prompt, win/lose messages)
- `settings.py` — Game constants (colors, sizes, speeds)

## Game Controls

- **Left/Right:** Arrow keys or A/D
- **Jump:** Up arrow, W, or Space

## Gameplay

- Enter your name when prompted
- Move your block from the left to the right side of the level
- Jump over obstacles and gaps
- Win by reaching the finish line; lose if you fall into a pit

## License
MIT

Enjoy coding and playing together!
