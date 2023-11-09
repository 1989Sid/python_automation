
import requests
import os

def get_repos(username, token):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get repositories. Status code: {response.status_code}")

def clone_repo(repo_url, repo_name):
    os.system(f'git clone {repo_url} {repo_name}')

def create_repo(repo_name, token):
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization': f'token {token}'}
    data = {'name': repo_name, 'auto_init': True}
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
        return response.json()['clone_url']
    else:
        raise Exception(f"Failed to create repository. Status code: {response.status_code}")

def push_to_repo(local_repo_path, target_repo_url):
    os.system(f'cd {local_repo_path} && git remote add target {target_repo_url} && git push target --all')

# GitHub username and access token
source_username = 'iam-veeramalla'
target_username = '1989Sid'
github_access_token = 'ghp_mx6546btr464drb64d64gb6dkhwj7'

# Get repositories from source user
repos = get_repos(source_username, github_access_token)

# Iterate through repositories
for repo in repos:
    repo_name = repo['name']

    # Clone the repository
    clone_repo(repo['clone_url'], repo_name)

    # Create a repository in the target account
    target_repo_url = create_repo(repo_name, github_access_token)

    # Push the cloned repository to the target repository
    push_to_repo(repo_name, target_repo_url)
