# Installation for Raspberry Pi 3 Modul B

## OS Image
- Installed via Raspberry Pi Imager, selected OS: Raspberry PI OS (32-bit), a port of debian bullseye
- Created user: hsm (password see keepass)

## SSH Access
> **_NOTE:_**  https://www.heise.de/tipps-tricks/Raspberry-Pi-SSH-einrichten-so-geht-s-4190645.html

Execute

    sudo apt-get install ssh

    sudo update-rc.d ssh defaults

Via Desktop: Einstellungen -> Raspberry-Pi-Konfiguration -> Interfaces -> SSH (enable it)

Via Desktop: Einstellungen -> Raspberry-Pi-Konfiguration -> System -> change hostname (name it 'pihsm')

## GIT
From Windows PC, Powershell:

    scp C:\Users\Rainer\.ssh\id_ed25519.pub hsm@pihsm:~/.ssh/.
    scp C:\Users\Rainer\.ssh\id_ed25519 hsm@pihsm:~/.ssh/.

Continue on pi

    sudo apt update 
    sudo apt install git
    chmod 600 ~/.ssh/id_ed25519*

    git config --global user.email raifal@users.noreply.github.com
    git config --global user.name "Rainer Faller"

    git clone git@github.com:raifal/my-home2.git

## Circuit:
> **_NOTE:_** https://raspberryautomation.com/connect-multiple-ds18b20-temperature-sensors-to-a-raspberry-pi/

## Secrets
Write this content (values, see keepass) to: `/home/hsm/hsm-config.xml`

    {
      "temperature-url": "..."
      "x-api-key": "...",
      "client": "..."
    }

## GPIO

    sudo apt update
    sudo apt-get install python-rpi.gpio python3-rpi.gpio

    sudo vi /boot/config.txt
    
    # and add to bottom line:
    dtoverlay=w1-gpio,gpiopin=4
    dtoverlay=w1-gpio,gpiopin=17

    sudo reboot

Test that it is working:

    ls -l /sys/bus/w1/devices/w1_bus_master1/
    # show temperature
    cat 28-000005a421f3/w1_slave
    
## Crontab 
    crontab -e
    
    # add:
    */15 * * * * python  /home/hsm/my-home2/pi/wqtemperature.py
	
## rest api server and database
sudo -H pip install flask
sudo -H pip install mysql
sudo -H pip install mysql-connector

sudo apt install mariadb-server
sudo mysql -u root 
CREATE DATABASE hsm;
CREATE USER 'hsm'@'localhost' IDENTIFIED BY 'hsm';
GRANT ALL PRIVILEGES ON hsm.* TO 'hsm'@'localhost';
RENAME USER "hsm"@"localhost" TO "hsm"@"%";
FLUSH PRIVILEGES;

sudo mysql -u hsm -p
connect hsm;
-- Active: 1671294883822@@192.168.0.241@3306@hsm
CREATE TABLE hsm_temperature (  
    create_time DATETIME not null PRIMARY KEY COMMENT 'Create Time',
    json VARCHAR(500) ) COMMENT '';
	
add to /etc/mysql/mysql.cnf
{code}
[mysqld]
bind-address = 0.0.0.0
{code}

sudo systemctl restart mysql

sudo nano /etc/rc.local
{code}    (vor exit 0)
sudo bash -c 'python /home/hsm/my-home2/pi/rest-api-server.py > /home/hsm/logs/rest-api-server.log 2>&1' &
{code}









# Userful snippets

sudo ps -ax | grep python
