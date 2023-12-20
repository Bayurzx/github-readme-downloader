import os
import requests


def download_readme_files(repo_urls, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for url in repo_urls:
        # Extract the owner and repo name from the GitHub URL
        parts = url.strip("/").split("/")
        owner = parts[-2]
        repo = parts[-1]

        # Construct the API URL to get the README content
        api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

        # Send a GET request to the GitHub API
        response = requests.get(api_url)

        if response.status_code == 200:
            # Get the content of the README file
            readme_content = response.json().get("content", "")

            # Decode the Base64-encoded content
            import base64
            readme_content = base64.b64decode(readme_content).decode("utf-8")

            # Save the content to a file
            readme_file_path = os.path.join(
                output_dir, f"{owner}_{repo}_README.md")
            with open(readme_file_path, "w", encoding="utf-8") as readme_file:
                readme_file.write(readme_content)
            print(
                f"Downloaded README.md from {owner}/{repo} to {readme_file_path}")
        else:
            print(
                f"Failed to download README.md from {owner}/{repo}: {response.status_code}")


# Example usage:
repo_urls_to_download = [
    "https://github.com/moment/moment",
    "https://github.com/lodash/lodash",
    "https://github.com/expressjs/express",
    "https://github.com/facebook/react",
    "https://github.com/axios/axios",
    "https://github.com/jmespath/jmespath.py",
    "https://github.com/python-pillow/Pillow",
    "https://github.com/fastify/fastify",
    "https://github.com/graphql/graphql-js",
    "https://github.com/socketio/socket.io",
    # Add more repository URLs here
]
output_directory = "."
download_readme_files(repo_urls_to_download, output_directory)
