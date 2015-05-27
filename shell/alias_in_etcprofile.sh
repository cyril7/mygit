#### Productivity
#alias makescript="fc -rnl | head -1 >"
#alias c="clear"
alias ls="ls --color=auto"
alias ll="ls --color -al"
alias wl='ll | wc -l'
alias grep='grep --color=auto'
alias rm="rm -i"                         # interactive
# alias cp="cp -iv"                      # interactive, verbose
# alias mv="mv -iv"                      # interactive, verbose


alias ..='cd ..'
alias ...='cd ../..'
# generate 8 bit random strings
alias genpasswd="strings /dev/urandom | grep -o '[[:alnum:]]' | head -n 8 | tr -d '\n'; echo"

# 进入目录并列出文件，如 cdl ../conf.d/
cls() { cd "$@" && pwd ; ls -alF; }
#cls() { cd "$1"; ls;}
mcd() { mkdir -p "$1"; cd "$1"; pwd}
md5check() { md5sum "$1" | grep "$2";}

# 备份文件
backup() { cp "$1"{,.bak};}
# 自动在文件末尾加上 .bak-日期 来备份文件，如 bak nginx.conf
bak() { cp "$@" "$@.bak"-`date +%y%m%d`; echo "`date +%Y-%m-%d` backed up $PWD/$@"; }
alias histg="history | grep"



# 解压所有归档文件工具
function extract {
 if [ -z "$1" ]; then
    # display usage if no parameters given
    echo "Usage: extract <path/file_name>.<zip|rar|bz2|gz|tar|tbz2|tgz|Z|7z|xz|ex|tar.bz2|tar.gz|tar.xz>"
 else
    if [ -f $1 ] ; then
        # NAME=${1%.*}
        # mkdir $NAME && cd $NAME
        case $1 in
          *.tar.bz2)   tar xvjf $1    ;;
          *.tar.gz)    tar xvzf $1    ;;
          *.tar.xz)    tar xvJf $1    ;;
          *.lzma)      unlzma $1      ;;
          *.bz2)       bunzip2 $1     ;;
          *.rar)       unrar x -ad $1 ;;
          *.gz)        gunzip $1      ;;
          *.tar)       tar xvf $1     ;;
          *.tbz2)      tar xvjf $1    ;;
          *.tgz)       tar xvzf $1    ;;
          *.zip)       unzip $1       ;;
          *.Z)         uncompress $1  ;;
          *.7z)        7z x $1        ;;
          *.xz)        unxz $1        ;;
          *.exe)       cabextract $1  ;;
          *)           echo "extract: '$1' - unknown archive method" ;;
        esac
    else
        echo "$1 - file does not exist"
    fi
fi
}



### System info
alias cmount="mount | column -t"
alias tree="ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'"
alias meminfo='free -m -l -t'
# 查看进程信息
alias psg='\ps aux | grep -v grep | grep --color'
# 快速查看文件末尾输出
alias tf='tail -f '
# 查看去掉#注释和空行的配置文件，如 nocomm /etc/squid/squid.conf
alias nocomm='grep -Ev '\''^(#|$)'\'''

sbs(){ du -b --max-depth 1 | sort -nr | perl -pe 's{([0-9]+)}{sprintf "%.1f%s", $1>=2**30? ($1/2**30, "G"): $1>=2**20? ($1/2**20, "M"): $1>=2**10? ($1/2**10, "K"): ($1, "")}e';}
# 快速根据进程号pid杀死进程，如 psid tomcat， 然后 kill9 两个tab键提示要kill的进程号
alias kill9='kill -9';
psid() {
  [[ ! -n ${1} ]] && return;   # bail if no argument
  pro="[${1:0:1}]${1:1}";      # process-name –> [p]rocess-name (makes grep better)
  ps axo pid,user,command | grep -v grep |grep -i --color ${pro};   # show matching processes
  pids="$(ps axo pid,user,command | grep -v grep | grep -i ${pro} | awk '{print $1}')";   # get pids
  complete -W "${pids}" kill9     # make a completion list for kk
}

#### Network
alias ipinfo="curl ifconfig.me && curl ifconfig.me/host"
# 查看服务器端口连接信息
alias netp='netstat -tulanp'
alias lsofp="lsof -P -i -n"

#### Funny
alias busy="cat /dev/urandom | hexdump -C | grep \"ca fe\""
