# cari solusi persamaan dari 3x + 2 = 11
# define hasil = 11
hasil = 11
print "bruteforcing..."
for x in range(1000):
    if (3*x) + 2 == hasil:
        break # stop bruteforcing
        print "found!", x

