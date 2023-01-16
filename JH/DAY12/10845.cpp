#include <bits/stdc++.h>
using namespace std;

queue<int>q;

int main(){


    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int n;
    cin >> n;

    for (int i = 0; i <n ; ++i) {
        string s;
        cin >> s;

        if(s=="push"){
            int x;
            cin >> x;
            q.push(x);
        }
        if(s=="pop"){
            if(q.size()==0){
                cout << "-1" << "\n";
            }else{
                cout << q.front() <<"\n";
                q.pop();
            }

        }
        if(s=="size"){
            cout << q.size()<<"\n";
        }
        if(s=="empty"){
            if(q.size()==0){
                cout << "1" <<"\n";
            }else{
                cout << "0" << "\n";
            }
        }
        if(s=="front"){
            if(q.size()==0){
                cout << "-1" << "\n";
            }else{
                cout << q.front() << "\n";
            }
        }
        if(s=="back"){
            if(q.size()==0){
                cout << "-1" << "\n";
            }else{
                cout << q.back() << "\n";
            }
        }

    }




}