# Importations

import pandas as pd
from tqdm.notebook import tqdm

# Données issues du site du gouvernement

url_dict = {
    '2022':'https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-152027/valeursfoncieres-2022-s1.txt',
    '2021':'https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-151704/valeursfoncieres-2021.txt',
    '2020':'https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-151136/valeursfoncieres-2020.txt',
    '2019':'https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-150616/valeursfoncieres-2019.txt',
    '2018':'https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20221017-145753/valeursfoncieres-2018.txt'
            }

# Récupération des données de toutes les années

def get_subsample():
    
    data_all_year=[]
    
    for year,url in tqdm(url_dict.items()):
        
    
        print(f'----------ANNEE {year} EN COURS----------')
        data_ = pd.read_csv(url, sep="|")
        
        # Suppression des colonnes innutiles
        data_ = data_.drop(['Reference document','1 Articles CGI','2 Articles CGI',
                                      '3 Articles CGI','4 Articles CGI','5 Articles CGI','Identifiant local','No Volume','B/T/Q',
                                      'Surface Carrez du 1er lot','2eme lot','Surface Carrez du 2eme lot','3eme lot',
                                      'Surface Carrez du 3eme lot','4eme lot','Surface Carrez du 4eme lot','5eme lot',
                                      'Surface Carrez du 5eme lot','Nature culture','Nature culture speciale','Surface terrain'], axis=1)
        
        # Restriction du dataset à une ville en particulier
        
        data_ville = data_[data_['Commune'].str.contains("BORDEAUX", na=False)]
        
        print('Shape from import: ',data_.shape)
        print('Shape after subsample: ',data_ville.shape)
        print(f'\n Sampling of {round((data_ville.shape[0]/data_.shape[0])*100,2)} % of the original dataframe \n')
        
        del data_
        
        # Ajout de la colonne année
        
        data_ville['year'] = year
        data_all_year.append(data_ville)
        del data_ville
        
        print(f'----------ANNEE {year} TERMINEE---------- \n')
        
    # Concatenation des datasets
    df = pd.concat(data_all_year)
    return df

df = get_subsample()