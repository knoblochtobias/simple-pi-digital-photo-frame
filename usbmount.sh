#/bin/bash

MountTo=/mnt/usbstick

ACTION=$1
DEVICE=$2

if [ "$ACTION" = "mount" ]; then
    echo `date +'%Y-%m-%d %H:%M:%S: usb mount'` >> /home/pi/simple-pi-digital-photo-frame/info.log
    [ ! -d $MountTo ] && mkdir -p $MountTo
    /bin/mount $DEVICE $MountTo
    /bin/su -l pi -c "DISPLAY=:0 /usr/bin/feh -FYr -D 5 $MountTo &"
elif [ "$ACTION" = "umount" ]; then
    echo `date +'%Y-%m-%d %H:%M:%S: usb umount'` >> /home/pi/simple-pi-digital-photo-frame/info.log
    /usr/bin/killall feh
    /usb/bin/killall checkstart.sh
    /bin/umount -f $DEVUCE
fi

exit 0

