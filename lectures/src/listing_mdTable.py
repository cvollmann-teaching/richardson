def mdTable(**columns):
    """
    prints a dict as markdown table. The keys are used as head
    and the content of the list as body of the table's columns.
    The lists do not need to have identical length.
    """
    headline = "|"
    separator = "|"
    for key in columns.keys():
        headline += key  + "|"
        separator += "-|"
    
    print(headline)
    print(separator)
    n_rows = [len(columns[k]) for k in columns.keys()]

    for row in range(max(n_rows)):
        col_number = 0 # ColumNumber
        for key, value in columns.items():
            if row < n_rows[col_number]:
                print("| " + str(value[row]) + " ", end="")
            else:
                print("| ", end="")
            col_number += 1
        print("|")
