import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load integrated omics data
integrated_data = pd.read_csv('results/integrated_data.csv')

# Visualize gene expression levels
gene_columns = integrated_data.filter(like='Transcriptomics').columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=integrated_data[gene_columns])
plt.title('Gene Expression Levels')
plt.xlabel('Genes')
plt.ylabel('Expression Level')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/gene_expression_levels.png')
plt.show()

# Visualize protein abundances
protein_columns = integrated_data.filter(like='Proteomics').columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=integrated_data[protein_columns])
plt.title('Protein Abundances')
plt.xlabel('Proteins')
plt.ylabel('Abundance')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/protein_abundances.png')
plt.show()

print("Visualization complete. Plots saved to 'results' directory.")
