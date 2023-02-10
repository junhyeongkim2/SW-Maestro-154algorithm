#import <bits/stdc++.h>
using namespace std;

int L,C;
vector<char>alphabet;

void dfs(char al, int a, int b, int index,string temp){
    temp += al;
    if(temp.size() == L && a>=1 && b>=2){
        cout << temp <<"\n";
        return;
    }
    for(int i = index+1; i<C ; i++ ){
        char next = alphabet[i];
        if (alphabet[i]=='a'||alphabet[i]=='e'||alphabet[i]=='i'||alphabet[i]=='o'||alphabet[i]=='u'){
            dfs(next,a+1,b,i,temp);
        }else{
            dfs(next,a,b+1,i,temp);
        }
    }
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> L >> C;

    for(int i = 0 ; i < C; i++){
        char a;
        cin >> a;
        alphabet.push_back(a);
    }

    sort(alphabet.begin(),alphabet.end());


    for(int i = 0 ; i <= C-L; i++){
        int a = 0;
        int b = 0;
        if (alphabet[i]=='a'||alphabet[i]=='e'||alphabet[i]=='i'||alphabet[i]=='o'||alphabet[i]=='u'){
            a = 1;
        }else{
            b = 1;
        }
        dfs(alphabet[i],a,b,i,"");
    }
}