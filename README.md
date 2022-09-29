# N-Queens-using-genetic-algorithm

## Description
This program uses the Python3 programming language to implement the N-Queens problem using genetic algorithms.<br>
Once the program has started, differents generations of posible solutions will be generated with their respective fitness. If we find the solution, the vector with the corresponding solution will be printed at the same time with a representative board.<br>
The fitness represent the quality of being suitable to solve this problem. <br>
This code has the following functions:<br>
<li>Random float generator for numbers between 0 and 1</li><br>
<li>Random int generator for numbers between N and M</li><br>
<li>Calculate fitness</li><br>
<li>Roulette wheel metod</li><br>
<li>Reproduce two chromosomes</li><br>
<li>Mute one chromosome</li><br><br>
This code need the following parameters:<br><br>
<li>Seed: Defines the seed number for randomization</li><br>
<li>Size_board: Defines the size of the board (Number of queens)</li><br>
<li>Population: Defines the amount of population</li><br>
<li>Cross_probability: Defines the probability of two chromosomes to reproduce</li><br>
<li>Mutation_probability: Defines the probability of one chromosome to mutate his genes</li><br>
<li>Number_iterations: Defines the number of generations to work</li><br>

## Usage
Yo can found this repository in `https://github.com/crozasc/N-Queens-using-genetic-algorithm`<br>
[Download here](https://github.com/crozasc/N-Queens-using-genetic-algorithm/archive/refs/heads/main.zip) <br>
Clone this repository and in the project folder run the terminal and type the command <br>
`python main.py seed size_board population cross_probability mutation_probability number_iterations`<br>
For example `python main.py 100 9 30 0.95 0.05 100`<br>
This repository was tested with `python@3.10.5`<br>

## Credits

Creator: Cristian Rozas <br>
GitHub: github.com/crozasc
