# 1850번 최대공약수
# https://www.acmicpc.net/problem/1850
# 유클리드 호제법(gdc) 이용

def gdc(x, y):
    if y==0:
        return x
    return gdc(y, x%y)

if __name__ == '__main__':
    A,B=map(int,input().split())
    print('1'*gdc(A, B))