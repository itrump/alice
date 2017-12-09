# .bashrc

# User specific aliases and functions

# Source global definitions
if [ -f /etc/bashrc ]; then
#	. /etc/bashrc
    echo source ok
fi
#alias
alias less=' less -N '
alias ll='ls -lah'

alias p=' pwd '
alias cdp=' cd .. && pwd '
alias cdpp=' cd ../../ && pwd' 
alias cdppp=' cd ../../../ && pwd '

alias svnm=' svn st | grep -v ? '
alias svnd=' svn diff  '
alias svnn=" svn st | grep -v '^M\|^A'"

alias grep=' grep --color=auto '
alias md5sum=' md5 -r '

export SVN_EDITOR='vim'
export EDITOR='vim'
