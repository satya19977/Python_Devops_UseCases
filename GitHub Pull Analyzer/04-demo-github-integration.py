# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

Output Received from pr_creators dictionary
atiratree:1 PR(s)
jsafrane:1 PR(s)
mimowo:1 PR(s)
mjudeikis:1 PR(s)
carlory:1 PR(s)
liangyuanpeng:2 PR(s)
lavacat:1 PR(s)
kerthcet:2 PR(s)
yylt:1 PR(s)
deads2k:1 PR(s)
cici37:1 PR(s)
benluddy:3 PR(s)
ah8ad3:1 PR(s)
erikgb:1 PR(s)
uucloud:1 PR(s)
kkkkun:1 PR(s)
chengjoey:2 PR(s)
HirazawaUi:1 PR(s)
gjkim42:1 PR(s)
p0lyn0mial:1 PR(s)
ArkaSaha30:3 PR(s)
l-technicore:1 PR(s)
sttts:1 PR(s)
