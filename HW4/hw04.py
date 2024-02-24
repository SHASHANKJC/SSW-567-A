"""
This file contains code utilizing a REST-based API that takes in a user's GitHub 
user ID and output's a list of the names of the repositories the user has along 
with number of commits that are in each of the repositories. 
Functions: get_user_repositories
Libraries used: requests, json
"""
import requests
import json


def get_user_repositories(user_id):
    """
    Prints the the user's repositories and commits in each repository. 
    If the response status code when fetching the user's repositories
    is not 200, an error message is displayed. Else, iterate through each
    repository. If the response status code when fetching the user's 
    repository's commits is not 200, an error message is displayed. Else, 
    the repository and number of commits is displayed on a single line.
    Args:
        user_id: string value of the user's GitHub ID
    Returns:
        N/A
    Raises:
        N/A
    """
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
