def to_arabic(s):
    match s.strip().lower():
        case 'zero':
            print('zero means 0.')
        case 'one':
            print('one means 1.')
        case 'two':
            print('two means 2.')
        case 'three':
            print('three means 3.')
        case 'four':
            print('four means 4.')
        case 'five':
            print('five means 5.')
        case 'six':
            print('six means 6.')
        case 'seven':
            print('seven means 7.')
        case 'eight':
            print('eight means 8.')
        case 'nine':
            print('nine means 9.')
        case s:
            print(s + ' is not a number.')

