
Source Code:

numb=int(input("enter any number"))

facts=[]

for a in range(1,numb+1):

    if numb%a==0:

       facts.append(a)

print ("Factors of {} = {}".format(numb,facts))

Output

enter a number 6

Factors of 6 = [2, 3]
