import requests

class GitHubUser:
    def __init__(self, username):
        self.username = username
        self.api_url = f"https://api.github.com/users/{self.username}"
        self.repos_url = f"https://api.github.com/users/{self.username}/repos"

    def get_user_info(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_first_repo_date(self):
        response = requests.get(self.repos_url)
        if response.status_code == 200:
            repos = response.json()
            if repos:
                # Sort repos by creation date
                sorted_repos = sorted(repos, key=lambda repo: repo['created_at'])
                first_repo = sorted_repos[0]
                return first_repo['created_at'], first_repo['name']
            else:
                return None, None
        else:
            return None, None

    def display_user_info(self):
        user_info = self.get_user_info()
        if user_info:
            print(f"User: {user_info['login']}")
            print(f"Name: {user_info['name']}")
            print(f"Bio: {user_info['bio']}")
            print(f"Public Repos: {user_info['public_repos']}")
            print(f"Followers: {user_info['followers']}")
            print(f"Following: {user_info['following']}")
            print(f"Account Created At: {user_info['created_at']}")

            first_repo_date, first_repo_name = self.get_first_repo_date()
            if first_repo_date:
                print(f"First Repository: {first_repo_name}")
                print(f"First Repository Created At: {first_repo_date}")
            else:
                print("No repositories found or unable to fetch them.")
        else:
            print(f"Failed to fetch information for user: {self.username}")

# Usage
if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    github_user = GitHubUser(username)
    github_user.display_user_info()
