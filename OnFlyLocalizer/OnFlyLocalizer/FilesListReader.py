def read_file(path):
    f = open(path, 'a+')
    f.seek(0)

    files = [line for line in f.readlines()]

    f.close()

    return files