import requests
import json


def get_user_repositories(user_id):
    # GitHub API endpoint for user repositories
    url = f'https://api.github.com/users/{user_id}/repos'

    # Make a request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            repo_name = repo['name']
            commits_url = f'https://api.github.com/repos/{user_id}/{repo_name}/commits'

            # Make a request to the GitHub API to get the commits for the repository
            commits_response = requests.get(commits_url)

            # Check if the request was successful
            if commits_response.status_code == 200:
                commits = commits_response.json()
                num_commits = len(commits)
                print(f'Repo: {repo_name} Number of commits: {num_commits}')
            else:
                print(f'Error fetching commits for repository {repo_name}')
    else:
        print(f'Error fetching repositories for user {user_id}')

# test by running this and let me know any changes is required.
# we can add a loop here to check for unlimited repos until user wants exit
# let me know if any changes is required, I'll be available


get_user_id = input('Enter the user_id you would like to: ')
get_user_repositories(get_user_id)
