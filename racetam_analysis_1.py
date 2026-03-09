import requests
import pandas as pd

def get_compound_data(name):
    try:
        # Removed 'LogP' as it's not a valid property name in PUG REST
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/MolecularWeight,XLogP,TPSA,HBondDonorCount,HBondAcceptorCount,CanonicalSMILES/JSON"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['PropertyTable']['Properties'][0]
        return None
    except:
        return None

racetams = ["Piracetam", "Aniracetam", "Oxiracetam", "Pramiracetam", "Phenylpiracetam", "Levetiracetam", "Nefiracetam", "Coluracetam", "Fasoracetam"]
data_list = []

for r in racetams:
    print(f"Fetching {r}...")
    res = get_compound_data(r)
    if res:
        row = {
            'Name': r,
            'MW': res.get('MolecularWeight'),
            'LogP': res.get('XLogP'),
            'TPSA': res.get('TPSA'),
            'HBD': res.get('HBondDonorCount'),
            'HBA': res.get('HBondAcceptorCount'),
            'SMILES': res.get('CanonicalSMILES')
        }
        data_list.append(row)

df = pd.DataFrame(data_list)
print("\nResults:")
print(df.to_markdown(index=False))
df.to_csv('racetams_properties.csv', index=False)
