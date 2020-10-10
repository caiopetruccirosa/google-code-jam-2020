cases_count = int(input())
cases = []

for case_index in range(cases_count):
    row_count = int(input())
    matrix = []

    for row_index in range(row_count):
        column = [int(num) for num in input().split(' ')]
        matrix.append(column)

    cases.append(matrix)

for case_index in range(cases_count):
    matrix = cases[case_index]
    transposed_matrix = [list(i) for i in zip(*matrix)]

    trace = 0
    rows_with_repeated = 0
    columns_with_repeated = 0

    row_count = len(matrix)
    for row_index in range(row_count):
        row = matrix[row_index]
        transposed_row = transposed_matrix[row_index]

        column_count = len(row)
        for column_index in range(column_count):
            if row_index == column_index:
                trace += row[column_index]

        if (len(row) - len(set(row))) != 0:
            rows_with_repeated += 1

        if (len(transposed_row) - len(set(transposed_row))) != 0:
            columns_with_repeated += 1

    print("Case #{}: {} {} {}".format(case_index+1, trace, rows_with_repeated, columns_with_repeated))