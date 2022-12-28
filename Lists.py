if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        com = input().split()
        if com[0] == 'insert':
            ls.insert(int(com[1]), int(com[2]))
        elif com[0] == 'print':
            print(ls)
        elif com[0] == 'remove':
            ls.remove(int(com[1]))
        elif com[0] == 'append':
            ls.append(int(com[1]))
        elif com[0] == 'sort':
            ls.sort()
        elif com[0] == 'pop':
            ls.pop()
        else:
            ls.reverse()
