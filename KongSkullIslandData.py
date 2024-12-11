import requests
from HelperFunctions import to_csv, scrape_json_key

# Information for site
base_url = "https://www.rottentomatoes.com/napi/movie/22940c20-37cd-376a-8ac9-9ce17b0a9799/reviews/all"
headers_to_be_scraped = ['criticName','creationDate','isFresh','isRotten','isTopCritic', 'quote', 'scoreSentiment','publicationName','reviewUrl']
json_key_to_scrape = 'reviews'

# Info for CSV file
file_name_to_create = "KongAllReviews.csv"
headers_for_file = ["Author", "Date", "Is Fresh", "Is Rotten", "Top Critic", "Review", "Sentiment", "Publication", "URL Publication"]

# Pagination
has_next = True
next_page = ""
data = []


while has_next:
    try:
        url = base_url + next_page
        response = requests.get(url)
        info = response.json()

        # Get data for this page
        this_pages_data = scrape_json_key(info[json_key_to_scrape],headers_to_be_scraped)
        data.extend(this_pages_data)

        # Determine if there are more pages to scrape
        has_next = info['pageInfo']['hasNextPage']
        if not has_next:
            break
        next_page = '?after=' + str(info['pageInfo']['endCursor'])
        print(next_page)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Write the data to a CSV file
        to_csv(file_name_to_create,headers_for_file,data)