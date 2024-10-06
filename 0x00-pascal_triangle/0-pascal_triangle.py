def pascal_triangle(n):
    pascal = [[1]]
    if n <= 0:
        return []
    if n > 1:
        pascal.append([1, 1])

    for i in range(2, n):
        prev_row = pascal[i - 1]
        current_row = [1]


        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        pascal.append(current_row)

    return pascal
