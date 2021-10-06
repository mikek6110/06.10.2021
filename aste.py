fails= open('lapa.txt', 'w', encoding='utf-8')

linija1= 'Rozes ir sarkanas.\n'
linija2= 'Rozes nav sarkanas.\n'
linija3= 'Rozes bus sarkanas.\n'
linija4= 'Rozem jabut sarkanam.\n'

fails.write(linija1 + linija2 + linija3 + linija4)
fails.close()