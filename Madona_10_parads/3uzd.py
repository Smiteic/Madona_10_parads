with open('example.txt', 'r') as file:
    lines = file.readlines()
    for i in range(2, 4):
        print(lines[i].strip())