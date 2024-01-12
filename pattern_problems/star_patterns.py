def print_star1(row):
    for i in range(row, 0, -1):
        spaces = row - i
        for space in range(0, spaces):
            print(' ', end=' ')
        for stars in range(0, i):
            print('*', end=' ')
        print('Hey')


# -----------------------------------------------------------------------


def print_star_triangle(row):
    for i in range(1, row + 1):
        spaces = row - i
        for j in range(0, spaces):
            print(' ', end=' ')
        # stars = row - i + 1
        for j in range(0, i):
            print('*', end=' ')
        rev_stars = i - 1
        for j in range(1, rev_stars + 1):
            print('*', end=' ')
        print()
    for i in range(row - 1, 0, -1):
        spaces = row - i
        for j in range(0, spaces):
            print(' ', end=' ')
        stars = i
        for j in range(0, stars):
            print('*', end=' ')
        rev_stars = i - 1
        for j in range(0, rev_stars):
            print('*', end=' ')
        print()


# -----------------------------------------------------------------------

def print_star_patter(n):
    for i in range(1,n+1):
        for j in range(0, i):
            print('*', end=' ')
        print()
    for row in range(i - 1, 0, -1):
        stars = row
        for j in range(0, stars):
            print('*', end=' ')
        print()




# ------------------------------------------------------------------------

# rows = int(input('Enter No of Rows : '))

print_star_patter(4)