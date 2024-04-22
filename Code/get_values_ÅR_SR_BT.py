from datetime import datetime,timedelta   # for date functions
from Funksjoner import get_x_datoer_x_ticks
from math import sqrt

def kjør(år):
    from main import SR,VR,BT,pop,VR_start,VR_stop,KT_start,KT_stop,KE
    #Startvariabler
    start_dato = datetime(2020,6,23)
    slutt_dato = datetime(2023,12,31)
    nåværende_dato = start_dato
    tidsteg = timedelta(days=1)

    #Naturlige parametere
    #SR = 1.05   #Smittespredning per pers. Ikke for høy
    populasjon = pop   # 6 MIllioner
    befolkningstetthet = BT
    i_karantene = bool
    i_karantene = False



    x_datoer,x_ticks = get_x_datoer_x_ticks(start_dato,slutt_dato,tidsteg)

    #Y-Verdier og parametere: Lister og arrays
    y_nye_tilfeller = [1]
    y_antall_syke = [1]
    y_alle_tilfeller = [1]
    y_antall_bærere = [1]
    y_antall_imune = [1]
    y_antall_vaksinerte = [0]
    y_prosentvis_imunitet = [0]   #I komma, feks: "0.1 = 10%"

    #Faktorer
    tetthet_faktor = [0]
    pop_faktor = [0]
    imunitet_faktor = [0]



    #Endring
    def get_endring_ANTAL(antall):
        # Utregning av nye smittede med naturlig parametere
        importert = 50 / 30  # Igjennomsnitt importerte vi 50 tilfeller hver måneder fra utlander
        ER = SR / 14  # Gjør om stigningsraten til kun endringsraten.
        nye_smittet = ER * antall
        tetthet_f = tetthet_faktor[dag_nr-1]
        imunitet_f = imunitet_faktor[dag_nr-1]
        pop_f = pop_faktor[dag_nr - 1]
        kar_f = get_karantene_faktor()


        antall_smittede = (nye_smittet + importert)*imunitet_f*tetthet_f*pop_f*kar_f  # *populasjon)/2)

        return antall_smittede
    #Imunitet
    def get_antall_imune():

        if år == "20":
            if len(y_nye_tilfeller) >= 182:
                fulstendig_imune = sum(y_nye_tilfeller) * y_prosentvis_imunitet[dag_nr - 1]
                grad_før_6md = 0.793 #i følge FHI 2020
                grad_etter_6md = 0.793 - (len(y_nye_tilfeller) - 182) * 0.0001
                antall_før_6md = sum(y_nye_tilfeller[-182:]) * grad_før_6md  # FRA FHI
                antall_etter_6md = sum(y_nye_tilfeller) - antall_før_6md * grad_etter_6md

                antall_imune_nå = antall_før_6md + antall_etter_6md

            else:
                grad_før_6md = 0.793  # Fra FHI
                antall_imune_nå = sum(y_nye_tilfeller) * grad_før_6md
                fulstendig_imune = sum(y_nye_tilfeller) * y_prosentvis_imunitet[dag_nr - 1]

            return antall_imune_nå+fulstendig_imune
        elif år == "22":
            globals()
            if len(y_nye_tilfeller) >= 93:

                fulstendig_imune = sum(y_nye_tilfeller) * y_prosentvis_imunitet[dag_nr - 1]
                antall_imune_nå = sum(y_nye_tilfeller[-93:])  # fra sykepleren.no
            else:
                fulstendig_imune = sum(y_nye_tilfeller) * y_prosentvis_imunitet[dag_nr - 1]
                antall_imune_nå = sum(y_nye_tilfeller)  # fra sykepleren.no

            return antall_imune_nå+fulstendig_imune
    def get_imunitet_prosent():
        globals()
        prosentvis_imunitet = 1/(populasjon/y_antall_imune[dag_nr-1])
        return prosentvis_imunitet
    #Faktorer, y verdier og sjekkere
    def get_tetthet_faktor():
        globals()
        tetthet_i_prosent = sqrt(befolkningstetthet) * 0.001
        if tetthet_i_prosent < 1:
            tetthet_f = (1+tetthet_i_prosent)
        return tetthet_f
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
    def get_pop_faktor():
        pop_max_f = ((populasjon - y_antall_bærere[dag_nr-1]) / populasjon)
        return pop_max_f
    def get_imunitet_faktor():
        if get_imunitet_prosent() < 1:
            imunitet_faktor = 1-y_prosentvis_imunitet[dag_nr-1]
            return imunitet_faktor
        else:
            return 1
    def sjekk_om_karantene():
        #print(KT)
        #print(x_ticks[dag_nr])
        if KT_start < x_ticks[dag_nr] and KT_stop >= x_ticks[dag_nr]:
            return True
        else:
            return False
    def get_karantene_faktor():
        bool = sjekk_om_karantene()
        if bool == True:
            return KE
        else:
            return 1
    def sjekk_om_vaksinerer():
        if VR_start < x_ticks[dag_nr] and VR_stop >= x_ticks[dag_nr]:
            return True
        else:
            return False
    def get_vakksinerte():
        if sjekk_om_vaksinerer() == True:
            return y_antall_vaksinerte[dag_nr-1]+VR/90   #Egt 30, men måtte lage en kjapp formel mtp 3 doser og slik
        else:
            return y_antall_vaksinerte[dag_nr-1]


    #Hovedløkka, motoren bak alt
    for i in range(1,len(x_datoer)):
        global dag_nr
        dag_nr = i
        y_nye_tilfeller.append(get_endring_ANTAL(y_antall_bærere[dag_nr-1]))
        #print("y_nye_tilfeller: ",get_endring_ANTAL(y_nye_tilfeller[dag_nr-1]))
        y_prosentvis_imunitet.append(get_imunitet_prosent())    #Faktor
        #print("prosentvis_imunitet: ", get_prosentvis_imunitet())
        y_antall_imune.append(get_antall_imune()+y_antall_vaksinerte[dag_nr-1])  # bygger på prosentvis
        #print("y_antall_imune: ", get_antall_imune())
        y_antall_bærere.append(get_antall_bærere())
        #print("y_antall_bærere: ",get_antall_bærere())
        y_antall_syke.append(get_antall_syke())
        #print("y_antall_syke: ",get_antall_syke())
        pop_faktor.append(get_pop_faktor()) # Denne skal ganges med
        #print("pop_faktor: ",get_imunitet_faktor())
        tetthet_faktor.append(get_tetthet_faktor())    # Denne skal ganges med
        #print("Tetthet_faktor: ", get_tetthet_faktor())
        imunitet_faktor.append(get_imunitet_faktor())
        #print("imunitet_faktor: ", get_imunitet_faktor())
        y_alle_tilfeller.append(y_alle_tilfeller[i-1]+y_nye_tilfeller[i])
        #print("y_alle_tilfeller: ",y_alle_tilfeller[i-1]+y_nye_tilfeller[i] )
        kar_f = get_karantene_faktor()
        #print("kaf_f: ", kar_f)
        y_antall_vaksinerte.append(get_vakksinerte())

        #Skriving til fil



    return x_ticks,y_antall_imune, y_nye_tilfeller,y_alle_tilfeller,y_antall_syke,y_antall_bærere,y_antall_vaksinerte









