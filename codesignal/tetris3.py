def simulate_drops(n, m, figures):
    # shape definitions (1 => occupied)
    shapes = {
        'A': [[1]],
        'B': [[1,1,1,1]],
        'C': [[1,1],
              [1,1]],
        'D': [[1,0],
              [1,1],
              [1,0]],
        'E': [[0,1,0],
              [1,1,1]]
    }

    # grid (rows 0..n-1, cols 0..m-1)
    grid = [[0]*m for _ in range(n)]

    def fits_at(r, c, shape):
        h = len(shape); w = len(shape[0])
        if r + h > n or c < 0 or c + w > m:
            return False
        for i in range(h):
            for j in range(w):
                if shape[i][j] and grid[r+i][c+j]:
                    return False
        return True

    for idx, ch in enumerate(figures):
        if ch not in shapes:
            raise ValueError(f"Unknown figure {ch}")
        shape = shapes[ch]
        h = len(shape); w = len(shape[0])
        start_col = (m - w)//2

        # if initial placement already overlaps, fail
        if not fits_at(0, start_col, shape):
            raise ValueError(f"Figure {ch} (index {idx}) cannot be placed at top")

        # drop: find largest r such that fits_at(r, start_col, shape) but r+1 doesn't
        r = 0
        while True:
            if fits_at(r+1, start_col, shape):
                r += 1
                if r + h > n:  # safety
                    break
            else:
                break

        # place with value = 1-based index
        val = idx + 1
        for i in range(h):
            for j in range(w):
                if shape[i][j]:
                    grid[r+i][start_col+j] = val

    return grid

# Example
if __name__ == "__main__":
    n, m = 6, 9
    figures = ['A','B','C','D','E']
    final = simulate_drops(n, m, figures)
    for row in final:
        print(row)
