# Joyland Schools Portal

A modern Flask-based web application for school management.

## Features
- User registration and login (with PostgreSQL)
- Responsive, modern UI with glassmorphism and animated accents
- Flash messages and error handling
- Admin-ready for future features

## Setup (Local)
1. Clone the repo and `cd` into the project directory.
2. Install Python 3.10+ and PostgreSQL.
3. Create a virtual environment and activate it:
	```bash
	python -m venv venv
	source venv/bin/activate  # or venv\Scripts\activate on Windows
	```
4. Install dependencies:
	```bash
	pip install -r backend/requirements.txt
	```
5. Set environment variables (create a `.env` file or set in shell):
	```env
	SECRET_KEY=your-secret-key
	DATABASE_URL=your-postgres-url
	```
6. Run the app:
	```bash
	cd backend
	flask run
	```

## Deployment (Render)
1. Provision a PostgreSQL database on Render and copy the connection string.
2. Set `DATABASE_URL` and `SECRET_KEY` as environment variables in your Render service.
3. Deploy via GitHub integration. Render will run using the `Procfile`.

## Backup & Restore
- Use your managed PostgreSQL provider's dashboard for backups.
- You can also export data with `pg_dump` and import with `psql`.

## Security
- Uses environment variables for secrets.
- CSRF protection enabled via Flask-WTF.

## License
MIT
