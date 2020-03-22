import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    s=(alpha[:size])

    if size==1:
        print(s)
    if size > 1:
        for i in range(len(s)):
            print("-".join(s[len(s)-i:len(s)][::-1]).rjust((size*2)-3,'-')+"-"+alpha[(size-1)-i]+ "-"+"-".join(s[len(s)-i:len(s)]).ljust((size*2)-3,'-') )
        
        for i in reversed(range(len(s)-1)):
            print("-".join(s[len(s)-i:len(s)][::-1]).rjust((size*2)-3,'-') +"-"+alpha[(size-1)-i] + "-"+"-".join(s[len(s)-i:len(s)]).ljust((size*2)-3,'-'))

if __name__ == '__main__':
    n = int(input()) # provide a number between 1 - 26 to generate n size of alphabet rangoli
    print_rangoli(n)