# Macro Tracker

**Macro Tracker** is a web application for tracking daily macronutrient intake. It allows users to log consumed foods and monitor their intake of proteins, carbohydrates, and fats in an organized and simple way.

The frontend is built with **Vue.js**, while the backend API is powered by **FastAPI**.

---

## Features

- Track daily intake of macronutrients
- Log foods with protein, carb, and fat values
- Responsive interface
- RESTful API backend

---

## Tech Stack

### Frontend
- Vue.js
- TypeScript

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL / SQLite (depending on configuration)

---

## Deployments

There's a production deployment at [this URL](https://macros.filipgrujic.rs/), which you can use freely. However, you can always deploy any of the branches yourself with docker. Just docker compose any one of the two configurations you want.

### ENV Variables

For configuration, there are some ENV vars you should configure:
- `DATABASE_URL` is the connection string to a remote postgres database. If left empty, it will default to creating a local sqlite file, at `/api/db/database.sqlite`
- `FRONTEND_URL` is the host of the frontend, used for CORS. If left empty, it defaults to `*`
- `SECRET_KEY` is used for JWT token generation, defaults to `SECRET`
- `VITE_API_URL` is the backend host, defaults to development default - `http://localhost:5000`

### Nginx configuration

For a production environment, a default Nginx configuration for serving the frontend is provided in `client/nginx.conf`. If you are running production, you should change it based on your own server architecture.

---

## Database setup

To set up a database for this project, you can use the postgres creation config provided in `/api/db/postgres_creation.sql`
