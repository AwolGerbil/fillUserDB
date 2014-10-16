#!/usr/bin/python

import sqlite3

users = sqlite3.connect('users.db')
c = users.cursor()

# Add table
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print "current tables:", c.fetchall()

# Empty database
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
for table in c.fetchall():
	print "deleting", table[0]
	c.execute("DROP TABLE %s;" % table[0])

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print "new tables:", c.fetchall()

c.execute("CREATE TABLE users(username TEXT PRIMARY KEY, password TEXT, email TEXT, full_name TEXT, date_of_birth TEXT, gender INTEGER, height REAL, weight REAL, hobbies TEXT);")

c.execute("CREATE TABLE courses(course_code TEXT PRIMARY KEY, handbook_url TEXT);")

c.execute("CREATE TABLE users_courses(id INTEGER PRIMARY KEY, username TEXT, course_code TEXT, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(course_code) REFERENCES courses(course_code));")

c.execute("CREATE TABLE bands(id INTEGER PRIMARY KEY, band_name TEXT, itunes_url TEXT);")

c.execute("CREATE TABLE users_bands(id INTEGER PRIMARY KEY, username TEXT, band_id INTEGER, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(band_id) REFERENCES bands(id));")

c.execute("CREATE TABLE shows(id INTEGER PRIMARY KEY, show_name TEXT, show_type INTEGER, general_url TEXT);")

c.execute("CREATE TABLE users_shows(id INTEGER PRIMARY KEY, username TEXT, show_id INTEGER, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(show_id) REFERENCES shows(id));")

c.execute("CREATE TABLE books(id INTEGER PRIMARY_KEY, book_name TEXT, google_books_url TEXT);")

c.execute("CREATE TABLE users_books(id INTEGER PRIMARY KEY, username TEXT, book_id INTEGER, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(book_id) REFERENCES books(id));")

users.close()
