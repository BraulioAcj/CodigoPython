#importar modulos/librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat

def pca(X):
	# normalizar las caracteristicas
	X = (X - X.mean()) / X.std()

	# obtener la matriz de covarianza
	X = np.matrix(X)
	cov = (X.T * X) / X.shape[0]

	#obtener SVD
	U, S, V = np.linalg.svd(cov)
	
	return U, S, V

def project_data(X, U, k):
	U_reduced = U[:,:k]
	return np.dot(X, U_reduced)

def recover_data(Z, U, k):
	U_reduced = U[:,:k]
	return np.dot(Z, U_reduced.T)


faces = loadmat('data/pca_faces.mat')
X = faces['X']
X.shape

face = np.reshape(X[4999,:], (32, 32))
plt.imshow(face)
plt.savefig('face_inicial.png')


U, S, V = pca(X)
Z = project_data(X, U, 100)

X_recovered = recover_data(Z, U, 100)
face = np.reshape(X_recovered[4999,:], (32, 32))
plt.imshow(face)
plt.savefig("face_final.png")

