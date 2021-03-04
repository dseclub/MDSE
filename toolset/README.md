# DSEtoolset


## Table of Contents

  - [Installation](#installation)
  - Integrated Development Environments (IDE)
    - [VSCode](#vscode)
    - [PySharm](#pysharm)
    - [Atom](#atom)
    - [Vim](#vim)
    - [RStudio](#rstudio)
  - [Bash Scripting / Command Line](#bash)
  - [Python virtual environments](#virtualenv)
    - [PipEnv](#pipenv)
    - [VirtualEnv](#virtualenv)
    - [PyEnv](#pyenv)
    - [Conda](#conda)
  - [Version control & repository systems](#git)
    - [Github cheat-sheet](github-cheat-sheet)
    - [Introduction to Git & Github RG](github)
  - Collaboration tools
    - [Slack](#slack)
    - [Zoom](#zoom)
  - Presentation tools
    - [Google Slides](#google-slides)
  - Resources
  - [Links](#resources)

## Installation

## Windows Development setup

Package managers like Chocolatey and Homebrew exist to streamline the process of getting new software installed (and keeping it updated) on your machine.

The package manager reduces the time to get software installed, saving hours of time and ensuring everyone's machines are setup correctly with minimal effort. Here's a quick overview of the tools you'll install in the next section:

1. A **package manager**: Chocolatey (for Windows) or Homebrew (for Mac)
2. **Docker** - to run containerized apps and create your own.
3. **Git** - a version control platform used to store and manage code.
4. **GitHub Desktop** - a friendly GUI which works with Git and GitHub.com.
5. **Python** - a software language useful for developing new programs and scripts, and also used for its popular package manager `pip`, which allows users to install Python programs written by others.
6. **Terraform** - the leading cross-platform solution for automating Infrastructure as Code (IaC).
7. **VS Code** - a robust, fast, and lightweight development environment (IDE).

## Installing Chocolatey and Core Tools

1. Open "cmd.exe" as an administrator.
2. Paste and run the [Chocolatey.org](https://chocolatey.org/docs/installation#install-with-cmdexe) install script:

    ```cmd
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```

    <a href="https://git-scm.com/"><img src="https://git-scm.com/images/logo@2x.png" alt="drawing" width="45" style="float: right"/></a>

3. Install git.

    ```cmd
    choco install -y git.install --params "/GitOnlyOnPath /SChannel /NoAutoCrlf /WindowsTerminal"
    ```

4. Install core tools:

    ```cmd
    choco install -y choco-protocol-support chocolateygui sudo terraform vscode
    choco install -y python3
    choco install -y docker-desktop
    ```

- **NOTE:** See the [Troubleshooting](#troubleshooting) tips below if you run into any difficulties during this process.

## Installing additional tools

Install any of the below that would be useful for your project, or find additional packages using [chocolatey.org/packages](https://chocolatey.org/packages)

- [choco://7zip](choco://7zip)
- [choco://anaconda3](choco://anaconda3) or [choco://miniconda](choco://miniconda)
- [choco://awscli](choco://awscli)
- [choco://GoogleChrome](choco://GoogleChrome)
- [choco://wsl](choco://wsl)
- [choco://wsl-ubuntu-1804](choco://wsl-ubuntu-1804)


## MacOS Development 

## Installing Homebrew and Core Tools

1. Open "Terminal".
2. Paste and run the [Homebrew](https://brew.sh) install script:

    ```bash
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

    <a href="https://git-scm.com/"><img src="https://git-scm.com/images/logo@2x.png" alt="drawing" width="45" style="float: right"/></a>

3. Install git.

    ```cmd
    brew install git
    ```

4. Install core tools:

    ```cmd
    brew install cask docker python3 terraform
    brew cask install cakebrew visual-studio-code
    ```

## Installing additional tools

After following the instructions from the above, you should now have the **Cakebrew** app installed, which gives a friendly GUI on top of the Homebrew installer.

To install any additional programs, either open the **Cakebrew** app or copy-paste the below samples into a Terminal window. (You can also find additional packages at [https://brew.sh](https://brew.sh).)

- `brew install awscli`
- `brew cask install github`
- `brew cask install google-chrome`
- `brew cask install slack`


##  Integrated Development Environments (IDE)

##  [VSCode](https://code.visualstudio.com/docs/python/python-tutorial)

##  [PyCharm](https://www.jetbrains.com/pycharm/)

##  [Atom](https://atom.io/)

##  [VIM](https://www.vim.org/)

[An introduction to Vim Editor (ITTCL second ed.)](https://tessarinseve.pythonanywhere.com/pelican/vim-ittcl-chapter.html)

[Jupyter notebook, JupyterHub, JupyterLab](http://jupyter.org/)

## [Nbviewer](https://nbviewer.jupyter.org/)

[Apache Zeppelin notebook](https://zeppelin.apache.org/)


## [RStudio](https://www.rstudio.com/)

## Bash
###  Bash Scripting / Command Line is a way of interacting with your computer  operating system using text-based commands.

Bash Scripting

https://programminghistorian.org/lessons/intro-to-bash

https://linuxconfig.org/bash-scripting-tutorial

Command Line

https://www.computerhope.com/issues/chusedos.htm

## Python virtual environments and package management system


### [Poetry - Python dependency management and packaging made easy](https://github.com/python-poetry/poetry) [Doc](https://python-poetry.org/docs/)

### VirtualEnv

Python virtualenv Ubuntu
```
$ sudo pip install virtualenv myenv    # if error   sudo apt install python-pip
$ sudo apt-get update
$ virtualenv myenv
$ source myenv/bin/activate          # deactivate
```

## [Conda](https://www.anaconda.com/download/) [Docs](https://conda.io/docs/)

```
$ conda create --name python37
$ conda activate python37
$ conda install pandas
$ deactivate
```
### Create a virtual environment with specific version
```
$ conda create --name mypython3version python=3.8
```
### Create a virtual environment with specific version and a single module
```
$ conda create --name mypython3version python=3.8 numpy
```
### Create a virtual environment with specific version with entire Anaconda distribution
```
$ conda create --name mypython3version python=3.8 anaconda
```
### To check the environments
```
$ conda info --envs
```

## Version control and repository systems
## Git

[Git](https://git-scm.com/)
[Github](https://github.com/)
[Gitlab](https://gitlab.com/)
[Bitbucket](https://bitbucket.org)

* [Github cheat-sheet](github-cheat-sheet)
* [Introduction to Git & Github RG](github)
* [Udacity's course How to Use Git and GitHub](udacitygitgithub)
* [Github template](github-template)

## [Vagrant](https://github.com/hashicorp/vagrant)

##  Collaboration tools

## Slack
https://dseclub.slack.com

https://join.slack.com/t/dseclub/shared_invite/enQtMjQxNTI1NDI3MjQ4LTFlZTA0NjVlNzNiMzI0MmY0YWJkNjMwYTZiY2NmMGJkMWM5NDExZTgyZTdhYzQ4NWZlYzFkNDI3ZmZjZTAyMDA

## Zoom
https://www.zoom.us/
https://blogs.otago.ac.nz/zoom/how-to-join-a-zoom-meeting-step-by-step/

## Skype
https://www.skype.com/en/

##  Presentation tools
##  Google Slides
[Google Slides](https://docs.google.com/presentation/u/0/)

##  jupyter notebook

## Resources
https://www.ngdata.com/top-tools-for-data-scientists/
