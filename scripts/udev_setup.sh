#!/bin/sh
# script for setting up udev (to enable adb) for LineageOS flashing

# Clone this repository
git clone https://github.com/M0Rf30/android-udev-rules.git
cd android-udev-rules
# Copy rules file
  # sudo cp -v 51-android.rules /etc/udev/rules.d/51-android.rules
# OR create a sym-link to the rules file - choose this option if you'd like to update your udev rules using git.
sudo ln -sf "$PWD"/51-android.rules /etc/udev/rules.d/51-android.rules
# Change file permissions
sudo chmod a+r /etc/udev/rules.d/51-android.rules
# If adbusers group already exists remove old adbusers group
groupdel adbusers
# add the adbusers group if it's doesn't already exist
sudo mkdir -p /usr/lib/sysusers.d/ && sudo cp android-udev.conf /usr/lib/sysusers.d/
sudo systemd-sysusers # (1)
# OR on Fedora:
  # groupadd adbusers
# Add your user to the adbusers group
sudo usermod -a -G adbusers $(whoami)
# Restart UDEV
sudo udevadm control --reload-rules
sudo service udev restart
# OR on Fedora:
  #sudo systemctl restart systemd-udevd.service
# Restart the ADB server
adb kill-server
# Replug your Android device and verify that USB debugging is enabled in developer options
adb devices
# You should now see your device

