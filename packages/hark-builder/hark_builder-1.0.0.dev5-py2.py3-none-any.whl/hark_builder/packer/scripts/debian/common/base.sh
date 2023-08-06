# Add the hark user to the sudo group
usermod -G sudo -p "$(perl -e'print crypt("hark", "hark")')" -s /bin/bash -m -d /home/hark hark

# Setup sudo to allow no-password sudo for hark user
echo "hark ALL=NOPASSWD:ALL" > /etc/sudoers.d/hark
