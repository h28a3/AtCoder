s = input()
a = []
for i in range(len(s)):
    a.append(ord(s[i]))
for i in range(97, 123):
    if not(i in a):
        print(chr(i))
        exit()
