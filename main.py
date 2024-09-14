import requests

class GitHubUser:
    def __init__(self, username):
        self.username = username
        self.api_url = f"https://api.github.com/users/{self.username}"

    def get_user_info(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def display_user_info(self):
        user_info = self.get_user_info()
        if user_info:
            print(f"User: {user_info['login']}")
            print(f"Name: {user_info['name']}")
            print(f"Bio: {user_info['bio']}")
            print(f"Public Repos: {user_info['public_repos']}")
            print(f"Followers: {user_info['followers']}")
            print(f"Following: {user_info['following']}")
        else:
            print(f"Failed to fetch information for user: {self.username}")

# Usage
if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    github_user = GitHubUser(username)
    github_user.display_user_info()
