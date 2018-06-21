grid = [['.','.','.','.','.','0','.'],
        ['0','.','.','.','0','.','0'],
        ['.','0','.','0','.','0','.'],
        ['0','0','0','0','0','.','0'],
        ['.','0','.','0','.','0','.'],
        ['0','.','.','.','0','.','0'],
        ['.','.','.','.','.','0','.']]

def character_picture_grid (grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[j][i], end='')
        print()

character_picture_grid(grid)