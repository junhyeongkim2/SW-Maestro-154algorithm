#include <vector>
#include <map>
#include <string>
using namespace std;

int solution(vector<int> nums)
{
    
    int answer = 0;
    map<string, int> m;
    for(int i = 0; i < nums.size(); i++){
        
        if(m.find(to_string(nums[i])) == m.end()){
            m.insert(make_pair(to_string(nums[i]), 1));
        }else{
            m[to_string(nums[i])]++;
        }
    }
    //종류를 카운트해야함.
    for(auto str : nums){
        if((nums.size() / 2) >= m.size()){
            
            if(nums.size() == m.size()){
                answer = m.size();
            }else{
                answer = m.size();
            }
        }else{
            answer = (nums.size() / 2);
        }
    }
    return answer;
}