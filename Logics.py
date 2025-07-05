import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat
  
def add_new_2(mat):
    r=0
    c=0
    while(mat[r][c]!=0):
         r=random.randint(0,3)
         c=random.randint(0,3)
    mat[r][c]=2
    return mat

def get_current_state(mat):
    for i in range(0,4):
        for j in range(0,4):
            if mat[i][j]==2048:
                return 'Won'
    #checking for zero
    for i in range(0,4):
        for j in range(0,4):
            if mat[i][j]==0:
                return 'Game is Not Over' 
    #checking for rows 1 to 3 and colummns 1 to 3          
    for i in range(0,3):
        for j in range(0,3):
            if mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]:
                return 'Game is Not Over' 
   # for fourth row
    for j in range(3):
        if mat[3][j]==mat[0][j+1]:
            return 'Game is Not Over'   

    # for fourth coulumn
    for i in range(3):   
        if mat[i][3]==mat[i+1][3]:
            return 'Game is Not Over'         
    return 'Lost'

# def slide_and_merge(row):
#     new_row = [num for num in row if num != 0]
#     i = 0
#     while i < len(new_row) - 1:
#         if new_row[i] == new_row[i + 1]:
#             new_row[i] *= 2
#             new_row[i + 1] = 0
#             i += 2
#         else:
#             i += 1
#     new_row = [num for num in new_row if num != 0]
#     return new_row + [0] * (len(row) - len(new_row))

# def move_left(grid):
#     new_grid = []
#     for row in grid:
#         new_grid.append(slide_and_merge(row))
#     return new_grid

# def move_right(grid):
#     new_grid = []
#     for row in grid:
#         reversed_row = row[::-1]
#         merged = slide_and_merge(reversed_row)
#         new_grid.append(merged[::-1])
#     return new_grid

# def move_up(grid):
#     transposed = [list(row) for row in zip(*grid)]
#     new_transposed = []
#     for row in transposed:
#         new_transposed.append(slide_and_merge(row))
#     new_grid = [list(row) for row in zip(*new_transposed)]
#     return new_grid

# def move_down(grid):
#     transposed = [list(row) for row in zip(*grid)]
#     new_transposed = []
#     for row in transposed:
#         reversed_row = row[::-1]
#         merged = slide_and_merge(reversed_row)
#         new_transposed.append(merged[::-1])
#     new_grid = [list(row) for row in zip(*new_transposed)]
#     return new_grid


def compress(mat):
    changed = False
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([mat[i][4 - j - 1] for j in range(4)])
    return new_mat

def transpose(mat):
    return [[mat[j][i] for j in range(4)] for i in range(4)]

# Movement Logic
def move_left(mat):
    mat, changed1 = compress(mat)
    mat, changed2 = merge(mat)
    mat, changed3 = compress(mat)
    changed = changed1 or changed2 or changed3
    return mat, changed

def move_right(mat):
    mat = reverse(mat)
    mat, changed = move_left(mat)
    mat = reverse(mat)
    return mat, changed

def move_up(mat):
    mat = transpose(mat)
    mat, changed = move_left(mat)
    mat = transpose(mat)
    return mat, changed

def move_down(mat):
    mat = transpose(mat)
    mat = reverse(mat)
    mat, changed = move_left(mat)
    mat = reverse(mat)
    mat = transpose(mat)
    return mat, changed
               
     


   