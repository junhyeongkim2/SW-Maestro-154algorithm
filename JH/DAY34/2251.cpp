#import <bits/stdc++.h>
using namespace std;

int A,B,C;

int visited[201][201][201] = {0,};

vector<int>result;

void bfs(){

    queue<pair<pair<int,int>,int>>q;
    q.push({{0,0},C});

    while(!q.empty()){
        int a = q.front().first.first;
        int b = q.front().first.second;
        int c = q.front().second;
        //cout << a << " " << b << " " << c << "\n";
        q.pop();

        if(visited[a][b][c]==1)continue;

        visited[a][b][c] = 1 ;

        if(a == 0){
            result.push_back(c);
        }

        if(a+b>B){
            q.push({{a+b-B,B},c});
        }else{
            q.push({{0,a+b},c});
        }

        if(a+c>C){
            q.push({{a+c-C,b},C});
        }else{
            q.push({{0,b},a+c});
        }

        if(b+a>A){
            q.push({{A,b+a-A},c});
        }else{
            q.push({{b+a,0},c});
        }

        if(b+c>C){
            q.push({{a,b+c-C},C});
        }else{
            q.push({{a,0},b+c});
        }

        if(c+a>A){
            q.push({{A,b},c+a-A});
        }else{
            q.push({{c+a,b},0});
        }

        if(c+b>B){
            q.push({{a,B},c+b-B});
        }else{
            q.push({{a,c+b},0});
        }


    }



}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);


    cin >> A >> B >> C;

    bfs();

    sort(result.begin(),result.end());

    for(auto x : result){
        cout << x << " ";
    }



}