# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy import linalg as LA
from matplotlib import pyplot as plt
from matplotlib.pyplot import cm


k = 6
iterationCounter = 0
sigma = 1.5
A = np.array([ [15,21.9], [14.8,22], [14,23], [13.5,23], [13,23], [12,22.6], [11.9,22], [11.7,21], [11.8,20.8], [12,20.3], [12.5,19.8], [13,19.7],[13.5,19.4], [14,19], [14.8,18], [14.9,17], [14.6,16.2],
	[14.2,16], [13,16], [12.5,16.5], [12,17], [21,22], [20,23], [18.8,23], [18,22], [17.6,21], [17.5,20], [17.4,19], [17.45,18], [17.7,17], [19,16], [20,16], [21,17], [21,18], [20,18],
	[5,10], [6,11], [7,11.6], [8,11.5], [9,11], [10,10], [9.8,9], [9.6,8], [9,7], [8,6], [7,5], [6,4], [5,3], [6,3], [7,3], [8,3], [9,3], [10,3],
	[14.4,12], [13,11], [12,10], [11.5,8], [11.5,6.6], [12,5], [13,3.8], [14.5,3], [15.6,3], [17,3.8], [18,5], [18.5,6.6], [18.5,8], [18,10], [17,11], [15.5,11.8], [14.4,12],
	[20, 10], [21,11], [22,12], [22,11], [22,10], [22,9], [22,8], [22,7], [22,6], [22,5], [22,4], [22,3], [21,3], [20,3], [23,3], [24,3],
	[31.5,10], [30,12], [28,11.9], [26.5,10], [27,8], [27.8,7.5], [28.6,6.8], [30,6], [31,5], [31,4] ,[30,2], [28,2], [26.8,4], [27.6,6], [30,7], [31,8], [31.5,10]
])

def distance(in_data1, in_data2):
       difference = abs(np.subtract(in_data1, in_data2))
       euclidian = (np.square(difference).sum(axis = 0))
       measure = np.exp(-(euclidian)/(2*sigma**2))
       return measure


def similarity_matrix(in_data):
    (row,col) = in_data.shape
    adj = np.zeros([row, row],dtype = np.float)
    for i in range(row):
        for j in range(row):
            adj[i,j] = distance(in_data[i], in_data[j])
    return adj


def degree_matrix(similarityMatrix):
    diag = similarityMatrix.sum(axis=1)
    diag = np.diag(diag)
    return diag

def laplacian_matrix(sim_mat, deg_mat):
    lap_mat = deg_mat - sim_mat
    return lap_mat




def spectral(lap_mat):
    eigval, eigvec= LA.eig(np.matrix(lap_mat))
    x = eigval.real.argsort()
    eigval = eigval[x]
    eigvec = eigvec[:, x]
    eigvec = np.transpose(eigvec)
    result = np.zeros([lap_mat.shape[0], k],dtype = np.float)
    for i in range(1,k):
        for j in range(lap_mat.shape[0]):
            result[j][i] = eigvec[i][j]
    result = np.delete(result, 0, 1)
    return result 


def dist(a,b):
    dis = np.sqrt(sum(np.square(a-b)))
    return dis


def assign_cluster(k, tan_mat, init_centroid):
    cluster = [-1]*len(tan_mat)
    for i in range(tan_mat.shape[0]):
        dist_arr = []
        for j in range(k):
            print(tan_mat[i], init_centroid[j])
            dist_arr.append(dist(tan_mat[i], init_centroid[j]))
        idx = np.argmin(dist_arr)
        print(idx)
        cluster[i] = idx
        
    return(np.asarray(cluster))
    

def compute_cluster(k, cluster, tan_mat):
    print(cluster)
    print(tan_mat)
    tan_mat = np.asarray(tan_mat)
    new_centroid = []
    for i in range(k):
        arr =[]
        for j in range(len(tan_mat)):
            if cluster[j] == i:
                tan_mat[j, :]
                arr.append(tan_mat[j, :])
        print("this is for "+ str(i))
        print(arr)
        new_centroid.append(np.mean(arr, axis = 0))
        print(new_centroid)
    return(new_centroid)
    
def measure_change(cg_prev, cg_new):
    res = 0
    for a,b in zip(cg_prev,cg_new):
        res+=dist(a,b)
    return res


def transformToSpectral(laplacian):
    global k
    e_vals, e_vecs = LA.eig(np.matrix(laplacian))
    ind = e_vals.real.argsort()[:k]
    result = np.ndarray(shape=(laplacian.shape[0],0))
    for i in range(1, ind.shape[0]):
        cor_e_vec = np.transpose(np.matrix(e_vecs[:,np.asscalar(ind[i])]))
        result = np.concatenate((result, cor_e_vec), axis=1)
    return result



    
    
def assign_matrix(init_centroid, tan_mat):
    matrix_cluster = np.ndarray(shape=(tan_mat.shape[0], 0))
    for i in range(0,k):
             mean_new = np.repeat(init_centroid[i, :], tan_mat.shape[0], axis = 0)
             abs_distance = abs(np.subtract(tan_mat, mean_new))
             distance = np.sqrt(np.square(abs_distance).sum(axis=1))
             matrix_cluster = np.concatenate((matrix_cluster, distance), axis = 1)
   
    return matrix_cluster


#def compute_mean():
    
def kmeans(tan_mat, init_centroid):
    while(True):
    
        clusterMatrix = np.ravel(np.argmin(assign_matrix(init_centroid, tan_mat), axis=1))
        
        cluster_member = [[] for i in range(k)]
        cluster_point = [[] for i in range(k)]
        
        for i in range(0, tan_mat.shape[0]):
                cluster_member[clusterMatrix[i]].append(np.array(tan_mat[i, :]).ravel())
                cluster_point[clusterMatrix[i]].append(np.array(A[i, :]).ravel())
                
        new_centroid = np.ndarray(shape=(0, init_centroid.shape[1]))
        for i in range(0, k):
            memberClusterTransf = np.asmatrix(cluster_member[i])
            centroidClusterTransf = memberClusterTransf.mean(axis=0)
            new_centroid = np.concatenate((new_centroid, centroidClusterTransf), axis=0)
        
                
        if((new_centroid == init_centroid).all()):                    
                    break              
        init_centroid = new_centroid
        
    plot_graph(cluster_point, A, k)
    

    
def plot_graph(listClusterMemberOri, A, k):
    color = iter(cm.rainbow(np.linspace(0, 1, k)))
    for i in range(k):
        col = next(color)
        cluster_point = np.asmatrix(listClusterMemberOri[i])
        plt.scatter(np.ravel(cluster_point[:, 0]), np.ravel(cluster_point[:, 1]), marker=".", s=100, c=col)
     

sim_mat = similarity_matrix(A)
deg_mat = degree_matrix(sim_mat)
lap_mat = laplacian_matrix(sim_mat, deg_mat)
tan_mat = transformToSpectral(lap_mat)
init_centroid = tan_mat[np.random.choice(tan_mat.shape[0], k, replace= True)]

kmeans(tan_mat, init_centroid)


