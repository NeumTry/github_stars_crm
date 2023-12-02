# Github stars CRM tracker

For those building an audience, a startup, or wanting feedback of the product you just built, you can use `github_stars_crm` to keep track of the people that have given you a star in your repo to talk to them and learn about your users.

# Code

Pretty simple, nothing fancy. Just using the github apis to get the list of users who starred a repo and then getting each user's information from github, all public data.

**Stargazers api**: https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28#list-stargazers

**User's API**: "https://api.github.com/users/<user>"

**You don't need a github api key** but might get throttle pretty fast. You can get one by going to `Github Profile -> Settings -> Developer Settings -> Tokens and generating one.`

# Requirements
Python

# How to run
Clone/fork the repo or just copy the code.
run `python stars_to_csv.py`

Done!
