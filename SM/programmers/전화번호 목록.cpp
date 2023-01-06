#include<iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    map<string, int> m;
    
    for(int i = 0; i < phone_book.size(); i++){
        m[phone_book[i]] = 1;
    } // 저장

    for(int i = 0; i < phone_book.size(); i++){
        string str = "";
        for(int j = 0; j < phone_book[i].size(); j++){
            str += phone_book[i][j];
            if(m[str] != 1 && phone_book[i] != str){
                return false;
            }
        }
    }

    return true;
}