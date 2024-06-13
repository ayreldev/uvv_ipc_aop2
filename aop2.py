import numpy as np

def ler_nota(prompt, min_val, max_val): # Verifica se os valores inseridos são válidos
    while True:
        try:
            nota = float(input(prompt))
            if min_val <= nota <= max_val:
                return nota
            else:
                print(f"Nota inválida! Digite um valor entre {min_val} e {max_val}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def main():
    num_alunos = 100
    aop1 = np.zeros(num_alunos)
    aop2 = np.zeros(num_alunos)
    aop3 = np.zeros(num_alunos)
    prova_regular = np.zeros(num_alunos)
    prova_recuperacao = np.zeros(num_alunos)
    sm = np.zeros(num_alunos)
    mm = np.zeros(num_alunos)

    status = [] # Inicializa uma lista para armazenar status (aprovado ou reprovado)

    for i in range(num_alunos):
        print(f"\nAluno {i + 1}:")
        aop1[i] = ler_nota("Nota da AOP1 [0, 1]: ", 0, 1)
        aop2[i] = ler_nota("Nota da AOP2 [0, 2]: ", 0, 2)
        aop3[i] = ler_nota("Nota da AOP3 [0, 1]: ", 0, 1)
        prova_regular[i] = ler_nota("Nota da Prova Regular [0, 6]: ", 0, 6)

        sm[i] = aop1[i] + aop2[i] + aop3[i] + prova_regular[i]

        if sm[i] >= 7:
            mm[i] = sm[i]  # Se o aluno já é aprovado pela SM, não precisa de recuperação
            status.append("Aprovado")
        else:
            prova_recuperacao[i] = ler_nota("Nota da Prova de Recuperação [0, 10]: ", 0, 10)
            mm[i] = (sm[i] + prova_recuperacao[i]) / 2
            if mm[i] >= 5:
                status.append("Aprovado")
            else:
                status.append("Reprovado")

    # Converte a lista de status para um array numpy
    status = np.array(status)

    aprovados = np.sum(status == "Aprovado")
    reprovados = np.sum(status == "Reprovado")

    porcentagem_aprovados = (aprovados / num_alunos) * 100
    porcentagem_reprovados = (reprovados / num_alunos) * 100

    for i in range(num_alunos): # Loop para exibir status e notas de cada aluno
        print(f"\nAluno {i + 1}:")
        print(f"Soma do Módulo (SM): {sm[i]}")
        print(f"Média do Módulo (MM): {mm[i]}")
        print(f"Status do Aluno: {status[i]}")

    print(f"\nPorcentagem de alunos aprovados: {porcentagem_aprovados}%")
    print(f"Porcentagem de alunos reprovados: {porcentagem_reprovados}%")