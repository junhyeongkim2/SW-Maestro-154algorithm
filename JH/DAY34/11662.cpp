#import <bits/stdc++.h>
using namespace std;

double Start(double start, double end){
    return start + (end - start) / 3;
}

double End(double start, double end){
    return end - (end - start) / 3;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    double m_start_x = 0, m_start_y = 0;
    double m_end_x = 0, m_end_y = 0;

    double g_start_x = 0, g_start_y = 0;
    double g_end_x = 0, g_end_y = 0;

    cin >> m_start_x >> m_start_y >> m_end_x >> m_end_y >> g_start_x >> g_start_y >> g_end_x >> g_end_y;

    int T = 100;

    double mid1 = 0, mid2 = 0;

    while(T--){
        mid1 = sqrt(pow(m_start_x - g_start_x,2) + pow(m_start_y - g_start_y, 2));
        mid2 = sqrt(pow(m_end_x - g_end_x, 2) + pow(m_end_y - g_end_y,2));

        if(mid1>mid2){
            m_start_x = Start(m_start_x, m_end_x);
            m_start_y = Start(m_start_y,m_end_y);
            g_start_x = Start(g_start_x,g_end_x);
            g_start_y = Start(g_start_y,g_end_y);
        }else if(mid1<mid2){
            m_end_x = End(m_start_x,m_end_x);
            m_end_y = End(m_start_y,m_end_y);
            g_end_x = End(g_start_x, g_end_x);
            g_end_y = End(g_start_y,g_end_y);
        }else{
            break;
        }
    }

    cout << fixed;
    cout.precision(10);
    cout << min(mid1,mid2);

}