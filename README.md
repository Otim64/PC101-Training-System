Why this structure?

templates/
Contains HTML pages.

static/
Contains files that never change.

routes/
Contains Flask routes.

models/
Talks to the database.
Instead of putting SQL inside app.py,
it stays here.

database/
Everything related to SQLite.
Creating tables.
Connecting.
Initializing.

utils/
Functions used everywhere.

1. users

For login system

id
username
email
password_hash
role (admin / trainer)
2. students

For managing learners

id
full_name
phone
email
course
date_registered
3. payments

For tracking money

id
student_id (FK)
amount
date_paid
description
4. attendance

For tracking class presence

id
student_id (FK)
date
status (Present / Absent)

WHAT THIS SYSTEM IS DOING
Registration flow
User fills form
→ Flask receives data
→ password hashed
→ stored in DB
→ redirected to login
Login flow
User enters credentials
→ Flask fetches user from DB
→ password compared
→ session created
→ redirected to dashboard
Logout flow
Session cleared
→ user logged out