package 프로그래머스_고득점_kit.DP.등굣길;

public class Solution_dp {
    public int solution(int m, int n, int[][] puddles) {

        int[][] map = new int[n][m];

        for(int[] p : puddles){
            map[p[1]-1][p[0]-1] = -1;
        }

        map[0][0] = 1;
        for(int i = 0; i<n;i++){
            for(int j = 0; j<m; j++){
                if(map[i][j]!=-1){
                    if(i+1<n&&map[i+1][j]!=-1){
                        map[i+1][j] = (map[i+1][j]+map[i][j])%1000000007;
                    }

                    if(j+1<m&&map[i][j+1]!=-1){
                        map[i][j+1] = (map[i][j+1]+map[i][j])%1000000007;
                    }
                }

            }
        }

        return map[n-1][m-1];
    }

    public static void main(String[] args) {
        int a = new Solution_dp().solution(4, 3, new int[][]{{2, 2}});

        System.out.println(a);
    }
}
