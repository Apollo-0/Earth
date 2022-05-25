
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
print(transcript1[0])
time.sleep(1)
print(transcript1[1])
time.sleep(2)
print()
print(transcript1[2])
time.sleep(2)
print(transcript1[3])
time.sleep(1)
print(transcript1[4])
time.sleep(2)
print(transcript1[5])
time.sleep(1)
print()
print(transcript2[0])
print()
time.sleep(1)
print(transcript2[1])
print()
print(transcript1[6])
print()
time.sleep(1)
print(transcript2[2])