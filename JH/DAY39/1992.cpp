#import <bits/stdc++.h>
using namespace std;

int n;
string graph[64];

//전체가 같은수인가 아닌가에 따라서 계속해서 그래프를 4분할, return이 되지 않았다면 마지막 curr값 출력

void printCompResult(int size, int y, int x){
    char curr = graph[y][x];

    for(int i = y; i < y+size; i++ ){
        for(int j = x; j < x+size; j++ ){

            if(graph[i][j]!=curr){
                cout << "(";
                printCompResult(size/2,y,x);
                printCompResult(size/2,y,x+size/2);
                printCompResult(size/2,y+size/2,x);
                printCompResult(size/2,y+size/2,x+size/2);
                cout << ")";
                return;
            }
        }
    }
    cout << curr;
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);


    cin >> n;

    for(int i = 0 ; i < n ; i++){
        cin >> graph[i];
    }

    printCompResult(n,0,0);

    return 0;

}