# simple-pi-digital-photo-frame
Use a Raspberry Pi as a simple digital photo frame. Automatically starts to show pictures from a plugged in USB stick.

# Install

1. Install deps
    
    ```
    sudo apt install feh python
    ```

2. clone repo
    
    ```
    git clone https://github.com/knoblochtobias/simple-pi-digital-photo-frame
    ```

3. Adjust path if path is not ```/home/pi/simple-pi-digital-photo-frame``` in following file:
    
    ```
    90-usbautomount.rules
    ```

4. copy udev rules:
    
    ```
    sudo cp 90-usbautomount.rules /etc/udev/rules.d/
    ```
    
5. Disable Screensaver

    ```
    sudo apt install xscreensaver
    ```
    
    Go to Main Menu -> Preferences -> Screensaver -> Mode -> "Disable screensaver"

6. *Optional* Add a shutdown button. Add the following line to autostart ```/etc/rc.local``` (
    
    ```
    /usr/bin/python /home/pi/simple-pi-digital-photo-frame/shutdown.py &
    ```

7. *Optional* Install Ramdisc to protect SD-Card

    Read http://www.tuxlog.de/raspberrypi/2014/die-sd-karte-beim-raspberry-pi-schonen/ for further details
    
