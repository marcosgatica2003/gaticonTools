#!/bin/bash

sudo systemctl stop sshd
sudo systemctl stop bluetooth.service
sudo systemctl mask bluetooth.service
sudo systemctl mask sshd


poweroff

