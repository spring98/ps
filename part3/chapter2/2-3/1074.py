

def z(x, y, n):
    if n == 0:
        return

    print(f'({x}, {y})')
    z(x, y, n/2)
    z(x, y+n/2, n/2)
    z(x+n/2, y, n/2)
    z(x+n/2, y+n/2, n/2)

z(0, 0, 3)

'''
    접근방법이 비슷했으나 실패
    1씩 더하는 것이 아니라 n/2 만큼 더하는 것이었다.
'''