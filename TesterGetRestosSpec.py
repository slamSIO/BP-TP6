#!/usr/bin/python3
# coding: utf-8


def affRestos():
    global lesRestos

    for unResto in lesRestos:
        if unResto['ouvert'] == True:
            libelleOuverture = 'ouvert'
        else:
            libelleOuverture = 'fermé'
        print( '{0} : {1}\t{2}'.format( unResto['arrdt'] , unResto['nom'] , libelleOuverture ) )


def getRestosSpec( specialite ) :
    global lesRestos

    # Votre code ici - Exercice 5


if __name__ == '__main__':
    lesRestos = [

        {'nom': 'Hao Long', 'arrdt': 1, 'ouvert': True, 'spec': 'chinois'},
        {'nom': 'A Casaluna', 'arrdt': 1, 'ouvert': True, 'spec': 'corse'},
        {'nom': 'Le Pot de Vins', 'arrdt': 1, 'ouvert': False, 'spec': 'français'},
        {'nom': 'Comptoir Montevideo', 'arrdt': 1, 'ouvert': False, 'spec': 'latino'},
        {'nom': 'Carrousel Français', 'arrdt': 1, 'ouvert': True, 'spec': 'français'},
        {'nom': 'Mumi', 'arrdt': 1, 'ouvert': True, 'spec': 'français'},
        {'nom': 'L\'Atelier du Tartare', 'arrdt': 1, 'ouvert': True, 'spec': 'français'},
        {'nom': 'Lobster Bar', 'arrdt': 1, 'ouvert': True, 'spec': 'américain'},
        {'nom': 'Sequana', 'arrdt': 1, 'ouvert': True, 'spec': 'français'},
        {'nom': 'Autour du Saumon Convention', 'arrdt': 15, 'ouvert': True, 'spec': 'scandinave'},
        {'nom': 'Chez Marc', 'arrdt': 15, 'ouvert': True, 'spec': 'libanais'},
        {'nom': 'Jeongané', 'arrdt': 15, 'ouvert': True, 'spec': 'coréen'},
        {'nom': 'Neige d\'été', 'arrdt': 15, 'ouvert': True, 'spec': 'fusion'},
        {'nom': 'Le Caroubier', 'arrdt': 15, 'ouvert': True, 'spec': 'marocain'},
        {'nom': 'Le Quinzième', 'arrdt': 15, 'ouvert': False, 'spec': 'français'},
        {'nom': 'Ristorantino Shardana', 'arrdt': 15, 'ouvert': False, 'spec': 'italien'},
        {'nom': 'Hanaza', 'arrdt': 15, 'ouvert': True, 'spec': 'japonais'},
        {'nom': 'Tipaza', 'arrdt': 15, 'ouvert': True, 'spec': 'marocain'},
        {'nom': 'Le Palais de Shah Jahan', 'arrdt': 15, 'ouvert': False, 'spec': 'indien'},
        {'nom': 'La Table Libanaise', 'arrdt': 15, 'ouvert': True, 'spec': 'libanais'},
        {'nom': 'Terres du Sud', 'arrdt': 15, 'ouvert': True, 'spec': 'latino'},
        {'nom': 'Sagarmatha', 'arrdt': 15, 'ouvert': True, 'spec': 'libanais'},
        {'nom': 'Lakou', 'arrdt': 15, 'ouvert': True, 'spec': 'asiatique'}

    ]

    selectionRestos = getRestosSpec( 'libanais' )

    print( 'Restaurants libanais :\n' )

    for unResto in selectionRestos :
        print( '\t-', unResto[ 'nom' ] , '\tArrondissement :' , unResto[ 'arrdt' ] )
