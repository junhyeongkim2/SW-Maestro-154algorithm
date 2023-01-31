#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a,b;
    cin >> a >> b;

    int m;
    cin >> m;
    int ten=0;
    while(m--){
        int x;
        cin >> x;
        ten += pow(a,m)*x ;

    }

    stack<int>s;

    while(ten!=0){

        int temp = ten % b;

        if(temp==0){
            s.push(0);
        }else{
            s.push(temp);
        }

        ten = ten/b;

    }

    while(!s.empty()){
        cout << s.top() << " ";
        s.pop();
    }



}