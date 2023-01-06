#include <string>
#include <vector>
#include <map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    //clothes[i][0~1] => 얼굴
    //clothes[i][0] => 상의
    //clothes[i][2][] => 하의
    //clothes[i][3] => 겉옷
    int answer = 1;
    map <string, int> m;

    for(int i = 0; i < clothes.size(); i++){
        m[clothes[i][1]]++;
    }

    for(auto tmp : m){
        answer *= tmp.second + 1;
    }
    answer = answer - 1;   
    return answer;
}
