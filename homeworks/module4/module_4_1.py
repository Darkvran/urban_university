from fake_math import divide as fake_divide
from true_math import divide as true_divide

def main():
    print(fake_divide(10, 2))
    print(true_divide(121, 11))
    print(fake_divide(10, 0))
    print(true_divide(123, 0))

if __name__ == '__main__':
    main()