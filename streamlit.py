import streamlit as st
import numpy as np

# Function to check if a number can be placed in a given cell
def is_valid(grid, row, col, num):
    for i in range(3):  # Check row and column
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

# Backtracking function to solve the 3x3 Sudoku
def solve_sudoku(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0:  # Empty cell found
                for num in range(1, 4):  # Try numbers 1 to 3
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):  # Recursively solve
                            return True
                        grid[row][col] = 0  # Backtrack
                return False  # No valid number found
    return True  # Solved

# Streamlit UI
st.title("3x3 Sudoku Solver with Interactive Grid")

# Creating a grid-like input for Sudoku
st.write("### Enter numbers (1-3), use 0 for empty cells:")
grid = np.zeros((3, 3), dtype=int)

# User input grid
for i in range(3):
    cols = []
    for j in range(3):
        cols.append(st.number_input(f"Row {i+1}, Col {j+1}", min_value=0, max_value=3, step=1, key=f"{i}{j}"))
    grid[i] = cols  # Store row input in the grid

# Solve button
if st.button("Solve Sudoku"):
    if solve_sudoku(grid):
        st.write("### Solved Sudoku:")
        st.table(grid)
    else:
        st.error("No solution exists!")
