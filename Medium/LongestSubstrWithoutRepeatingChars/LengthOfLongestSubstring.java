package LongestSubstrWithoutRepeatingChars;

import java.util.HashSet;
import java.util.Set;

class LengthOfLongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> hashSet = new HashSet<Character>();
        int maxSubStr = 0;
        int l = 0;
        for(int i=0; i<s.length(); i++){
            while(hashSet.contains(s.charAt(i))){
                hashSet.remove(s.charAt(l));
                l++;
            }
            hashSet.add(s.charAt(i));
            maxSubStr = Math.max(hashSet.size(), maxSubStr);
        }
        return maxSubStr;
    }
}