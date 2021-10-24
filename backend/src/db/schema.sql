-- schema.sql
-- Drop tables if already exists
DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS seller CASCADE;

-- Create tables
-- Create table product
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name CHAR (64) NOT NULL,
    condition CHAR (64) NOT NULL DEFAULT "good",
    seller CHAR (64) NOT NULL REFERENCES seller (name),
    image VARCHAR NOT NULL
);

-- Create table seller
CREATE TABLE seller (
    id INTEGER PRIMARY KEY,
    name CHAR (64) NOT NULL UNIQUE,
    description VARCHAR
);
