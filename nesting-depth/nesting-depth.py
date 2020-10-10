cases_count = int(input())

for case_index in range(cases_count):
    s = [int(i) for i in input()]
    ret = []

    depth = 0
    for current in s:
        if (current > depth):
            for i in range(current - depth):
                ret.append('(')
                depth += 1
        elif (current < depth):
            for i in range(depth - current):
                ret.append(')')
                depth -= 1
        
        ret.append(str(current))

    while depth > 0:
        ret.append(')')
        depth -= 1

    print("Case #{}: {}".format(case_index+1, ''.join(ret)))