import math


def data_types():
    integer = 3
    float = 3.3
    string = "String"
    boolean = True

    print(integer)
    print(float)
    print(string)
    print(boolean)


# For string[-1], it always indicates the last character of the string


def string_manipulation():
    test_string = "Python Is Cool!"

    print(test_string[:])
    print(test_string[0:])
    print(test_string[:-1])
    print(test_string[-1:])
    print(test_string[0:-1])
    print(test_string[:3])
    print(test_string[-1])
    print(test_string[1:-1])
    print(test_string)


def escape_sequence():
    test_str = "ESCAPE \"Sequence\""

    print(test_str)


def format_string():
    test_str = "String"
    integer_value = 3

    print(
        f"The fomatted string is: String = {test_str}, Integer Value = {integer_value}")


def string_functions():
    string = "My String"
    test_strip = "   Test Strip"

    print(string.upper())
    print(string.lower())
    print(string.find("S"))
    print(string.replace("S", "_"))
    print(test_strip.rstrip(" "))
    print(test_strip.lstrip(" "))
    print(test_strip.strip(" "))
    print(string.title())
    print("S" not in string)
    print("M" in string)


# j indicates the i for complex number as in 2 + 3i is 2 + 3j in Python


def complex_number():
    complex_number = 1 + 2j
    print(complex_number)


def math_operators():
    x = 5
    x += 3  # Augmented operator +=, or, -=, or, *=, or, /= and others

    print(3 ** 4)  # Exponential Operator
    print(5 / 3)  # Float division
    print(5 // 5)  # Integer Division
    print(9 % 4)  # Modulus Operator
    print(x)


def math_functions():
    x = 3.907
    n = -5

    print(math.ceil(x))
    print(math.floor(x))
    print(round(x))
    print(abs(n))


def type_conversion_and_truth_value():
    x = "3"
    print(f"Sum of x = \"3\" and 1 is: {int(x) + 1}")

    print("")
    print(None)


def main():
    data_types()
    print("-------------------------------------")

    string_manipulation()
    print("-------------------------------------")

    escape_sequence()
    print("-------------------------------------")

    format_string()
    print("-------------------------------------")

    string_functions()
    print("-------------------------------------")

    complex_number()
    print("-------------------------------------")

    math_operators()
    print("-------------------------------------")

    math_functions()
    print("-------------------------------------")

    type_conversion_and_truth_value()
    print("-------------------------------------")


if __name__ == '__main__':
    main()
