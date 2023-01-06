#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, int> music;
    map<string, map<int,int>> musicRecord;
    
    for(int i = 0; i < genres.size(); i++){
        music[genres[i]] += plays[i];
        musicRecord[genres[i]][i] = plays[i]; // 장르, 고유번호, 플레이횟수 순
    }
    
    
    while(music.size() > 0){
        int max = 0;
        string maxGenre = "";
        for(auto tmp : music){
            if(max < tmp.second){
                max = tmp.second;
                maxGenre = tmp.first;
            }
        }
        
        for(int i = 0; i < 2; i++){

            int uniqueNum = -1;
            int play = 0;
            for(auto tmp2 : musicRecord[maxGenre]){
                if(play < tmp2.second){
                    uniqueNum = tmp2.first;
                    play = tmp2.second;
                }
            }
            if(uniqueNum == -1){
                break;
            }
            musicRecord[maxGenre].erase(uniqueNum);
            answer.push_back(uniqueNum);
        }
        music.erase(maxGenre);
    }
    return answer;
}