def get_spaces(string, max_num = 0, operator = ''):
    if string == '-':
        while len(string) <= max_num:
            string += '-'
        # print(string)
        return string
    length = len(string)
    s = []
    length_of_max = len(f'{max_num}')
    while length < length_of_max + 1:
        s.append(' ')
        length += 1
    s = ''.join(s)
    if not operator == '':
        s = operator + s
    else:
        s = ' ' + s
    return s + string


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    upper_line = ''
    down_line = ''
    dashed_line = ''
    result_line = ''
    
    index = -1
    operator = ''
    for item in problems:
        for char in item:
            if not char.isnumeric() and not char == ' ' and not (char == '+' or char == '-'):
                return "Error: Operator must be '+' or '-'."
            if char == '+' or char == '-':
                operator = char
                index = item.index(char)
                num1 = item[:index-1]
                num2 = item[index+2:]
                if not num1.isnumeric() or not num2.isnumeric():
                    return 'Error: Numbers must only contain digits.'
                if len(num1) > 4 or len(num2) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                max_num = max(int(num1), int(num2))
                result = eval(item)
                upper_line += get_spaces(num1, max_num)
                down_line += get_spaces(num2, max_num, operator)
                dashed_line += get_spaces('-', len(f'{max_num}') + 1)

                result_line += get_spaces(f'{result}', f'{max_num}')
                if problems.index(item) < len(problems) - 1:
                    upper_line += '    '
                    down_line += '    '
                    dashed_line += '    '
                    result_line += '    '

    final_str = upper_line + '\n' + down_line + '\n' + dashed_line
    if show_answers == True:
        return  final_str + '\n' + result_line
    else:
        return final_str

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
