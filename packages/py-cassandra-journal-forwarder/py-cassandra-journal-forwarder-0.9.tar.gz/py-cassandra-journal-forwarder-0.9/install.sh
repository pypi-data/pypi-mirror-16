#!/bin/bash
mkdir $HOME/.config/cassandra-journal-forwarder
cp settings.yaml $HOME/.config/cassandra-journal-forwarder/
sudo pip2 install pyyaml
sudo pacman -S python-systemd
sudo apt-get install python-systemd
sudo cp journal-scraper.service /etc/systemd/system/journal-scraper.service
