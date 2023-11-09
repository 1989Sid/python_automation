import requests
import os

# Set your GitHub username and access token
github_username = "1989Sid"
github_access_token = "ghp_msghfdytsfdhstfdhadada7"

# Set the source GitHub account and branch
source_username = "praveen1994dec"
branch = "main"

# Set the target GitHub account
target_username = "1989Sid"

# Function to authenticate with GitHub API
def get_headers():
    return {
        "Authorization": f"Bearer {github_access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

# Function to clone repositories from source account to target account
def clone_repositories():
    # Get the list of repositories from the source account
    url = f"https://api.github.com/users/{source_username}/repos"
    response = requests.get(url, headers=get_headers())
    repositories = response.json()

    # Clone each repository
    for repo in repositories:
        repo_name = repo["name"]

        # Clone the repository
        os.system(f"git clone --branch {branch} https://github.com/{source_username}/{repo_name}.git")

        # Create a new repository in the target account with the same name
        create_repo_url = f"https://api.github.com/user/repos"
        create_repo_payload = {
            "name": repo_name,
            "private": False
        }
        response = requests.post(create_repo_url, headers=get_headers(), json=create_repo_payload)
        new_repo = response.json()

        # Push the cloned repository to the new repository
        os.chdir(repo_name)
        os.system(f"git remote add origin https://github.com/{target_username}/{repo_name}.git")
        os.system("git push -u origin main")
        os.chdir("..")

        print(f"Repository '{repo_name}' cloned and pushed to '{target_username}/{repo_name}'")

if __name__ == "__main__":
    clone_repositories()
