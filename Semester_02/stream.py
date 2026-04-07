from os import strerror

try:
    stream = open ("/Users/lordcroft/Documents/stream.txt", "r+")
    content = stream.read()
    stream.write("vem quicando, vem sua safada")
    print(content)
    stream.close()

except Exception as exec:
    print("Cannot open the file", exec)

try:
    cnt = 0
    s = open ("/Users/lordcroft/Documents/stream.txt", "r+")
    ch = s.read(1)
    while ch != '':
        print(ch, end="")
        cnt +=1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

    