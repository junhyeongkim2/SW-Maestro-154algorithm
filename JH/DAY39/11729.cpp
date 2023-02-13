#include <iostream>
#include <cmath>
using namespace std;

//하노이의탑... 분할정복... 어..렵..다.. 

void hanoi(int n, int from , int to){
    if(n==0)return;

    int remain = 6 - to - from;

    hanoi(n-1, from, remain);

    cout << from << " " << to <<'\n';

    hanoi(n-1, remain , to);
}

int main(){
    int n;

    cin >> n;

    cout << (1<<n)-1 << "\n";

    hanoi(n,1,3);

    return 0 ;
}
