-- schema.sql
-- Drop tables if already exists
DROP TABLE IF EXISTS seller CASCADE;
DROP TABLE IF EXISTS product CASCADE;

-- Create tables
-- Create table seller
CREATE TABLE seller (
    id SERIAL,
    name VARCHAR (64) NOT NULL UNIQUE,
    password_hash VARCHAR(64),
    PRIMARY KEY (id)
);

-- Create table product
CREATE TABLE product (
    id SERIAL,
    name VARCHAR (64) NOT NULL,
    seller VARCHAR (64) NOT NULL,
    image VARCHAR (128) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (seller) REFERENCES seller (name) ON DELETE CASCADE
);
