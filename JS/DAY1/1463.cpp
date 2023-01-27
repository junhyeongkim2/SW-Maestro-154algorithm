#include<iostream>
#include<queue>
#define p pair<int, int>

using namespace std;

int x, cnt; 

void bfs(){
	queue<p> q;
	
	q.push({x, 0});
	
	while(q.size()){
		int cx = q.front().first;
		int t = q.front().second;
		
		if(cx == 1){
			cnt = t;
			break;	
		}
		
		q.pop();
		
		if(cx % 3 == 0){
			q.push({cx/3, t + 1});
		}
		
		if(cx % 2 == 0){
			q.push({cx / 2, t + 1});
		}
		
		q.push({cx - 1, t + 1});
	}
}

int main(){
	
	cin >> x;
	bfs();
	cout << cnt;
}