#importing needed libraries
import time

#entering our wordbook
calling_buk = {
    '+38','+7','+0'
}

#entering phone number
number = input('Type the phone number and we wil call it, maybe:\n')

#number is right
if number in calling_buk:
    print('Calling it, wait a minute')
    time.sleep(3)
    print("Heisenberg\n-Say my name")
    time.sleep(2.5)
    print("Jessie(hedgehog-fish)\n-Heisenberg")
    time.sleep(3.5)
    print("Heisenberg\n-You are damn right")
#another way
else:
    print("Джесі ті рібайож")

#exit
exit()
