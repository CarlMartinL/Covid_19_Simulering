from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def plott_vaksinerte_f():
    from main import y_antall_vaksinerte,pop,x_ticks,y_antall_syke2,y_antall_imune2,y_antall_syke
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    #setup
    fig1,ax=plt.subplots(nrows=1,ncols=1)
    #Definering
    vaksinerte = y_antall_vaksinerte
    ikke_vaksinerte = []
    for i in range(len(y_antall_vaksinerte)):
        ikke_vaksinerte.append(pop - vaksinerte[i]-y_antall_syke2[i])


    #FunkAnimation
    def myupdating(i):
        #loopen
        ax.clear()
        if i >= 26:     #i = frame_nr
            index = i-26
            size=[vaksinerte[i % len(ikke_vaksinerte)], ikke_vaksinerte[i % len(ikke_vaksinerte)], sum(y_antall_syke2[index:i])]

        else:
            size = [vaksinerte[i % len(ikke_vaksinerte)], ikke_vaksinerte[i % len(ikke_vaksinerte)], sum(y_antall_syke2[0:i])]

        #tittel
        title_dato = str(x_ticks[i % len(ikke_vaksinerte)])
        antall_imune = y_antall_imune2[i % len(ikke_vaksinerte)]
        imune_prosent = round(antall_imune/pop*100,2)
        title_imune_prosent = "Antall Imune: " +str(imune_prosent)+"%"
        #Labels
        labels = ["Vaksinerte", "Rest_befolkning", "Syke, gjennomsnittsår"]

        #plot
        ax.pie(size,labels=labels,wedgeprops={'edgecolor':'black'},
            autopct='%.f%%',explode=(0.0,0,0),shadow=True)

        fig1.suptitle(title_dato)
        ax.set_title(title_imune_prosent)

    myanimation=FuncAnimation(fig1,myupdating,interval=0.1,cache_frame_data=False)
    plt.show()

