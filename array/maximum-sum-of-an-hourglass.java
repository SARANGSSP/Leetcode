class Solution {
    static
    {
        for(int i=0;i<=200;i++) maxSum(new int[3][3]);
    }
    public static int maxSum(int[][] A) {
         int max=0;  int sum=0;
         int n=A.length;
        for(int i=0;i<n-2;i++){
            for(int j=0;j<A[0].length-2;j++){
                sum=A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j+1]+A[i+2][j]+
                        A[i+2][j+1]+A[i+2][j+2];

                max=Math.max(sum,max);
            }
        }
        return max;
    }
}