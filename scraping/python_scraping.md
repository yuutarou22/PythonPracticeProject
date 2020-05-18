# ＜Pythonを使ってYahooニュースをスクレイピングする＞
pipを使って、サードパーティが配布しているrequestsをインストールする

`$ pip install requests`
> Requirement already satisfied: requests in /Library/Python/2.7/site-packages (2.20.0)
Requirement already satisfied: idna<2.8,>=2.5 in /Library/Python/2.7/site-packages (from requests) (2.7)
Requirement already satisfied: urllib3<1.25,>=1.21.1 in /Library/Python/2.7/site-packages (from requests) (1.24)
Requirement already satisfied: certifi>=2017.4.17 in /Library/Python/2.7/site-packages (from requests) (2018.10.15)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /Library/Python/2.7/site-packages (from requests) (3.0.4)
You are using pip version 18.1, however version 19.0.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

pipのバージョンが低いと言われたら、pipをアップグレードする。

`$ sudo pip install --upgrade pip`

> Password:
The directory '/Users/yutaro_matsunaga/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/yutaro_matsunaga/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting pip
  Downloading https://files.pythonhosted.org/packages/d8/f3/413bab4ff08e1fc4828dfc59996d721917df8e8583ea85385d51125dceff/pip-19.0.3-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 1.1MB/s 
Installing collected packages: pip
  Found existing installation: pip 18.1
    Uninstalling pip-18.1:
      Successfully uninstalled pip-18.1
Successfully installed pip-19.0.3

改めてrequestsをインストールする

`$ pip install requests`

> DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
Requirement already satisfied: requests in /Library/Python/2.7/site-packages (2.20.0)
Requirement already satisfied: idna<2.8,>=2.5 in /Library/Python/2.7/site-packages (from requests) (2.7)
Requirement already satisfied: urllib3<1.25,>=1.21.1 in /Library/Python/2.7/site-packages (from requests) (1.24)
Requirement already satisfied: certifi>=2017.4.17 in /Library/Python/2.7/site-packages (from requests) (2018.10.15)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /Library/Python/2.7/site-packages (from requests) (3.0.4)

プロジェクトファイルを作成（今回はデスクトップに作成する）
```
$ cd Desktop/
$ mkdir python_project
$ ls
python_project  
$ cd python_project/
$ ls
$ mkdir scraping
$ ls
scraping
$ cd scraping
$ vi scraping.py 
（viで存在しないファイル名で編集を始めると、自動で新規作成してくれる）
$ ls
scraping.py
```

中身を確認する
```
$ cat scraping.py 
import requests
r = requests.get('https://news.yahoo.co.jp/')
print(r.headers)
print('------------------')
print(r.encoding)
```

pyenvをインストールする
（なんか、Homebrewのアップグレードもやっちゃったみたい。）
```
$ brew install pyenv
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/core).
==> New Formulae
apache-arrow             cmusfm                   gtranslator              libkeccak                protoc-gen-go            signal-cli               ungit
apache-arrow-glib        cstore_fdw               h3                       libopenmpt               re-flex                  spirv-cross              usbredir
bumpversion              diskus                   homeassistant-cli        mage                     reprepro                 step                     vulkan-headers
cafeobj                  fff                      jinja2-cli               man-db                   riff                     swagger2markup-cli
cassandra-reaper         git-absorb               jp                       phpmd                    sha3sum                  tesseract-lang
==> Updated Formulae
ruby-build ✔                       cmus                               gibo                               logstash                           psql2csv
abcde                              cockroach                          git                                logtalk                            pulumi
abcmidi                            cocoapods                          git-extras                         lolcat                             pushpin
.............
cmark-gfm                          ghc                                logrotate                          prometheus
==> Renamed Formulae
resin-cli -> balena-cli                                                                todolist -> ultralist
==> Installing dependencies for pyenv: readline
==> Installing pyenv dependency: readline
==> Downloading https://homebrew.bintray.com/bottles/readline-8.0.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring readline-8.0.0.sierra.bottle.tar.gz
==> Caveats
readline is keg-only, which means it was not symlinked into /usr/local,
because macOS provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only.
For compilers to find readline you may need to set:
  export LDFLAGS="-L/usr/local/opt/readline/lib"
  export CPPFLAGS="-I/usr/local/opt/readline/include"
For pkg-config to find readline you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/readline/lib/pkgconfig"
==> Summary
🍺  /usr/local/Cellar/readline/8.0.0: 48 files, 1.5MB
==> Installing pyenv
==> Downloading https://homebrew.bintray.com/bottles/pyenv-1.2.9.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring pyenv-1.2.9.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/pyenv/1.2.9: 619 files, 2.4MB
==> `brew cleanup` has not been run in 30 days, running now...
Removing: /Users/yutaro_matsunaga/Library/Caches/Homebrew/ruby-build--20181225.tar.gz... (59.0KB)
Removing: /Users/yutaro_matsunaga/Library/Caches/Homebrew/portable-ruby-2.3.3.leopard_64.bottle.1.tar.gz... (12.3MB)
Pruned 0 symbolic links and 2 directories from /usr/local
==> Caveats
==> readline
readline is keg-only, which means it was not symlinked into /usr/local,
because macOS provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only.
For compilers to find readline you may need to set:
  export LDFLAGS="-L/usr/local/opt/readline/lib"
  export CPPFLAGS="-I/usr/local/opt/readline/include"
For pkg-config to find readline you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/readline/lib/pkgconfig"
$ vim ~/.bash_profile
$ cat ~/.bash_profile
# show git branch
# https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
source ~/.git-prompt.sh
# Color-coded and displayed.
alias ls='ls -G'
export PS1='\[\e[30;47m\] \t \[\e[37;46m\]▶︎\[\e[30m\] \W \[\e[36;49m\]▶︎\[\e[0m\] $(__git_ps1 "(%s)") $ '
source ~/.bashrc
#nodebrew
export PATH=$PATH:$HOME/.nodebrew/current/bin
export ANDROID_HOME=/Users/yutaro_matsunaga/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
export PATH=$ANDROID_HOME/build-tools/25.0.3:$PATH
```

