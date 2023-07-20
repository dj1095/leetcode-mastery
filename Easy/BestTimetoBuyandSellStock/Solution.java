class Solution {
    // Time Complexity - O(N);
    // Space Complexity - O(1);

    public int maxProfit(int[] prices) {
       int wd1 = 0, wd2 = 1;
       int maxProfit = 0;
        for(int i=0; i<prices.length - 1; i++){
            int profit = prices[wd2] - prices[wd1];
            if(profit > 0){
                maxProfit = Math.max(profit, maxProfit);
            }else{
                wd1 = i+1;
            }
            wd2++;
        }
         return maxProfit;
    }
}