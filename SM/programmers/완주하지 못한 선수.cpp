#include <string>
#include <vector>
#include <map>

using namespace std;



string solution(vector<string> participant, vector<string> completion) {
    map<string, int> m;
    string answer = "";

    for(int i = 0; i < participant.size(); i++){
        
        if(m.end() == m.find(participant[i])){
            m.insert(make_pair(participant[i], 1));
        }else{
            m[participant[i]]++;
        }

    }
    
    for(int i = 0; i < completion.size(); i++){
        m[completion[i]]--;
    }
    
    for(int i = 0; i < participant.size(); i++){
        if(m[participant[i]] > 0){
            answer = participant[i];
            break;
        }
    }
    return answer;
}