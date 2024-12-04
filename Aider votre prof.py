import random
liste_nom=[] 
liste_note=[]
    
ok="o"
while ok =="o":
      val= input("Nom: ")
      val2 = int(input("Note: "))
      liste_nom.append(val)
      liste_note.append(val2)
      ok = input("Voulez-vous continuer (o/n)?:")
cp=0
cp1=0
cp2=0
index = 0
print(liste_note)
total_note = 0
for i in liste_note:
    total_note=total_note+i
    if liste_note[index]<10:
        cp=cp+1
    elif liste_note[index]<14:
        cp1=cp1+1
    else:
        cp2=cp2+1
    index = index + 1
print("La moyenne est: ",total_note/len(liste_note))
print("Le nombre de note < 10: ",cp)
print("Le nombre de note entre 10 et 14: ",cp1)
print("Le nombre de note < 14: ",cp2)
