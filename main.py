
for i in range(10, 12):

    print(f'Iteration {i+1}')

    a = input('Que edad tienes?: ')

    if int(a) < 18:
        a = int(a)
        print('Eres menor de edad')
        while a > 0:
            print(a)
            a -= 1
    else:
        print('Eres mayor de edad')
