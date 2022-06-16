#!/usr/bin/env python

### Install mysql
#pip install mysql-connector-python
import mysql.connector as mariadb

#####    DEFINES    #####

#########    Connection to the database server    ##########

#####    Set here the login to your database server
LOGIN = ''

#####    Set here the password that corresponds to your login to the database
PASSWORD = ''

#####    Set here the host that corresponds to your database server address
ADDRESS = 'localhost'

#####    Set here the port to connect to yout database server
PORT = '3306'

#########    Manipulate your databases    ##########

#####    Define here the name of your database in which you will work
DATABASE_NAME = 'Testing'


## create mysql connection and define cursor
class dbServer:
    def __init__(self, dbLogin, dbPass, dbHost, dbPort):
        self.mariadb_connection = mariadb.connect(user=dbLogin, password=dbPass, host = dbHost, port=dbPort)
        
        self.create_cursor = self.mariadb_connection.cursor() # dictionary = True
        print('Conection with database exit with sucess!')


    #####   CREATE DATABASE   #####
    def createDB(self, dbName):
        self.create_cursor.execute('CREATE DATABASE {};'.format(dbName))
        print('Database {} created successfully!'.format(dbName))
    
    #####    LIST DATABASES    #####
    def listDB(self):
        print('\n### List Databases ###\n')
        self.create_cursor.execute('SHOW DATABASES;')
        for x in self.create_cursor:
            print(x)

    #####    DELETE DATABASE    #####
    def deleteDB(self, dbName):
        self.create_cursor.execute('DROP DATABASE {};'.format(dbName))
        print('Database {} deleted successfully'.format(dbName))


    #####    MANIPULATE TABLES    ##### ( IN WORK )
    #def createTable(self):
    #    self.create_cursor.execute()

#####    Connection    #####
dbserver = dbServer(LOGIN, PASSWORD, ADDRESS, PORT)

#####    Operations    #####

# Remove the '#' to list all databases
dbserver.listDB()

# Remove the '#' to create database with name defined at beginning of file
#dbserver.createDB(DATABASE_NAME)

# Remove the '#' to delete database with name defined at beginning of file
#dbserver.deleteDB(DATABASE_NAME)

