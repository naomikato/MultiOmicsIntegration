import pandas as pd

# Load genomics, transcriptomics, and proteomics data
genomics_data = pd.read_csv('data/genomics_data.csv')
transcriptomics_data = pd.read_csv('data/transcriptomics_data.csv')
proteomics_data = pd.read_csv('data/proteomics_data.csv')

# Merge datasets based on Sample_ID
integrated_data = genomics_data.merge(transcriptomics_data, on='Sample_ID')
integrated_data = integrated_data.merge(proteomics_data, on='Sample_ID')

# Save integrated data to CSV
integrated_data.to_csv('results/integrated_data.csv', index=False)

print("Integration complete. Integrated data saved to 'results/integrated_data.csv'.")
