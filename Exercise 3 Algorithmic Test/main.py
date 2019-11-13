from IntegertoRoman import IntegertoRoman

if __name__ == '__main__':
    input = int(input())
    instance = IntegertoRoman(input)
    instance.convert()
    instance.print_result()
