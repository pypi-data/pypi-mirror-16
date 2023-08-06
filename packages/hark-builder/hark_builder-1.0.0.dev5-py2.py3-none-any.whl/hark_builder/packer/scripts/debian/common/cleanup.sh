UNINSTALL="apt-get -y --purge --auto-remove remove"

apt-get clean -y
apt-get autoclean -y

# Clean up orphaned packages
apt-get -y install deborphan
while [ -n "$(deborphan --guess-all --libdevel)" ]; do
    deborphan --guess-all --libdevel | xargs apt-get -y purge
done
$UNINSTALL deborphan dialog

rm -rf /usr/src/vboxguest*
rm -rf /usr/src/linux-headers*

unset HISTFILE
rm -f /root/.bash_history

for loc in af am an ang ar as ast az az_IR bal be be_BG be@latin bg bg_BG bn bn_IN br bs byn ca ca@valencia cr crh cs cs_CZ csb cy da de de@hebrew de.us-ascii de_AT de_CH de_DE dz el en@arabic en@boldquot en@cyrillic en_AU en_CA en_GB en@greek en@hebrew en_NZ en@piglatin en@shaw en@quot eo es es_ES es.us-ascii et et_EE eu fa fa_IR fi fo fr fur ga gez gl gu haw he hi hr hu hu_HU hy ia id id_ID io is it ja ka kk km kn ko kok ks ku ky li lg lt lv mai mg mi mk ml mn mr ms mt my nb nds ne nl nl_NL nn no no.us-ascii nso oc or pa pl ps pt pt_BR pt_BR.us-ascii pt.us-ascii qu ro ru rw si sk sl so sq sr sr@ije sr@Latn sr*latin sv sw ta te th ti tg tig tk tl tr tt tt@iqtelif ug uk ur urd uz@cyrillic ve vi wa wal wo xh yi zh zh_HK zh_CN zh_TW zu; do
	rm -rf /usr/share/locale/$loc
done

find /var/log -type f | while read f; do echo -ne '' > $f; done;


# clean up udev rules and dhcp
rm -rf /dev/.udev/
rm /lib/udev/rules.d/7*-persistent-net*
rm /etc/udev/rules.d/7*-persistent-net*

# Remove Bash history
unset HISTFILE
rm -f /root/.bash_history
rm -f /home/hark/.bash_history
