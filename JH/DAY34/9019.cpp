#import <bits/stdc++.h>
using namespace std;

int T;
int check[10000];


void bfs(int A, int B, string temp){
    queue<pair<pair<int,int>,string>>q;
    q.push({{A,B},temp});


    while(!q.empty()){
            int a = q.front().first.first;
            int b = q.front().first.second;
            string t = q.front().second;
            q.pop();

            if(a==b){
                cout << t << "\n";
                return;
            }

            for(int i = 0 ; i < 4; i ++){
                int na  = 0;
                if(i==0){
                    na = (a * 2) % 10000;
                    if(check[na]==0){
                        check[na]=1;
                        q.push({{na,b},t+"D"});
                    }

                }else if(i==1){
                    int na  = a - 1 < 0 ? 9999 : a - 1;
                    if(check[na]==0){
                        check[na]=1;
                        q.push({{na,b},t+"S"});
                    }
                }else if(i==2){

                    int sti = (a % 1000) * 10 + (a / 1000);
                    if(a<10){
                        q.push({{sti,b},t+"L"});
                    }else{
                        if(check[sti]==0) {
                            check[sti]=1;
                            q.push({{sti,b},t+"L"});
                        }
                    }



                }else if (i==3){
                    int sti = (a / 10) + (a % 10) * 1000;

                    if(a<10){
                        q.push({{sti, b}, t + "R"});
                    }else{
                        if(check[sti]==0) {
                            check[sti] = 1;
                            q.push({{sti, b}, t + "R"});
                        }

                    }


                }


        }

    }

}



int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);


    cin >> T;

    while(T--){
        int A,B;
        cin >> A >> B;
        bfs(A,B,"");
        memset(check,0,sizeof check);

    }

}