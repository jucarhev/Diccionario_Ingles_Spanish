#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


class Database_Manager():
	connection = None
	cursor = None
	def __init__(self):
		pass

	def start_connection(self):
		self.connection = sqlite3.connect('src/dict.db')
		self.cursor = self.connection.cursor()

	def close_connection(self):
		self.cursor.close()
		self.connection.close()

	def select(self):
		self.start_connection()
		self.cursor.execute('SELECT * FROM dict')
		for row in self.cursor:
			print(row)
		self.close_connection()

	def num_rows(self,sql):
		n = 0
		self.start_connection()
		self.cursor.execute(sql)
		for row in self.cursor:
			n = n + 1
		self.close_connection()
		return n

	def query(self,sql):
		array = []
		self.start_connection()
		self.cursor.execute(sql)
		for row in self.cursor:
			array.append(row[0] + ':' + row[1])
		self.close_connection()
		return array