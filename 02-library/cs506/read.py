def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file = open(csv_file_path,"r")
    X = []
    for i in file.readlines():
        cur = i.strip('\n').split(',')
        for j in range(len(cur)):
            if not_numeric(cur[j]):
                cur[j] = cur[j].strip('\"')
            elif cur[j] == '':
                cur[j] = float('nan')
            else:
                cur[j] = float(cur[j])
        X.append(cur)
    file.close()
    return X

def not_numeric(s):
    for c in s:
        if c.isalpha() and c != '.':
            return True
    return False
