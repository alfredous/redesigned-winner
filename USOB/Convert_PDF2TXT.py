#!/usr/bin/python
import datetime,time
import os, sys
import USOB_PDFReadr_V1

# Variables definition
Exe_Path="C:\\USOB\\pdftotext.exe"
PDF_path = "C:\\USOB\\FEUILLES_MATCH\\PDF_IN"
List_Erreurs = "Liste des Fichiers ignorés :"
PDF_dirs = os.listdir( PDF_path )
Nb_fichiersPDF=0
Nb_fichiersTXT=0

# Convertion des PDF en texte
print("-----------------------------------------------------------")
print("#1 - Convertion des PDF en texte")
print("-----------------------------------------------------------")
for PDF_file in PDF_dirs:
    if PDF_file .endswith(".pdf"):
        #print("Traitement de : " + PDF_file)
        Nb_fichiersPDF+=1        
        try:
            os.popen((Exe_Path + " " + PDF_path + "\\" + PDF_file))
            print("File : " + PDF_file)
        except:
            ##print("OS error: {0}".format(err))
            ##List_Erreurs=List_Erreurs + ("OS error: {0}".format(err)) + " Fichier : " + PDF_file
            List_Erreurs=List_Erreurs + " Fichier : " + PDF_file
print(str(Nb_fichiersPDF) + " PDF Convertis.")

# 
print("-----------------------------------------------------------")
print("#2 - Dedos Chasing starts !")
print("-----------------------------------------------------------")
Nb_fichiersTXT=0
USOB_PDFReadr_V1.GiveMeDedos
All_Dedos_OUT=""
Lst_Files=os.listdir( PDF_path )

for TXT_File in Lst_Files:
   if TXT_File.endswith(".txt"):
       Nb_fichiersTXT+=1
       print("                   ***************** ")
       print("Traitement de : " + TXT_File)
       LesDedos=USOB_PDFReadr_V1.GiveMeDedos(PDF_path + "\\" +TXT_File)
       All_Dedos_OUT=All_Dedos_OUT+LesDedos
   
print(str(Nb_fichiersTXT) + " TXT Convertis.")

All_Dedos_OUT=All_Dedos_OUT+List_Erreurs

# EXPORT DATAS
print("-----------------------------------------------------------")
print("#3 - Sortie du fichier final.")
print("-----------------------------------------------------------")
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S')
print(All_Dedos_OUT)
fichier = open(PDF_path + "\\" + "NewDatas" + st +".txt", "a")
fichier.write(All_Dedos_OUT)
fichier.close()

print("-----------------------------------------------------------")
print("FINI !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("-----------------------------------------------------------")
print(str(Nb_fichiersPDF) + " PDF ET " + str(Nb_fichiersTXT) + " TXT Convertis.")
