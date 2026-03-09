import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('racetams_properties.csv')

# Set the style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))

# Create the scatter plot
scatter = sns.scatterplot(
    data=df, 
    x='TPSA', 
    y='LogP', 
    size='MW', 
    hue='Name', 
    palette='viridis', 
    sizes=(100, 500),
    alpha=0.7
)

# Add labels for each point
for i in range(df.shape[0]):
    plt.text(
        df.TPSA[i]+1, 
        df.LogP[i]+0.05, 
        df.Name[i], 
        fontsize=10, 
        weight='bold'
    )

# Highlight the "Ideal CNS Penetration Zone"
# Typically TPSA < 60-70 and LogP > 0
plt.axvspan(0, 70, color='green', alpha=0.1, label='Ideal CNS Zone (TPSA < 70)')
plt.axhspan(0, 3, color='blue', alpha=0.05, label='Ideal CNS Zone (LogP > 0)')

# Add titles and labels
plt.title('Racetams: Physicochemical Properties & CNS Penetration Potential', fontsize=16, pad=20)
plt.xlabel('Topological Polar Surface Area (TPSA, Å²)', fontsize=12)
plt.ylabel('Lipophilicity (LogP)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Add annotations for Rule of Five
plt.text(85, 2.5, "Lipinski's Rule of Five:\nMW < 500 (All Pass)\nLogP < 5 (All Pass)\nHBD < 5 (All Pass)\nHBA < 10 (All Pass)", 
         bbox=dict(facecolor='white', alpha=0.5), fontsize=10)

plt.tight_layout()
plt.savefig('racetams_analysis_plot.png', dpi=300)
print("Visualization saved as racetams_analysis_plot.png")
