-- Set's up a MySQL server for Quizztopia

DROP DATABASE IF EXISTS quizztopia_dev_db;
CREATE DATABASE IF NOT EXISTS quizztopia_dev_db;
CREATE USER IF NOT EXISTS 'quizztopia_dev'@'localhost' IDENTIFIED BY 'Quiz_dev_pwd_01';
GRANT ALL PRIVILEGES ON `quizztopia_dev_db`.* TO 'quizztopia_dev'@'localhost';
GRANT SELECT ON `perfomance_schema`.* TO 'quizztopia_dev'@'localhost';
FLUSH PRIVILEGES;

