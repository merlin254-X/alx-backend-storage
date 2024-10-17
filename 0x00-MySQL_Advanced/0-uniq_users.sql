-- Task: Create a users table with specific requirements
-- The table has an id (auto increment and primary key), email (unique), and name

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- id: integer, never null, auto-incremented, primary key
    email VARCHAR(255) NOT NULL UNIQUE,          -- email: string, never null, unique
    name VARCHAR(255)                            -- name: string
);
