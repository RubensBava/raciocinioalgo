import numpy as np

#aqui vai estat a nota do aluno
notas = np.array([
    [85,92,78],
    [70,88,60],
    [62,50,70]
    ])
#mediaalunos
medias_alunos = np.mean(notas, axis=1)
print('Media do aluno',medias_alunos)

#media de cada avaliacao
media_avaliacoes = np.mean(notas, axis=0)
print('Media por avaliacoes', media_avaliacoes)
