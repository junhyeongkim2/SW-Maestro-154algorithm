#include <iostream>

using namespace std;

// 분할정복... DP보다 개인적으로 더 어려운듯.. 

int star(int i, int j , int n);


int main(){

    int n ;
    cin >> n ;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            star(i,j,n);
        }
        cout << '\n';
    }
return 0;

}


int star(int i, int j , int n){

    if((i/n)%3==1&&(j/n)%3==1){
        cout << ' ';
    }
    else if(n/3==0){
        cout << '*';
    }
    else{
        star(i,j,n/3);
    }
    return 0 ;


}

