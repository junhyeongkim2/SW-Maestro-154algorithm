#include <bits/stdc++.h>
using namespace std;

int n;
int arr[10001];

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    for (int a,i = 0; i <n ; ++i) {
        cin >> a;
        arr[a]+=1;
    }


    for (int i = 0; i <10001; ++i) {
        for (int j = 0; j <arr[i]; ++j) {
            cout << i << "\n";
        }
    }

}
