def do(s):
        print (s)

def spin(s, sNew):
        if (len(s) == 2):
                do (sNew + s[0] + s[1])
                do (sNew + s[1] + s[0])
        else:
                for char in s:
                        srl = s.replace (char, "", 1)
                        spin (srl, sNew + char)

def combine(s):
        if (len(s) > 1):
                spin (s,"")
        else:
                do(s)

def main():
        combine ("boop")

main()
