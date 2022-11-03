def just_do_it(func):
    def wrapper(self, value):
        if type(value) is not str:
            raise TypeError("unsupported operand type(s) for +: 'Int' and 'tuple'")
        match value.lower():
            case 'один' | '1':
                return self.real + 1
            case 'два' | '2':
                return self.real + 2
            case 'три' | '3':
                return self.real + 3
            case 'четыре' | '4':
                return self.real + 4
            case 'пять' | '5':
                return self.real + 5
            case _:
                raise TypeError('справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.')

    return wrapper


class Int(int):
    @just_do_it
    def __add__(self, other):
        return super().__add__(other)


if __name__ == '__main__':
    x = Int(5)
    print(x + '1')
    print(x + '5')  # 10
    print(x + 'один')  # 6
    print(x + 'пять')  # 10
    print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'
