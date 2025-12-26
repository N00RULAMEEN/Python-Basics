import requests


def main():
    print("Search the Art Institute of Chicago! \n")
    artist = input("Artist: ")

    try:  
        Response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
           # {q : "Monet"}

            )
        Response.raise_for_status()
    except requests.HTTPError:
        print("Coudn't complete request!")
        return
    

    content = Response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")



main()