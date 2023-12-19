import sys
import os
current_file_path = os.path.abspath(__file__)
code_directory = os.path.abspath(os.path.join(current_file_path, '..', '..'))
sys.path.append(code_directory)

import pandas as pd
from Python.Constants import *
from kmodes.kmodes import KModes
import joblib



class Clusters:

    def __init__(self, cases, count, path_cluster, train_on_innit=False, data_per_cluster=50):
        
        self.path_cluster = path_cluster

        self.cases = cases
        self.data_per_cluster = data_per_cluster
        self.clustering = self.create_clusters() if train_on_innit else self.load_cluster(path_cluster)

        self.count = count

        self.tree = self.create_tree()


    def __len__(self):
        return len(self.cases)


    def __repr__(self):
        for i, value in self.tree.items():
            print(f'Cluster {i} contains {len(value)} cases')
        return ''
        

    def return_cases(self):
        return [case for cases in self.tree.values() for case in cases], self.count


    def add_case(self, cluster, case):
        self.count += 1
        self.cases.append(case)
        self.tree[cluster].append(case)

        self.recreate_clusters()
    
        

    def remove_case(self, cluster, case):
        # we have add a change in the clusters
        self.count += 1
        self.cases.remove(case)
        self.tree[cluster].remove(case)
        self.recreate_clusters()


    def get_case(self, cluster, index):
        return self.tree[cluster][index]


    def create_tree(self):
        cases_clusters = self.predict(self.cases)
        clusters = {}
        for i, case in enumerate(self.cases):
            cluster = cases_clusters[i]
            
            if cluster in clusters:
                clusters[cluster].append(case)
            else:
                clusters[cluster] = [case]

        return clusters


    def load_cluster(self, path_cluster):
        clustering = joblib.load(path_cluster)
        return clustering


    def predict(self, cases):
        return self.clustering.predict(self._get_data_for_clustering(cases))


    def recreate_clusters(self):
        if self.count > 50:
            self.clustering = self.create_clusters()
            self.tree = self.create_tree()
            self.count = 0


    def create_clusters(self):
        data = self._get_data_for_clustering(self.cases)

        clustering = KModes(init='Huang', n_init=5, verbose=0)

        number = len(self) // self.data_per_cluster
        clustering.n_clusters = number
        clustering.fit(data)
        joblib.dump(clustering, self.path_cluster)

        return clustering
        

    def _get_data_for_clustering(self, cases):
        columns=['Antiquity', 'Pages', 'Bestseller', 'Film', 'Saga'] + GENRES
        def get_variables(case):
            variables, genres = case.get_variables()
            return variables + genres
        data = [get_variables(case) for case in cases]
        data = pd.DataFrame(data, columns=columns)
        return data