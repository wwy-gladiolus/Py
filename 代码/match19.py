def identify_race(person):
    match person:
        case {
                'skin': 'white' | 'brown',
                'hair': 'gray' | 'blonde' | 'yellow' | 'red' | 'brown' | 'black',
                'pupil': 'gray' | 'blue' | 'green' | 'red' | 'gold',
                **info}:
            print(info['name'] + ', ' 
                    + str(info['age']) + ' years old, '
                    + 'belongs to the white race.')
        case {
                'skin': 'yellow' | 'white',
                'hair': 'black' | 'brown' | 'red',
                'pupil': 'black' | 'brown',
                **info}:
            print(info['name'] + ', ' 
                    + str(info['age']) + ' years old, '
                    + 'belongs to the yellow race.')
        case {
                'skin': 'black' | 'brown',
                'hair': 'black',
                'pupil': 'black' | 'brown',
                **info}:
            print(info['name'] + ', ' 
                    + str(info['age']) + ' years old, '
                    + 'belongs to the black race.')



