import os
compiled=[]
for x in os.listdir('.'):
    with open(x, encoding='utf-16') as f:
        compiled.append(f.read())
print('\n'.join(compiled))
