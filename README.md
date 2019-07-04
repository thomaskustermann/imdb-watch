# imdb-watch
Small python script that randomly selects an entry from your IMDB watchlist (movie, series, other).
Requires exported watchlist from imdb (bottom of page on waitlist).
Currently allows specification of:
- Watchlist file (-f "filename")
- Open IMDB page of watchlist item in browser (-b "yes" or "no", default "no")
- Genre selection (-g "Genre", see exported IMDB watchlist file for possibilities, specifying multiple genres currently not possible)

Use "python imdb-watch.py --help" to see options

Example usage:
python imdb-watch.py -f "/Users/incognito/Downloads/watchlist.csv" -b "yes" -g "Documentary"
