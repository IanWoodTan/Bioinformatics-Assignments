import networkx as nx  
import pandas as pd  
import matplotlib.pyplot as plt  
  
# Your file path  
file_path = r'D:\KNOWLEDGE\Biology\Bioinformatics\Bioinformatic Exp. term paper\string_interactions (3).csv'  
  

df = pd.read_csv(file_path)  
G = nx.from_pandas_edgelist(df, '#node1', 'node2', ['combined_score'])  
  
'''
'''  
  
# Calculate degree centrality for each protein  
degree_centrality = nx.degree_centrality(G)  
  
# Calculate degree centrality for each protein  
degree_centrality = nx.degree_centrality(G)  
  
# Calculate betweenness centrality for each protein  
betweenness_centrality = nx.betweenness_centrality(G)  
  
'''
'''  
  
# Visualize the degree centrality values with a bar plot  
plt.figure(figsize=(12, 6), dpi=1000)  
plt.bar(degree_centrality.keys(), degree_centrality.values(), color='skyblue')  
plt.xlabel('Protein')  
plt.ylabel('Degree Centrality')  
plt.title('Degree Centrality of Proteins in PPI Network')  
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()  
  
  
# Visualize the betweenness centrality values with a bar plot  
plt.figure(figsize=(12, 6), dpi=1000)  
plt.bar(betweenness_centrality.keys(), betweenness_centrality.values(), color='orange')  
plt.xlabel('Protein')  
plt.ylabel('Betweenness Centrality')  
plt.title('Betweenness Centrality of Proteins in PPI Network')  
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()  
  
  
# Visualize the degree centrality results  
plt.figure(figsize=(12, 6), dpi=1000)  
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True, font_size=8,  
                 node_size=[v * 3000 for v in degree_centrality.values()], node_color=list(degree_centrality.values()),  
                 cmap=plt.cm.Blues, font_color="black", font_weight="bold", edge_color="gray", width=1)  
plt.title('Degree Centrality of Proteins in PPI Network')  
plt.colorbar(label='Degree Centrality')  
plt.show()  
