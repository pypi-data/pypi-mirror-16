cat >> /etc/ssh/sshd_config <<EOF
UseDNS no
PasswordAuthentication no
AuthorizedKeysFile %h/.ssh/authorized_keys /etc/ssh/authorized_keys/%u
EOF

mkdir /etc/ssh/authorized_keys

# Put in the public key for hark
cat >> /etc/ssh/authorized_keys/hark <<EOF
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDJOFJG7/QOkz91/FPBsHmiO2rY9CKO3z1M42s1KCRDo/h7ICyQwT2+rDtIjZT7v77h41H//JncjVWelDOtTDkbgkhLvGQwablL6i6YcBN5vjYEM7Jih9D/HPjOWoPynX/VMm74o533uRKHlOtB9HEad9xGPxgRX2whUIL5nM/J5ESJKlRb6e5iocr+WjOdm4JAxH4UnXiJGYw29Wg+abJJogkaxEX/KRbmxwixM9PRI3Yy0X8muk0snf9qKnroFoVCphOdrhQHKZ3Jb0srRjhGD+luDSUmrQkhK16jcsRmcpZQaHvQ6aPjPs0U/+u7Imw8TNUhfdqs5p1V0S59CoLn
EOF
