import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation




M, N = 60, 60          #matriz
beta = 0.35            #transmissão
gamma = 0.06           #recuperação
passos = 120           #simulação


S = 0   #suscetível
I = 1   #infectado
R = 2   #recuperado



def inicializar_grade():
    grade = np.zeros((M, N), dtype=int)

    
    iniciais = 8
    for _ in range(iniciais):
        x = np.random.randint(0, M)
        y = np.random.randint(0, N)
        grade[x, y] = I

    return grade


def contar_vizinhos_infectados(grade, x, y):
    k = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue

            nx, ny = x + dx, y + dy

           
            if 0 <= nx < M and 0 <= ny < N:
                if grade[nx, ny] == I:
                    k += 1
    return k


def passo_temporal(grade):
    nova = grade.copy()

    for i in range(M):
        for j in range(N):

            estado = grade[i, j]

            
            if estado == S:
                k = contar_vizinhos_infectados(grade, i, j)

                
                p_infeccao = 1 - (1 - beta) ** k

                if np.random.rand() < p_infeccao:
                    nova[i, j] = I

             
            elif estado == I:
                if np.random.rand() < gamma:
                    nova[i, j] = R

             

    return nova


def contar_estados(grade):
    s = np.sum(grade == S)
    i = np.sum(grade == I)
    r = np.sum(grade == R)
    return s, i, r



grade = inicializar_grade()

historico_S = []
historico_I = []
historico_R = []

for t in range(passos):
    s, i, r = contar_estados(grade)

    historico_S.append(s)
    historico_I.append(i)
    historico_R.append(r)

    grade = passo_temporal(grade)



plt.figure(figsize=(12, 4))

#mapa final
plt.subplot(1, 2, 1)
plt.title("Distribuição espacial final")
plt.imshow(grade, cmap="viridis")
plt.colorbar(label="0=S, 1=I, 2=R")

#curvas sir
plt.subplot(1, 2, 2)
plt.title("Curvas epidemiológicas")
plt.plot(historico_S, label="Suscetíveis")
plt.plot(historico_I, label="Infectados")
plt.plot(historico_R, label="Recuperados")
plt.legend()
plt.xlabel("Tempo")
plt.ylabel("Indivíduos")

plt.tight_layout()
plt.show()