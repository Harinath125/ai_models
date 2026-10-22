college ="HARINATH"
def evendemo(n=100):
    if (n&1)==0:
        return "its even"
    else:
        return "its odd"
def palindrome(s):
    if str(s)==str(s)[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
def addition(a=10,b=122):
    print(a+b)
    