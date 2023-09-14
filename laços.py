a = int(input("\n\nPrimeiro semestre: "))
b = int(input("Segundo semestre: "))
c = int(input("Terceiro semestre: "))
d = int(input("Quarto semestre: "))

while(a>10 or b>10 or c>10 or d>10):
    print("\nUma ou mais notas são INVÁLIDAS")
    a = int(input("\nPrimeiro semestre: "))
    b = int(input("Segundo semestre: "))
    c = int(input("Terceiro semestre: "))
    d = int(input("Quarto semestre: "))
    

med = (a+b+c+d) / 4

print("\nSua média é de : ",med)

if(med >= 6):
    print("\nVocê foi APROVADO")
else:
    print("\nVocê foi REPROVADO")





    