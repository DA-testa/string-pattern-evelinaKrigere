# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    input1=input()

    if input1=='F':
        filename=input()
        with open(filename,'r') as f:
            pattern=f.readline()
            text=f.readline()
    else:
        pattern=input()
        text=input()


    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())
    return(pattern,text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p=10**9+7
    x=31

    occurances=[]

    n=len(text)
    m=len(pattern)

    phash=0
    thash=[0]*(n-m+1)
    xpow=[1]*(n-m+1)

    for i in range(1,n-m+2):
        if i==1:
            xpow[i-1]=1
            for j in range(m):
                phash=(phash*x+ord(pattern[j])%p)
                thash[i-1]=(thash[i-1]*x+ord(text[j]))%p
        else:
            xpow[i-1]=(xpow[i-2]*x)%p
            thash[i-1]=((thash[i-2]-ord(text[i-2])*xpow[i-2])*x+ord(text[i+m-2]))%p

    for i in range(n-m+1):
        if phash==thash[i]:
            if pattern==text[i:i+m]:
                occurances.append(i)

    # and return an iterable variable
    #return [0]
    return occurances


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

