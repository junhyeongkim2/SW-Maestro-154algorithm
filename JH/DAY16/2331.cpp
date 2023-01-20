#include <bits/stdc++.h>
using namespace std;



int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string a;
    int p ;

    cin >> a >> p;
    string temp = a;
    vector<string>v;

    int visited[250001]={0,};
    v.push_back(a);
    visited[stoi(a)]++;

    while(true){
        int sum =0;
        for (int i = 0; i <temp.size() ; ++i) {
            int x = temp[i]-'0';
            sum += pow(x,p);
        }

        visited[sum]++;
        if(visited[sum]>2){
            break;
        }

        temp = to_string(sum);

        v.push_back(temp);

    }


    int ans =0;
    for (int i = 0; i <250001 ; ++i) {
        if(visited[i]==1){
            ans++;
        }
    }
    cout << ans << "\n";

}