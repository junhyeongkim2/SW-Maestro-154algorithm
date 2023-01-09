#include <bits/stdc++.h>

using namespace std;


int a,b;

int main(){

    cin >> a >> b;

    int day = 0;

    for (int i = 1; i <a ; ++i) {
        if(i==1 || i==3 || i==5 || i==7 || i==8 || i==10 || i==12 ){
            day+=31;
        }else if(i==4||i==6||i==9||i==11){
            day+=30;
        }else if(i==2){
            day+=28;
        }
    }
    day+=b;
    int c = day % 7;
    if(c == 1){
        cout << "MON";
    }
    if(c == 2){
        cout << "TUE";
    }
    if(c == 3){
        cout << "WED";
    }
    if(c == 4){
        cout << "THU";
    }
    if(c == 5){
        cout << "FRI";
    }
    if(c == 6){
        cout << "SAT";
    }
    if(c == 0){
        cout << "SUN";
    }

}






