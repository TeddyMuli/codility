#!/usr/bin/python3
def solution(field, target):
    rows = len(field)
    cols = len(field[0])
    figure_size = len(target)

    for col in range(cols - figure_size + 1):
        row = 0
        while can_fit(field, target, row+1, col):
            row += 1
        
        new_matrix = [r[:] for r in field]
        for i in range(figure_size):
            for j in range(figure_size):
                if target[i][j] == 1:
                    new_matrix[row+i][col+j] = 1

        if any(all(col == 1 for col in row) for row in new_matrix):
            return col

    return -1

def can_fit(field, target, row, column):
    fig_size = len(target)
    if row + fig_size > len(field):
        return False

    for i in range(fig_size):
        for j in range(fig_size):
            if target[i][j] == 1 and field[row + i][column+i] == 1:
                return False
            
    return True

if __name__ == "__main__":
    field = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [1, 1, 0, 1, 0],
             [1, 0, 1, 0, 1]]
    
    figure = [[1, 1, 1],
              [1, 0, 1],
              [1, 0, 1]]

    print(solution(field, figure))