## problem ##
Estimating the strength of any password is an important aspect of Information Security. In this challenge, your task is
to calculate the strength of a given password in terms of weights assigned to the characters. A password consists of English lowercase letters only.
Each English lowercase letter has assigned an integer weight in the range from 0 to 25 inclusive in such a way that
the weight of letter is given explicitly and weights of other letters follow in cyclic order. For example, if
weight(a)=5, then weight(b)=6, .. weight(v)=0,,weight(z)=4. The strength of a password is the sum of weights of all characters the password consists of


-- Solution 
import string
from collections import *

def getStrength(password, weight_a):

    dA = defaultdict(list)
    s=string.ascii_lowercase
    ns=s[26-weight_a::]+s[0:26-weight_a]
    [dA[ns[i]].append(i) for i in range(0,26)]
    lst=[]
    for char in password:
        if dA[char]:
            lst.append(*dA[char])
    return sum(lst)
