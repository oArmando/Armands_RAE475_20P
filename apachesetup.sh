#!/bin/bash
#script for apache 2 run
sudo apt install apacahe2
sudo ufw allow 'Apache'
sudo ufw enable
sudo mkdir -p /var/www/example.com/html
sudo chow -R $USER:$USER /var/www/example.com/html
sudo chmod -R 755 /var/www/example.com
nano /var/www/example.com/html/index.html
