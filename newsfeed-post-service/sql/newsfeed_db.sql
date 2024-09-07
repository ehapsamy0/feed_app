CREATE DATABASE IF NOT EXISTS user_service_db;

USE user_service_db;

-- Creating role table to store different user roles
CREATE TABLE IF NOT EXISTS roles (
    id CHAR(36) NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Creating user table for managing users
CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) NOT NULL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role_id CHAR(36) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT user_role_fk FOREIGN KEY (role_id) REFERENCES roles(id)
);

ALTER TABLE
    users
ADD
    UNIQUE (username);

ALTER TABLE
    users
ADD
    UNIQUE (email);

-- ------------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS post_service_db;

USE post_service_db;

CREATE TABLE IF NOT EXISTS posts (
    id CHAR(36) NOT NULL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    user_id CHAR(36),
    -- Nullable as per request
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE
);

-- Creating comment table for storing comments on posts
-- Note: Likes can be implemented for comments if needed in future, but keep it simple for now
CREATE TABLE IF NOT EXISTS comments (
    id CHAR(36) NOT NULL PRIMARY KEY,
    user_id CHAR(36),
    -- Nullable as per request
    post_id CHAR(36) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    CONSTRAINT comment_post_fk FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS likes (
    id CHAR(36) NOT NULL PRIMARY KEY,
    user_id CHAR(36),
    -- Nullable as per request
    post_id CHAR(36) NOT NULL,
    CONSTRAINT like_post_fk FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

-- ------------------------------------------------------------------
= CREATE DATABASE IF NOT EXISTS fellowship_service_db;

USE fellowship_service_db;

-- Creating followers table to store follow relationships between users
CREATE TABLE IF NOT EXISTS followers (
    id CHAR(36) NOT NULL PRIMARY KEY,
    follower_id CHAR(36) NOT NULL,
    -- User who follows
    following_id CHAR(36) NOT NULL,
    -- User being followed
    accepted BOOLEAN NOT NULL DEFAULT FALSE,
    -- Indicating if the follow request is accepted (in case of private accounts)
    created_at DATETIME NOT NULL
);

