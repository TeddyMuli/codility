from typing import List

def solution(board: List[List[str]]) -> List[List[str]]:
    rows, cols = len(board), len(board[0])
    to_destroy = set()
    directions = [(-1,-1),(-1,0),(-1,1),
                  (0,-1),         (0,1),
                  (1,-1), (1,0), (1,1)]

    for c in range(cols):
        write_row = rows - 1
        for r in range(rows-1, -1, -1):
            if board[r][c] == "*":
                write_row = r - 1
            elif board[r][c] == "#":
                if write_row != r:
                    board[write_row][c] = "#"
                    board[r][c] = "_"
                write_row -= 1
    for row in board:
        print(row)
    print()

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "*":
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < rows and nc < cols:
                        if board[nr][nc] == "#":
                            to_destroy.add((nr, nc))
    
    for r, c in to_destroy:
        board[r][c] = "_"

    return board

if __name__ == "__main__":
    test = [
        ['-', '-', '-', '#', '-'],
        ['-', '-', '-', '#', '-'],
        ['-', '#', '-', '*', '-'],
        ['-', '#', '#', '-', '-']
    ]

    sol = solution(test)
    for row in sol:
        print(row)
