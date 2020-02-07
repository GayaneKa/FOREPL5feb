import matplotlib.pyplot as plt
import numpy as np
h = "xx"
def hourlyplot(fig,ax1,arag,nora,yere,i,lim):
    aragats = arag
    noramberd = nora
    yerevan = yere
    y_pos = np.arange(len(aragats))
    ax1.set_ylim(0,lim)
    ax1.bar(y_pos, aragats, width = 0.3, label = 'Aragats',  hatch= "-", edgecolor = 'white', color='C0')
    ax1.bar(y_pos - 0.3, noramberd,width = 0.3,label = 'Nor Amberd', hatch= "\\\\", edgecolor = 'white', color='C3')
    ax1.bar(y_pos + 0.3, yerevan,width = 0.3,label = 'Yerevan', hatch= h, edgecolor = 'white', color='C1')
    ax1.tick_params(axis='both', which='major', labelsize=16)
    ax1.set_ylabel('Averaged count of event per year', fontsize = 18, labelpad = 18)
    ax1.set_xlabel('Time(LT)', fontsize = 18)
    ax1.text(-1, -1.2, 'c)', fontsize = 16)

def monthlybar(mlst1,mlst2,mlst3,ax2):
    ind1 = np.arange(7)

    ax2.bar(ind1  , mlst1 ,width = 0.3,label = 'Aragats', hatch= "-", edgecolor = 'white', color='C0')
    ax2.bar(ind1 - 0.3, mlst2 ,width = 0.3,label = 'Nor Amberd',  hatch= "\\\\", edgecolor = 'white', color='C3')
    ax2.bar(ind1 + 0.3, mlst3 ,width = 0.3,label = 'Yerevan', hatch= h, edgecolor = 'white', color='C1')
    ax2.set_ylim(0,120)
    xTickMarks = [' ','April','May','June','July','Aug.','Sept.','Oct.']
    xtickNames = ax2.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, fontsize = 16)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    ax2.set_ylabel('Count of Thunderstorm', fontsize = 18)
    ax2.set_xlabel('Months', fontsize = 18)
    ax2.text(-1, -15, 'b)', fontsize = 16)
    ax2.legend(fontsize = 18)
def yearlybar(lst1,lst2,lst3,ax3):
    ind = np.arange(8)
    ax3.bar(ind  , lst1 ,width = 0.3,label = 'Aragats', hatch= "-", edgecolor = 'white', color='C0')
    ax3.bar(ind - 0.3, lst2 ,width = 0.3,label = 'Nor Amberd', hatch= "\\\\", edgecolor = 'white', color='C3')
    ax3.bar(ind + 0.3, lst3 ,width = 0.3,label = 'Yerevan', hatch= h, edgecolor = 'white', color='C1')
    #ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize = 13)
    ax3.legend(fontsize = 18)
    ax3.tick_params(axis='y', which='major', labelsize=18)
    ax3.set_ylim(0,120)
    #ax3.set_ylim(0,14)
    xTickMarks = [' ','2012','2013','2014','2015','2016','2017','2018','2019']
    xtickNames = ax3.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, fontsize = 16)
    
    ax3.set_ylabel('Count of Thunderstorm', fontsize = 16)
    #ax3.set_title('Averaged max wind speed during thunderstorms (2012-2019)', fontsize = 22)
    #ax3.set_ylabel('Averaged wind speed(m/s)', fontsize = 20)
    ax3.set_xlabel('Years', fontsize = 20)
    ax3.text(-1, -15, 'a)', fontsize = 18)

