d = {'A':'A','E':'3','H':'H', 'I':'I', 
'J':'L', 'L':'J', 'M':'M', 'O':'O', 
'S':'2', 'T':'T', 'U':'U', 'V':'V', 
'W':'W', 'X':'X', 'Y':'Y', 'Z':'5',
'1':'1', '2':'S', '3':'E', '5':'Z','8':'8',
 }

while True:
        try:

                n = input()
                s = ''
                for i in n:
                    if i in d.keys():
                        s += d[i]    
                if n == n[::-1]:
                        if s[::-1] == n:
                                print("{} -- is a mirrored palindrome." .format(n))
                                print('')
                        else:
                                print("{} -- is a regular palindrome." .format(n))
                                print('')                
                elif s[::-1] == n:
                                print("{} -- is a mirrored string." .format(n))
                                print('')

                else:
                        print("{} -- is not a palindrome." .format(n))
                        print('')
        except EOFError:
                break                                