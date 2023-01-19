#include <iostream>
using namespace std;

int n=0;
int N=0;

int main(){

    cin >> n;

    N = ((n*2)-1);
    //cout << N << "\n";

    int x = 0;

    for(int i = 0;i<n-1;i++){
        for(int i2=0;i2<x;i2++){
            cout << " ";
        }
        x++;
        for(int i1=0;i1<N;i1++){
            cout << "*";


            //cout << i1;
        }
        N=  N-2;
        cout << "\n";
    }
    for(int i2=0;i2<x;i2++){
        cout << " ";
    }
    cout << "*";
    cout << "\n";


    for(int i = 0 ; i<n-1;i++){
        N= N+2;
        x--;
        for(int i2=0;i2<x;i2++){
            cout << " ";
        }
        for(int i1=0;i1<N;i1++){
            cout << "*";
        }
        cout << "\n";
    }



}