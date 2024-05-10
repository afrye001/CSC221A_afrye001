import requests
import matplotlib.pyplot as plt

url = 'https://api.github.com/search/repositories'
params = {
    'q': 'language:javascript language:ruby language:c language:java language:perl language:haskell language:go',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 5
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    repos = [repo['name'] for repo in data['items']]
    stars = [repo['stargazers_count'] for repo in data['items']]

    plt.bar(repos, stars)
    plt.xlabel('Repository')
    plt.ylabel('Stars')
    plt.title('Most Popular Repositories in Other Languages')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("Failed to retrieve data from GitHub API. Status code:", response.status_code)
