-- Table definitions for the catalog project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS catalog;

CREATE DATABASE catalog;
\c catalog;

CREATE TABLE users
  (
  	id INT PRIMARY KEY,
  	name VARCHAR(90) NOT NULL,
  	description VARCHAR(255),
  	profile_pic_url VARCHAR(255),
  	email VARCHAR(255),
  	phone_number VARCHAR(20)
  );

CREATE TABLE categories
  (
  	id INT PRIMARY KEY,
  	name VARCHAR(90) NOT NULL,
  	description VARCHAR(255)
  );

CREATE TABLE items
  (
  	id INT PRIMARY KEY,
  	name VARCHAR(90) NOT NULL,
  	description VARCHAR(255),
  	image_url VARCHAR(255),
  	category_id INT references categories(id) ON DELETE CASCADE,
  	owner_id INT references users(id) ON DELETE CASCADE
  );