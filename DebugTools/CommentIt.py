fname = input("Enter a file to be commented\n\t>")
symbol = input("Enter the comment symbol\n\t>")
try:
    f = open(fname)
    print("file found!")
    print("commenting file")

    # read file into program
    lineList = [line.rstrip('\n') for line in f]
    f.close()

    # write data into file now with comments
    output = open(fname, "w+")
    for line in lineList:
        output.write("{} {}\n".format(symbol, line))
    output.close()

    print("commenting completed!")

except FileNotFoundError:
    print('File does not exist')
