# 🎮 Tic Tac Toe Game with AI ❌⭕

A professional, fully-featured Tic Tac Toe game built with Python and Pygame, featuring smooth animations and an unbeatable AI powered by the Minimax algorithm.

## 👨‍💻 Creator

**Ankush Kumar**
- LinkedIn: [linkedin.com/in/ankush-kumar-60333537b](https://www.linkedin.com/in/ankush-kumar-60333537b/)
- GitHub: [ankushkumarake1234-lang/Tic-Tac-Toe](https://github.com/ankushkumarake1234-lang/Tic-Tac-Toe)

---

## ✨ Features

### 🎯 Game Modes
- **Player vs Player (PvP)**: Play against a friend locally
- **Player vs AI (PvE)**: Challenge an unbeatable AI opponent

### 🎨 Animations & Visual Effects (NEW!)
- **Smooth Scale Animations**: X's and O's smoothly scale up when placed
- **Fade-In Effects**: Elegant fade-in animations for all elements
- **Winning Line Animation**: Animated line that draws across winning combinations
- **Hover Effects**: Visual feedback when hovering over cells
- **Gradient Buttons**: Beautiful gradient menu buttons with hover states
- **Game Over Overlay**: Smooth fade-in overlay with results
- **Credits Animation**: Animated creator credits on main menu

### 🧠 Artificial Intelligence
- **Minimax Algorithm**: The AI uses the classic Minimax algorithm with Alpha-Beta pruning
- **Unbeatable**: The AI plays optimally and cannot be beaten (you can only draw or lose)
- **Realistic Delay**: Small thinking delay for a more natural feel

### 🎨 Graphics & Visuals
- Beautiful gradient background
- Custom X and O symbols with smooth animations
- Clean, modern grid design
- Smooth visual feedback
- Animated game over screen with results
- Professional UI with shadows and gradients

### 🔊 Sound & Audio
- **Move Sound**: Plays when a move is made
- **Win Sound**: Celebratory sound when someone wins
- **Draw Sound**: Sound effect for a draw
- **Voice Audio**: 
  - "You Win" voice feedback
  - "AI Wins" voice feedback
  - "Draw" voice feedback

### 🎮 Game Logic
- ✅ Complete win/draw detection
- ✅ Proper turn management
- ✅ Invalid move prevention
- ✅ Game state management
- ✅ Restart functionality (Press R)
- ✅ Return to menu (Press M)

## 📋 Requirements

- **Python 3.7+**
- **Pygame 2.0+**

## 🚀 Installation & Setup

### Step 1: Install Python

If you don't have Python installed:

**macOS/Linux:**
```bash
# Python is usually pre-installed. Check version:
python3 --version

# If not installed, download from python.org
```

**Windows:**
- Download Python from [python.org](https://www.python.org/downloads/)
- During installation, **check "Add Python to PATH"**

### Step 2: Install Pygame

Open your terminal/command prompt and run:

```bash
# Install pygame using pip
pip3 install pygame

# Or on some systems:
pip install pygame
```

To verify installation:
```bash
python3 -c "import pygame; print(pygame.version.ver)"
```

### Step 3: Download the Game

1. Clone this repository:
```bash
git clone https://github.com/ankushkumarake1234-lang/Tic-Tac-Toe.git
cd Tic-Tac-Toe
```

Or download the ZIP file and extract it.

### Step 4: Run the Game

```bash
python3 tictactoe.py
```

The game will automatically create the assets folder and generate basic graphics if image files are missing!

## 🎮 How to Run the Game

### Quick Start

Simply run:
```bash
python3 tictactoe.py
```

Or:
```bash
python tictactoe.py
```

### First-Time Setup Issues?

If you get an error about missing pygame:
```bash
# Install pygame first
pip3 install pygame

# Then run the game
python3 tictactoe.py
```

## 🎯 How to Play

### Starting the Game

1. Run the game
2. You'll see the main menu with animated buttons:
   - **Player vs Player**: Play against a friend
   - **Player vs AI**: Challenge the AI
3. Creator credits are displayed at the bottom

### During the Game

- **Hover** over cells to see highlight effects
- **Click** on any empty cell to make your move
- **Watch** the smooth scale-up animation as your symbol appears
- **X** always goes first (Player 1)
- **O** goes second (Player 2 or AI)

### Game Over

When the game ends, you'll see:
- Smooth fade-in overlay
- Animated winning line (if someone won)
- The result with emoji
- Press **R** to restart with the same mode
- Press **M** to return to the main menu

### Animation Features

- **Cell Placement**: Symbols smoothly scale from 0 to full size
- **Winning Line**: A golden line animates across the winning combination
- **Menu Buttons**: Hover effects with gradient color changes
- **Game Over**: Smooth overlay fade-in with results

## 🎨 Animation Details

### Scale Animation
When you place an X or O, it starts at 0% size and smoothly grows to 100%:
- **Speed**: Controlled by `SCALE_SPEED` constant
- **Effect**: Creates a "popping in" effect

### Fade Animation
All elements fade in smoothly:
- **Alpha Transitions**: Smooth opacity changes
- **Speed**: Controlled by `FADE_SPEED` constant

### Winning Line Animation
When someone wins:
- A golden line draws from start to end of the winning combination
- **Progress**: 0% to 100% smooth transition
- **Effect**: Clearly shows which combination won

### Hover Effects
- Cells glow slightly when mouse hovers over them
- Menu buttons change gradient colors on hover
- Provides clear visual feedback

## 🧠 Understanding the Minimax Algorithm

### What is Minimax?

Minimax is a decision-making algorithm used in two-player games. Here's how it works:

1. **Game Tree**: The algorithm builds a tree of all possible game states
2. **Evaluation**: Each terminal state (win/loss/draw) gets a score:
   - AI wins: +10 points
   - Player wins: -10 points
   - Draw: 0 points
3. **Maximizing/Minimizing**: 
   - AI tries to **maximize** the score
   - Player tries to **minimize** the score
4. **Recursion**: The algorithm recursively evaluates all possible moves
5. **Best Move**: Chooses the move with the best guaranteed outcome

### Alpha-Beta Pruning

To optimize performance, the algorithm uses Alpha-Beta pruning:
- **Alpha**: Best value the maximizer (AI) can guarantee
- **Beta**: Best value the minimizer (Player) can guarantee
- Branches that won't affect the final decision are **pruned** (skipped)
- This makes the algorithm **much faster** without losing accuracy

## 📝 Code Structure

```
tictactoe.py
├── Constants & Enums
│   ├── Window settings (WIDTH, HEIGHT, etc.)
│   ├── Colors (BLUE, RED, GREEN, etc.)
│   ├── Animation settings (speeds, delays)
│   └── GameMode enumeration
│
└── TicTacToe Class
    ├── __init__()              # Initialize game
    ├── load_assets()           # Load/create images and sounds
    ├── reset_game()            # Reset game state
    │
    ├── Animation Methods
    │   ├── add_animation()     # Add cell animation
    │   ├── update_animations() # Update all animations
    │   └── draw_gradient_rect()# Draw gradient rectangles
    │
    ├── Drawing Methods
    │   ├── draw_menu()         # Render animated menu
    │   ├── draw_board()        # Render game board
    │   └── draw_game_over()    # Render game over screen
    │
    ├── Game Logic
    │   ├── make_move()         # Handle player moves
    │   ├── check_winner()      # Check for winner
    │   └── is_board_full()     # Check for draw
    │
    ├── AI Methods
    │   ├── minimax()           # Minimax algorithm
    │   └── get_best_move()     # Find optimal move
    │
    ├── Event Handlers
    │   ├── handle_menu_click() # Menu interactions
    │   └── handle_game_click() # Game interactions
    │
    └── run()                   # Main game loop
```

## 🎨 Customization

### Adjust Animation Speed

Edit these constants in `tictactoe.py`:

```python
ANIMATION_SPEED = 15      # Overall animation speed
FADE_SPEED = 10          # Fade-in speed
SCALE_SPEED = 0.1        # Symbol scale-up speed
GLOW_SPEED = 5           # Glow effect speed
```

### Change Colors

Modify the color constants:

```python
BLUE = (52, 152, 219)
RED = (231, 76, 60)
GREEN = (46, 204, 113)
GOLD = (255, 215, 0)
# Add your own!
```

### Replace Sounds

You can replace the sound files with your own:

1. Record or download better sound effects
2. Place them in `assets/sounds/` folder
3. Keep the same filenames and `.wav` format

### Replace Graphics

1. Create your own images
2. Place them in `assets/` folder
3. Recommended sizes:
   - `x.png` and `o.png`: 512x512 pixels
   - `grid.png`: 450x450 pixels
   - `background.png`: 600x700 pixels

## 🐛 Troubleshooting

### "pygame not found" Error
```bash
pip3 install pygame
```

### "No module named pygame" on macOS
```bash
python3 -m pip install pygame
```

### Sound Not Playing
- Check that sound files exist in `assets/sounds/`
- Check your system volume
- The game will work without sounds

### Animations Too Fast/Slow
- Edit the animation speed constants in the code
- Increase values to slow down, decrease to speed up

### Performance Issues
- Close other applications
- The game runs at 60 FPS and is very lightweight
- Update your graphics drivers if needed

## 🎓 Learning Resources

To learn more about game development and AI:

- **Pygame Documentation**: [pygame.org/docs](https://www.pygame.org/docs/)
- **Minimax Algorithm**: [Wikipedia - Minimax](https://en.wikipedia.org/wiki/Minimax)
- **Alpha-Beta Pruning**: [Wikipedia - Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- **Python Game Development**: [Real Python - PyGame Tutorial](https://realpython.com/pygame-a-primer/)
- **Animation Techniques**: [Pygame Animation Tutorial](https://www.pygame.org/wiki/tutorials)

## 📄 License

This project is created for educational purposes. Feel free to use, modify, and distribute.

## 🤝 Contributing

Suggestions and improvements are welcome! Some ideas:
- [ ] Add difficulty levels for AI
- [ ] Add online multiplayer
- [ ] Add different board sizes (4x4, 5x5)
- [ ] Add more animation effects
- [ ] Add score tracking across games
- [ ] Add different themes/skins
- [ ] Add particle effects for wins
- [ ] Add sound toggles in settings

## 🌟 New Features in This Version

### v2.0 - Animation Update
- ✨ Smooth scale animations for X's and O's
- ✨ Fade-in effects for all UI elements
- ✨ Animated winning line
- ✨ Hover effects on cells and buttons
- ✨ Gradient buttons with smooth transitions
- ✨ Animated game over overlay
- ✨ Creator credits with fade-in animation
- ✨ Professional gradient backgrounds
- ✨ Enhanced visual feedback throughout

## 📞 Contact

**Ankush Kumar**
- LinkedIn: [linkedin.com/in/ankush-kumar-60333537b](https://www.linkedin.com/in/ankush-kumar-60333537b/)
- GitHub: [ankushkumarake1234-lang](https://github.com/ankushkumarake1234-lang)

---

## 🚀 Quick Start Summary

1. **Install Python** (if needed)
2. **Install Pygame**: `pip3 install pygame`
3. **Clone/Download** this repository
4. **Run the game**: `python3 tictactoe.py`
5. **Enjoy the animations!** 🎮✨

**Made with ❤️ by Ankush Kumar**

---

⭐ If you like this project, please give it a star on GitHub! ⭐
