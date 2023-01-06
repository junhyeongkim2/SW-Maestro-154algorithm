#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    queue<pair<int, int>> q;
    priority_queue<int, vector<int>,less<int>> pq;
    int answer = 0;

    for(int i = 0; i < priorities.size(); i++){
        q.push(make_pair(priorities[i], i));
        pq.push(priorities[i]);
    }
    int cnt = 0;
    while(!q.empty()){
        if(q.front().first != pq.top()){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            q.push(make_pair(x, y));
        }else if(q.front().first == pq.top()){
            cnt++;
            if(q.front().second == location){
                answer = cnt; 
            }
            q.pop();
            pq.pop();
        }
    }
  

    return answer;
}