-- This file is a configuration file for setting up a postgres database for this project

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
);

CREATE TABLE plans (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    owner_id INTEGER NOT NULL,
    num_proteins INTEGER NOT NULL,
    num_carbs INTEGER NOT NULL,
    num_fats INTEGER NOT NULL,
    CONSTRAINT fk_plans_owner
        FOREIGN KEY (owner_id)
        REFERENCES users (id)
        ON DELETE CASCADE
);

CREATE TABLE eaten (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    food_name TEXT NOT NULL,
    datetime_eaten TIMESTAMP NOT NULL,
    num_proteins INTEGER NOT NULL,
    num_carbs INTEGER NOT NULL,
    num_fats INTEGER NOT NULL,
    CONSTRAINT fk_eaten_user
        FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE CASCADE
);
