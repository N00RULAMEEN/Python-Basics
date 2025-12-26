# from museum.artists import get_artists
from artwork import get_artworks

from artists import get_artists

def main():
    print("Search the Art Institute of Chicago! \n")

    artist = input("Artist: ")
    artists = get_artists(query=artist, limit = 3)
    for artist in artists:
        print(f"* {artist}")

main()




"""
from artwork import get_artworks

def main():
    print("Search the Art Institute of Chicago! \n")

    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit = 3)
    for artwork in artworks:
        print(f"* {artwork}")

main()

"""

# here yu coud move both packages artists.py & artwrok.py to a folder name it museum and yu could imort like this
# from museum.artist import get_artists