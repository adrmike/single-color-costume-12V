# single-color-costume-12V
Code and Pi OS configuration files for my single color LED 12V strip based costumes


### Basic PI setup that isn't currently scripted
#### Git setup
```
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python-pip flask pigpio rng-tools
git config --global user.name "Admiral Funtimes"
git config --global user.email noman800@gmail.com
git config --global init.defaultBranch main
git config --global core.editor vim
```


### refernces 

[networkd setup](https://raspberrypi.stackexchange.com/questions/108592/use-systemd-networkd-for-general-networking/108593#108593)
[access point setup](https://raspberrypi.stackexchange.com/questions/88214/setting-up-a-raspberry-pi-as-an-access-point-the-easy-way/88234#88234)