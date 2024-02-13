import requests


def list_github_packages(owner, repo, token):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/packages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        packages = response.json()
        if packages:
            print(f"Packages found for {owner}/{repo}:")
            for package in packages:
                print(f"Name: {package['name']}, ID: {package['id']}")
        else:
            print("No packages found.")
    else:
        print(
            "Failed to fetch packages. Make sure the repository exists and your API token is correct."
        )


# Example usage
if __name__ == "__main__":
    OWNER = "zoeleve"
    REPO = "TEST"
    TOKEN = "your_github_token"
    list_github_packages(OWNER, REPO, TOKEN)
