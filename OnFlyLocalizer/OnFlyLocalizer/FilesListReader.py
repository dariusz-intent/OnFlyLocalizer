def read_file(path):
    f = open(path, 'r')

    files = [line for line in f.readlines()]

    f.close()

    return files