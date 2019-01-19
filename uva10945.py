import re 
while True:

    n = input()
    if n == 'DONE':
        break
    else:
        nn = re.sub(r'[^\w]', ' ', n)
        np  = nn.replace(" ","")
        np = np.lower()        
        if np == np[::-1]:
            print("You won't be eaten!")
        else:
            print("Uh oh..")    
       
