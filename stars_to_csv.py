import requests
import csv
page_num = 1
results = []
csv_file_path = "output.csv"
interested_properties = ["name", "email", "twitter_username","blog", "company", "location", "login", "type"]
github_key_for_rate_limits = "<key>"
owner = "NeumTry"
repo_name = "NeumAI"
headers = {"Authorization":f"Bearer {github_key_for_rate_limits}"}
with open(csv_file_path, 'w', newline='', encoding="cp1252") as csv_file:
    print("opening file")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(interested_properties)
    while page_num == 1 or len(results) > 0:
        print(f"Reading github stars api, page number: {page_num}")
        results = requests.get(url=f"https://api.github.com/repos/{owner}/{repo_name}/stargazers?per_page=100&page={page_num}", headers=headers).json()
        print(f"Found {len(results)} results. Reading each result and storing in csv")
        for result in results:
            user_info = requests.get(url=result['url'], headers=headers).json()    
            values = [user_info.get(prop, "") for prop in interested_properties]
            try:
                csv_writer.writerow(values)
            except Exception as e:
                print(f"could not write to csv. Error {e}. User: {user_info['login']}")
        page_num += 1

print("Finished")
