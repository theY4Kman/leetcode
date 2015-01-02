class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        NORTH = 0, -1
        EAST = 1, 0
        SOUTH = 0, 1
        WEST = -1, 0

        xmin, xmax = 0, len(matrix) - 1
        ymin, ymax = 0, len(matrix[0]) - 1

        direction = EAST

        x, y = 0, 0

        spiral = []
        while xmin != xmax or ymin != ymax:
            #XXX######################################################################################
            print (x, y), matrix[y][x]
            #XXX######################################################################################
            spiral.append(matrix[y][x])

            x += direction[0]
            y += direction[1]

            if x == xmax:
                # Northeast corner, turning south
                if y == ymin and direction == EAST:
                    ymin += 1
                    direction = SOUTH

                    #XXX######################################################################################
                    #XXX######################################################################################
                    #XXX######################################################################################
                    print 'Northeast corner, turning south'

                # Southeast corner, turning west
                elif y == ymax and direction == SOUTH:
                    xmax -= 1
                    direction = WEST

                    #XXX######################################################################################
                    #XXX######################################################################################
                    #XXX######################################################################################
                    print 'Southeast corner, turning west'
            elif x == xmin:
                # Southwest corner, turning north
                if y == ymax and direction == WEST:
                    ymax -= 1
                    direction = NORTH

                    #XXX######################################################################################
                    #XXX######################################################################################
                    #XXX######################################################################################
                    print 'Southwest corner, turning north'

                # Northwest corner, turning east
                elif y == ymin and direction == NORTH:
                    xmin += 1
                    direction = EAST
                    #XXX######################################################################################
                    #XXX######################################################################################
                    #XXX######################################################################################
                    print 'Northwest corner, turning east'

        return spiral

    tests = [
        ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5]),

        # ([[ 1,  2,  3,  4],
        #   [ 5,  6,  7,  8],
        #   [ 9, 10, 11, 12],
        #   [13, 14, 15, 16]],
        #     [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
    ]
