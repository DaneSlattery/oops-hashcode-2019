from cell import cell
from slice import slice
from bigChungus import BigPizza


def main():

    # input data
    with open('d_big.in', 'r') as f:
        line_one = f.readline().split()
        R = line_one[0]
        C = line_one[1]
        L = line_one[2]
        H = line_one[3]

        print('Rows: ' + R)
        print('Columns: ' + C)
        print('Min Ingredient: ' + L)
        print('Max Cells: ' + H)
        print(' ')
        #

        # iterate over rows and add to bigPizza
        for i in range(int(R)):
            line = f.readline()
            chararray = list(line.strip('\n'))

            for char in chararray:
                BigPizza.append(cell(char, False))

    f.closed


if __name__ == '__main__':
    main()
