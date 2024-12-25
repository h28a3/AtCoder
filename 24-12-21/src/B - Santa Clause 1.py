h, w, x, y = map(int, input().split())
s = []
for i in range(h):
    s.append(input())
t = input()
pos = [x - 1, y - 1]
count = 0
for i in range(len(t)):
    if t[i] == "L" and s[pos[0]][pos[1] - 1] == ".":
        pos[1] -= 1
    elif t[i] == "L" and s[pos[0]][pos[1] - 1] == "@":
        s[pos[0]] = s[pos[0]][:pos[1] - 1] + "." + s[pos[0]][pos[1]:]
        pos[1] -= 1
        count += 1
    elif t[i] == "R" and s[pos[0]][pos[1] + 1] == ".":
        pos[1] += 1
    elif t[i] == "R" and s[pos[0]][pos[1] + 1] == "@":
        s[pos[0]] = s[pos[0]][:pos[1] + 1] + "." + s[pos[0]][pos[1] + 2:]
        pos[1] += 1
        count += 1
    elif t[i] == "D" and s[pos[0] + 1][pos[1]] == ".":
        pos[0] += 1
    elif t[i] == "D" and s[pos[0] + 1][pos[1]] == "@":
        s[pos[0] + 1] = s[pos[0] + 1][:pos[1]] + "." + s[pos[0] + 1][pos[1] + 1:]
        pos[0] += 1
        count += 1
    elif t[i] == "U" and s[pos[0] - 1][pos[1]] == ".":
        pos[0] -= 1
    elif t[i] == "U" and s[pos[0] - 1][pos[1]] == "@":
        s[pos[0] - 1] = s[pos[0] - 1][:pos[1]] + "." + s[pos[0] - 1][pos[1] + 1:]
        pos[0] -= 1
        count += 1
print(pos[0] + 1, pos[1] + 1, count)
