import csv
import sys
import os

#FichierToDO="FEDE_NM3_I_53_US_O_BEZONS_-_1_WASQUEHAL_FLASH_B_200000009072594.txt"
#FichierToDO="Feuille_de_Marque_[2018-09-22_reg_NM3_ASA_SCEAUX-US_O_BEZONS_1] - Copie.txt"
#FichierToDO="Feuille_de_Marque_[2018-09-30_reg_RM3_US_O_BEZONS_2-BC_CHILLY_MAZAR].txt"

def GiveMeDedos(myfile):

    All_Dedos=""
    #myfile = os.path.join('C:\\USOB', FichierToDO)

    # Chargement Feuille de Match convertie.
    file = open("%s" %(myfile), "rt")
    txt=file.read()


    # RECUPERATION : MATCH (Numero et DAte)
    Pos_GAME=txt.find('Rencontre N°')
    nb_car=len('Rencontre N°')
    Game_Nb=txt[Pos_GAME+nb_car:Pos_GAME+nb_car+6]
    Game_Date=txt[Pos_GAME+nb_car+11:Pos_GAME+nb_car+11+8]
    #print("Rencontre N°" + Game_Nb)
    #print("Rencontre jouée le " + Game_Date)

    #####################################
    # RECHERCHE des informations importantes :
    #########################################

    # Equipe qui recoit
    Pos_Team_Home=txt.find('Équipe A')
    TEAM_HOME=txt[Pos_Team_Home+10:Pos_Team_Home+10+93]
    TEAM_HOME=TEAM_HOME.replace('.','')
    Pos_Licences_HOME=txt.find('LICENCES')
    Pos_Entraineur_HOME=txt.find('Entraîneur')
    # Est-ce bezons ?
    if TEAM_HOME.find('BEZONS')>0:
        Game_Lieu="DOMICILE"
    else:
        Game_Lieu="EXTERIEUR"

   # print(Pos_Licences_HOME , Pos_Entraineur_HOME, Pos_Team_Home, TEAM_HOME,Game_Lieu)

    # Equipe en déplacement
    TEAM_VISITOR=txt[Pos_Team_Home+115:Pos_Team_Home+115+91]
    TEAM_VISITOR=TEAM_VISITOR.replace('.','')

    Pos_Licences_VISITORS=txt.find('LICENCES',Pos_Licences_HOME+10)
    Pos_Entraineur_VISITORS=txt.find('Entraîneur',Pos_Licences_VISITORS+10)
    #print(Pos_Licences_VISITORS,Pos_Entraineur_VISITORS,TEAM_VISITOR,Game_Lieu)



    #Fin Section Licences :
    Pos_MARQUE_COURANTE=txt.find('MARQUE COURANTE')


    # Début section : Officiels
    Pos_Officiels = txt.find('OFFICIELS, DÉLÉGUÉ DE CLUB ET DÉLÉGUÉ AUX OFFICIELS')
    Pos_1st_Arbitre= txt.find('1er arbitre')
    Pos_2sd_Arbitre= txt.find('2e arbitre')
    Pos_Commisaire= txt.find('Commissaire')
    Pos_Marqueur= txt.find('Marqueur')
    Pos_Aide_Marqueur= txt.find('Aide-marqueur')
    Pos_Chrono= txt.find('Chronométreur')
    Pos_Delegue= txt.find('Délégué de club Délégué aux officiels')



    # RECHERCHE LICENCIES DEDOS
       ## Update du 10/11/18 suppression de "VT749226":"JEAN-BAPTISTE"}
    Liste_Licences_DEDOS = {"VT550082":"LE ROY",
                            "VT757569":"MENDES",
                            "VT754483":"LASSEN",
                            "VT711304":"SEKKAI",
                            "VT000004":"STEPHANE",
                            "VT710821":"DEBROISE",
                            "VT740652":"ATADEGNON",
                            "VT841052":"DIMOUAMOUA",
                            "VT890456":"RAMIREZ",
                            "VT751789":"CHOUPAS",
                            "VT772029":"EL OUKID",
                            "VT797813":"EL OUKID",
                            "VT718940":"ORTOLANI",
                            "VT891527":"CHUTTUR"}



    for Num_licence in Liste_Licences_DEDOS.keys():
        #print(Num_licence)
        Licence_DEDO=txt.find(Num_licence)
        if Licence_DEDO>0 :

            Activite=""
            # Joueur ou entraineur ?
            if (Licence_DEDO<Pos_Entraineur_HOME and Licence_DEDO>Pos_Licences_HOME) or (Licence_DEDO<Pos_Entraineur_VISITORS and Licence_DEDO>Pos_Licences_VISITORS):

                Pos_Licence_Name=txt.find(Liste_Licences_DEDOS[Num_licence])
                if (Pos_Licence_Name>Pos_Entraineur_HOME and Pos_Licence_Name<Pos_Licences_VISITORS) or (Pos_Licence_Name>Pos_Entraineur_VISITORS and Pos_Licence_Name<Pos_MARQUE_COURANTE) :
                    Activite="ENTRAINEUR"
                else:
                    Activite="JOUEUR"
            elif Licence_DEDO>Pos_Officiels :
                Activite="Officiel"

                if Licence_DEDO>Pos_1st_Arbitre and Licence_DEDO<Pos_Commisaire :
                    Activite="ARBITRAGE"

            else:
                Activite="NON TROUVEE"
            # Autre (Table, arbitre etc)
            #print(Liste_Licences_DEDOS[Num_licence] + " a été " + Activite + " lors du match n°" + Game_Nb + " le " + Game_Date +"\n")
            Cur_Dedo=Num_licence +";" + Liste_Licences_DEDOS[Num_licence] +";;" + Game_Nb + ";" +Game_Date + ";;" + Game_Lieu + ";" +Activite + ";" + TEAM_HOME +" - " + TEAM_VISITOR + "\n"
            print(Cur_Dedo)
            All_Dedos=All_Dedos + Cur_Dedo

    return All_Dedos
# REcherche