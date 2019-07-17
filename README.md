# Monty Hall Simulator

This Python script generates games according to the Monty Hall problem
(see [Wikipedia's article describing the problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)). I implemented the "standard" version of the game, where all doors except two are revealed after the initial choice of the player, then the player has the possibility to change his mind, no matter if he was correct or not.

This thought experiment is sometimes described as a paradox: the real solution can seem counterintuitive at first.

After doors are revealed, the winning strategy is to switch doors - with a 3 doors problem, this gives you a 2/3 chance of winning, vs 1/3 otherwise.

This script allows you to see this fact by yourself!

To use it, you can launch the script with 3 arguments:
- First argument: the number of games you want to simulate
- Second argument: if you want the player to switch doors or not after having some doors revealed. Should be True for the switching strategy, False if the player does not change his mind.
- Third argument: the number of doors. Should be 3 for the classic game.

The command line:
```
python3 simulation.py 10000 True 3
```
Will launch 10000 games where the player will switch when offered the opportunity, with the classic 3 doors problem. (And returns 0.667, as it should be :) )
