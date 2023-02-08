#import <bits/stdc++.h>
using namespace std;

int n;
int paper[2187][2187];
int answer[3];


bool check(int start, int end, int size){
    int color = paper[start][end];
    for(int i = start ; i < start+size ; i ++){
        for(int j = end; j < end+size ; j ++){
            if(paper[i][j]!=color){
                return false;
            }
        }
    }
    return true;
}

void div_paper(int x, int y, int len){

    if(check(x,y,len)){
        answer[paper[x][y]]++;
        return;
    }

    int div_len = len / 3;
    for(int i = 0 ; i <3;i++){
        for(int j = 0 ; j <3; j++){
            div_paper(x + i * div_len,y + j * div_len ,div_len);
        }
    }


}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for(int i = 0 ; i < n; i++){
        for(int j = 0 ; j < n; j++){
            cin >> paper[i][j];
            paper[i][j]++;
        }
    }
    div_paper(0,0,n);

    for(auto x : answer){
        cout << x << "\n";
    }








}