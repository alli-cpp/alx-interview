#!/usr/bin/python3

""" returns perimeter of the island in grid for"""



def island_perimeter(grid):
    """ returns the perimeter of island described in grid """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
                        
                        
    return perimeter
