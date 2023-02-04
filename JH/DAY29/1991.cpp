#import <bits/stdc++.h>

using namespace std;



int n;

pair<char,char>arr[26];


void preorder(char x){
    if(x!='.'){
        cout << x;
        preorder(arr[x-'A'].first);
        preorder(arr[x-'A'].second);

    }
}

void inorder(char x){
    if(x!='.'){
        inorder(arr[x-'A'].first);
        cout << x ;
        inorder(arr[x-'A'].second);
    }
}

void postorder(char x){
    if(x!='.'){
        postorder(arr[x-'A'].first);
        postorder(arr[x-'A'].second);
        cout << x ;
    }
}



int main(){

    cin >> n;

    for(int i = 0 ; i < n ; i++){
        char node, left, right;
        cin >> node >> left >> right;
        arr[node-'A'].first = left;
        arr[node-'A'].second = right;
    }

    preorder('A');
    cout << "\n";
    inorder('A');
    cout << "\n";
    postorder('A');
    cout << "\n";












}