# 🧠 Understanding the Minimax Algorithm

## What is Minimax?

Minimax is a **decision-making algorithm** used in turn-based, two-player games like Tic Tac Toe, Chess, and Checkers. The algorithm gets its name from its goal: one player tries to **MAXIMIZE** their score, while the other tries to **MINIMIZE** it.

## Core Concept

Imagine you're playing Tic Tac Toe and thinking ahead:
- "If I move here, my opponent will move there..."
- "Then I'll move here, and they'll move there..."
- "This leads to me winning!"

That's exactly what Minimax does - but **perfectly** and for **every possible move**.

## How It Works: Step by Step

### Step 1: Build a Game Tree

The algorithm creates a tree of all possible game states:

```
        Current State
       /      |      \
    Move 1  Move 2  Move 3
    /   \    /   \    /   \
  ...   ... ...  ... ...  ...
```

Each branch represents a possible move, and the tree continues until the game ends (win/loss/draw).

### Step 2: Assign Scores to Terminal States

When the game reaches an end state, we assign scores:

```
AI Wins    = +10 points   (Good for AI)
Player Wins = -10 points   (Bad for AI)
Draw       =  0 points    (Neutral)
```

### Step 3: Backtrack with Min/Max

Starting from the bottom of the tree, we work backwards:

- **AI's Turn (Maximizing Player)**: Choose the move with the **highest** score
- **Player's Turn (Minimizing Player)**: Choose the move with the **lowest** score

### Example: Simple Game Tree

```
                    [AI to move]
                   /      |      \
                  4       0      -10
                  ↑       ↑       ↑
            [Player]  [Player]  [Player]
             /   \     /   \     /   \
            4    3    0   -10  -10  5
            ↑    ↑    ↑    ↑    ↑   ↑
          [AI] [AI] [AI]  [AI] [AI] [AI]
```

**How AI chooses:**
1. Look at each possible move's outcomes
2. For the left branch: Player will choose MIN(4, 3) = 3? No! Actually 4, 3 are outcomes, player chooses MIN = 3
3. For middle branch: Player will choose MIN(0, -10) = -10
4. For right branch: Player will choose MIN(-10, 5) = -10
5. AI then chooses MAX(3, -10, -10) = **3** (left branch)

Wait, let me fix this example:

```
                [AI's turn - MAX]
                  Choose best
               /       |        \
           MIN=4    MIN=0    MIN=-10
              ↑        ↑         ↑
          [Player]  [Player]  [Player]
           /    \    /    \    /    \
          4     5   0    -10 -10    3
```

**Step by step:**
1. Left branch: Player sees [4, 5], chooses MIN = 4
2. Middle branch: Player sees [0, -10], chooses MIN = -10
3. Right branch: Player sees [-10, 3], chooses MIN = -10
4. AI sees [4, -10, -10], chooses MAX = **4**

So AI picks the left branch!

## Real Code Example

Here's simplified pseudocode:

```python
def minimax(board, is_maximizing):
    # BASE CASE: Check if game is over
    if ai_wins:
        return +10
    if player_wins:
        return -10
    if draw:
        return 0
    
    # RECURSIVE CASE
    if is_maximizing:  # AI's turn
        best_score = -infinity
        
        for each_empty_cell:
            # Try move
            board[cell] = AI_MARK
            
            # Get score recursively
            score = minimax(board, False)  # Now player's turn
            
            # Undo move
            board[cell] = EMPTY
            
            # Keep track of best score
            best_score = max(score, best_score)
        
        return best_score
    
    else:  # Player's turn
        best_score = +infinity
        
        for each_empty_cell:
            # Try move
            board[cell] = PLAYER_MARK
            
            # Get score recursively
            score = minimax(board, True)  # Now AI's turn
            
            # Undo move
            board[cell] = EMPTY
            
            # Keep track of worst score (for AI)
            best_score = min(score, best_score)
        
        return best_score
```

## Alpha-Beta Pruning: Making It Faster

Without optimization, Minimax checks **every possible game state**. For Tic Tac Toe, that's up to **255,168 possible games**!

**Alpha-Beta Pruning** is a clever optimization that **skips branches that won't matter**.

### How Alpha-Beta Works

