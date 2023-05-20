ticket = input('Enter a number of ticket: ')
sumHalfLeft = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
sumHalfRight = int(ticket[3]) + int(ticket[4]) + int(ticket [5])

if sumHalfLeft == sumHalfRight:
    print('Yes!')
else:
    print('No :(')