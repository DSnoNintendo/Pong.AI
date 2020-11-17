# PONG.AI

NOTE: Original single player pong game forked from https://github.com/skar91/pong-python. I found this particular repo while searching for games to implement AI for <br />

Changes I made to forked code:
- Recoded from ground up. Implemented object-oriented programming. Necessary for a big project like this where there are many moving parts <br />
- Original game could only be controlled by human input from keyboard. Changed so AI can play. Also, for AI to learn quickly there needs to be multiple instances of pong games running at the same time, so I had to implement that.  <br />
- Removed hardcoding <br />
- Fixed movement glitch and added some extra features like paddle/ball colors, etc. <br />

## How to use:
1. Navigate to directory in terminal
2. ``` pip install -r requirements.txt ```
3. ``` python3 main.py ```
4. Watch as AI learns how to play Pong. I programmed the AI to run 1000 iterations of pong for each generation of genomes, so as currently constructed, AI should master the game by the second generation or sooner

## Settings to mess around with:
⋅⋅* ***pop_size*** (AI/config-feedforward.txt) - This controls how many genomes will play pong for each generation. The lower the number is, the longer it will take for AI to learn

⋅⋅* ***fitness_threshold*** (AI/config-feedforward.txt) - This controls what score a genome will have to reach in order to reach maximum fitness. Fitness scores are controlled in main.py and I seem to have found the sweet spot to make the AI learn as efficiently as possible

⋅⋅* ***SCREEN_WIDTH*** and ***SCREEN_HEIGHT*** (main.py) - Controls size of the window. The wider the window, the harder it is for the paddle to move around. The shorter the window, the shorter the amount of time it takes for the ball to touch the ground

⋅⋅* ***Ball.speed*** and ***Paddle.speed*** (main.py) - Self explanatory. Default speed is set to 6 for the paddle and 5 for the ball. You can set speeds like so:
```python
Paddle(100, 20, SCREEN_WIDTH/2, SCREEN_HEIGHT, color=color, speed=x)
Ball(15, random.randrange(5, SCREEN_WIDTH - 10, 5), color=color, speed=x)
```
⋅⋅* ***GAME_SPEED** (main.py) - Default setting is 6. Raising this will make AI work faster
