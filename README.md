# COMP 472 - Assignment 3 (Winter 2021)
https://github.com/aramich100/COMP472_A3

<img src="https://fas.concordia.ca/adfs/portal/logo/logo.png?id=728F70A3E333A7E7AB58C4185D855224308D7AA511313D14AFF478183F60D900">
 
 
# Team Members
- Michael Arabian
- Thomas Le
- Andre Saad


# Introduction
In this assignment, we implemented and analyzed the Alpha-Beta pruning algorithm to play a two-player game called
PNT: pick numbered-tokens..

The rules for the PNT game are as followed:
- The game start with n token
- Player take turns removing a token with some conditions
- At the first move, the first player must choose an odd-numbered token that is strictly less than n/2
- The next move the token number that a player can take must be a multiple or factor of the last move
- If a player cannot take a token, he/she loses the game.

# Instructions
  
- Download our GitHub repository as a Zip or use 'Git Clone' to have a copy on your computer. <br />
```
git clone https://github.com/aramich100/COMP472_A3

```
- Make sure to have Python 3.9.2 installed on your computer. If you do not have it, you can install it here : https://www.python.org/downloads/  <br />
- To run the script, type the following commands into the terminal. Make sure you are in the proper directory.

```
py main.py 
```

# Alpha-Beta Pruning
- Ignores (cuts off/prunes) branches of the tree that cannot contribute to the solution
- Reduces branching factor
- allows deeper search with same effort
