[user]
  email = ylxbsoftware@gmail.com
  name = ylxbsoftware
[credential]
  helper = store
[alias]
  st = status
  co = checkout
  ci = commit
  br = branch
  unstage = reset HEAD
  hist = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
[core]
  excludesfile = /Users/wanbao/.gitignore_global
  autocrlf = false
[difftool "sourcetree"]
  cmd = opendiff \"$LOCAL\" \"$REMOTE\"
  path =
[mergetool "sourcetree"]
  cmd = /Applications/SourceTree.app/Contents/Resources/opendiff-w.sh \"$LOCAL\" \"$REMOTE\" -ancestor \"$BASE\" -merge \"$MERGED\"
  trustExitCode = true
[push]
  default = simple
