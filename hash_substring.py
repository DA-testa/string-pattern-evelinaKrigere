# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    ievade=input()

    if "F" in ievade:
        path='./tests/'+'06'
        with open(path,'r') as f:
            pattern=f.readline().rstrip()
            text=f.readline().rstrip()

            return(pattern,text)
    if "I" in ievade:
        pattern=input().rstrip()
        text=input().rstrip()
        
        return(pattern,text)
        
        


    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p=10**9+7
    x=31

    occurrences=[]

    n=len(text)
    m=len(pattern)

    phash=0
    thash=0
    xpow=1

    for i in range(m):
        phash=(phash*x+ord(pattern[i]))%p
        thash=(thash*x+ord(text[i]))%p
        if i < m-1:
            xpow = (xpow*x)%p

    for i in range(n-m+1):
        if phash==thash:
            if pattern==text[i:i+m]:
                occurrences.append(i)
        if i < n-m:
            thash = ((thash-ord(text[i])*xpow)*x+ord(text[i+m]))%p

    # and return an iterable variable
    #return [0]
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

