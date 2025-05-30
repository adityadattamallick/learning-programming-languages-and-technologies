"""Python basic boilerplate code is as follows:

def main():
    print("First module name is {}".format(__name__))

if __name__ == '__main__':
    main()
"""

"""The special variable __name__ is set to '__main__' when a Python file is executed directly. 
Nevertheless, the __name__ variable is set to the module's name when a Python file is imported 
as a module into another file. 
__name__ is a variable that exists in every Python module, and is set to the name of the module.
"""


def main():
    print("Hello World!", end="\n")
    print("Hello World!" * 3, end="\n")

    number = 3 + 5
    print(number)


if __name__ == '__main__':
    main()
