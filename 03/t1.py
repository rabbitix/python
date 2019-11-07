while True:
    num = input('enter your number(end for quit): ')
    if num == 'end':
        print('good luck')
        break
    num = int(num)
    if num % 2 == 0:
        print(num , ' is zoje~!')
    else:
        print(num , ' is fard~~!')

