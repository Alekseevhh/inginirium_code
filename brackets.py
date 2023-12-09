def check_string_brackets(input_string):
    open = 0
    close = 0
    for s in input_string:
        if '(' == s:
            open += 1
        if ')' == s:
            close += 1
    if open == close:
        print('YES')
    else:
        print('no')

check_string_brackets('()')