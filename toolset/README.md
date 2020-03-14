# DSEtoolset


## Table of Contents

  - [Installation](#installation)
  - Operational Systems
    - [Linux Ubuntu](#ubuntu)
  - Integrated Development Environments (IDE)
    - [Anaconda](#anaconda)
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
  - Virtualization - Containerization
  - Collaboration tools
    - [Slack](#slack)
    - [Zoom](#zoom)
  - Presentation tools
    - [Google Slides](#google-slides)
  - Resources
  - [Links](#resources)

## Installation

##  Operational Systems

## Ubuntu

### Linux excels at all of these points:

## MacOS

## Windows

##  Integrated Development Environments (IDE)
##  Anaconda

[Jupyter notebook, JupyterHub, JupyterLab](http://jupyter.org/)

[Nbviewer](https://nbviewer.jupyter.org/)

[Apache Zeppelin notebook](https://zeppelin.apache.org/)

##  PyCharm
[PyCharm](https://www.jetbrains.com/pycharm/)

##  Atom
[Atom](https://atom.io/)

##  Vim - Tmux
According to a recent Stack Overflow's survey, [VIM](https://www.vim.org/) text editor is the fourth most popular developer environment and code editor despite it was first released in 1991.
The reasons for this longevity are many, it's free software with a permissive GNU-like license (VIM License), fast, cross-platform and terminal-based.

The distinctive feature compared with other popular editors is its incredibly efficient multimodal editing style that depends entirely on keyboard commands.
It's considered to be rather difficult to master at a professional level. A short introduction about VIM main can be found at this link:

[An introduction to Vim Editor (ITTCL second ed.)](https://tessarinseve.pythonanywhere.com/pelican/vim-ittcl-chapter.html)

Plugins are used to introduce new functionalities and VIM has an incredibly rich ecosystem of many, some really useful, plugins. Plugins can be written in VIM's own programming language, called Vimscript, which can be quite tricky to learn. Another approach is to write plugins with a generic programming language such as python, this requires a VIM instance compiled with the corresponding Python support, both python 2 and 3 are supported. Plugins can be installed and updated with a plugin-manager.

Some of the most widely appreciated are listed below:

* [vim - fugitive](https://github.com/tpope/vim-fugitive) a Git wrapper.
* [nerdtree](https://github.com/preservim/nerdtree) a file explorer.
* [YCM](https://github.com/ycm-core/YouCompleteMe) the code-completion engine.
* [startify](https://github.com/mhinz/vim-startify) a start screen.

It's always recommendable to use the latest stable release (VIM 8.2 at the time of writing). 

Many program developers prefer to use VIM inside a [Tmux](https://en.wikipedia.org/wiki/Tmux) session which allows efficient management of several concurrent terminals.




##  RStudio
[RStudio](https://www.rstudio.com/)

## Bash
###  Bash Scripting / Command Line is a way of interacting with your computer  operating system using text-based commands.

Bash Scripting

https://programminghistorian.org/lessons/intro-to-bash
https://linuxconfig.org/bash-scripting-tutorial

Command Line

https://www.computerhope.com/issues/chusedos.htm

## Python virtual environments and package management system
## PipEnv

Pip + VirtualEnv    https://docs.pipenv.org/

https://realpython.com/pipenv-guide/  https://github.com/pypa/pipenv

https://opensource.com/article/18/2/why-python-devs-should-use-pipenv

https://feici02.github.io/2017/09/24/pipenv-cheatsheet.html


## PipEnv from Scratch
https://github.com/daneah/pipenv-tutorial

https://github.com/daneah/pipenv-tutorial/blob/master/cheatsheet.md



### VirtualEnv

Python virtualenv Ubuntu
```
$ sudo pip install virtualenv myenv    # if error   sudo apt install python-pip
$ sudo apt-get update
$ virtualenv myenv
$ source myenv/bin/activate          # deactivate
```

http://docs.python-guide.org/en/latest/dev/virtualenvs/

https://virtualenv.pypa.io/en/stable/
https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

### PyEnv
[PyEnv](https://github.com/pyenv)


## Conda
https://conda.io/docs/ https://www.anaconda.com/download/

https://conda.io/docs/user-guide/getting-started.html
https://conda.io/docs/user-guide/tasks/manage-environments.html

```
$ conda create --name python37
$ conda activate python37
$ conda install pandas
$ deactivate
```
### Create a virtual environment with specific version
```
$ conda create --name mypython3version python=3.5
```
### Create a virtual environment with specific version and a single module
```
$ conda create --name mypython3version python=3.5 numpy
```
### Create a virtual environment with specific version with entire Anaconda distribution
```
$ conda create --name mypython3version python=3.5 anaconda
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



##  Containerization - Virtualization



## VM VirtualBox Oracle

## Vagrant

https://github.com/hashicorp/vagrant

##  Dockerconda



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
