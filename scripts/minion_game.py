def minion_game(string):
    strln=len(string)
    vw="AEIOU"
    kevsc = 0
    stusc = 0
    
    for i in range(strln):
        if string[i] in vw:
            kevsc += strln-i
        else:
            stusc += strln-i
            
    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()  #A single line of input containing the string, only uppercase letters [A-Z]
    minion_game(s)