以下を追加
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(rbenv init -)"
```

bashを反映する
```
bash-20190301 15:54:04 scraping$ source ~/.bash_profile
bash-20190301 15:54:54 scraping$ pyenv install --list
Available versions:
  2.1.3
  2.2.3
  2.3.7
  2.4
  2.4.1
  2.4.2
  2.4.3
  2.4.4
.....
```

pyenvのインストールとパスを通すことが完了したので、
pyenvを使って、Python 3.5.0をインストールする
```
$ pyenv install 3.5.0
python-build: use openssl from homebrew
python-build: use readline from homebrew
Downloading Python-3.5.0.tar.xz...
-> https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz
Installing Python-3.5.0...
python-build: use readline from homebrew
Installed Python-3.5.0 to /Users/yutaro_matsunaga/.pyenv/versions/3.5.0
```

pyenvを使って、バージョンの切り替えをしてみる。
localの場合は今いるディレクトリに、
globalの場合は全体に反映される。
```
$ python --version
Python 2.7.10
$ pyenv local 3.5.0
$ python --version
Python 3.5.0
```

序盤でインストールしたrequestsはバージョン3以上に対応していないため、
インストールし直す。
```
$ pip3 install requests
Collecting requests
  Downloading https://files.pythonhosted.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl (57kB)
    100% |████████████████████████████████| 61kB 575kB/s 
Collecting urllib3<1.25,>=1.21.1 (from requests)
  Downloading https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl (118kB)
    100% |████████████████████████████████| 118kB 472kB/s 
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
    100% |████████████████████████████████| 135kB 555kB/s 
Collecting idna<2.9,>=2.5 (from requests)
  Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 2.3MB/s 
Collecting certifi>=2017.4.17 (from requests)
  Downloading https://files.pythonhosted.org/packages/9f/e0/accfc1b56b57e9750eba272e24c4dddeac86852c2bebd1236674d7887e8a/certifi-2018.11.29-py2.py3-none-any.whl (154kB)
    100% |████████████████████████████████| 155kB 423kB/s 
Installing collected packages: urllib3, chardet, idna, certifi, requests
Successfully installed certifi-2018.11.29 chardet-3.0.4 idna-2.8 requests-2.21.0 urllib3-1.24.1
You are using pip version 7.1.2, however version 19.0.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
bash-20190301 16:04:43 scraping$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/d8/f3/413bab4ff08e1fc4828dfc59996d721917df8e8583ea85385d51125dceff/pip-19.0.3-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 130kB/s 
Installing collected packages: pip
  Found existing installation: pip 7.1.2
    Uninstalling pip-7.1.2:
      Successfully uninstalled pip-7.1.2
