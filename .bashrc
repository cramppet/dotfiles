# System-wide .bashrc file for interactive bash(1) shells.
if [ -z "$PS1" ]; then
   return
fi

PS1='\[\033[1;31m\u\]\[\033[1;36m\]@\[\033[1;32m\]\h\[\033[0m\] (\W)# '
# Make bash check its window size after a process completes
shopt -s checkwinsize

[ -r "/etc/bashrc_$TERM_PROGRAM" ] && . "/etc/bashrc_$TERM_PROGRAM"

alias ls='ls -G'
alias la='ls -a'
alias grep='grep --color=auto'

set -o vi
set -o ignoreeof
set -o noclobber

export TERM=xterm-256color

