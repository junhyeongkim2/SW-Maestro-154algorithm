#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

int n;
int arr[500001];
int tmp[500001];
long long result = 0;


void merge(int start, int last){

    int mid = (start + last) / 2;
    int i = start;
    int j = mid + 1;
    int k = start;
    int cnt = 0;

    while(i<= mid && j<= last){
        if(arr[i] <= arr[j]){
            tmp[k++] = arr[i++];
            result += (long long)cnt;
        }else{
            tmp[k++] = arr[j++];
            cnt++;
        }
    }

    if(i>mid){
        int s = j;
        while(s<=last){
            tmp[k++] = arr[s++];
            cnt++;
        }
    }else{
        int s = i;
        while(s<=mid){
            tmp[k++] = arr[s++];
            result += (long long)cnt;
        }
    }

    for(int t = start; t<= last; t++){
        arr[t] = tmp[t];
    }
}


void mergesort(int start, int last){

    if(start<last){
        int mid = (start + last) / 2;
        mergesort(start,mid);
        mergesort(mid+1,last);
        merge(start,last);
    }

}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for(int i = 0 ; i < n ; i++){
        cin >> arr[i];
    }

    mergesort(0,n-1);
    cout << result;

}
