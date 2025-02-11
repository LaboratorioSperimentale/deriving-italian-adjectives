"""
    RUN:
	python3 src/annotate_synsets.py > data/adj_synsets.csv
"""

import collections
# import nltk
from nltk.corpus import wordnet as wn


all_possibilities = set()
lexnames_adjs = {}
n_synsets = {}

with open("data/adjectives_with_labels.csv") as fin:
	fin.readline()
	for line in fin:
		cluster, adj, cluster2 = line.strip().split(",")
		adj = adj.split("/")[0].strip()
		lexnames_adjs[adj] = collections.defaultdict(int)

		synset = wn.synsets(adj, lang="ita", pos="a")
		n_synsets[adj] = len(synset)

		for s in synset:
			lexnames_adjs[adj][s.lexname()] += 1
			all_possibilities.add(s.lexname())


possbilities_str = '\t'.join([x for x in all_possibilities])
print(f"ADJ\tNCLUSTERS\t{possbilities_str}")
with open("data/adjectives_with_labels.csv") as fin:
	fin.readline()
	for line in fin:
		cluster, adj, cluster2 = line.strip().split(",")
		adj = adj.split("/")[0]

		possibilies_str = '\t'.join([str(lexnames_adjs[adj][x]) for x in all_possibilities])
		print(f"{adj}\t{n_synsets[adj]}\t{possibilies_str}")