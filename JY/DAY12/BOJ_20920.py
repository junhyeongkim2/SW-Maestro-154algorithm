n, m = map(int, input().split())
words = {}
for _ in range(n):
    word = input()
    if len(word) >= m:
        if word in words:
            words[word] +=1
        else:
            words[word] = 1
        
for i in sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0])):
    print(i[0])
