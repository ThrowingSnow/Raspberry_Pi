# temp_sql.py

It's configured that you can read the temperature and humidity with the DHT11 Sensor and sends automaticly to the sql database.

1. sudo apt-get update && sudo apt-get upgrade
2. sudo apt-get install mysql-server
3. sudo apt-get -y install python3-mysql.connector
4. sudo apt-get install mysql-client php5-mysql
5. sudo apt-get install phpmyadmin
6. Create database readings
7. Create 3 column Data, Temperature, Humidity
8. sudo git clone https://github.com/ThrowingSnow/Raspberry_Pi.git
9. change on line 11 the information to the SQL login
9. sudo python temp_sql.py 11 4

to be continued...


# camera_timestamp.py

Whene you take a photo it makes a timestamp ind the filename

