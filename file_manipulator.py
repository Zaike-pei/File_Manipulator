import sys

def reverse(content):
    with open(sys.argv[3], 'w') as f:
        f.write(content[::-1])
    
def copy(content):
    with open(sys.argv[3], 'w') as f:
        f.write(content)

def duplicate_contents(content):
    with open(sys.argv[2], 'a') as f:
        for x in range(int(sys.argv[3])):   
            f.write(content)

def replace_string(content):
    target = sys.argv[3]
    newstr = sys.argv[4]

    while content.find(target) >= 0:
        content = content.replace(target, newstr)

    with open(sys.argv[2], 'w') as f:
        f.write(content)

def main():
    content = ''
    command = sys.argv[1]

    with open(sys.argv[2], 'r') as f:
        content = f.read()    

    if command == 'reverse':
        reverse(content)
    elif command == 'copy':
        copy(content)
    elif command == 'duplicate-contents':
        duplicate_contents(content)
    elif command == 'replace-string':
        replace_string(content)
    else:
        print("'" + command + "' does not exist.")
        return
        
    
main()


