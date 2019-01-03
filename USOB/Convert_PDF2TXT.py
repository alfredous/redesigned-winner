#!/usr/bin/python
import datetime,time
import os, sys
import USOB_PDFReadr_V1

# Open a file
Exe_Path="C:\\USOB\\pdftotext.exe"
PDF_path = "C:\\USOB\\FEUILLES_MATCH\\PDF_IN"
List_Erreurs = "Liste des Fichiers ignorés :"
PDF_dirs = os.listdir( PDF_path )

# This would print all the files and directories
for PDF_file in PDF_dirs:
    if PDF_file .endswith(".pdf"):
        #print("Traitement de : " + PDF_file)
        try:
            os.popen((Exe_Path + " " + PDF_path + "\\" + PDF_file))
        except:
            ##print("OS error: {0}".format(err))
            ##List_Erreurs=List_Erreurs + ("OS error: {0}".format(err)) + " Fichier : " + PDF_file
            List_Erreurs=List_Erreurs + " Fichier : " + PDF_file
print("Conversions terminées !")

USOB_PDFReadr_V1.GiveMeDedos
print("Dedos Chasing starts !")
All_Dedos_OUT=""
Lst_Files=os.listdir( PDF_path )
for TXT_File in Lst_Files:
   if TXT_File.endswith(".txt"):
    print("-----------------------------------------------------------")
    print("Traitement de : " + TXT_File)
    LesDedos=USOB_PDFReadr_V1.GiveMeDedos(PDF_path + "\\" +TXT_File)
    All_Dedos_OUT=All_Dedos_OUT+LesDedos

All_Dedos_OUT=All_Dedos_OUT+List_Erreurs

# EXPORT DATAS
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S')
print(All_Dedos_OUT)
fichier = open("NewDatas" + st +".txt", "a")
fichier.write(All_Dedos_OUT)
fichier.close()
