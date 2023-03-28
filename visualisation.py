# Importations

from preprocessing import *
import seaborn as sns
import plotly.express as px

# Affichage des premières lignes du dataset

dfi.head(20)

# Statistiques sur le dataset

dfi.describe()

# Visualisation des données
# Evolution du marché de l'immobilier sur les dernières années

sns.set(style='dark')
sns.countplot(x="year", data=dfi)

# Présentation des différents types de bien et leur volume

fig1 = px.histogram(df, x="year", color="Type local", marginal="violin")
fig1.update_layout(bargap=0.2)
fig1.show()

# Répartition des prix sur plusieurs années

fig2 = px.box(dfi, x="year", y="Valeur fonciere", hover_data=['No voie','Voie','Code postal'])
fig2.show()

# Tracé de la valeur foncière en fonction de la surface. L'objectif est de déterminer les biens d'exception qui pourraient être rénovés: grande surface et prix bas.

fig3 = px.scatter(dfi, x="Surface reelle bati", y="Valeur fonciere", color = "year", size = "Nombre pieces principales")
fig3.show()

# On se focalise désormais sur le nombre de pièces

fig4 = px.scatter(dfi, x="Valeur fonciere", y="Nombre pieces principales", color = "year", size = "Surface reelle bati", log_x=True, size_max=50)
fig4.show()

# Présentation avec informations statistiques

fig5 = px.scatter(df, x="Valeur fonciere", y="Surface reelle bati", color="year", marginal_y="violin",
           marginal_x="box", template="simple_white", log_y=True)
fig5.show()

# Présentation en 3d

fig6 = px.scatter_3d(df, x="Valeur fonciere", y="Surface reelle bati", z="Nombre pieces principales", color="year", log_x=True, log_y=True)
fig6.show()