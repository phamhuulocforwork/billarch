#####################################
##==> Variables
#####################################
function shenv; set -gx $argv; end
source ~/.env

#####################################
##==> Aliases
#####################################
# Windows Development Aliases
alias github="cd ~/Github"

# Github alias
alias python="python3"

# Quick Navigation
alias home="cd ~"
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

# File Operations
alias ll="ls -la"
alias la="ls -la"
alias l="ls -l"
alias cls="clear"

# Git Shortcuts
alias gs="git status"
alias ga="git add"
alias gaa="git add ."
alias gc="git commit"
alias gcm="git commit -m"
alias gp="git push"
alias gl="git pull"
alias gco="git checkout"
alias gb="git branch"
alias gd="git diff"
alias glog="git log --oneline --graph --decorate"

# Node.js/NPM Shortcuts
alias ni="npm install"
alias ns="npm start"
alias nt="npm test"
alias nb="npm run build"
alias nd="npm run dev"
alias nrd="npm run dev"
alias nrs="npm run start"
alias nrt="npm run test"
alias nrb="npm run build"

# Yarn Shortcuts
alias ys="yarn start"
alias yi="yarn install"
alias yt="yarn test"
alias yb="yarn build"
alias yd="yarn dev"

# System Utils
alias reload="source ~/.zshrc"
alias editrc="code ~/.zshrc"
alias editalias="code ~/.zsh_aliases"

# Docker Shortcuts
alias dc="docker-compose" 
alias dcu="docker-compose up"
alias dcd="docker-compose down"
alias dcb="docker-compose build"
alias dps="docker ps"
alias di="docker images"

# VS Code Shortcuts
alias code="code ."
alias cursor="cursor ."
alias codeh="code ~"
alias cursorh="cursor ~"

#####################################
##==> Custom Functions
#####################################
function wget
    command wget --hsts-file="$XDG_DATA_HOME/wget-hsts" $argv
end

function nvidia-settings
    mkdir -p $XDG_CONFIG_HOME/nvidia/
    command nvidia-settings --config="$XDG_CONFIG_HOME/nvidia/settings" $argv
end

if [[ "$PWD" == "$HOME" ]]; then
    cd ~/Github
fi

function mkcd() {
    mkdir -p "$1" && cd "$1"
}

function ginit() {
    git init
    git add .
    git commit -m "feat: initial commit"
}

function gclone() {
    git clone "git@github.com:phamhuulocforwork/$1.git"
    if [ "$2" ]; then
        cd "$2"
    else
        cd "$1"
    fi
}

function mclone() {
  local file="$1"

  if [[ -z "$file" || ! -f "$file" ]]; then
    echo "Usage: mclone <file_with_repo_urls>"
    return 1
  fi

  local repos=()
  while IFS= read -r line; do
    line=$(echo "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    repos+=("$line")
  done < "$file"

  local n=${#repos[@]}
  if [[ $n -eq 0 ]]; then
    echo "File does not have a valid repo"
    return 1
  fi

  echo "Cloning $n repos in parallel..."

  if command -v parallel >/dev/null 2>&1; then
    printf "%s\n" "${repos[@]}" | parallel -j "$n" 'git clone "{}"'
  else
    for repo in "${repos[@]}"; do
      git clone "$repo" &
    done
    wait
  fi
}

function clone() {
    git clone "$1"
    if [ "$2" ]; then
        cd "$2"
    else
        cd "$(basename "$1" .git)"
    fi
}

function system-clean() {
  echo "Cleaning temp files in /tmp and /var/tmp..."
  sudo rm -rf /tmp/* /var/tmp/*

  echo "Cleaning apt cache..."
  if command -v apt-get &>/dev/null; then
    sudo apt-get clean -y
    sudo apt-get autoclean -y
    sudo apt-get autoremove -y
  fi

  echo "Cleaning pip, npm, and user cache..."
  rm -rf ~/.cache/pip ~/.npm ~/.cache/* ~/.local/share/*Trash*/files/*

  echo "Cleaning old logs..."
  sudo journalctl --vacuum-time=7d
  sudo rm -rf /var/log/*.gz /var/log/*.[0-9]

  echo "Done!"
}

function venv-clean() {
  echo "Deleting 'venv' folders..."
  find . -type d -name "venv" -exec rm -rf {} +
  echo "Done"
}

function npkill() {
  echo "Deleting 'node_modules' ..."
  find . -type d -name "node_modules" -exec rm -rf {} +
  echo "Done"
}

#####################################
##==> Interactive Session Settings
#####################################
if status is-interactive

end

if [[ "$PWD" == "$HOME" ]]; then
    cd ~/Github
fi

#####################################
##==> Shell Customization
#####################################
starship init fish | source
set fish_greeting

#####################################
##==> Development Tools
#####################################
##==> Pyenv
pyenv init - | source

#####################################
##==> Fun Stuff
#####################################
pokemon-colorscripts --no-title -s -r 1,3,6
