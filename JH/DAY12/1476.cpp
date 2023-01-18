#include <bits/stdc++.h>
using namespace std;


deque<int>deck;

int main(){


    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int e,s,m;

    e=1;
    s=1;
    m=1;

    int a,b,c;
    cin >> a >> b >> c;

    int cnt =1;

    while(true){


        if(e>=16){
            e=1;
        }
        if(s>=29){
            s=1;
        }
        if(m>=20){
            m=1;
        }

        if(a==e&&b==s&&c==m){
            cout << cnt;
            break;
        }

        cnt++;
        e++;
        s++;
        m++;

    }




}