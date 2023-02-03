"""
bin() : 이진수
hex() : 16진수
oct() : 8진
"""
#1373 2진수 8진수
b = input()
dc = int(b,base=2)
print(format(dc,'o'))