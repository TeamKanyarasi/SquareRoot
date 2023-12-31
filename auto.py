import requests, os

def check_for_new_commits():
    latest_commit_id = None
    headers = {'Authorization': f'token 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'}
    url = f'https://api.github.com/repos/TeamKanyarasi/CICD_Project/commits?sha=prod'
    response = requests.get(url, headers=headers)
    commit_ids = []

    if response.status_code == 200:
        commits = response.json()
        print(f'New commits found: {len(commits)}')
        for commit in commits:
            commit_ids.append({commit["sha"]})
        print(commit_ids)
    else:
        print(f'Error: {response.status_code}')
       

    if commit_ids[0] != latest_commit_id:
        latest_commit_id = commit_ids[0]
        print(latest_commit_id)
        # os.system('git pull origin prod')
        # os.system('sudo cp -rf *.html /var/www/html/')
        # os.system("sudo service nginx restart")

check_for_new_commits()