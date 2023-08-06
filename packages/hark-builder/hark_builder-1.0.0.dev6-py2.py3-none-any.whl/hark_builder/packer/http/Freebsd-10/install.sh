PARTITIONS=ada0
DISTRIBUTIONS="base.txz kernel.txz lib32.txz"

#!/bin/sh
echo 'WITHOUT_X11="YES"' >> /etc/make.conf
echo 'nameserver 8.8.8.8' >> /etc/resolv.conf
cat >> /etc/rc.conf <<EOF
ifconfig_vtnet0_name="em0"
ifconfig_vtnet1_name="em1"
ifconfig_em0="DHCP"
sshd_enable="YES"
dumpdev="AUTO"
rpcbind_enable="YES"
nfs_server_enable="YES"
mountd_flags="-r"
EOF

env ASSUME_ALWAYS_YES=1 pkg bootstrap
pkg update
pkg install -y sudo
pkg install -y bash
pkg install -y curl
pkg install -y ca_root_nss

ln -sf /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem

echo -n 'hark' | pw usermod root -h 0
pw groupadd -n hark -g 1000
echo -n 'hark' | pw useradd -n hark -u 1000 -s /usr/local/bin/bash -m -d /home/hark/ -G hark,wheel -h 0
echo 'hark ALL=(ALL) NOPASSWD:ALL' >> /usr/local/etc/sudoers

reboot
