# Cheminformatics Analysis of Racetam Nootropics

## Project Overview
This project focuses on the **physicochemical property analysis** of the racetam class of nootropics. Using Python and the PubChem PUG REST API, I extracted and analyzed key molecular descriptors to evaluate their potential for **Blood-Brain Barrier (BBB) penetration** and overall drug-likeness.

## Key Objectives
*   Extract molecular properties (MW, LogP, TPSA, HBD, HBA) for 9 common racetams.
*   Evaluate adherence to **Lipinski's Rule of Five**.
*   Visualize the relationship between lipophilicity (LogP) and polar surface area (TPSA) to predict CNS activity.

## Methodology
The analysis was performed using a custom Python script leveraging the following libraries:
*   `requests`: For API interaction with PubChem.
*   `pandas`: For data manipulation and tabular representation.
*   `matplotlib` & `seaborn`: For high-quality data visualization.

### Analyzed Compounds
1. Piracetam
2. Aniracetam
3. Oxiracetam
4. Pramiracetam
5. Phenylpiracetam
6. Levetiracetam
7. Nefiracetam
8. Coluracetam
9. Fasoracetam

## Results & Findings

### 1. Physicochemical Properties Table
| Name | MW (g/mol) | LogP | TPSA (Å²) | HBD | HBA |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Piracetam** | 142.16 | -1.3 | 63.4 | 1 | 2 |
| **Aniracetam** | 219.24 | 1.6 | 46.6 | 0 | 3 |
| **Oxiracetam** | 158.16 | -2.2 | 83.6 | 2 | 3 |
| **Pramiracetam** | 269.38 | 0.8 | 52.7 | 1 | 3 |
| **Phenylpiracetam** | 218.25 | 0.1 | 63.4 | 1 | 2 |
| **Levetiracetam** | 170.21 | -0.3 | 63.4 | 1 | 2 |
| **Nefiracetam** | 246.3 | 1.4 | 49.4 | 1 | 2 |
| **Coluracetam** | 341.4 | 2.4 | 75.4 | 1 | 4 |
| **Fasoracetam** | 196.25 | 0.0 | 49.4 | 1 | 2 |

### 2. Key Insights for Drug Discovery
*   **Lipinski's Rule of Five:** All compounds fully comply with the Rule of Five (MW < 500, LogP < 5, HBD < 5, HBA < 10), indicating high oral bioavailability.
*   **CNS Penetration Potential:** 
    *   Compounds like **Aniracetam**, **Nefiracetam**, and **Fasoracetam** show optimal TPSA (< 60 Å²) and positive LogP values, suggesting superior passive diffusion across the BBB compared to the parent compound, Piracetam.
    *   **Phenylpiracetam** demonstrates how a simple structural modification (adding a phenyl group) significantly increases lipophilicity (LogP from -1.3 to 0.1), enhancing its potency.

## Visualization
The project includes a scatter plot (`racetams_analysis_plot.png`) that maps the "Ideal CNS Penetration Zone," providing a clear visual representation of which molecules are most likely to be effective nootropics based on their physical chemistry.

## How to Run
1. Ensure you have Python 3.x installed.
2. Install dependencies: `pip install requests pandas matplotlib seaborn`.
3. Run the analysis script: `python racetam_analysis.py`.
4. Generate the plot: `python visualize_racetams.py`.

---
*This project was developed as part of a professional portfolio for Pharmaceutical R&D roles.*
