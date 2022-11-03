def iss(arg_1: int, arg_2):
    if arg_1 is arg_2 and arg_1 == arg_2:
        print('Две переменные ссылаются на один и тот же адрес в памяти, имеют одинаковые значения.')
    elif arg_1 is not arg_2 and arg_1 == arg_2:
        print('Две переменные ссылаются на разные адреса в памяти, имеют одинаковые значения.')
    else:
        print('Две переменные ссылаются на разные адреса в памяти, имеют разные значения.')
    print(f'id первой переменной: {id(arg_1)}')
    print(f'id второй переменной: {id(arg_2)}')
    print(f'Значение первой переменной: {arg_1}')
    print(f'Значение второй переменной: {arg_2}')


if __name__ == '__main__':
    x = y = [1, [2]]
    iss(x, y)

    x, y = [1, [2]], [1, [2]]
    iss(x, y)

    x = [1, [2]]
    y = x.copy()
    y[1] = 2
    iss(x, y)

    A = 'spam'
    B = A
    B = 'shrubbery'
    iss(A, B)

    A = ['spam']
    B = A
    B[0] = 'shrubbery'
    iss(A, B)

    A = ['spam']
    B = A[:]
    B[0] = 'shrubbery'
    iss(A, B)

    iss([], [])
    iss('', '')
    iss({}, {})

    x = y = [1, True, [1, 2]]
    y[2] = [-1, -2]
    iss(x, y)

    x = 5
    y = 5
    iss(x, y)
