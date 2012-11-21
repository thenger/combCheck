"""
"" Author: Thenger
"" This program is aimed to check all combinations of a set of letters
""
"" exemple: for the set (a,b,c,d) there's 4! possible combinations
"" (abcd, abdc, acbd, acdb, ..., dcba)
"" this includes the possible doubles like "boop" and "boop" where the
"" two 'o' aren't the same.
""
"" trust the recursivity
"""

# do something with the string
def do(s):
        print (s)

# recursive method
# s   : remaining letters of the string
# sNew: new built string while going futher in the recursion
def spin(s, sNew):
        # end recursion when there's only 2 letters left
        if (len (s) == 2):
                # these are the two left letters
                do(sNew + s[0] + s[1])
                do(sNew + s[1] + s[0])
        else:
                #this is the main loop:
                # for each character in the string
                # remove this letter from the set, add it to the new
                #  built string
                # continue with the trucated string and the new one
                for char in s:
                        srl = s.replace (char, "", 1)# rl is "remaining letters"
                        spin (srl, sNew + char)

# this is a hat method just to launch the recursion with an empty string
# and separate the first len() test
def combine(s):
        if (len (s) > 1):
                spin (s, "")
        else:
                do (s)

def main():
        print ("Hey !")
        combine ("boop")

main()