def plot_grafer_f():
    from main import x_ticks, y_antall_imune, y_nye_tilfeller, y_alle_tilfeller, y_antall_syke, y_antall_bærere,x_ticks2, y_antall_imune2, y_nye_tilfeller2, y_alle_tilfeller2, y_antall_syke2, y_antall_bærere2,VR_start, VR_stop,KT_start,KT_stop
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex=True)
    ax1.plot(x_ticks, y_antall_imune)#, label="Antall Imune, 2020")
    ax1.plot(x_ticks, y_antall_imune2)#, label="Antall Imune, 2022")

    ax2.plot(x_ticks, y_nye_tilfeller,label="2020")
    ax2.plot(x_ticks, y_nye_tilfeller2,label="2022")

    ax3.plot(x_ticks, y_alle_tilfeller)#, label="alle tilfeler, 2020")
    ax3.plot(x_ticks, y_alle_tilfeller2)#, label="alle tilfeler, 2022")

    ax4.plot(x_ticks, y_antall_syke)#, label="Antall syke, 2020")
    #ax4.plot(x_ticks, y_antall_bærere, label="Antall bærere, 2020")
    ax4.plot(x_ticks, y_antall_syke2)#, label="Antall syke, 2022")
    #ax4.plot(x_ticks, y_antall_bærere2, label="Antall bærere, 2022")

    #Plotting karantene
    ax1.fill_between(x_ticks,y_antall_imune, where=(np.array(x_ticks) >= KT_start) & (np.array(x_ticks) <= KT_stop),color="#00FF00",alpha=0.5,edgecolor="#000000")
    ax2.fill_between(x_ticks, y_nye_tilfeller2, where=(np.array(x_ticks) >= KT_start) & (np.array(x_ticks) <= KT_stop),color="#00FF00", alpha=0.5,edgecolor="#000000",label="Karantene_periode")
    ax3.fill_between(x_ticks, y_alle_tilfeller2, where=(np.array(x_ticks) >= KT_start) & (np.array(x_ticks) <= KT_stop),color="#00FF00", alpha=0.5,edgecolor="#000000")
    ax4.fill_between(x_ticks, y_antall_syke2, where=(np.array(x_ticks) >= KT_start) & (np.array(x_ticks) <= KT_stop),color="#00FF00", alpha=0.5,edgecolor="#000000")

    #Prolling vaksine
    ax1.fill_between(x_ticks, y_antall_imune, where=(np.array(x_ticks) >= VR_start) & (np.array(x_ticks) <= VR_stop),color="yellow", alpha=0.5,edgecolor="blue")
    ax2.fill_between(x_ticks, y_nye_tilfeller2, where=(np.array(x_ticks) >= VR_start) & (np.array(x_ticks) <= VR_stop),color="yellow", alpha=0.5,edgecolor="blue",label="Vaksineringsperiode")
    ax3.fill_between(x_ticks, y_alle_tilfeller2, where=(np.array(x_ticks) >= VR_start) & (np.array(x_ticks) <= VR_stop),color="yellow", alpha=0.5,edgecolor="blue")
    ax4.fill_between(x_ticks, y_antall_syke2, where=(np.array(x_ticks) >= VR_start) & (np.array(x_ticks) <= VR_stop),color="yellow", alpha=0.5,edgecolor="blue")

    #Regresjon. Norges epedemi
    data = pd.read_csv("Smitterate_Norge", delimiter=",")
    dager_norge = np.array(data["måned"]) * 30  # Ganger med 30 siden vi jobber med dager
    rate = data["smitterate"]

    reg = np.polyfit(dager_norge, rate, 50)
    x = []
    for i in dager_norge:
        x.append(x_ticks[i])

    y = np.polyval(reg, dager_norge)
    ax2.plot(x, y, c="black", linestyle="--",label="data",linewidth=1)
    ax2.scatter(x,rate,c="#0000aa",s=15)

    #Pynt
    ax1.set_yticks([1_000_000,2000000,3000000,4_000_000,5_000_000],["1mil","2mil","3mil","4mil","5mil"])
    ax2.set_yticks([1_000,5_000, 10_000, 15_000, 20_000, 25_000], ["1K", "5K", "10K", "15K","20K","25K"])
    ax3.set_yticks([100_000, 2_000_000, 3_000_000, 4_000_000,6_000_000], ["100K", "2mil", "3mil", "4mil","6mil"])
    ax4.set_yticks([10_000, 30_000, 50_000, 70_000, 100_000],[10_000, 30_000, 50_000, 70_000, 100_000])
    #Layout
    plt.xticks(rotation=45)
    ax1.set_title("imune")
    ax2.set_title("nye tilfeller/dag")
    ax3.set_title("Totalt antall tilfeller")
    ax4.set_title("Syke")
    ax2.legend(loc=(0.7,0.2))
    for i in (ax1,ax2,ax3,ax4):
        pass
        #i.grid


def plot_antall_f():
    from main import x_ticks, y_antall_imune, y_nye_tilfeller, y_alle_tilfeller, y_antall_syke, y_antall_bærere,x_ticks2, y_antall_imune2, y_nye_tilfeller2, y_alle_tilfeller2, y_antall_syke2, y_antall_bærere2,VR_start,VR_stop,KT_start,KT_stop
    plt.style.use("fivethirtyeight")
    fig2,ax = plt.subplots(nrows=1,ncols=1)
    ax.plot(x_ticks, y_nye_tilfeller, label="2020",c="red")
    ax.plot(x_ticks, y_nye_tilfeller2, label="2022",c="blue")

    # Regresjon. Norges epedemi
    data = pd.read_csv("Smitterate_Norge", delimiter=",")
    dager_norge = np.array(data["måned"]) * 30  # Ganger med 30 siden vi jobber med dager
    rate = data["smitterate"]

    reg = np.polyfit(dager_norge, rate, 50)
    x = []
    for i in dager_norge:
        x.append(x_ticks[i])

    y = np.polyval(reg, dager_norge)
    ax.plot(x, y, c="black", linestyle="--", label="data", linewidth=1)
    ax.scatter(x, rate, c="#0000aa", s=15)


    ax.fill_between(x_ticks, y_nye_tilfeller2, where=(np.array(x_ticks) >= KT_start) & (np.array(x_ticks) <= KT_stop),color="#00FF00", alpha=0.5, edgecolor="#000000", label="Karantene_periode")
    ax.fill_between(x_ticks, y_nye_tilfeller2, where=(np.array(x_ticks) >= VR_start) & (np.array(x_ticks) <= VR_stop),color="yellow", alpha=0.5,edgecolor="blue",label="Vaksineringsperiode")
    plt.xticks(rotation=45)
    ax.set_title("Antall tilfeller/dag")
    ax.legend()







