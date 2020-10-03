import time

print('What do you get when you cross a snowman with a vampire?')
input1 = input()

if input1 == 'frostbite' or input1 == 'Frostbite' or input1 == 'Frostbite!':
        print('Excuse me. I\'m telling the jokes here.')
        time.sleep(3)
        print('Ahem.')
        time.sleep(1)
else:
        print('Frostbite!')
        print()

print('What do dentists call an astronaut\'s cavity?')
input2 = input()
if input2 == 'A black hole.' or input2 == 'a black hole' or input2 == 'black hole':
        print('I see you also stay up late looking up terrible jokes.')
        time.sleep(3)
        print('Where was I? Oh, right-')
        time.sleep(1)
        print('A black hole!')
else:
        print('A black hole!')
        print()

print('Knock knock.')
input3 = input()
if input3 != 'Who\'s there?':
        print('Hey! Play along!')
        time.sleep(3)
        print('Sheesh.')
        time.sleep(1)
print('Delayed cow.')
time.sleep(4)
print('MOO!')
