import math

class IntegertoRoman:
    __ROMAN_DIGITS_DICT = {
        1: 'I', 2:'II', 3:'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 
        20: 'XX', 30: 'XXX', 40:'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 
        200: '', 300: '', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M'
    }

    __integer_to_convert = 0
    __result = ''

    def __init__(self, input):
        assert input >= 1, '0 and less then 0 is not accepted'
        self.__integer_to_convert = input

    def __get_length(self):
        return len(str(self.__integer_to_convert))

    def __store(self, roman_equivalent):
        self.__result = roman_equivalent + self.__result
    
    def __get_roman_equivalent(self, digit):
        return self.__ROMAN_DIGITS_DICT[digit]

    def convert(self):
        single_decimal = self.__integer_to_convert % 10
        self.__store(self.__get_roman_equivalent(single_decimal))
        if self.__get_length() == 1:
            return

        ten_decimal = self.__integer_to_convert % 100 - single_decimal
        self.__store(self.__get_roman_equivalent(ten_decimal))
        if self.__get_length() == 2:
            return
        
        hundred_decimal = self.__integer_to_convert % 1000 - (ten_decimal + single_decimal)
        self.__store(self.__get_roman_equivalent(hundred_decimal))
        if self.__get_length() == 3:
            return

        thousand_decimal = self.__integer_to_convert - (hundred_decimal + ten_decimal + single_decimal)
        self.__store('M'*int(thousand_decimal/1000))

    def print_result(self):
        print(f'Roman equivalent of {self.__integer_to_convert} is {self.__result}')
