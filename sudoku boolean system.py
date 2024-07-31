import itertools

# polynomial ring over GF(2) (9x9x9 variables)
R = PolynomialRing(GF(2), 'x', 729)
x = R.gens()

# input puzzle
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

equations = []

# equations given starting board
for i in range(9):
    for j in range(9):
        if puzzle[i][j] != 0:
            rang = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            k = puzzle[i][j] - 1                           # index to start at 0
            rang.remove(k)
            equations.append(x[i*81 + j*9 + k] - 1)
            for u in rang:
                equations.append(x[i*81 + j*9 + u])

print('Starting Sudoku board:')
for r in range(9):
    for c in range(9):
        val = puzzle[r][c]
        if val == 0:
            print('-', end=' ')
        else:
            print(val, end=' ')
    print()

# Define constraint function for 2 cells in a row, column, or block
def constraints(a, b):
    sum = 0
    # for each value of k (range 9): Product of two booleans should always = 0 for every pair 
    for k in range(9):
        sum += x[81*(a // 9) + 9*(a % 9) + k] * x[81*(b // 9) + 9*(b % 9) + k]
    return sum

# Apply pair constraints to each pair combination for rows, columns, and blocks
for i in range(9):
    row = [i*9 + j for j in range(9)]
    for a, b in itertools.combinations(row, 2):
        equations.append(constraints(a, b))

for j in range(9):
    col = [i*9 + j for i in range(9)]
    for a, b in itertools.combinations(col, 2):
        equations.append(constraints(a, b))

for block_row in range(3):
    for block_col in range(3):
        block = [block_row*27 + block_col*3 + 9*i + j for i in range(3) for j in range(3)]
        for a, b in itertools.combinations(block, 2):
            equations.append(constraints(a, b))

# Each cell contains exactly one number: sum of all booleans is 1 for each cell
for i in range(9):
    for j in range(9):
        cons = sum(x[i*81 + j*9 + k] for k in range(9)) - 1
        equations.append(cons)

# Each num appears exactly once in each row: for every row the sum of all booleans for some value k is 1
for i in range(9):
    for k in range(9):
        cons = sum(x[i*81 + j*9 + k] for j in range(9)) - 1
        equations.append(cons)

# Each num appears exactly once in each column: for every column the sum of all booleans for some value k is 1
for j in range(9):
    for k in range(9):
        cons = sum(x[i*81 + j*9 + k] for i in range(9)) - 1
        equations.append(cons)

# Each num appears exactly once in each 3x3 block: for every block the sum of all booleans for some value k is 1
for row in range(3):
    for col in range(3):
        for k in range(9):
            cons = sum(x[(block_row*3 + i)*81 + (block_col*3 + j)*9 + k]
                        for i in range(3) for j in range(3)) - 1
            equations.append(cons)

X= Set(equations)
print('Number of generators: ' + str(X.cardinality()))
# Solve for Ideal and Grobner basis
I = R.ideal(list(equations))
print('Ideal Generation Complete.')
G = I.groebner_basis()
print("Grobner Basis Computed:", end='')
print(G)

# Determine solution
bool = [[0 for _ in range(9)] for _ in range(9)]
solution = [[0 for _ in range(9)] for _ in range(9)]
for g in G:
    var = g.variables()[0]
    if g - var == 1:
        index = int(str(var).strip('x'))  # Obtain Index
        i = index // 81
        j = (index % 81) // 9
        k = index % 9
        solution[i][j] = k + 1 # back to counting from 1
        bool[i][j] = g

print('Solved Sudoku puzzle:')
print('in boolean values = 1:')
for r in range(9):
    for c in range(9):
        print(bool[r][c], end=', ')
    print()
print('in sudoku numbers:')
for r in range(9):
    for c in range(9):
        print(solution[r][c], end=' ')
    print()
print(':)')
    