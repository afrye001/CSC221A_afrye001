import requests
import matplotlib.pyplot as plt

base_url = "https://hacker-news.firebaseio.com/v0/"

response = requests.get(base_url + "topstories.json")

if response.status_code == 200:
    top_story_ids = response.json()
    
    top_story_ids = top_story_ids[:5]
    
    top_story_details = []
    for story_id in top_story_ids:
        story_response = requests.get(base_url + f"item/{story_id}.json")
        if story_response.status_code == 200:
            story_details = story_response.json()
            top_story_details.append(story_details)
        else:
            print(f"Failed to retrieve details for story ID {story_id}")

    titles = [story['title'] for story in top_story_details]
    num_comments = [story['descendants'] if 'descendants' in story else 0 for story in top_story_details]

    # Plot the data
    plt.bar(titles, num_comments)
    plt.xlabel('Top Stories')
    plt.ylabel('Number of Comments')
    plt.title('Number of Comments on Top Stories on Hacker News')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print('Failed to retrieve data from the Hacker News API')
