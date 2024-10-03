import requests
from bs4 import BeautifulSoup

def main():
    
    # Making a GET request to
    r = requests.get('https://www.is.fi/uutiset/')
    
    # check status code for response received
    # success code - 200
    print(r)
    
    # parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    # Finding all h2 tags with the class 'teaser-m__title teaser-title-30'
    titles = soup.find_all('h2', class_='teaser-m__title teaser-title-30')

    if titles:
        for title in titles:
            # Find the span tag within the h2 tag to get the actual text
            span = title.find('span')
            if span:
                # Print the text inside the span
                print(span.get_text(strip=True))
            else:
                print("No span tag found inside h2")
    else:
        print("No titles found.")
    
if __name__ == "__main__":
    main()