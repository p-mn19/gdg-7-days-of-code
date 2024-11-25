def set_matrix_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0
if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the matrix row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)
    set_matrix_zeroes(matrix)
    print("Modified matrix:")
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()
