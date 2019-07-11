ximport modulo_kmeans
from modulo_kmeans import *

#------------Pajaro--------------

#Cargamos la imagen
data_imagen = loadmat('data/bird_small_kmeans.mat')
A = data_imagen ['A']
A.shape

#Normalicemos los rangos de los valores
A = A/255

#Reshape el arreglo
X = np.reshape(A, (A.shape[0] * A.shape[1], A.shape[2]))

#Iniciar los centroides aleatoriamente
initial_centroids = init_centroids(X,16)

#Correr el algoritmo
idx, centroids = run_k_means(X, initial_centroids,10)

#Obtener los centroides mas cercanos una vez mas
idx = find_closest_centroids(X,centroids)

#mapear cada pixel al valor del centroide
X_recovered = centroids[idx.astype(int),:]

#recambiar a las dimensiones originales
X_recovered = np.reshape(X_recovered, (A.shape[0], A.shape[1], A.shape[2]))

plt.imshow(X_recovered)
plt.savefig('kmeanspajaro.png')


#-----------Clima--------------

#Carguemos una base de datos del clima
data = loadmat('data/clustering_colors.mat')
X = data['X']

#propongamos unos centroides iniciales en el principio esto debe ser ale
initial_centroids = np.array([[3,3],[6,2],[8,5]])

#estimemos donde estan los centroides mas cercanos
idx = find_closest_centroids(X,initial_centroids)
print(idx[0:3])

#corremos el algoritmo
idx, centroids = run_k_means(X, initial_centroids, 10)

#print(idx)
print(centroids)

#hacer graficas
#Aqui definimos nuestros cluster
cluster1 = X[np.where(idx == 0)[0],:]
cluster2 = X[np.where(idx == 1)[0],:]
cluster3 = X[np.where(idx == 2)[0],:]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')
ax.legend()

plt.xlabel('Diferencia de temperatura')
plt.ylabel('Diferencia de presion')
plt.savefig("kmeansclima.pdf")

