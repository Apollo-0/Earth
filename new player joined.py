
import time

file = open("transcript1.txt","r")
transcript1 = []

for line in file:
    transcript1.append(line.strip())
    
file.close()

file = open("transcript2.txt","r")
transcript2 = []

for line in file:
    transcript2.append(line.strip())
    
file.close()

print()
#new player joined the lobby
print(transcript1[0])
time.sleep(1)
#welcome player : '?'
print(transcript1[1])
time.sleep(2)
print()
#hello?
print(transcript1[2])
time.sleep(2)
#is anybody out there?
print(transcript1[3])
time.sleep(2)
#...
print(transcript1[4])
time.sleep(3)
#hello!
print(transcript1[5])
time.sleep(2)
print()
#*from behind*
print(transcript2[0])
print()
time.sleep(2)
#hello.
print(transcript2[1])
print()
time.sleep(1.5)
#argg
print(transcript1[6])
print()
time.sleep(2)
print(transcript2[2])
time.sleep(2)
print()
#*stares*
print(transcript2[3])
print()
time.sleep(3)
#why are you yelling
print(transcript2[4])