'''
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. 
Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
 

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.
'''

'''
* anything after + to be trimmed off
* remove periods

2 functions->
cleanse

cutAt

look through the emails, apply the functions, we will put that into a set because it's a O(1) time lookup. get the length of the set will give us the amount of unique cleansed emails (removed period and +after)
'''

'''
more efficient of beautiful?
make email a class?
'''
from typing import Tuple, List
class Email:
    def __init__(self, email):
        self.original = email
        self.localName, self.domainName = self.cutAt(self.original, '@')
        self.cleansed = self.cleanse(self.original)

    #cuts at the character. returns both sides of character, if any
    def cutAt(self, email: str, char: str) -> Tuple:
        beforeChar, afterChar = "", ""
        emailSplitted = email.split(char, 1)
        beforeChar = emailSplitted[0]
        if len(emailSplitted) > 1:
            afterChar = emailSplitted[1]
        return (beforeChar, afterChar) 
        
    # removes after + sign in localName, strips periods in localName
    def cleanse(self, email: str) -> str:
        local, domain = self.cutAt(email, '@')
        cleansedLocal, _stuffAfterPlus = self.cutAt(local, "+")
        return cleansedLocal.replace(".", "") + '@' + domain 

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()

        for email in emails:
            email = Email(email)
            uniqueEmails.add(email.cleansed)
        
        return len(uniqueEmails)

# O(n) going through emails, split  -> actually it is O(a) with a being number of characters in longest localDomain
# O(n) space because of set, copying str


sol = Solution()

output = sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(output)

output = sol.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])
print(output)