#import <bits/stdc++.h>
using namespace std;

int board[9][9];
vector<pair<int,int>> points;
int cnt = 0;
bool found = false;


// 빈곳에 1~9 값 할당
// check 함수로 행,열 3x3안에 같은 수 있는지 검사
// 없을 시 n+1 해줌
// n == 빈자리갯수와 같으면 종료
// 최적해를 못찾았을 시 board 0으로 초기화

bool check(pair<int,int> p){
    int square_x = p.first / 3;
    int square_y = p.second / 3;

    for(int i = 0 ; i < 9 ; i++){
        if(board[p.first][i] == board[p.first][p.second] && i != p.second)
            return false;
        if(board[i][p.second] == board[p.first][p.second] && i != p.first)
            return false;
    }

    for(int i = 3 * square_x;i < 3 * square_x+3; i++){
        for(int j = 3 * square_y; j < 3 * square_y+3; j++){
            if(board[i][j]==board[p.first][p.second]){
                if(i!=p.first && j!= p.second)
                    return false;
            }
        }
    }
    return true ;
}



void sudoku(int N){
    if (N == cnt){
        for(int i = 0 ; i < 9 ; i ++){
            for (int j = 0 ; j < 9; j++){
                cout << board[i][j] << " ";
            }
            cout << "\n";
        }
        found = true;
        return;
    }

    for(int j = 1 ; j <= 9 ; j++){
        board[points[N].first][points[N].second] = j;
        if(check(points[N])){
            sudoku(N+1);
        }
        if(found)
            return;
    }
    board[points[N].first][points[N].second] =  0;
    return;

}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    pair<int,int>point;

    for(int i = 0 ; i < 9; i++){
        for(int j = 0; j < 9 ; j++){
            cin >> board[i][j];
            if(board[i][j]==0){
                cnt ++;
                point.first = i;
                point.second = j;
                points.push_back(point);
            }
        }
    }

    sudoku(0);

}