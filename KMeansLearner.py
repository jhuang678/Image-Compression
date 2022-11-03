import numpy as np
import time
class KmeansLearner(object):

    def __init__(self, verbose = False):
        self.verbose = verbose
        if self.verbose:
            print("\nInitialized K-means Cluster")
            print("Author: ", self.author())

    def author(self): return "Jeffrey Huang"

    def random_initialize_centroids(self, X, k):
        # Randomly assign k observations from X as centers.
        from numpy.random import choice
        int_centers = choice(len(X), size=k, replace=False)
        return X[int_centers, :]

    def compute_distance(self, X, centers, norm):
        m = len(X)
        k = len(centers)
        distance_matrix = np.empty((m, k))

        for i in range(m): distance_matrix[i, :] = np.linalg.norm(X[i, :] - centers, ord=norm, axis=1)  # **2
        return distance_matrix

    def assign_data_to_clusters(self, distance_matrix):
        cluster_labels = np.argmin(distance_matrix ,axis=1)
        return cluster_labels

    def assign_centers(self, X, k, cluster_labels, norm):
        m, n = X.shape
        centers = np.empty((k, n))
        if (norm ==1):
            for j in range(k):
            # Compute the new center of cluster j,
                centers[j, :] = np.median(X[cluster_labels==j,:], axis =0)
        else:
            for j in range(k):
            # Compute the new center of cluster j,
                centers[j, :] = np.mean(X[cluster_labels==j,:], axis =0)
        return centers

    def has_converged(self, old_centers, centers):
        return set([tuple(x) for x in old_centers]) == set([tuple(x) for x in centers])

    def train_data(self, X, k, norm=2):
        # Set up parameters
        converged = False
        labels = np.zeros(len(X))
        i = 0
        cum_time = 0
        # (1) Random Initialize Centroids
        centers = self.random_initialize_centroids(X, k)
        ts = time.time()
        while (not converged) and (i <= 150):
            old_centers = centers

            # (2) Computing the Distances
            distance_matrix = self.compute_distance(X, centers, norm)

            # (3) Assign Data Points to Clusters
            cluster_labels = self.assign_data_to_clusters(distance_matrix)

            # (4) Assign New Centers
            centers = self.assign_centers(X, k, cluster_labels, norm)

            # (5) Assign New Centers
            converged = self.has_converged(old_centers, centers)
            i += 1
        ts = time.time() - ts
        print("iteration", i, "Cumulative Time = ", ts)
        if (i > 150):
            print("Iteration exceed 150 times.")
        return cluster_labels, centers

if __name__ == "__main__":
    print("This is a K-Means Cluster Machine Learner.")
