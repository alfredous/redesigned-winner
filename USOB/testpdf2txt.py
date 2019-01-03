import os
import PyPDF2
myfile = os.path.join('C:\\USOB', 'F.pdf.pdf')
print (myfile)
pdfFileObj = open(myfile, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
NbPages=pdfReader.numPages-1

# nb = 7 # On garde la variable contenant le nombre dont on veut la table de multiplication
# i = 0 # C'est notre variable compteur que nous allons incrémenter dans la boucle
# while i < 10: # Tant que i est strictement inférieure à 10
#    print(i + 1, "*", nb, "=", (i + 1) * nb)
#    i += 1 # On incrémente i de 1 à chaque tour de boucle
i=0
print(i)
print(NbPages)
while i<=NbPages:
    pageObj = pdfReader.getPage(i)
    print('PAGE N°', i, ' *********************************')
    print(pageObj.extractText())
    i+=1

