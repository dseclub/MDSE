## Ubuntu 20.04 3


https://ubuntu.com/download/desktop

```
sudo visudo

sudo apt install curl

sudo apt-get update
sudo apt-add-repository ppa:umang/indicator-stickynotes
sudo apt update && sudo apt install -y indicator-stickynotes

sudo apt install git
git --version

git config --global user.name "x"
git config --global user.email "xx@gmail.com"

sudo snap install atom --classic 
```

## Docker

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
apt-cache policy docker-ce
sudo apt install docker-ce
```

## Docker-compose

https://docs.docker.com/compose/install/
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version


```
