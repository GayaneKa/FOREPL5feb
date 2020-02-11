import matplotlib.pyplot as plt
import fforplot
import statistics

from_ar = open('fwaragdata.txt', 'r+')
from_na = open('fwnadata.txt', 'r+')
from_ye = open('fwyedata.txt', 'r+')
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

def main(dat,opt):
    hour = []
    months = []
    years = []
    Temperature = []
    Humidity = []
    Windspeed = []
    Pressure = []
    WSyearly =[]
    Tempyearly =[]
    aa = '((datetime.datetime('
    for d in dat:
        for j in range(len(d.split(aa))):
            dt = d.split(aa)[j]
            if len(dt) > 0:
                year, month, day, h,m,temp,hum,ws,press,something = dt.split(',')
                if condit(temp):
                    if str(temp)[1] != 'N':
                        #print(temp, float(temp))
                        Temperature.append(float(temp))
                if condit(hum):
                    Humidity.append(float(hum))
                if condit(ws):
                    if float(ws) != 0:
                        Windspeed.append(float(ws))
                if condit(press):
                    if float(press.split(')')[0]) < 950:
                        Pressure.append(float(press.split(')')[0]))
            else:
                continue
        return(Temperature,Humidity,Windspeed,Pressure)



#main(nadat,1)

fig, ax = plt.subplots(2,2, figsize = (12,8)) #,sharey = True)
#plt.title('Distribution of meteorological parameters during thunderstorms')
plt.suptitle('Distribution of meteorological parameters during fair weather at Yerevan station', fontsize = 16)     # (1)

ax[0, 0].hist(strtofloat(main(yedat,4)[0]), bins=30, density=False,color = 'C1',alpha = 0.8, edgecolor = 'C1') #,hatch= "xx",edgecolor = 'C1')
ax[0, 0].hist(strtofloat(main(nadat,4)[0]), bins=30, density=False,color = 'C3',alpha = 0.7, edgecolor = 'C3')  #,hatch= "xx", edgecolor = 'C3')
ax[0, 0].hist(strtofloat(main(ardat,4)[0]), bins=30, density=False,color = 'C0',alpha = 0.7, edgecolor = 'C0') #,hatch= "xx", edgecolor = 'C0')

#ax[0, 0].set_title('Distribution of meteorological parameters during Fair weather in Aragats', fontsize = 16)
ax[0,0].set_xlabel('Outside temperature (C)', fontsize = 14)
ax[0,0].set_ylabel('N of events', fontsize = 14)
ax[0,0].tick_params(axis='both', which='major', labelsize=14)
ax[0,1].hist(strtofloat(main(yedat,5)[1]), bins=30, label = 'Aragats',density=False,color = 'C1',alpha = 0.7, edgecolor = 'C1')
ax[0,1].hist(strtofloat(main(nadat,5)[1]), bins=30, label = 'Nor Amberd',density=False,color = 'C3',alpha = 0.7, edgecolor = 'C3')
ax[0,1].hist(strtofloat(main(ardat,5)[1]), bins=30, label = 'Yerevan',density=False,color = 'C0',alpha = 0.8,edgecolor = 'C0')
ax[0,1].set_xlabel('Outside Humidity(%)', fontsize = 14)
ax[0,1].set_ylabel('N of events', fontsize = 14)
ax[0,1].tick_params(axis='both', which='major', labelsize=14)
ax[1,0].hist(strtofloat(main(yedat,6)[2]), bins=30, density=False,color = 'C1',alpha = 0.7, edgecolor = 'C1')
ax[1,0].hist(strtofloat(main(nadat,6)[2]), bins=30, density=False,color = 'C3',alpha = 0.7, edgecolor = 'C3')
ax[1,0].hist(strtofloat(main(ardat,6)[2]), bins=30, density=False,color = 'C0',alpha = 0.8,edgecolor = 'C0')
ax[1,0].set_xlabel('Wind speed(m/s)', fontsize = 14)
ax[1,0].set_ylabel('N of events', fontsize = 14)
ax[1,0].tick_params(axis='both', which='major', labelsize=14)
ax[1,1].hist(strtofloat(main(yedat,7)[3]), bins=30,label = 'Aragats', density=False,color = 'C1',alpha = 0.7,hatch= "xx", edgecolor = 'C1')
ax[1,1].hist(strtofloat(main(nadat,7)[3]), bins=30,label = 'Nor Amberd', density=False,color = 'C3',alpha = 0.7,hatch= "xx", edgecolor = 'C3')
ax[1,1].hist(strtofloat(main(ardat,7)[3]), bins=30,label = 'Yerevan', density=False,color = 'C0',alpha = 0.8,hatch= "xx",edgecolor = 'C0')
ax[1,1].set_xlabel('Pressure(mbar)', fontsize = 14)
ax[1,1].set_ylabel('N of events', fontsize = 14)
ax[1,1].tick_params(axis='both', which='major', labelsize=14)
#ax[0,1].legend(loc='upper center',  shadow=True,  bbox_to_anchor=(1.2, 0.8),ncol=1, fontsize = 16)
fig.legend(labels=['Yerevan ','Nor Amberd','Aragats'],   # The labels for each line
           loc="right",   # Position of legend
           fontsize = 14)
           #bbox_to_anchor=(1.01, 0.8))

plt.subplots_adjust(left=None, bottom=None, right=0.8, top=None, wspace=None, hspace=None)

ax[1,1].set_ylim(0,650)
ax[1,0].set_ylim(0,650)
ax[0,1].set_ylim(0,650)
ax[0,0].set_ylim(0,650)
plt.savefig('Figure7.png') #, dpi = 600)

plt.show()