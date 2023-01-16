#include <bits/stdc++.h>
using namespace std;


deque<int>deck;

int main(){


    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int n;
    cin >> n;

    for (int i = 0; i <n; ++i) {
        string s;
        cin >> s;

        if(s == "push_front"){
            int x;
            cin >> x;
            deck.push_front(x);
        }
        if(s == "push_back"){
            int x;
            cin >> x;
            deck.push_back(x);
        }
        if(s == "pop_front"){
            if(deck.size()==0){
                cout << "-1" << "\n";
            }else{
                cout << deck.front() << "\n";
                deck.pop_front();
            }
        }
        if(s == "pop_back"){
            if(deck.size()==0){
                cout << "-1" << "\n";
            }else{
                cout << deck.back() << "\n";
                deck.pop_back();
            }
        }
        if(s == "size"){
            cout << deck.size()<<"\n";
        }
        if(s == "empty"){
            if(deck.empty()){
                cout << "1" <<"\n";
            }else{
                cout << "0" << "\n";
            }
        }
        if(s == "front"){
            if(deck.size()==0){
                cout << "-1" << "\n";
            }else{
                cout << deck.front() << "\n";
            }
        }
        if(s == "back"){
            if(deck.size()==0){
                cout << "-1" << "\n";
            }else{
                cout << deck.back() << "\n";
            }
        }

    }





}