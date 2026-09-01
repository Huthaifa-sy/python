svar='ja'
while svar=='ja':
    tall=int(input('oppgi tall'))
    while tall%2!=0:
        print('ikke partall')
        tall=int(input('oppgi tall'))
    while tall>1:
        tall=tall/2
        print(tall)
    svar=input('vil du kjøre på ny')
print('done')

        
