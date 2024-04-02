
def create_github_issue_in_this_repo(title, body):
	import os
	github_token = os.environ.get("GITHUB_TOKEN")
	from github import Github
	from github import Auth
	auth = Auth.Token(github_token)
	g = Github(auth=auth) # Public Web Github
	repo = g.get_repo("refigo/ai8cb")
	repo.create_issue(title=title, body=body)
	g.close()

def print_github_issues_in_this_repo():
	import os
	github_token = os.environ.get("GITHUB_TOKEN")
	from github import Github
	from github import Auth
	auth = Auth.Token(github_token)
	g = Github(auth=auth) # Public Web Github
	repo = g.get_repo("refigo/ai8cb")
	open_issues = repo.get_issues(state="open")
	for issue in open_issues:
		print(issue)
	g.close()
