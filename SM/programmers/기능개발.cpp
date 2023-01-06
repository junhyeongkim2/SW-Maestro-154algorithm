#include <string>
#include <vector>
#include <queue>
#include<algorithm>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    

    for(int i = 0; i < progresses.size(); i++){
        int rprogresses = 100 - progresses[i];

        int day = (rprogresses / speeds[i]);
        // 제대로 안나눠졌다면? => +1일 
        if(rprogresses % speeds[i] != 0){
            day = day + 1;
        }
        q.push(day);
    }
    
    while(!q.empty()){
        int cur = q.front();
        int cnt = 1;
        q.pop();
        while(!q.empty() && cur >= q.front()){
            cnt++;
            q.pop();
        }
        answer.push_back(cnt);
    }
    //개발 기간이 다 정해졌다. 기능들은 앞에 일 수에 맞춰야한다.
    
   
    
    


    return answer;
}