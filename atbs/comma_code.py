test_list = ['A', 'B', 'C', 'D', 'E']

def comma_code (arg):
    combined = arg[0]
    for item in arg[1:]:
        combined = combined + ', ' + item
    print(combined)

comma_code(test_list)