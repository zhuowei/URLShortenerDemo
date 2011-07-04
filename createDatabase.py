#!/usr/bin/python

import sqlite3

conn = sqlite3.connect("c/data/urls.db")

c = conn.cursor();

c.execute("CREATE TABLE urls(id INTEGER PRIMARY KEY AUTOINCREMENT, url VARCHAR(1000))");

conn.commit()
conn.close()
