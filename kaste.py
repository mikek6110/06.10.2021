import os
#os.remove('aste.txt')
if os.path.exists('kaste.txt'):
    os.rename('kaste.txt', 'kastite.txt')
else:
    print('Fails neeksiste')