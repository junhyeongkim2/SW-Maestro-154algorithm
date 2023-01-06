#include<string>
#include <iostream>
#include<stack>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> st;
    int cnt = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == '('){
            st.push('(');
            cnt++;
        }else if(s[i] == ')'){
            st.pop();
            cnt--;
        }

        if(cnt < 0){
            break;
        }
    }
    if(cnt == 0){
        answer = true;
    }else{
        answer = false;
    }
    

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return answer;
}