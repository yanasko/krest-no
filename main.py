print("добро пожаловать в игру 'Крестики-нолики'")
def osnova():
    print("Игрок 1, выберите сторону(x или 0)")
    x=input()

    N=4
    M=4
    matrix = [
        [' ', '1', '2', '3'],
        ['1', '-', '-', '-'],
        ['2', '-', '-', '-'],
        ['3', '-', '-', '-'],
    ]
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end=" ")
        print()  # перенос на новую строку


    def dlja_oschibki_X(i, j):
        while i==0 or 3<i or j==0 or 3<j or  matrix[i][j] =='x' or matrix[i][j] =='0':
            print('Ошибка! Введите еще раз...')
            print("Игрок X делайте свой ход!")
            i = int(input())
            j = int(input())
            if 1<=i<=3 and 1<=j<=3:
                if matrix[i][j] == '-':
                    matrix[i][j] = 'x'
                    break
        return' '

    def povtor():
        print("Хотите ли продолжить?(нажмите 1, если да/ 0, если нет)")
        t = int(input())
        if t == 1:
            print(osnova())
        else:
            print("До новых встреч!")

    def wibor_X(i, j):
        print("Игрок x делайте свой ход!")
        i=int(input())
        j=int(input())
        if 1 <= i <= 3 and 1 <= j <= 3:
            if matrix[i][j] =='x' or matrix[i][j] =='0':
                print(dlja_oschibki_X(i, j))
            else:
                matrix[i][j] = 'x'

        else:
            print(dlja_oschibki_X(i, j))

        for i in range(N):
            for j in range(M):
                print(matrix[i][j], end=" ")
            print()  # перенос на новую строку
        return' '
    def dlja_oschibki_0(i, j):
        while i==0 or 3<i or j==0 or 3<j or matrix[i][j] =='x' or matrix[i][j] =='0':
            print('Ошибка! Введите еще раз...')
            print("Игрок 0 делайте свой ход!")
            i = int(input())
            j = int(input())
            if 1<=i<=3 and 1<=j<=3:
                if matrix[i][j] == '-':
                    matrix[i][j] = '0'
                    break
        return' '
    def wibor_0(i, j):
        print("Игрок 0 делайте свой ход!")
        i=int(input())
        j=int(input())
        if 1 <= i <= 3 and 1 <= j <= 3:
            if matrix[i][j] =='x' or matrix[i][j] =='0':
                print(dlja_oschibki_0(i, j))
            else:
                matrix[i][j] = '0'

        else:
            print(dlja_oschibki_0(i, j))

        for i in range(N):
            for j in range(M):
                print(matrix[i][j], end=" ")
            print()  # перенос на новую строку
        return ' '



    def wiig_comb(i, j):
        if  matrix[1][1]=='0' and matrix[1][2]=='0' and matrix[1][3]=='0':
            print("выиграл игрок 0")
            print(povtor())
        elif matrix[1][1] == '0' and matrix[2][1] == '0' and matrix[3][1] == '0':
            print("выиграл игрок 0")
            print(povtor())
        elif  matrix[2][1]=='0' and matrix[2][2]=='0' and matrix[2][3]=='0':
            print("выиграл игрок 0")
            print(povtor())
        elif  matrix[3][1]=='0' and matrix[3][2]=='0' and matrix[3][3]=='0':
            print("выиграл игрок 0")
            print(povtor())
        elif  matrix[1][2]=='0' and matrix[2][2]=='0' and matrix[3][2]=='0':
            print("выиграл игрок 0")
            print(povtor())
        elif  matrix[1][3]=='0' and matrix[2][3]=='0' and matrix[3][3]=='0':
            print("выиграл игрок 0")
            print(povtor())
        elif  matrix[1][1]=='0' and matrix[2][2]=='0' and matrix[3][3]=='0':
            print("выиграл игрок 0")
            print(povtor())
        elif  matrix[3][1]=='0' and matrix[2][2]=='0' and matrix[1][3]=='0':
            print("выиграл игрок 0")
            print(povtor())

        elif  matrix[1][1]=='x' and matrix[1][2]=='x' and matrix[1][3]=='x':
            print("выиграл игрок x")
            print(povtor())
        elif  matrix[1][1]=='x' and matrix[2][1]=='x' and matrix[3][1]=='x':
            print("выиграл игрок x")
            print(povtor())
        elif  matrix[2][1]=='x' and matrix[2][2]=='x' and matrix[2][3]=='x':
            print("выиграл игрок x")
            print(povtor())
        elif  matrix[3][1]=='x' and matrix[3][2]=='x' and matrix[3][3]=='x':
            print("выиграл игрок x")
            print(povtor())
        elif  matrix[1][2]=='x' and matrix[2][2]=='x' and matrix[3][2]=='x':
            print("выиграл игрок x")
            print(povtor())
        elif  matrix[1][3]=='x' and matrix[2][3]=='x' and matrix[3][3]=='x':
            print("выиграл игрок x")
            print(povtor())
        elif  matrix[1][1]=='x' and matrix[2][2]=='x' and matrix[3][3]=='x':
            print("выиграл игрок x")
            print(povtor())
        elif  matrix[3][1]=='x' and matrix[2][2]=='x' and matrix[1][3]=='x':
            print("выиграл игрок x")
            print(povtor())
        else:
            print("ничья")
            print(povtor())
    if x =='0':
        print("Прекрасно!Тогда игрок 2 будет - x")
        while True:
            if not((matrix[1][1]=='0' and matrix[1][2]=='0' and matrix[1][3]=='0' or matrix[2][1]=='0' and matrix[2][2]=='0' and matrix[2][3]=='0' or matrix[3][1]=='0' and matrix[3][2]=='0' and matrix[3][3]=='0' or matrix[1][1]=='0' and matrix[2][1]=='0' and matrix[3][1]=='0' or matrix[1][2]=='0' and matrix[2][2]=='0' and matrix[3][2]=='0' or matrix[1][3]=='0' and matrix[2][3]=='0' and matrix[3][3]=='0' or matrix[1][1]=='0' and matrix[2][2]=='0' and matrix[3][3]=='0' or matrix[3][1]=='0' and matrix[2][2]=='0' and matrix[1][3]=='0') or (matrix[1][1]=='x' and matrix[1][2]=='x' and matrix[1][3]=='x' or matrix[2][1]=='x' and matrix[2][2]=='x' and matrix[2][3]=='x' or matrix[3][1]=='x' and matrix[3][2]=='x' and matrix[3][3]=='x' or matrix[1][1]=='x' and matrix[2][1]=='x' and matrix[3][1]=='x' or matrix[1][2]=='x' and matrix[2][2]=='x' and matrix[3][2]=='x' or matrix[1][3]=='x' and matrix[2][3]=='x' and matrix[3][3]=='x' or matrix[1][1]=='x' and matrix[2][2]=='x' and matrix[3][3]=='x' or matrix[3][1]=='x' and matrix[2][2]=='x' and matrix[1][3]=='x')):

                print(wibor_0(i, j))
                if matrix[1][1] == '-'  or matrix[1][2] == '-' or matrix[1][3] == '-' or matrix[2][1] == '-' or matrix[2][2] == '-' or matrix[2][3] == '-' or matrix[3][1] == '-' or matrix[3][2]== '-' or matrix[3][3] == '-':
                    if  not((matrix[1][1]=='0' and matrix[1][2]=='0' and matrix[1][3]=='0' or matrix[2][1]=='0' and matrix[2][2]=='0' and matrix[2][3]=='0' or matrix[3][1]=='0' and matrix[3][2]=='0' and matrix[3][3]=='0' or matrix[1][1]=='0' and matrix[2][1]=='0' and matrix[3][1]=='0' or matrix[1][2]=='0' and matrix[2][2]=='0' and matrix[3][2]=='0' or matrix[1][3]=='0' and matrix[2][3]=='0' and matrix[3][3]=='0' or matrix[1][1]=='0' and matrix[2][2]=='0' and matrix[3][3]=='0' or matrix[3][1]=='0' and matrix[2][2]=='0' and matrix[1][3]=='0') or (matrix[1][1]=='x' and matrix[1][2]=='x' and matrix[1][3]=='x' or matrix[2][1]=='x' and matrix[2][2]=='x' and matrix[2][3]=='x' or matrix[3][1]=='x' and matrix[3][2]=='x' and matrix[3][3]=='x' or matrix[1][1]=='x' and matrix[2][1]=='x' and matrix[3][1]=='x' or matrix[1][2]=='x' and matrix[2][2]=='x' and matrix[3][2]=='x' or matrix[1][3]=='x' and matrix[2][3]=='x' and matrix[3][3]=='x' or matrix[1][1]=='x' and matrix[2][2]=='x' and matrix[3][3]=='x' or matrix[3][1]=='x' and matrix[2][2]=='x' and matrix[1][3]=='x')):

                        print(wibor_X(i, j))

                else:
                    print(wiig_comb(i, j))
                    break

            else:
                print(wiig_comb(i, j))
                break

    else:
        print("Прекрасно!Тогда игрок 2 будет", 0)
        while True:
            if not((matrix[1][1]=='0' and matrix[1][2]=='0' and matrix[1][3]=='0' or matrix[2][1]=='0' and matrix[2][2]=='0' and matrix[2][3]=='0' or matrix[3][1]=='0' and matrix[3][2]=='0' and matrix[3][3]=='0' or matrix[1][1]=='0' and matrix[2][1]=='0' and matrix[3][1]=='0' or matrix[1][2]=='0' and matrix[2][2]=='0' and matrix[3][2]=='0' or matrix[1][3]=='0' and matrix[2][3]=='0' and matrix[3][3]=='0' or matrix[1][1]=='0' and matrix[2][2]=='0' and matrix[3][3]=='0' or matrix[3][1]=='0' and matrix[2][2]=='0' and matrix[1][3]=='0') or (matrix[1][1]=='x' and matrix[1][2]=='x' and matrix[1][3]=='x' or matrix[2][1]=='x' and matrix[2][2]=='x' and matrix[2][3]=='x' or matrix[3][1]=='x' and matrix[3][2]=='x' and matrix[3][3]=='x' or matrix[1][1]=='x' and matrix[2][1]=='x' and matrix[3][1]=='x' or matrix[1][2]=='x' and matrix[2][2]=='x' and matrix[3][2]=='x' or matrix[1][3]=='x' and matrix[2][3]=='x' and matrix[3][3]=='x' or matrix[1][1]=='x' and matrix[2][2]=='x' and matrix[3][3]=='x' or matrix[3][1]=='x' and matrix[2][2]=='x' and matrix[1][3]=='x')):

                print(wibor_X(i, j))
                if matrix[1][1] == '-' or matrix[1][2] == '-' or matrix[1][3] == '-' or matrix[2][1] == '-' or matrix[2][2] == '-'or  matrix[2][3] == '-' or matrix[3][1] == '-' or matrix[3][2] == '-'or  matrix[3][3] == '-':
                    if not((matrix[1][1]=='0' and matrix[1][2]=='0' and matrix[1][3]=='0' or matrix[2][1]=='0' and matrix[2][2]=='0' and matrix[2][3]=='0' or matrix[3][1]=='0' and matrix[3][2]=='0' and matrix[3][3]=='0' or matrix[1][1]=='0' and matrix[2][1]=='0' and matrix[3][1]=='0' or matrix[1][2]=='0' and matrix[2][2]=='0' and matrix[3][2]=='0' or matrix[1][3]=='0' and matrix[2][3]=='0' and matrix[3][3]=='0' or matrix[1][1]=='0' and matrix[2][2]=='0' and matrix[3][3]=='0' or matrix[3][1]=='0' and matrix[2][2]=='0' and matrix[1][3]=='0') or (matrix[1][1]=='x' and matrix[1][2]=='x' and matrix[1][3]=='x' or matrix[2][1]=='x' and matrix[2][2]=='x' and matrix[2][3]=='x' or matrix[3][1]=='x' and matrix[3][2]=='x' and matrix[3][3]=='x' or matrix[1][1]=='x' and matrix[2][1]=='x' and matrix[3][1]=='x' or matrix[1][2]=='x' and matrix[2][2]=='x' and matrix[3][2]=='x' or matrix[1][3]=='x' and matrix[2][3]=='x' and matrix[3][3]=='x' or matrix[1][1]=='x' and matrix[2][2]=='x' and matrix[3][3]=='x' or matrix[3][1]=='x' and matrix[2][2]=='x' and matrix[1][3]=='x')):

                     print(wibor_0(i, j))

                else:
                    print(wiig_comb(i, j))

            else:
                print(wiig_comb(i, j))
                break
    return' '
print(osnova())
