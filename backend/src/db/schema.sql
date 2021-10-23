-- schema.sql
-- Drop tables if already exists
DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS seller CASCADE;

-- Create tables
-- Create table product
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name CHAR (64) NOT NULL,
    description VARCHAR NOT NULL,
    original_price FLOAT NOT NULL,
    price FLOAT NOT NULL,
    condition CHAR (64) NOT NULL,
    seller CHAR (64) NOT NULL REFERENCES seller (name)
);

-- Create table seller
CREATE TABLE seller (
    name CHAR (64) PRIMARY KEY,
    description VARCHAR,
    location VARCHAR NOT NULL
);

-- Create table image
CREATE TABLE image (
);