Successfully installed pip-19.0.3
$ pip3 install requests
Requirement already satisfied: requests in /Users/yutaro_matsunaga/.pyenv/versions/3.5.0/lib/python3.5/site-packages (2.21.0)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /Users/yutaro_matsunaga/.pyenv/versions/3.5.0/lib/python3.5/site-packages (from requests) (3.0.4)
Requirement already satisfied: urllib3<1.25,>=1.21.1 in /Users/yutaro_matsunaga/.pyenv/versions/3.5.0/lib/python3.5/site-packages (from requests) (1.24.1)
Requirement already satisfied: certifi>=2017.4.17 in /Users/yutaro_matsunaga/.pyenv/versions/3.5.0/lib/python3.5/site-packages (from requests) (2018.11.29)
Requirement already satisfied: idna<2.9,>=2.5 in /Users/yutaro_matsunaga/.pyenv/versions/3.5.0/lib/python3.5/site-packages (from requests) (2.8)
```

スクレイピング実行！
```
$ python scraping.py 
{'Via': 'http/1.1 edge2454.img.djm.yahoo.co.jp (ApacheTrafficServer [c sSf ])', 'Transfer-Encoding': 'chunked', 'Server': 'ATS', 'Content-Type': 'text/html;charset=UTF-8', 'Content-Language': 'en-US', 'Age': '1', 'Date': 'Fri, 01 Mar 2019 07:05:17 GMT', 'Vary': 'Accept-Encoding', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'X-Vcap-Request-Id': '60d0d2de-562d-4973-5fd1-9cb1fcd8cd46', 'Set-Cookie': 'B=5ou6plqvap76d&b=3&s=27; Max-Age=63072000; Expires=Mon, 01-Mar-2021 07:05:18 GMT; Domain=yahoo.co.jp; Path=/, TLS=v=1.2&r=1; path=/; domain=.yahoo.co.jp; Secure'}
------------------
UTF-8
bash-20190301 16:05:18 scraping$ 
```

それぞれ取得したいデータを指定してあげるとその情報のみ抜き出すことができる。

headers → ヘッダー
encoding → エンコード情報(UTF-8とか)
content → スクレイピングしてきたhtmlの内容（これが本体）

beautifulsoupとは、requestsなどで取ってきたスクレイピングデータを実際に解析するツール。
いわゆるパーサーと呼ばれているもの。そのパーサーをインストールする。

```
$ pip3 install beautifulsoup4
Collecting beautifulsoup4
  Downloading https://files.pythonhosted.org/packages/1d/5d/3260694a59df0ec52f8b4883f5d23b130bc237602a1411fa670eae12351e/beautifulsoup4-4.7.1-py3-none-any.whl (94kB)
    100% |████████████████████████████████| 102kB 417kB/s 
Collecting soupsieve>=1.2 (from beautifulsoup4)
  Downloading https://files.pythonhosted.org/packages/77/78/bca00cc9fa70bba1226ee70a42bf375c4e048fe69066a0d9b5e69bc2a79a/soupsieve-1.8-py2.py3-none-any.whl (88kB)
    100% |████████████████████████████████| 92kB 1.1MB/s 
Installing collected packages: soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.7.1 soupsieve-1.8
$ vi scraping.py 
$ cat scraping.py 
import requests
from bs4 import BeautifulSoup
html = requests.get('https://news.yahoo.co.jp/')
yahoo = BeautifulSoup(html.content, "html.parser")
for title in yahoo.select("ul.toptopics_list"):
    print (title.getText())
print('------------------')
print(html.encoding)
bash-20190301 16:27:44 scraping$ python scraping.py 
          予算案めぐり攻防 今夜ヤマ場
          動画
          北に抵抗 団体が「臨時政府」
          
        
          タカタ元社員がインサイダー
          NEW
          駆除したシカ ライオンの餌に
          NEW
          虎仕様ICOCA求め 420分待ち
          
        
          引退臨む岩瀬&荒木が育成契約
          NEW
          太川&蛭子復活 テレ東旅番組
          NEW
          ZIP!卒業残念 オイル関連協会
          
        
もっと見る
全カテゴリのトピックス一覧
------------------
UTF-8
```

# 補足
### pip
Pythonのパッケージ管理ツールのこと。
パッケージには、公式が配布しているものと、サードパーティ（第三者団体）が配布しているものがある。
公式が配布しているパッケージは、大抵Pythonのインストール時に付属されているが、
サードパーティが配布しているものは別でインストールする必要がある。その際に使うのがpip。
パッケージの管理も簡単にできる。
「python -m pip list」
### requestパッケージとは
「人間のためのHTTP」とも呼ばれている。
https://requests-docs-ja.readthedocs.io/en/latest/
簡単にHTTPリクエストを作成できる。
特定のWebサイトの情報をJSONで返してくれる。
### pyenv とは
複数バージョンのPythonをインストールし、バージョンを切り替えることが可能なツール。
折りたたむ
