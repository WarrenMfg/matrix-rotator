import sys


# define color
def color(msg, color):
    PRE = '\x1b['
    POST = '\x1b[0m'
    colors = {
        "magenta": '1;35;40m',
        "cyan": '1;36;40m',
        "green": '1;32;40m',
        "red": '1;31;40m'
    }
    print(PRE + colors[color] + msg + POST)


# define function to convert user input string to array
def rowToArray(string, colLength):
    # split comma-separated string
    data = string.split(',')

    # check if enough data is present
    if len(data) != colLength:
        return data

    # clean data
    for i, val in enumerate(data):
        stripped = val.strip()
        if len(stripped) > 0:
            data[i] = int(stripped)
        else:
            data[i] = None

    # return to promptUser function
    return data


# print matrix utility function
def printMatrix(matrix):
    for i, arr in enumerate(matrix):
        print(matrix[i])


# define prompt for user input
def promptUser():
    # welcome user
    color('😎 Welcome to the matrix rotator! 😎', 'cyan')
    color('====================================\n', 'magenta')

    # try to collect input
    try:
        # collect length of matrix columns
        colLength = int(
            input('👉 Enter the number of columns in your matrix (2 or more): '))
        # validate colLength
        if colLength < 2:
            raise ValueError()

        # collect length of matrix rows
        rowLength = int(
            input('👉 Enter the number of rows in your matrix (2 or more): '))
        # validate rowLength
        if rowLength < 2:
            raise ValueError()

        color('\nOk, great! Let\'s fill in the matrix with data!', 'cyan')
        color('==============================================', 'magenta')

        # declare and initialize matrix to empty list
        matrix = []
        # iterate over rowLength to collect data for each row
        for row in range(rowLength):
            data = input(
                f'👉 Enter {colLength} comma-separated integers for row {row + 1}: ')
            # convert string to an array
            data = rowToArray(data, colLength)
            # if data length matches colLength
            if len(data) == colLength:
                # append it to the matrix
                matrix.append(data)
            else:
                # otherwise raise exception
                raise ValueError()

        # print matrix
        color('\nOk, great! Here is your matrix:', 'cyan')
        color('===============================', 'magenta')
        printMatrix(matrix)

        # prompt rotation direction
        direction = int(input(
            '\n👉 Enter 1 for clockwise rotation, or -1 for counterclockwise rotation: '))
        # validate direction
        if direction == 1 or direction == -1:
            # return matrix to main function
            return {"matrix": matrix, "direction": direction}
        else:
            raise ValueError()

    except TypeError:
        # only accept integers greater than zero
        color('Please only enter integers. You\'ll have to start over. 😭', 'red')
        sys.exit(0)
    except ValueError:
        # user did not enter enough data
        color('Illogical value. You\'ll have to start over. 😭', 'red')
        sys.exit(0)


# define rotate matrix
def rotateMatrix(matrix, direction):
    # declare and initialize result (the rotated matrix)
    result = []
    matrixLength = len(matrix)

    # rotate clockwise
    if direction == 1:
        row = matrixLength - 1
        col = 0
        while col < len(matrix[0]):
            newRow = []
            while row >= 0:
                newRow.append(matrix[row][col])
                row -= 1
            result.append(newRow)
            row = matrixLength - 1
            col += 1

    # rotate counterclockwise
    else:
        row = 0
        col = len(matrix[0]) - 1
        while col >= 0:
            newRow = []
            while row < matrixLength:
                newRow.append(matrix[row][col])
                row += 1
            result.append(newRow)
            row = 0
            col -= 1

    # return result
    return result


# define main function
def main(inProd=True, testData={}):
    # collect user data or use test data
    data = promptUser() if inProd else testData
    rotatedTestData = []

    # rotate matrix 90 degrees
    result = rotateMatrix(data["matrix"], data["direction"])
    # print if inProd
    if inProd:
        color('\n✅ Here is your matrix rotated 90 degrees:', 'green')
        printMatrix(result)
    else:
        rotatedTestData.append(result)

    # rotate matrix 180 degrees
    result = rotateMatrix(result, data["direction"])
    # print if inProd
    if inProd:
        color('\n✅ Here is your matrix rotated 180 degrees:', 'green')
        printMatrix(result)
    else:
        rotatedTestData.append(result)

    # rotate matrix 270 degrees
    result = rotateMatrix(result, data["direction"])
    # print if inProd
    if inProd:
        color('\n✅ Here is your matrix rotated 270 degrees:', 'green')
        printMatrix(result)
    else:
        rotatedTestData.append(result)

    # return rotatedTestData for tests
    return rotatedTestData


if __name__ == '__main__':
    # clear console
    print('\033c')
    # invoke main function
    main()
    # print goodbye
    color('\n😎 Y\'all come back now, ya hear?! 😎', 'cyan')
    color('====================================\n', 'magenta')
