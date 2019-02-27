from cell import cell
from slice import slice
from bigChungus import BigPizza


def main():
    sliceList = []
    numSlices = 0

    # input data
    with open('a_example.in', 'r') as f:
        line_one = f.readline().split()
        R = line_one[0]
        C = line_one[1]
        L = line_one[2]
        H = line_one[3]

        BigPizza = [[cell('', False) for j in range(int(C))]
                    for i in range(int(R))]

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

            for j in range(int(C)):
                BigPizza[i][j].ingredient = chararray[j]

    f.closed

    # output data
    with open('a_example.out', 'w') as out:
        out.write(str(numSlices) + '\n')
        s = slice()
        s.start_x=0
        s.start_y=0
        s.end_x=2
        s.end_y=1
        sliceList.append(s)
        for x in sliceList:
            out.write(x.outputSlice()+'\n')
            #print(x.outputSlice())
    out.closed


if __name__ == '__main__':
    main()
