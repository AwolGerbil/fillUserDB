#!/usr/bin/python

import os
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

c.execute("CREATE TABLE users(username TEXT PRIMARY KEY, password TEXT, email TEXT, full_name TEXT, date_of_birth TEXT, gender INTEGER, height REAL, weight REAL, hobbies TEXT, pref_gender TEXT, pref_min_age INTEGER, pref_max_age INTEGER, hair_colour TEXT, pref_min_height INTEGER, pref_max_height INTEGER, pref_min_weight INTEGER, pref_max_weight INTEGER);")

c.execute("CREATE TABLE hair_colours(colour TEXT PRIMARY KEY);")

c.execute("CREATE TABLE users_pref_colours(id INTEGER PRIMARY KEY, username TEXT, colour TEXT, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(colour) REFERENCES hair_colours(colour));")

c.execute("CREATE TABLE courses(course_code TEXT PRIMARY KEY, handbook_url TEXT);")

c.execute("CREATE TABLE users_courses(id INTEGER PRIMARY KEY, username TEXT, course_code TEXT, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(course_code) REFERENCES courses(course_code));")

c.execute("CREATE TABLE bands(id INTEGER PRIMARY KEY, band_name TEXT, itunes_url TEXT);")

c.execute("CREATE TABLE users_bands(id INTEGER PRIMARY KEY, username TEXT, band_id INTEGER, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(band_id) REFERENCES bands(id));")

c.execute("CREATE TABLE shows(id INTEGER PRIMARY KEY, show_name TEXT, show_type INTEGER, general_url TEXT);")

c.execute("CREATE TABLE users_shows(id INTEGER PRIMARY KEY, username TEXT, show_id INTEGER, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(show_id) REFERENCES shows(id));")

c.execute("CREATE TABLE books(id INTEGER PRIMARY_KEY, book_name TEXT, google_books_url TEXT);")

c.execute("CREATE TABLE users_books(id INTEGER PRIMARY KEY, username TEXT, book_id INTEGER, FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(book_id) REFERENCES books(id));")

for root, dirs, files in os.walk('users'):
	if root != 'users':
		print root
		preferences = open(root + '/preferences.txt', 'r')
		mode = ""
		submode = ""
		hairColours = []
		gender = ""
		minAge = 0
		maxAge = 0
		minWeight = 0
		maxWeight = 0
		minHeight = 0
		maxHeight = 0
		for line in preferences:
			if line in ["hair_colours:\n", "gender:\n", "age:\n", "weight:\n", "height:\n"]:
				mode = line
			elif line in ["\tmin:\n", "\tmax:\n"]:
				submode = line.strip()
			elif mode == "hair_colours:\n":
				hairColours.append(line.strip())
			elif mode == "gender:\n":
				gender = line.strip()
			elif mode == "age:\n":
				if submode == "min:":
					minAge = int(line.strip())
				if submode == "max:":
					maxAge = int(line.strip())
			elif mode == "weight:\n":
				if submode == "min:":
					minWeight = int(line.strip()[:-2])
				if submode == "max:":
					maxWeight = int(line.strip()[:-2])
			elif mode == "height:\n":
				if submode == "min:":
					minHeight = float(line.strip()[:-1])
				if submode == "max:":
					maxHeight = float(line.strip()[:-1])
			else:
				print line
		
		print hairColours, gender, minAge, maxAge
		preferences.close()
		
		profile = open(root + '/profile.txt', 'r')
		print profile
		profile.close()

users.close()
