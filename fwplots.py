import matplotlib.pyplot as plt
import fforplot
import statistics
import numpy as np

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
    aa = '((datetime.datetime('
    for d in dat:
        for j in range(len(d.split(aa))):
            dt = d.split(aa)[j]
            if len(dt) > 0:
                year, month, day, h,m,temp,hum,ws,press,something = dt.split(',')
                if float(year) == yer and condit(temp):
                    if str(temp)[1] != 'N':
                        #print(temp, float(temp))
                        Temperature.append(float(temp))
                '''if condit(hum):
                    Humidity.append(float(hum))
                if condit(ws):
                    if float(ws) != 0:
                        Windspeed.append(float(ws))
                if condit(press):
                    if float(press.split(')')[0]) < 950:
                        Pressure.append(float(press.split(')')[0]))'''
            else:
                continue
        #return(Temperature,Humidity,Windspeed,Pressure)
    try:
        return(statistics.mean(Temperature))
    except:
        return(None)
'''dat1 = []
dat2 = []
dat3 = []
for y in range(2012,2019):
    dat1.append(main(ardat,1,y))
    dat2.append(main(nadat,1,y))
    dat3.append(main(yedat,1,y))
print(dat1)
print(dat2)
print(dat3)'''
'''fig, ax = plt.subplots(2,2, figsize = (12,8)) #,sharey = True)
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
plt.savefig('Figure7q.png', dpi = 600)

plt.show()'''

def yearlybar(lst1,lst2,lst3,ax3,tt):
    ind = np.arange(7)
    ax3.bar(ind  , lst1 ,width = 0.3,label = 'Aragats', hatch= "-",edgecolor = 'white', color='C0')
    ax3.bar(ind - 0.3, lst2 ,width = 0.3,label = 'Nor Amberd', hatch= "\\\\",edgecolor = 'white', color='C3')
    ax3.bar(ind + 0.3, lst3 ,width = 0.3,label = 'Yerevan',  hatch= 'xx', edgecolor = 'white', color='C1')
    #ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize = 13)
    #ax3.legend(title = tt,fontsize = 14)
    ax3.tick_params(axis='y', which='major',labelsize=14)
    #ax3.set_ylim(0,120)
    ax3.set_ylim(0,30)
    xTickMarks = [' ','2012','2013','2014','2015','2016','2017','2018','2019']
    xtickNames = ax3.set_xticklabels(xTickMarks)
    plt.setp(xtickNames,fontsize=14)
    leg = ax3.legend(fontsize = 14)
    leg.set_title(tt,prop={'size':14})
    ax3.set_ylabel('Temperature(C)',fontsize=14)
    #ax3.set_title('Averaged max wind speed during thunderstorms (2012-2019)', fontsize = 22)
    #ax3.set_ylabel('Averaged wind speed(m/s)', fontsize = 20)
    ax3.set_xlabel('Years',fontsize=14)


arfw = [7.65164177989337, 4.247474731795916, 8.337681181647856, 8.830650167453216, 7.285443037253203, 8.160952378667536, 8.074033151468191]
nafw = [12.058333347241083, 11.577251216105376, 15.073018287842322, 16.839251042735064, 14.962929053372731, 16.5813559501374, 15.849693884122736]
yefw = [0, 19.740488847434584, 20.87193717080417, 22.76706763532825, 20.972662710155962, 22.85959913408706, 21.196266056080823]


ar = [3.673437513760291, 2.24871800133051, 4.035384609951422, 1.9337662593884901, 3.473529404577087, 1.4263157682460652, 4.323684190841098]
na =[9.980000019073486, 10.661904755092802, 11.39705880950479, 11.526829242706299, 11.531999969482422, 11.758064577656407, 11.641025711328556]
ye =[0, 14.433333290947807, 18.340000009536745, 16.894117579740637, 19.12500003973643, 19.56666660308838, 22.55714289347331]

fig = plt.subplots(figsize=(10, 10))
ax1=plt.subplot(2, 1, 1)
ax2=plt.subplot(2, 1, 2)

#ax1, ax2 = plt.subplots()
yearlybar(arfw,nafw,yefw,ax1, 'Fair weather')
yearlybar(ar,na,ye,ax2, 'Thunderstorm')

plt.savefig('Figure8.png')
plt.show()