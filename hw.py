def solve_n_queens(n=8, show_boards=True):
    solutions = []
    cols = [0] * n  

    used_cols = set()
    used_diag1 = set()  
    used_diag2 = set()  

    def place(row):
        if row == n:
            solutions.append(cols.copy())
            if show_boards:
                print_board(cols)
            return

        for c in range(n):
            d1 = row - c
            d2 = row + c
            if c in used_cols or d1 in used_diag1 or d2 in used_diag2:
                continue

            cols[row] = c
            used_cols.add(c)
            used_diag1.add(d1)
            used_diag2.add(d2)

            place(row + 1)

            used_cols.remove(c)
            used_diag1.remove(d1)
            used_diag2.remove(d2)

    def print_board(cols):
        n = len(cols)
        for r in range(n):
            row = ['.'] * n
            row[cols[r]] = 'Q'
            print(' '.join(row))
        print()  

    place(0)
    return solutions

if __name__ == "__main__":
    sols = solve_n_queens(8, show_boards=True)
    print(f"Total solutions found: {len(sols)}")
