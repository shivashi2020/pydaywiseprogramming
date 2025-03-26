def sqrootof_number():

    try:
        numb = float(input('Enter a number: '))
        numsqrt = numb ** 0.5
        return numsqrt
    except Exception as e:
        print(f'Errror {e}')



print(sqrootof_number())



