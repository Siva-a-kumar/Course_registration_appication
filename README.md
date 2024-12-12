# Course_registration_appication


Requirements

mysql-connector-python for MySQL database connection.
pandas for data manipulation and storing the fetched data.
python-dotenv for loading environment variables from a .env file.

Create a .env

DB_HOST=your_host
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database_name

Running the Script

python fetch_data.py


Example output


  program         email course_name applying_level current_level  fee_details application_status
0      cs  sk@gmail.com       CS101       freshman      freshman       1000.0           pendinng
1      EE  ak@gmail.com       EE102      sophomore     sophomore       1200.0           approved
2    Math  mk@gmail.com     Math103         junior        junior       1500.0           rejected

