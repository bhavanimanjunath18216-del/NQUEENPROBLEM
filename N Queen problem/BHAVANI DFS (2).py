import time
import sys
import tracemalloc

sys.setrecursionlimit(10000)


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def dfs(n):
    board = [-1] * n
    solutions = 0

    def solve(row):
        nonlocal solutions

        if row == n:
            solutions += 1
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solve(0)
    return solutions


def run(n):
    print(f"\nRunning DFS for N = {n}")

    tracemalloc.start()
    start_time = time.time()

    status = "Completed"

    try:
        result = dfs(n)

    except Exception as e:
        result = 0
        status = f"Error: {str(e)}"

    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("Solutions:", result)
    print("Time (sec):", round(end_time - start_time, 4))
    print("Memory (KB):", round(peak / 1024, 2))
    print("Status:", status)


# REQUIRED VALUES
test_values = [10, 30, 50, 100, 200, 500]

for n in test_values:
    run(n)