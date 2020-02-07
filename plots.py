import matplotlib.pyplot as plt
import fforplot
import statistics

from_ar = open('ardata.txt', 'r+')
from_na = open('nadata.txt', 'r+')
from_ye = open('yedata.txt', 'r+')
ardat = from_ar.readlines()
nadat = from_na.readlines()
yedat = from_ye.readlines()

'''st,ust,et,uet,dur,ll,time,temp,hum,ws,press = ardat[10].split(',')
Year, month, day = st.split()[0].split('-')
h, m, s = st.split()[1].split(':')'''

def strtofloat(lst1):
	lst2 = []
	for l in lst1:
		lst2.append(float(l))
	return(lst2)


def counter(lst,o1,o2):
    time = []
    for i in range(o1,o2):
        #print(i)
        c = 0
        for l in lst:
            if int(l) == i:
                c = c + 1
        if o2 == 24:
            time.append(c/7)
        else:
            time.append(c)
    return(time)

def condit(para):
    if str(para)[0] != 'N':
        return(True)

def main(dat,opt,yer):
    hour = []
    months = []
    years = []
    Temperature = []
    Humidity = []
    Windspeed = []
    Pressure = []
    WSyearly =[]
    Tempyearly =[]
    for d in dat:
        st,ust,et,uet,dur,ll,time,temp,hum,ws,press = d.split(',')
        Year, month, day = st.split()[0].split('-')
        h, m, s = st.split()[1].split(':')
        if int(m) > 30:
            h= int(h) + 1
        if int(h) == 24:
            h = 0
        hour.append(h)
        months.append(int(month))
        years.append(int(Year))
        if condit(temp):
            Temperature.append(float(temp))
            if opt == 10 and float(Year) == float(yer):
                Tempyearly.append(float(temp))
        if condit(hum):
            Humidity.append(float(hum))
        if condit(ws):
            if opt == 10 and float(Year) == float(yer):
                WSyearly.append(float(ws))
            if float(ws) != 0:
                Windspeed.append(float(ws))
        if condit(press):
            Pressure.append(float(press))
    if opt == 1:
        return(counter(hour,0,24))
    if opt == 2:
        return(counter(months,4,11))
    if opt == 3:
        return(counter(years,2012,2020))
    if opt == 4:
        return(Temperature)
    if opt == 5:
        return(Humidity)
    if opt == 6:
        return(Windspeed)
    if opt == 7:
        return(Pressure)
    if opt == 10:
        if len(WSyearly) >1 :
            return(statistics.mean(WSyearly),statistics.mean(Tempyearly))
        else:
            return(None,0)




'''tempdat = strtofloat(main(ardat,4))
dewdat = strtofloat(main(ardat,5))
humdat = strtofloat(main(ardat,6))
presdat = strtofloat(main(ardat,7))

print(max(presdat))
#plt.subplots(nrows=2,ncols=2,sharex=False,sharey=False)
fig, ax = plt.subplots(2,2, figsize = (10,8)) #,sharey = True)
#plt.title('Distribution of meteorological parameters during thunderstorms')
plt.suptitle('Distribution of meteorological parameters during thunderstorm at Aragats station', fontsize = 16)     # (1)

ax[0, 0].hist(tempdat, bins=50, density=False,color = 'C0',hatch= "-",edgecolor = 'white')
#ax[0, 0].set_title('Distribution of meteorological parameters during Fair weather in Aragats', fontsize = 16)
ax[0,0].set_xlabel('Outside temperature (C)', fontsize = 14)
ax[0,0].set_ylabel('N of events', fontsize = 14)
ax[0,0].tick_params(axis='both', which='major', labelsize=14)
ax[0,1].hist(dewdat, bins=50, density=False,color = 'C3',hatch= "-",edgecolor = 'white')
ax[0,1].set_xlabel('Outside Humidity(%)', fontsize = 14)
ax[0,1].set_ylabel('N of events', fontsize = 14)
ax[0,1].tick_params(axis='both', which='major', labelsize=14)
ax[1,0].hist(humdat, bins=50, density=False,color = 'C1',hatch= "-",edgecolor = 'white')
ax[1,0].set_xlabel('Wind speed(m/s)', fontsize = 14)
ax[1,0].set_ylabel('N of events', fontsize = 14)
ax[1,0].tick_params(axis='both', which='major', labelsize=14)
ax[1,1].hist(presdat, bins=50,color = 'C2',hatch= "-",edgecolor = 'white')
ax[1,1].set_xlabel('Pressure(mbar)', fontsize = 14)
ax[1,1].set_ylabel('N of events', fontsize = 14)
ax[1,1].tick_params(axis='both', which='major', labelsize=14)

ax[1,1].set_ylim(0,70)
ax[1,0].set_ylim(0,70)
ax[0,1].set_ylim(0,70)
ax[0,0].set_ylim(0,70)
plt.savefig('Figure3.png', dpi = 600)

plt.show()'''
#---------------------------------------------------Figure 1----------------------------------------

'''l= max(main(ardat,1))+1

fig, ax = plt.subplots(figsize=(16, 12))

ax3=plt.subplot(2, 2, 1)
ax2=plt.subplot(2, 2, 2)
ax1=plt.subplot(2,2,(3,4))

fig.suptitle('Thunderstorm daily, monthly and yearly activity',fontsize = 20)
fforplot.hourlyplot(fig,ax1,main(ardat,1),main(nadat,1),main(yedat,1),8,l)
fforplot.monthlybar(main(ardat,2),main(nadat,2),main(yedat,2),ax2)
fforplot.yearlybar(main(ardat,3),main(nadat,3),main(yedat,3),ax3)
plt.savefig('Figure1.png')
plt.show()'''

#--------------------------------------------Figure2-----------------------------
arwinds = []
artemps = []
nawinds = []
natemps = []
yewinds = []
yetemps = []
for y in range(2012,2020):
    arwinds.append(main(ardat,10,y)[0])
    artemps.append(main(ardat,10,y)[1])
    nawinds.append(main(nadat,10,y)[0])
    natemps.append(main(nadat,10,y)[1])
    yewinds.append(main(yedat,10,y)[0])
    yetemps.append(main(yedat,10,y)[1])
fig, ax3 = plt.subplots(figsize=(14, 10))
#ax3=plt.subplot(1, 2, 1)
#ax2=plt.subplot(1, 2, 2)
fforplot.yearlyplot(arwinds,nawinds,yewinds,ax3)
#fforplot.yearlybar(artemps,natemps,yetemps,ax2)
plt.savefig('Figure2.png')#, dpi = 600)
plt.show()