from matplotlib import pyplot as plt
from get_values_ÅR_SR_BT import kjør
from plot import plot_grafer_f,plot_antall_f,plott_vaksinerte_f
from datetime import datetime
import numpy as np
import warnings

#Setup
warnings.simplefilter("ignore",np.RankWarning)
plt.style.use("ggplot")

#Naturlige parametere
SR = 1.3    #Antall hver syke smitter i løpet av sin bæreperiode
pop = 6_000_000   #befolkning
BT = 24000  #Befolkningstetthet: Fra 0-25_000 pers/KM^2,                      #240
KE = 0.7 #Karantene efekt                                                      #0.8
#VE = 0.9   #Vaksinesns effektivitet.

#Kunstige parametere
VR = 120_000 # vaksinerte per måned
VR_start  = datetime(2020,12,21)   #Dag inført vaksine, 2020,12,21
VR_stop = datetime(2024,1,9)
KT_start  = datetime(2020,8,30)   #Dag inført karantene, 2020,08,30
KT_stop = datetime(2021 ,12,1)


#Her setter vi y verdiene
x_ticks, y_antall_imune, y_nye_tilfeller, y_alle_tilfeller, y_antall_syke, y_antall_bærere,y_antall_vaksinerte = kjør("20")
x_ticks2, y_antall_imune2, y_nye_tilfeller2, y_alle_tilfeller2, y_antall_syke2, y_antall_bærere2,y_antall_vaksinerte = kjør("22")

#plt.tight_layout()

plot_grafer_f()
plot_antall_f()
#plott_vaksinerte_f()
plt.show()

