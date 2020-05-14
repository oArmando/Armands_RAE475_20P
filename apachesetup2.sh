#!/bin/bash
sudo nano /etc/apache2/sites-available/sampledomain.com.conf
a2ensite sampledomain.com.conf
sudo a2dissite 000-default.conf
sudo systemctl restart apache2
sudo apache2ctl configtest
