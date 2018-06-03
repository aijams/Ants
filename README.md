![Stylized picture of an ant][ant-img]
# Ants
### Ants is a simple ant colony simulation. It is not intended to be scientifically
### accurate, but merely a test of complex swarm behavior.

## How it works
Each ant is a simple automaton that can move around, sense the local pheromone and
food levels and make crude probabilistic decisions.

## The ant AI
Each ant stores an ai state consisting of a set of components specified by the common
ai program, whcih each ant follows. Different ants can be created with
different ai states and can ehxibit different behavior depending on ant type as well
as being able to switch behavior on environmental conditions.

### The ant program
The common program is a table that maps from (ai state, local environment) -> (ant action. probability).
When an ant recieves an ai event, it looks up relevant data in its ai state and its
environment, then looks for a corresponding entry in the program table. If one exists, it
executes the corresponding action, otherwise the ant will search up the table until it reaches
a looser match or it reaches a default behavior.

[ant-img]: https://github.com/aijams/Ants/blob/master/img/ant_img.png
