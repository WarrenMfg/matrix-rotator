from matrix_rotator import main


# define assertion function
def assertEqual(number, case, expected, actual):
    for i, matrix in enumerate(expected):
        rotation = 90
        if i == 1:
            rotation = 180
        elif i == 2:
            rotation = 270
        for j, row in enumerate(matrix):
            if expected[i][j] != actual[i][j]:
                print(f'\n🚨 {number}. {case}')
                print(f'at a rotation of {rotation} degrees')
                print(f'expected {expected[i][j]} but received {actual[i][j]}')
                return
    print(f'\n✅ {number}. {case}')


# clear console
print('\033c')
# announce testing
print(f'TESTING...TESTING...TESTING')


# TEST CASE 1
testData = {
    "matrix": [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    "direction": 1
}
expected = [
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ],
    [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ],
    [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ]
]
actual = main(False, testData)
assertEqual('1', 'it should rotate a square matrix clockwise', expected, actual)


# TEST CASE 2
testData = {
    "matrix": [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    "direction": -1
}
expected = [
    [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ],
    [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ],
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
]
actual = main(False, testData)
assertEqual(
    '2', 'it should rotate a square matrix counterclockwise', expected, actual)


# TEST CASE 3
testData = {
    "matrix": [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3],
        [4, 4, 4]
    ],
    "direction": 1
}
expected = [
    [
        [4, 3, 2, 1],
        [4, 3, 2, 1],
        [4, 3, 2, 1]
    ],
    [
        [4, 4, 4],
        [3, 3, 3],
        [2, 2, 2],
        [1, 1, 1]
    ],
    [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]
]
actual = main(False, testData)
assertEqual(
    '3', 'it should rotate a rectangular matrix clockwise', expected, actual)


# TEST CASE 4
testData = {
    "matrix": [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3],
        [4, 4, 4]
    ],
    "direction": -1
}
expected = [
    [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ],
    [
        [4, 4, 4],
        [3, 3, 3],
        [2, 2, 2],
        [1, 1, 1]
    ],
    [
        [4, 3, 2, 1],
        [4, 3, 2, 1],
        [4, 3, 2, 1]
    ]
]
actual = main(False, testData)
assertEqual(
    '4', 'it should rotate a rectangular matrix counterclockwise', expected, actual)


# end with new line
print('')
