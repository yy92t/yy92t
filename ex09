file = None
try:
    file = open("testing.txt","w")  
    file.write("line 1\nline 2\nline 3\n")           
except OSError as ex:
    print(type(ex).__name__, ex.errno, ex, sep=" : ")
finally:
    if file != None:
        file.close()

file = None
try:
    file = open("testing.txt","r")
    # file = open("testing2.txt","r")   # Error for testing later
    print(file.read())           
except OSError as ex:
    print(type(ex).__name__, ex.errno, ex, sep=" : ")
finally:
    if file != None:
        file.close()
print()

file = None
try:
    file = open("testing.txt","r")  
    print(file.read(3))          # only read first 3 characters
except OSError as ex:
    print(type(ex).__name__, ex.errno, ex, sep=" : ")
finally:
    if file != None:
        file.close()
print()

file = None
try:
    file = open("testing.txt","a")  
    file.write("line 4\nline 5\nline 6\n")           
except OSError as ex:
    print(type(ex).__name__, ex.errno, ex, sep=" : ")
finally:
    if file != None:
        file.close()

try:
    with open("testing.txt","r") as f:
        # f.write("aaa")   # Error for testing later
        for line in f.readlines():
            print(line, end="")   # newline is already included in line
except OSError as ex:
    print(type(ex).__name__, ex.errno, ex, sep=" : ")
print("File Closed:",f.closed)
