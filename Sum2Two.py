def find_all_expressions(target=200):
    def helper(expression, current, prev, index, results):
        if index == len(numbers):
            if current == target:
                results.append(expression)
            return

        num = numbers[index]
        helper(f"{expression}+{num}", current + num, num, index + 1, results)
        helper(f"{expression}-{num}", current - num, -num, index + 1, results)

        if prev >= 0:
            new_num = prev * 10 + num
            helper(expression + str(num), current - prev + new_num, new_num, index + 1, results)
        else:
            new_num = prev * 10 - num
            helper(expression + str(num), current - prev + new_num, new_num, index + 1, results)

    numbers = list(range(9, -1, -1))
    results = []
    helper("9", 9, 9, 1, results)
    return (results)


expressions = find_all_expressions()
print(f"Найдено {len(expressions)} выражений, которые дают 200:")
for expr in expressions:
    print(f"{expr} = 200")
