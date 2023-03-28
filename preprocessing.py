from data_collect import *

def preprocessing(df):
    # Format de la date
    df['Date mutation'] = pd.to_datetime(df['Date mutation'], format='%d/%m/%Y')
    df['year'] = df['Date mutation'].dt.year
    df['months'] = df['Date mutation'].dt.year
    df['day'] = df['Date mutation'].dt.year
    
    # Suppression des doublons
    
    df = df.drop_duplicates()
    
    # Restrictions aux maisons et appartements
    df = df[df['Type local'].isin(['Maison','Appartement'])]
    
    # Formatage du prix
    df['Valeur fonciere'] = df['Valeur fonciere'].str.replace(',','.')
    df['Valeur fonciere']  = df['Valeur fonciere'].astype(float)
    
    # Restriction à l'immobilier < 10M€ et moins de 21 pièces
    
    df = df[df['Valeur fonciere'] < 10000000]
    df = df[df['Nombre pieces principales'] < 21]

    return df

dfi = df.copy()   
dfi  = preprocessing(dfi)