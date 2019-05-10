import webbrowser
import pandas as pd
import sys
import os

imdb=pd.read_csv(os.path.join(sys.path[0], 'WATCHLIST.csv'),delimiter=',',encoding = 'latin')

satisfied = 'no'
while satisfied != 'yes':
    movie=imdb.sample(axis=0)    
    print('\nMovie: {}'.format(movie.iloc[0]["Title"]))
    print('Rating: {}'.format(movie.iloc[0]["IMDb Rating"]))
    print('Genre: {}'.format(movie.iloc[0]["Genres"]))
    print('Year: {}'.format(movie.iloc[0]["Year"]))
    print('Runtime: {}\n'.format(movie.iloc[0]["Runtime (mins)"]))
    print('URL: {}\n'.format(movie.iloc[0]["URL"]))
    webbrowser.open_new(movie.iloc[0]["URL"])
    satisfied = input('Enter yes if you are satisfied, otherwise press ENTER:\n')
    
    #%%
loc= os.path.realpath(os.path.join(os.getcwd(), os.path.dirname('WATCHLIST.csv')))