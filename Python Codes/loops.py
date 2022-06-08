
for i in range(6):
    print(i,end=' ')
print()
words=['eat','meet','sleep','good','poor']

for word in words:
    print(word,end=' ')

print()
i=0
while i<6:
    print(i,end=' ')
    i=i+1
print()

# additional controls

for i in range(6):
    if i%2==0:
        continue
    print(i)
else:
    print('I am getting executed because loop ended normally without any break condition.')