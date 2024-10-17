-- Task: Create a users table with specific attributes and constraints
-- The table should include id, email, name, and country, with constraints on nullability and uniqueness

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,            -- id: integer, never null, auto-incremented, primary key
    email VARCHAR(255) NOT NULL UNIQUE,                    -- email: string, never null, unique
    name VARCHAR(255),                                     -- name: string
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'   -- country: enumeration with values US, CO, TN, default US
);
