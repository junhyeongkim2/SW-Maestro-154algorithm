#include <bits/stdc++.h>
using namespace std;


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    string s;
    int n;

    cin >> s;
    cin >> n;

    stack<char>l;
    stack<char>r;

    for (int i = 0; i <s.length() ; ++i) {
        l.push(s[i] );
    }

    while(n--){
        string temp;
        cin >> temp;
        if(temp=="L"){
            if(l.size()==0)continue;
            char top = l.top();
            l.pop();
            r.push(top);
        }
        if(temp=="D"){
            if(r.size()==0)continue;
            char top = r.top();
            r.pop();
            l.push(top);
        }
        if(temp=="B"){
            if(l.size()==0)continue;
            l.pop();
        }
        if(temp=="P"){
            char x;
            cin >> x;
            l.push(x);
        }
    }


    int leftsize = l.size();
    //cout << "leftsize : " << leftsize <<"\n";

    for (int i = 0; i <leftsize ; ++i) {
        char temp ;
        temp = l.top();
        l.pop();
        r.push(temp);
        //cout << temp << "\n";
    }
    int rightsize = r.size();

    //cout << "\n";
    //cout << "rightsize : " << rightsize <<"\n";
    for (int i = 0; i <rightsize ; ++i) {
        char temp ;
        temp = r.top();
        r.pop();
        cout << temp;
    }


}
