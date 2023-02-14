#import <bits/stdc++.h>
using namespace std;

char graph[3072][6144];

void R(int x, int y, int n){

    if(n==3){
        graph[x][y] = '*'; // 제일 위           
        graph[x+1][y-1]= '*'; //               *
        graph[x+1][y+1]= '*'; //              * *
        for(int j = y-2; j <= y +2; j++){ // *****
            graph[x+2][j] = '*';
        }
        return;
    }

    
    R(x,y,n/2); // 위쪽 삼각형
    R(x+n/2,y-n/2,n/2); // 왼쪽 삼각형
    R(x+n/2,y+n/2,n/2); // 오른쪽 삼각형

}


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for(int i = 0 ; i<n; i++){
        for(int j = 0 ; j< 2 * n ; j++){
            graph[i][j] = ' ';
        }
    }

    R(0,n-1,n);


    for(int i = 0 ; i<n; i++){
        for(int j = 0 ; j< 2 * n -1; j++){
            cout << graph[i][j];
        }
        cout << "\n";
    }



}
