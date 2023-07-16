package Hard.TrappingRainWater;

class Solution {
    public int trap(int[] height) {
        /* //This algo uses linear time and linear memory to solve this

        //Time Complexity - O(N)
        //Space Complexity - O(N)


        int[] maxLeft = new int[height.length];
        int[] maxRight = new int[height.length];
        
        //Populating maximum left
        int maxLeftVal = 0;
        for(int i=0; i<height.length; i++){
             maxLeft[i] = maxLeftVal;
            if(maxLeftVal < height[i]){
                maxLeftVal = height[i];
            }
        }
        //System.out.println(Arrays.toString(maxLeft));

        //Populating maximum Right
        int maxRightVal = 0;
        for(int i=height.length-1; i>=0; i--){
             maxRight[i] = maxRightVal;
            if(maxRightVal < height[i]){
                maxRightVal = height[i];
            }
        }
        //System.out.println(Arrays.toString(maxRight));

        //Calculating trapped water
        int totUnitsOfWater = 0;
        int water = 0;
        for(int i=0; i<height.length;i++){
            water = Math.min(maxLeft[i] , maxRight[i]) - height[i];
            if( water > 0){
                totUnitsOfWater += water;
            }
        }
        return totUnitsOfWater;
    }
    */

    
    //let us improvise this problem to solve in constant space using two pointer approach.
    //Time Complexity - O(N)
    //Space Complexity - O(1)
    int leftPtr = 0;
    int rightPtr = height.length - 1 ;
    int maxL = height[leftPtr];
    int maxR = height[rightPtr];
    int totUnitsOfWater = 0;

    while(leftPtr < rightPtr){
        if(maxL <= maxR){
            totUnitsOfWater += maxL - height[leftPtr] > 0 ? maxL - height[leftPtr] : 0;
            leftPtr++;
            maxL = height[leftPtr] > maxL ? height[leftPtr] : maxL;
        }else{
            totUnitsOfWater += maxR - height[rightPtr] > 0 ? maxR - height[rightPtr] : 0;
            rightPtr--;
            maxR = height[rightPtr] > maxR ? height[rightPtr] : maxR;
        }
    }
     return totUnitsOfWater;

    }
}