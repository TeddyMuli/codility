def draw_figures_on_grid(n, m, figures):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    
    # Define figure shapes (relative positions from top-left corner)
    figure_shapes = {
        'A': [(0, 0)],  # Single cell
        'B': [(0, 0), (0, 1), (0, 2), (0, 3)],  # Horizontal line (1x4)
        'C': [(0, 0), (0, 1), (1, 0), (1, 1)],  # 2x2 square
        'D': [(0, 1), (1, 0), (1, 1), (1, 2)],  # T-piece
        'E': [(0, 0), (1, 0), (2, 0), (2, 1)]   # L-piece
    }
    
    # Define positions for each figure (row, col for top-left corner)
    figure_positions = {
        'A': (1, 1),   # Position based on the image
        'B': (3, 2),   # Horizontal rectangle
        'C': (5, 1),   # 2x2 square
        'D': (1, 6),   # T-piece (purple)
        'E': (4, 6)    # L-piece (purple)
    }
    
    # Draw each figure
    for i, figure_type in enumerate(figures, 1):
        if figure_type in figure_shapes and figure_type in figure_positions:
            start_row, start_col = figure_positions[figure_type]
            shape = figure_shapes[figure_type]
            
            # Draw the figure
            for dr, dc in shape:
                r, c = start_row + dr, start_col + dc
                if 0 <= r < n and 0 <= c < m:
                    grid[r][c] = 1  # Use 1-based indexing for figures
    
    return grid

def print_grid(grid):
    """Print the grid in a readable format"""
    for row in grid:
        print('[' + ', '.join(f'{cell:2d}' for cell in row) + ']')

# Example usage based on the image
def main():
    # Create a grid (adjust size based on your needs)
    n, m = 8, 10  # 8 rows, 10 columns
    
    # List of figures to draw (based on the image)
    figures = ['A', 'B', 'C', 'D', 'E', 'T', 'L']
    
    # Create and draw the grid
    result_grid = draw_figures_on_grid(n, m, figures)
    
    # Print the result
    print("Grid with figures drawn:")
    print_grid(result_grid)
    
    # Also return as the format shown in the example
    print("\nAs nested list format:")
    for row in result_grid:
        print(row)

if __name__ == "__main__":
    main()

# Alternative: More flexible version that takes figure definitions as input
def draw_custom_figures(n, m, figure_definitions):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    
    for figure_id, positions in figure_definitions:
        for r, c in positions:
            if 0 <= r < n and 0 <= c < m:
                grid[r][c] = figure_id
    
    return grid

# Example of how to use the custom version
def example_custom():
    print("\n" + "="*50)
    print("Custom figure example:")
    
    # Define figures with their exact positions
    custom_figures = [
        (1, [(1, 1)]),  # Figure A at position (1,1)
        (2, [(3, 2), (3, 3), (3, 4), (3, 5)]),  # Figure B - horizontal line
        (3, [(5, 1), (5, 2), (6, 1), (6, 2)]),  # Figure C - 2x2 square
        (4, [(2, 5)]),  # Figure D
        (5, [(5, 5)]),  # Figure E
    ]
    
    grid = draw_custom_figures(8, 10, custom_figures)
    print_grid(grid)