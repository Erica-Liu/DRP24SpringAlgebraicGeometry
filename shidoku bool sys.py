import itertools

# polynomial ring over GF(2) (4x4x4 variables)
R = PolynomialRing(GF(2), 'x', 64)
x = R.gens()

puzzle = [
    [1, 0, 0, 4],
    [0, 0, 1, 0],
    [0, 4, 0, 0],
    [2, 0, 0, 3]
]

equations = []

# Equations given the starting board
for i in range(4):
    for j in range(4):
        if puzzle[i][j] != 0:
            k = puzzle[i][j] - 1  # match index starting at 0
            rang = [0, 1, 2, 3]
            rang.remove(k)
            equations.append(x[i*16 + j*4 + k] - 1)
            for u in rang:
                equations.append(x[i*16 + j*4 + u])

print('Starting Shidoku board:')
for r in range(4):
    for c in range(4):
        val = puzzle[r][c]
        if val == 0:
            print('-', end=' ')
        else:
            print(val, end=' ')
    print()

# Define constraint function for 2 cells in a row, column, or block
def constraints(a, b):
    sum = 0
    for k in range(4):
        sum += x[16*(a // 4) + 4*(a % 4) + k] * x[16*(b // 4) + 4*(b % 4) + k]
    return sum

# Apply constraints to each pair combination for rows, columns, and blocks
for i in range(4):
    row = [i*4 + j for j in range(4)]
    for a, b in itertools.combinations(row, 2):
        equations.append(constraints(a, b))

for j in range(4):
    col = [i*4 + j for i in range(4)]
    for a, b in itertools.combinations(col, 2):
        equations.append(constraints(a, b))

for block_row in range(2):
    for block_col in range(2):
        block = [block_row*8 + block_col*2 + 4*i + j for i in range(2) for j in range(2)]
        for a, b in itertools.combinations(block, 2):
            equations.append(constraints(a, b))

# Each cell contains exactly one number: sum of all booleans is 1 for each cell
for i in range(4):
    for j in range(4):
        cons = sum(x[i*16 + j*4 + k] for k in range(4)) - 1
        equations.append(cons)

# Each num appears exactly once in each row: for every row the sum of all booleans for some value k is 1
for i in range(4):
    for k in range(4):
        cons = sum(x[i*16 + j*4 + k] for j in range(4)) - 1
        equations.append(cons)

# Each num appears exactly once in each column: for every column the sum of all booleans for some value k is 1
for j in range(4):
    for k in range(4):
        cons = sum(x[i*16 + j*4 + k] for i in range(4)) - 1
        equations.append(cons)

# Each num appears exactly once in each 2x2 block: for every block the sum of all booleans for some value k is 1
for row in range(2):
    for col in range(2):
        for k in range(4):
            cons = sum(x[(row*2 + i)*16 + (col*2 + j)*4 + k]
                        for i in range(2) for j in range(2)) - 1
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
bool = [[0 for _ in range(4)] for _ in range(4)]
solution = [[0 for _ in range(4)] for _ in range(4)]
for g in G:
    var = g.variables()[0]
    if g - var == 1:
        index = int(str(var).strip('x'))  # Obtain Index
        i = index // 16
        j = (index % 16) // 4
        k = index % 4
        solution[i][j] = k + 1 # back to counting from 1
        bool[i][j] = g

print('Solved puzzle:')
print('in boolean values = 1:')
for r in range(4):
    for c in range(4):
        print(bool[r][c], end=', ')
    print()
print('in shidoku numbers:')
for r in range(4):
    for c in range(4):
        print(solution[r][c], end=' ')
    print()
print(':)')
    
    
