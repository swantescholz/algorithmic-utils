from plotting import *


res_path = "/home/swante/ownCloud/mensa/mywes/artikel-nov18/"

lines = [it for it in open("../in.txt")][1:]
medians, sds, ages, sizes, internationals, newcomers, places = [],[],[],[],[], [], []

for line in lines:
    median, sd, age,size,international,newcomer,place = line.split("\t")
    median, sd, age = map(float, (median, sd, age))
    size, international, newcomer = map(int, [size, international, newcomer])
    medians.append(median)
    sds.append(sd)
    ages.append(age)
    sizes.append(size)
    internationals.append(international)
    newcomers.append(newcomer)
    places.append(place)

for i in range(1,len(places),2):
    places[i] = "\n" + places[i]


indices = np.arange(len(places))
opacity = 0.72

bar_width = 0.28
plt.bar(indices, sizes, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Insgesamt')

plt.bar(indices + bar_width, newcomers, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Erstteilnehmer')
plt.bar(indices + 2*bar_width, internationals, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Internationale')

plt.xlabel('Weekend')
plt.ylabel('Teilnehmer')
plt.xticks(indices + bar_width, places)
plt.legend()

myshow()

indices = indices[:-1]
medians = medians[1:]
places = places[1:]
ages = ages[1:]
sds = sds[1:]
bar_width = 0.75
plt.bar(indices, ages, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Durchschnitt, mit\nStandardabweichung')

# plt.bar(indices + bar_width, medians, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Median')
plt.errorbar(indices, ages, yerr=sds, fmt='ko')
plt.xlabel('Weekend')
plt.ylabel('Alter')
plt.xticks(indices, places)
plt.legend()
save_image("alter.png", 1000,400)
myshow()