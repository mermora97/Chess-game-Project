import pandas as pd

#This database is used to find the opening name of the chess game
df = pd.read_csv('Input/games.csv')
df['opening_moves'] = df.apply(lambda m:m.moves.split(' ')[:m.opening_ply],axis = 1)

def openingName(game):
    for index,opening in enumerate(df.opening_moves):
        if game[:df.opening_ply[index]] == opening:
            return(df.opening_name[index])

#Save modified database
df.to_csv('Output/openings.csv')