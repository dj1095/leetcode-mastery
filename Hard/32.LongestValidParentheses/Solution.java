class Solution {
    public int longestValidParentheses(String s) {
         
        int open=0,close=0;
        int ans=0;
        
        for(int i=0;i<s.length();++i){
            
            char ch=s.charAt(i);
            
            if(ch=='(')
                ++open;
            
            else
                ++close;
            
            if(open==close)
                ans=Math.max(ans,open+close);
            
            // current substring is invalid. So reset
            else if(close>open)
                open=close=0;
        }
        
        open=close=0;
        
        for(int i=s.length()-1;i>=0;--i){
            
            char ch=s.charAt(i);
            
            if(ch=='(')
                ++open;
            
            else
                ++close;
            
            if(open==close)
                ans=Math.max(ans,open+close);
            
            // current substring is invalid. So reset
            else if(open>close)
                open=close=0;
        }
        
        return ans;
        
    }
        
    
}