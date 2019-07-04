import webbrowser
import pandas as pd
import sys
import os
import argparse
import re
#%%
# parse input arguments
# - watchlist file
# - open selection in browser
parser = argparse.ArgumentParser(description='Select watchlist file')
parser.add_argument('-f', dest="imdb_file", metavar='watchlist', type=str, default='WATCHLIST.csv',
                    help='Watchlist file that will be loaded')
parser.add_argument('-b', dest="open_browser", metavar='browser_open', type=str, default='no',
                    help='Open imdb page in browser (yes/no)')
parser.add_argument('-g', dest="genre", metavar='genre_film', type=str, default=None,
                    help='Define a genre of interest')
args = parser.parse_args()
#%%
#imdb=pd.read_csv(os.path.join(sys.path[0], 'WATCHLIST.csv'),delimiter=',',encoding = 'latin')
imdb=pd.read_csv(os.path.join(sys.path[0], args.imdb_file),delimiter=',',encoding = 'latin')
#%%
def sel_genre(x):
    return re.match(args.genre,x)
if args.genre is not None:    
    imdb_row=imdb["Genres"].apply(lambda x: sel_genre(str(x)) is not None)
    imdb = imdb.loc[imdb_row]
#%%
satisfied = 'no'
browser   = 'no'
while satisfied != 'yes':
    movie=imdb.sample(axis=0)    
    print('\nMovie: {}'.format(movie.iloc[0]["Title"]))
    print('IMDB Rating: {}'.format(movie.iloc[0]["IMDb Rating"]))
    print('Genre: {}'.format(movie.iloc[0]["Genres"]))
    print('Year: {}'.format(movie.iloc[0]["Year"]))
    print('Runtime: {}\n'.format(movie.iloc[0]["Runtime (mins)"]))
    print('URL: {}\n'.format(movie.iloc[0]["URL"]))
    if args.open_browser.lower()=='yes' or browser == 'yes':
        webbrowser.open(movie.iloc[0]["URL"])
    satisfied = input('Enter yes if you are satisfied, otherwise press ENTER'
                      '(to show selections in browser type "browser"):\n')
    if satisfied.lower() == "browser":
    	browser = 'yes'
    	browser='yes'