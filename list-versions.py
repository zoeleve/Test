import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_package_versions(owner, repo, package_name):
    token = os.getenv("GH_TOKEN")
    if not token:
        print("GitHub token not found. Please set it in your environment variables.")
        return

    api_url = f"https://api.github.com/repos/{owner}/{repo}/packages/container/{package_name}/versions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        versions = response.json()
        if versions:
            print(f"Versions for package '{package_name}':")
            for version in versions:
                print(version["name"])
        else:
            print(f"No versions found for package '{package_name}'.")
    else:
        print(
            "Failed to fetch package versions. Check the package name and your API token."
        )


if __name__ == "__main__":
    owner = input("Enter the GitHub owner (user/org): ")
    repo = input("Enter the repository name: ")
    package_name = input("Enter the package name: ")
    get_package_versions(owner, repo, package_name)
