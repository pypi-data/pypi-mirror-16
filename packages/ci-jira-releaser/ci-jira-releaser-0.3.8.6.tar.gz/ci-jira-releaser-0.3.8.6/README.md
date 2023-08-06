# ci-jira-releaser
Simple way to release past(or current) commits within Jira

Credit to @shamrin for the name generator code [https://github.com/shamrin/namesgenerator](https://github.com/shamrin/namesgenerator)

```
usage: ci-jira-releaser [-h] -p PROJECT_KEY -u JIRA_URL [-r REPO_ROOT]
                        [-U JIRA_USERNAME] [-P JIRA_PASSWORD] --from-commit
                        FROM_COMMIT [--to-commit TO_COMMIT]
                        [--project-name PROJECT_NAME]
                        [--build-number BUILD_NUMBER] [--development]
                        [--production]

A simple way to label development tags or auto make a releaser within Jira

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_KEY, --project-key PROJECT_KEY
                        The Jira project key: e.g PROJ
  -u JIRA_URL, --jira-url JIRA_URL
                        The url Jira is located at including http://
  -r REPO_ROOT, --repo-root REPO_ROOT
                        The location of the git repo, must have a .git inside
  -U JIRA_USERNAME, --jira-username JIRA_USERNAME
                        environment_var[JIRA_USER]
  -P JIRA_PASSWORD, --jira-password JIRA_PASSWORD
                        environment_var[JIRA_PASSWORD]
  --from-commit FROM_COMMIT
                        Hash of git commit to start grabbing issues from
  --to-commit TO_COMMIT
                        End commit to parse through
  --project-name PROJECT_NAME
                        The name of the project to help generate the label
  --build-number BUILD_NUMBER
                        For build systems usually an environment variable.
                        Usually passed by Jenkins as a ENV variable.
  --development         Pass flag if using for development
  --production          Pass flag if using for production

Don't forget you can use environment variables
  ```
Examples
-- 

Development  
---
```
ci-jira-releaser -p PROJ -u http://site.atlassian.net --from-commit SHA -r ~/my-project --project-name my-project --build-number 123 --development
```
Production
---  
```
ci-jira-releaser -p PROJ -u http://site.atlassian.net --from-commit SHA -r ~/my-project --production
```