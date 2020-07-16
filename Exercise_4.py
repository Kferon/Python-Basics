with open('file3.txt', 'r') as my_f:
    for line in my_f:
        x = line.split()
        print(x)
        if x[0] == 'One':
            out_f = open("out_file.txt", "w")
            out_f.writelines("Odin — 1"'\n')
            out_f.close()
        if x[0] == 'Two':
            out_f = open("out_file.txt", "a")
            out_f.writelines("Dva — 1"'\n')
            out_f.close()
        if x[0] == 'Three':
            out_f = open("out_file.txt", "a")
            out_f.writelines("Tri — 1"'\n')
            out_f.close()
        if x[0] == 'Four':
            out_f = open("out_file.txt", "a")
            out_f.writelines("Chetire — 1"'\n')
            out_f.close()