def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file = open(csv_file_path,"r")
    X = []
    for i in file.readlines():
        cur = i.split(',')
        for j in range(len(cur)):
            if cur[j] == '?':
                cur[j] = float('nan')
            else:
                cur[j] = float(cur[j])
        X.append(cur)
    return X
