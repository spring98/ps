
def main():
    ref = input()

    ascending_ref = ['1', '2', '3', '4', '5', '6', '7', '8']
    descending_ref = ['8', '7', '6', '5', '4', '3', '2', '1']

    ref = ref.split(' ')

    if ref == ascending_ref:
        print('ascending')
    elif ref == descending_ref:
        print('descending')
    else:
        print('mixed')


if __name__ == '__main__':
    main()

