import sys
set = []
boop = 0
for char in sys.argv[1]:
    if char in set:
        continue
    else:
        set.append(char)
        boop += 1
ping = 0
lamp = lambda x: x.lower() 
string = str(list(map(lamp, set)))
marked = "False"
check = []
with open("records.txt", "r+") as F:
    print("Matching Records...")
    for line in F.readlines():
        for char in line:
            if char in set:
                if char in check:
                    ping += 1
                    continue
                else:
                    check.append(char)
                    ping += 1
            if ping == boop:
                marked = "True"
        ping = 0
    F.write(str(list(map(lamp, set))))
    F.write('\n')
    F.write(sys.argv[1])
    F.write('\n')
    F.write('\n')
print("")
print("")
print("")
print("Marked: " + marked )
print("phrase:"+sys.argv[1])
print("set:"+(str(list(map(lamp, set)))))
print("real")
