# Clustering evaluation

# Elbow method, silhouette method, gap statistic, Davies-Bouldin index, calinski-harabasz index, Dunn index

from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer, InterclusterDistance
from sklearn.metrics import davies_bouldin_score, adjusted_rand_score

import seaborn as sns
import matplotlib.pyplot as plt


def evaluate_cluster_by_labels(X, y, model):
    pass 

def evaluate_clusters(X, model, k_range=(2, 10)):
    """
    Evaluate clustering model using elbow method, silhouette method, gap statistic, Davies-Bouldin index, calinski-harabasz index, Dunn index
    
    Elbow method
    Purpose: Helps to determine the optimal number of clusters in a dataset.
    Explanation: The method involves plotting the variance explained as a function of the number of 
    clusters. The "elbow" point on the graph represents the optimal number of clusters where adding more 
    clusters does not significantly improve the variance explained.

    Silhouette method
    Purpose: Measures how well-separated the clusters are.
    Explanation: For each data point, it calculates the average distance from other points in the same 
    cluster (a) and the average distance from points in the nearest cluster (b). 
    The silhouette score is then (b - a) / max(a, b). The higher the silhouette score, 
    the better-separated the clusters.

    Gap Statistic:
    Purpose: Compares the performance of a clustering algorithm to a reference distribution of random data.
    Explanation: It measures the difference between the intra-cluster distances in the actual data and 
    the expected intra-cluster distances in a random distribution. A larger gap statistic indicates 
    better-defined clusters.

    Davies-Bouldin Index:
    Purpose: Measures the compactness and separation of clusters.
    Explanation: For each cluster, it calculates the average distance between points within the cluster
    (intra-cluster) and the average distance to the nearest cluster (inter-cluster). The index is the 
    average ratio of the intra-cluster distance to the inter-cluster distance. A lower Davies-Bouldin 
    index indicates better clustering.

    Calinski-Harabasz Index:
    Purpose: Measures the ratio of the between-cluster variance to within-cluster variance.
    Explanation: It evaluates how well-separated clusters are and is calculated as the ratio of 
    the between-cluster variance to the within-cluster variance. A higher Calinski-Harabasz index 
    suggests better clustering.
    

    Dunn Index:
    Purpose: Measures the compactness and separation of clusters, similar to Davies-Bouldin index.
    Explanation: It is the ratio of the minimum inter-cluster distance to the maximum intra-cluster distance.
    A higher Dunn index indicates better clustering, with smaller within-cluster distances and larger
    between-cluster distances.
    """


    # Elbow method
    visualizer = KElbowVisualizer(model, k=k_range, metric="distortion")
    visualizer.fit(X)
    visualizer.show()

    # Silhouette method
    visualizer = KElbowVisualizer(model, k=k_range, metric="silhouette")
    visualizer.fit(X)
    visualizer.show()

    # Calinski-Harabasz Index
    visualizer = KElbowVisualizer(model, k=k_range, metric="calinski_harabasz")
    visualizer.fit(X)
    visualizer.show()

    # Davies-Bouldin Index
    scores = []
    for k in range(k_range[0], k_range[1]):
        m = model(n_clusters=k, random_state=42)
        m.fit(X)

        labels = m.labels_
        score = davies_bouldin_score(X, labels)
        scores.append(score)

    plt.plot(range(k_range[0], k_range[1]), scores)
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Davies-Bouldin Score')
    plt.title('Davies-Bouldin Score for Different Values of k')
    plt.show()

def profiling_clustering_num(data, num_vars, cluster_var='cluster', verbose=1):
    
    num_plots = len(num_vars)
    fig, axes = plt.subplots(num_plots, 1, figsize=(10, num_plots * 5))
    grid = axes.flatten()

    for i, num_var in enumerate(num_vars):
        fg = sns.barplot(data=data, x=cluster_var, y=num_var, ax=grid[i])
        fg.set_title(f'Clusters by {num_var}')
        real_mean = data[num_var].mean()

        if verbose:
            print(real_mean)
            print(data.groupby(cluster_var)[cluster_var].mean())

        grid[i].plot([-0.4, 1.4], [real_mean, real_mean], linewidth=5, color='red')
        grid[i].text(0.5, (real_mean + 1), num_var, horizontalalignment='center', size='large', color='black', weight='bold')
        grid[i].text(-0.27, (real_mean + 0.4), "Real Mean", horizontalalignment='center', size='medium', color='red', weight='semibold')
        grid[i].set_ylabel('percent')

    plt.tight_layout()
    plt.show()

def profiling_clustering_cats(data, cat_vars, cluster_var='cluster'):

    fig, axes = plt.subplots(len(cat_vars), 1, figsize=(10, len(cat_vars) * 5))

    for i, cat_var in enumerate(cat_vars):
        
        fg = (data
        .groupby(cluster_var)[cat_var]
        .value_counts(normalize=True)
        .mul(100)
        .rename('percent')
        .reset_index()
        .pipe((sns.catplot,'data'), x=cluster_var, y='percent', hue=cat_var, kind='bar', ax=axes[i]))

        fg.fig.suptitle(f'Clusters by {cat_var}')

        for ax in fg.axes.ravel():

            # add annotations
            for c in ax.containers:

                # custom label calculates percent and add an empty string so 0 value bars don't have a number
                labels = [f'{w:0.1f}%' if (w := v.get_height()) > 0 else '' for v in c]

                _ = ax.bar_label(c, labels=labels, label_type='edge', fontsize=8, padding=2)
            
            _ = ax.margins(y=0.2)

    _ = plt.tight_layout()
    _ = plt.show()

    