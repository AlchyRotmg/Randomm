-- Create the SQLite database
CREATE DATABASE IF NOT EXISTS goals;
DROP DATABASE IF EXISTS goals;

-- Connect to the database
USE goals;

-- Define the table 'goals' with the specified schema
CREATE TABLE IF NOT EXISTS goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    description TEXT,
    start_date DATE,
    end_date DATE,
    priority INT,
    achieved BOOLEAN
);
 -- Select all goals and display them
SELECT * FROM goals;