We keep track of two values:
- **Alpha**: Best score the maximizer (AI) can guarantee so far
- **Beta**: Best score the minimizer (Player) can guarantee so far

**Key Insight**: If we discover a branch is worse than what we already know is available elsewhere, we can **skip** (prune) it!

### Example of Pruning

```
               [AI - MAX, α=-∞, β=+∞]
              /                      \
       [Player - MIN]           [Player - MIN]
        /      \                (not evaluated!)
       3        5
```

1. AI evaluates left branch first
2. Player would choose MIN(3, 5) = 3
3. So AI knows left branch gives 3
4. Now α = 3 (AI can guarantee at least 3)
5. AI starts evaluating right branch...
6. If first child gives 2 (which is < 3)
7. Since it's Player's turn to minimize, and they already found 2
8. Even if other children are better, Player will choose ≤ 2
9. **AI doesn't care!** AI can get 3 from left branch
10. **PRUNE** the rest of right branch!

### Alpha-Beta Code

```python
def minimax(board, depth, is_maximizing, alpha, beta):
    # ... base cases ...
    
    if is_maximizing:
        max_score = -infinity
        for each_move:
            score = minimax(board, depth+1, False, alpha, beta)
            max_score = max(score, max_score)
            alpha = max(alpha, score)
            
            if beta <= alpha:
                break  # Beta cutoff - prune!
        return max_score
    else:
        min_score = +infinity
        for each_move:
            score = minimax(board, depth+1, True, alpha, beta)
            min_score = min(score, min_score)
            beta = min(beta, score)
            
            if beta <= alpha:
                break  # Alpha cutoff - prune!
        return min_score
```

## Why Is This Unbeatable?

The Minimax algorithm is **perfect** because:

1. ✅ It considers **every possible move**
2. ✅ It assumes the opponent plays **perfectly**
3. ✅ It chooses moves that guarantee the **best outcome**
4. ✅ In Tic Tac Toe, this means **AI never loses**

### Possible Outcomes Against Minimax AI:

- 🏆 **AI Wins** - If you make any mistake
- 🤝 **Draw** - If you play perfectly
- ❌ **You Win** - IMPOSSIBLE (if AI is coded correctly)

## Performance

For Tic Tac Toe:
- **State Space**: 5,478 valid game states
- **Game Tree Nodes**: ~255,168 (without pruning)
- **With Alpha-Beta Pruning**: ~50% fewer nodes evaluated
- **Speed**: Instant for Tic Tac Toe

For larger games:
- **Chess**: ~10^120 possible games (minimax impractical - need evaluation function)
- **Checkers**: Solved in 2007 using improved minimax
- **Go**: Too complex for pure minimax (requires deep learning)

## Try It Yourself!

Here's a simple 3-move example to trace:

```
Current board:
X | O | X
---------
O | X |  
---------
  |   | O

X to move (Player)
O to move (AI)
```

**Your task**: Trace the minimax algorithm!

1. What are all possible moves for X?
2. For each move, what would O do?
3. What's the score of each branch?
4. What should X choose?

**Answer**: 
- Move 1: X at (1,2) - O can win at (2,0) or (2,1) → O wins → -10
- Move 2: X at (2,0) - O must play (1,2) → X threatens (2,1) → likely draw → 0
- Move 3: X at (2,1) - O must play (1,2) → X threatens (2,0) → likely draw → 0

X should avoid position (1,2) and choose (2,0) or (2,1)!

## Further Learning

- **Video**: Search "Minimax Algorithm Explained" on YouTube
- **Practice**: Implement minimax for Connect 4
- **Advanced**: Learn about Negamax (cleaner implementation)
- **Expert**: Study Monte Carlo Tree Search (used in AlphaGo)

## Summary

**Minimax** is like playing chess in your head, but perfectly and for all possibilities:
1. 🌳 Build a tree of all possible games
2. 📊 Score the end states
3. 🔙 Work backwards, alternating min/max
4. ✂️ Prune branches that don't matter (Alpha-Beta)
5. 🎯 Choose the best guaranteed move

**That's how the AI becomes unbeatable!** 🤖

---

*This document is part of the Tic Tac Toe with AI project.*
*For code implementation, see `tictactoe.py`*
