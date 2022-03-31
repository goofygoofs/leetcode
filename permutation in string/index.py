'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

'''
s2 contains a permutation of s1?
letter, index are important
index can be reversed, ie. "ab" and "ba" but "boa" won't work

put all characters of s1 into a dictionaryy
copy dictionary
loop through s2 and find out where it starts containing letters from s1 and minus 1, until length of copied dicionary is 0. get the start and end indexes and make new string out of it


check if length is equal
create another function to find out if permutation exists
actually permutation, the ordering doesn't matter. so just the dictionary portion matters


so... that means we have to make sure no other letters in substring of s2. and also careful of duplicates. 
if there's duplicates we can remove the firstmost index of found character and see if it affects sustring

"aab" "zzeaaab"
"aaaaa" "sadfw3efdafds"

what if there is only 1 char in dict?

Time compliexity is O(n) for creating dictionary and looping through s2
well it is O(m+n)
space is O(m) for s1 dictionary and copying it
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        seen = set()
        for char in s1:
            if char not in s1dict:
                s1dict[char] = 1
                seen.add(char)
            else:
                s1dict[char] += 1
        
        s1dictCopy = s1dict.copy()
        seenCopy = seen.copy()
        leftPointer = 0
        for i, char in enumerate(s2):
            # if i == 0:
            #     continue
            
            startingChar = s2[leftPointer]
            if char in s1dictCopy:
                # check if s1dict is altered yet
                if s1dictCopy == s1dict and seenCopy == seen:
                    leftPointer = i
                s1dictCopy[char] -= 1

                if s1dictCopy[char] == 0:
                    if char in seenCopy:
                        seenCopy.remove(char)

                # check if permutation
                if len(seenCopy) == 0:
                    return True
                
                if s1dictCopy[char] < 0:
                    # for new starting char
                    s1dictCopy[startingChar] += 1
                    leftPointer += 1
                        

            else:
                # char not in dict. not in permutation
                seenCopy = seen.copy()
                s1dictCopy = s1dict.copy()



        return False


sol = Solution()

output = sol.checkInclusion("kuzntqeuvaszrspkgjvxrupwxwrexztptsowceibeewxbslvosbobmyymikdscshybtmanuxeqtanrjekbwirmhgvfmzipfiqxcilarfyasoayepgfzmdytlpjymeaztsyubkbmblepwozffxiitdhwaquozlfmnascomqczrbhxcnzugppddtudxrigfeaozzojpeamnobapgwksudbiwdedvprwonmzardsodhxmkgghqzfhorjaijdvwzsnfpdfklwibbsnwqsoajcpjisbgizgttlnmclawbgnhbmtcpuusuammvgxnopdngclxumgfgwjrinamevhirpmlkwtyxkrmoffrreotdosjghsrkgxyiyrytbbofgczndgmdalyvvoljczcztxitxelywqemjigtuanubpstndwzvtiejtoqvetaehvcuujyupncumjnkesmoadzyvkwvjqgqewvvvpheyyvkewefbjjqzajxnhouodanyruqpzdcjmgnxkmhsgqjhpcyviewmrkfioudzqivmmguxjxuxdmpsmkwnvbxcomifgxqmcovlkooptjpfxjllwtlkkoaayzduodgsusaogswmoqkznynwiukkrrxzkwcknwlazxnlmghybxmyvquzbdqlpfydhnnuvlmyjmixyzso","zthosfejqodcstlqczkndmgwtcakxzxaklkrehkfwnokclametzpnblcwaspdblfoopsiqrpzlbmlysddlqxcjzezcpknwzljvhmqxqinmptcppipifchxexlytleambzwmqwgvxlehnecdqsqbrxqfwvcovgdvtmwbnvajvkizixbmuiuyuixjhiohimghdbohetogrhzsbzgpekosxcjglsrvzenovpjyzknuumpsdrufcjsyfbuwfmaaztxjbpjctnuwcqknnemptjbgfthyafeatskfmysaioqikcpywmefujnvthumyhareltknxyvqprexgbwyzodfkinltwobeukrmpyjkrgvwhbtnzaozgxouxndmkyvzlujhxxwebptykctbojgnvcwhhgsyohccrqxksdyygcwdsazlznhqjdddisjmfqvjqcquuvjrzkcvzpxpfakbkrqlzacanqbggavezedqmoffxmkrlcwxdeosvhvvknqimwpasrlldewvhppzixgcxisysgeppcwfknecupyrrqnkhvessintrequaqiuoesgyndovaqxnlldmdupjcjzejannfjfasguyvgsdakwxezrginhdstbrtqmznpkasytqtbfyftwhgnuazcwehsvcdukuifmkefzabxyhihgnldpsvglubalbsvqstfxehvnpxmrejnkqacafuvzghbttgqmjhqzejasoasbpjirfawcvwahykvrfpaadcgvxssebdznzyvamyilahahgdslwvpuvzsinbbqecdqyvwnucjzyxmxwqwyxbxoljnjcqqdumghmcvqpcpjlxemupospxvkicqvyiavatbojgzurfzitgpeqjmvsgzzqphciyweyavebslgegjcyqmgehchryyclswjequeijzpsvuercqzhwgtgyxhxavhqkrwqdvkqvklicxpasnsnbgybtufdgbwrpaewzwczabckvddtewuns")
print(output)

# output = sol.checkInclusion(s1 = "ab", s2 = "eidbaooo")
# print(output)

# output = sol.checkInclusion(s1 = "ab", s2 = "eidboaoo")
# print(output)
