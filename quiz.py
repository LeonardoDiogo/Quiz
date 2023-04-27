
print("Seja muito bem vindo ao quiz")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("pergunta numero 1")
print("""Qual foi a primeira linguagem de programação?
\n (A) Assembly \n (B) Fortran \n (C) Lisp \n (D) Cobol""")

answer_1 = input("Resposta: ")

if answer_1 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto alternativa certa é a (B) Fortran")

continuar = input("Deseja continuar? (S/N) ")

if continuar == "S":
    print("Continuando")
else:
    quit()

print("pergunta 2")

print("""qual a linguagem mais famosa da atualidade?
\n (A) JavaScript \n (B) Python \n (C) Java \n (D) C# """)

answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto")
    score = score + 1
else:
    print("Incorreto alternativa certa é a (B) Python")

print(f"sua pontuação foi de {score}/2")
