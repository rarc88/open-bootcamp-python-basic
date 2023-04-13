from operations import sum as s
from operations.multiplier import Multiplier

# No se recomienda
from operations import *


def main():
    print(s.sum(2, 5))
    m = Multiplier()
    print(m.multiply(2, 5))

    print(sum.sum(1, 3))


if __name__ == '__main__':
    main()
