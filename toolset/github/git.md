##  Git commands

```
git init
git add <file> OR git add .
git status
git commit -am "<commit_message>"
Clone From Github
git clone git@github.com:/<user>/<project>	Download repo (later you keep refreshing with 'git pull origin master') -> You need SSH key. If you don't want, use https://github.com/<user>/<repo> for address.
```

# Create remote repository on website.
```
git remote add origin git@github.com:/<user>/<project>.git
git pull origin master
git push origin master
```
# Sometimes also: git push --set-upstream origin master

## Tags
```
git push --tags	Push tags
git fetch --tags	Pulling tags (automatically if on the same branch and there is a new commit?)
```
## Undo
```
git reset
--hard HEAD~1	Delete last commit and all of its changes
HEAD~1	Delete last commit but keep your changes
```
