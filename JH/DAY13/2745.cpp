#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    string s;
    cin >> s;
    int n;
    cin >> n;
    long long int sum =0;
    int cnt =0;
    for (int i =s.length()-1; i >=0 ; --i) {
        int temp = s[i];

        if(s[i] - '0' >= 0&& s[i] - '0' < 10){
            sum +=  (temp-'0') * ((int) pow(n,cnt));
        }else{
            sum += (temp-'A'+10) * ((int) pow(n,cnt));
        }
        cnt++;
    }
    cout << sum << "\n";





}