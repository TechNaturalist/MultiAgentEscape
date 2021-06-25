## Nathan Holst
## Max Clark
## Dick Loveland


# Summer 2021 Group 9 Final Project

## Project Summary
This project was created to explore various Multiagent
System fundamentals and create a game to play around
with them.

A thief has stolen gold and must make their way to the
exit. The guards have been notified and are ready to
catch the thief. The reward for the guards is the
remaining gold. The guards know the thief is crafty,
so they will make coalitions to split the gold when
the thief is caught.

## Multiagent Systems Fundamentals Used

### Agents

Guards are automated agents aware of their environment who
use their percepts to catch the thief. Guards negotiate
with the thief and may take a bribe.

Guards will join a coalition at the beginning of the game
depending on their utility. They share the gold at the
end if the thief is caught.

The thief is another automated agent that tries to get to
the exit. The thief will try to negotiate with guards to
bribe them.

The thief wins the game if they reach the exit with gold.

### Bimatrix solver

We have incorporated a bimatrix solver which finds:
- Nash Equilibria
- Mixed solutions

### Coalitions

Guards will join coalitions based on utility. Guards will
only join if the coalition is superaddative. Grand
coalitions are hard to get. 