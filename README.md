# uvv_ipc_aop2
Trabalho de IPC 1º período

DESCRIÇÃO DO PROBLEMA: SISTEMA DE AVALIAÇÃO - UVVON
 
Faça um algoritmo em Python que leia de cem (100) alunos de um curso EAD da UVV:
  
LER DO USUÁRIO: Nota [0, 1] na AOP1: Atividade Online Pontuada 1;
LER DO USUÁRIO: Nota [0, 2] na AOP2: Atividade Online Pontuada 2;
LER DO USUÁRIO: Nota [0, 1] na AOP3: Atividade Online Pontuada 3;
LER DO USUÁRIO: Nota [0, 6] da PROVA REGULAR;
LER DO USUÁRIO: Nota [0, 10] da PROVA DE RECUPERAÇÃO: Somente se o aluno não obteve Soma do Módulo (AOP1 + AOP2 + AOP3 + Prova Regular) >=7
E, calcule e mostre na tela: as informações a seguir:
Soma do Módulo (SM) = AOP1 + APO2 + AOP3 + PROVA REGULAR
Média do Módulo (MM) = (AOP1 + APO2 + AOP3 + PROVA REGULAR + PROVA DE RECUPERAÇÃO)/2
EXIBIR:
Status do Aluno: Aprovado, Prova de recuperação ou Reprovado;
A quantidade de alunos (em porcentagem) que foram: Aprovado ou Reprovado;

Lembrando que, é considerado com Status Aprovado, o aluno que:
Obteve Soma do Módulo (SM) >= 7.0 ou
Obteve Média Módulo (MM) >= 5.0
Observações:
Para testar seu programa reduzir a quantidade de alunos da turma para 5 alunos, apenas.
É IMPORTANTE realizar a validação das notas inseridas pelo usuário. Não existem notas negativas, e, igualmente, não podemos aceitar notas que excedam o valor máximo estabelecido. Ex: Se o usuário digitar nota da AOP1 = -4, o programa precisa alertar e solicitar que digite um número válido entre 0-1.
