#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, b;

    cin >> n >> b;
    string string_num;

    while(n!=0){
        int tmp = n % b;

        if(tmp>9){
            tmp = tmp-10+'A';
            string_num += tmp;
        }else{
            tmp = tmp + '0';
            string_num += tmp;
        }
        n = n/b;
    }

    std::reverse(string_num.begin(), string_num.end());

    cout << string_num << "\n";


}