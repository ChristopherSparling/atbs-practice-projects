table_data = [['A1234','B234','C34','D1'],
              ['E111111','F2323','G1234','H4123412'],
              ['I123','J1231','K12351235','L3443']]
"""
Takes list of lists and outputs in right-justified table where the
first element of each sublist corresponds to the first row, and so 
on
"""
def printTable(table):
    colWidth = [0] * len(table)
    max_len = 0
    num_rows = len(table[0])
    num_cols = len(table)

    # determine padding requirements
    for index, sublist in enumerate(table):
        for item in sublist:
            if len(item) > max_len:
                max_len = len(item)
        colWidth[index] = max_len
        max_len = 0
    
    # Output table
    for i in range(num_rows):
        for j in range(num_cols):
            print(table[j][i].rjust(colWidth[j]), end=' ')
        print()

printTable(table_data)