class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // put all of the same ones as a map of strings and lists of all anagrams to the string
        // return the values of the map

        // private function checking anagram

        // if (strs.length() == 1) {
        //     return strs.toString();
        // }

        // sort each individual word by letter alphabetically
        Map<String, List<String>> m = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            char[] sArr = strs[i].toCharArray();
            Arrays.sort(sArr);
            String sorted = new String(sArr);
            if (m.containsKey(sorted)) {
                m.get(sorted).add(strs[i]);
            } else {
                ArrayList<String> newList = new ArrayList<>();
                newList.add(strs[i]);
                m.put(sorted, newList);
            }
        }
        return new ArrayList<>(m.values());
    }
}
