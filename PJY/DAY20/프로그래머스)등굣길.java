class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] arr = new int[m+1][n+1];

        for(int[] puddle : puddles){
            int x = puddle[0];
            int y = puddle[1];

            arr[x][y] = -1;
        }

        for(int i = 1; i < arr.length; i++){
            for(int j = 1; j < arr[i].length; j++){
                if(arr[i][j] == -1) continue;
                arr[i][j] = minStreet(i, j, arr) % 1000000007;
            }
        }

        return arr[m][n];
    }

    public int minStreet(int x, int y, int[][] arr){
        if(x == 1 && y == 1) return 1;
        int result = 0;

        int a = arr[x-1][y];
        int b = arr[x][y-1];

        if(a > 0) result += a;
        if(b > 0) result += b;

        return result;
    }
}
