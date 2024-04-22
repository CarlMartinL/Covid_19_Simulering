from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime,timedelta   # for date functions
from matplotlib.dates import drange



def get_x_datoer_x_ticks(start_dato,slutt_dato,tidsteg):   # Genererer datoer fra start til slutt
    #Variabler

    nåværende_dato = start_dato
    # Setter standardvariabler/lister
    x_datoer = drange(start_dato,slutt_dato,tidsteg)
    x_ticks = []
    while nåværende_dato <  slutt_dato:
        x_ticks.append(nåværende_dato)
        nåværende_dato += tidsteg


    return x_datoer,x_ticks  # returnerer verdiene

def get_endring_ANTAL(antall,SR):
    # Utregning av nye smittede med naturlig parametere
    importert = 50 / 30  # Igjennomsnitt importerte vi 50 tilfeller hver måneder fra utlander
    ER = (SR) / 14  # Gjør om stigningsraten til kun endringsraten.
    nye_smittet = ER * antall
    #faktorer


    antall_smittede = (nye_smittet + importert)  # *populasjon)/2)

    return antall_smittede

def get_antall_imune():
    global y_nye_tilfeller
    global y_prosentvis_imunitet
    global dag_nr
    if len(y_nye_tilfeller) >= 182:
        fulstendig_imune = sum(y_nye_tilfeller) * y_prosentvis_imunitet[dag_nr - 1]
        grad_før_6md = 0.793
        grad_etter_6md = 0.793 - (len(y_nye_tilfeller) - 182) * 0.0001
        antall_før_6md = sum(y_nye_tilfeller[-182:]) * grad_før_6md  # FRA FHI
        antall_etter_6md = sum(y_nye_tilfeller) - antall_før_6md * grad_etter_6md

        antall_imune_nå = antall_før_6md + antall_etter_6md

    else:
        grad_før_6md = 0.793  # Fra FHI
        antall_imune_nå = sum(y_nye_tilfeller) * grad_før_6md
        fulstendig_imune = sum(y_nye_tilfeller) * y_prosentvis_imunitet[dag_nr - 1]

    return antall_imune_nå+fulstendig_imune

def get_faktorer():
    tetthet = get_tetthet_prosent() * nye_smittet  # I KM^2
    pop = ((populasjon - antall) / populasjon)
    imunitet = nye_smittet * prosentvis_imunitet[dag_nr - 1]
    return tetthet,pop,imunitet
def get_antall_imune():
    globals()
    if len(y_nye_tilfeller) >= 182:
        fulstendig_imune = sum(y_nye_tilfeller) * prosentvis_imunitet[dag_nr - 1]
        grad_før_6md = 0.793
        grad_etter_6md = 0.793 - (len(y_nye_tilfeller) - 182) * 0.0001
        antall_før_6md = sum(y_nye_tilfeller[-182:]) * grad_før_6md  # FRA FHI
        antall_etter_6md = sum(y_nye_tilfeller) - antall_før_6md * grad_etter_6md

        antall_imune_nå = antall_før_6md + antall_etter_6md

    else:
        grad_før_6md = 0.793  # Fra FHI
        antall_imune_nå = sum(y_nye_tilfeller) * grad_før_6md
        fulstendig_imune = sum(y_nye_tilfeller) * prosentvis_imunitet[dag_nr - 1]

    return antall_imune_nå+fulstendig_imune

def get_prosentvis_imunitet():
    globals()
    1/(populasjon/y_antall_imune[dag_nr])

def get_tetthet_prosent():
    globals()
    tetthet_i_prosent = sqrt(befolkningstetthet) * 0.001
    return tetthet_i_prosent
def get_antall_bærere():
    globals()
    if len(y_nye_tilfeller) >= 14:
        antall_nå = sum(y_nye_tilfeller[-14:])
    else:
        antall_nå = sum(y_nye_tilfeller)

    return antall_nå

def get_antall_syke():
    globals()
    if len(y_nye_tilfeller) >= 5:
        antall_nå = sum(y_nye_tilfeller[-5:])
    else:
        antall_nå = sum(y_nye_tilfeller)

    return antall_nå
