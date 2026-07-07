class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> sseen = new TreeMap<>();
        for (int i = 0; i <= s.length()-1; i++) {
            if (!sseen.containsKey(s.charAt(i))) {
                sseen.put(s.charAt(i), 1);
            }
            sseen.put(s.charAt(i), sseen.get(s.charAt(i)) + 1);
        }

        Map<Character, Integer> tseen = new TreeMap<>();
        for (int i = 0; i <= t.length()-1; i++) {
            if (!tseen.containsKey(t.charAt(i))) {
                tseen.put(t.charAt(i), 1);
            }
            tseen.put(t.charAt(i), tseen.get(t.charAt(i)) + 1);
        }
        if (sseen.equals(tseen)) {
            return true;
        }
        else {
            return false;
        }
    }
}
