# temp_sql.py

Is configured that you can read the temperature and humidity with the DHT11 Sensor and sends automaticly to the sql database.

1. sudo apt-get update && sudo apt-get upgrade
2. sudo apt-get install mysql-server
3. sudo apt-get -y install python3-mysql.connector
4. sudo apt-get install mysql-client php5-mysql
5. sudo apt-get install phpmyadmin
6. Create database readings
7. Create 3 column data, temperature, humidity
8. sudo python temp_sql.py 11 4
