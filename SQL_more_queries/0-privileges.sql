-- Create users if they do not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Grant SELECT and INSERT privileges to user_0d_2 on user_2_db
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Ensure the privileges are applied
FLUSH PRIVILEGES;

-- List the privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List the privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
