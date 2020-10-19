x = input().split()

n1, n2, n3, n4 = x

Med = (float(n1)*2+float(n2)*3+float(n3)*4+float(n4)*1)/(2+3+4+1)

print("Media: %.1f"%Med)

if Med>=7: 
    print("Aluno aprovado.")

elif Med<5:
    print("Aluno reprovado.")

elif 5<=Med<=6.9:
    print("Aluno em exame.")
    nf = float(input())
    print("Nota do exame: %.1f"%nf)

    if (nf+Med)/2 >= 5:
        print("Aluno aprovado.")
        print("Media final: %.1f"%float((nf+Med)/2))
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f"%float((nf+Med)/2))
