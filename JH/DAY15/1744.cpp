#include <bits/stdc++.h>
using namespace std;

int n;

vector<int>vm;
vector<int>vp;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        if(a<=0){
            vm.push_back(a);
        }else{
            vp.push_back(a);
        }
    }

    std::sort(vm.begin(), vm.end(),less<int>());
    std::sort(vp.begin(), vp.end(),greater<int>());


    int vmsize = vm.size();
    int vpsize = vp.size();

    int ans =0;

    for (int i = 0; i <vmsize ; i+=2) {
        if(vm.size()>=2){
            int sum = vm[i] * vm[i+1];
            ans+=sum;
            vm.pop_back();
            vm.pop_back();
        }
    }

    for (int i = 0; i <vpsize ; i+=2) {
        if(vp.size()>=2){
            int sum = max ((vp[i] * vp[i+1]),(vp[i]+vp[i+1]) );

            ans+=sum;
            vp.pop_back();
            vp.pop_back();
        }
    }

    if(vp.size()==1){
        ans+=vp[vpsize-1];
    }
    if(vm.size()==1){
        ans+=vm[vmsize-1];
    }

    cout << ans << "\n";


}