from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app import DB

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_one(cls, id):
            query = "SELECT * FROM dojos WHERE id = %(id)s"
            data = {'id':id}
            results = connectToMySQL(DB).query_db(query, data)
            return cls(results[0])





    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , location , language , comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s, %(comment)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DB).query_db( query, data )




    @staticmethod
    def validate_dojo(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if data['location'] == "empty":
            flash("Please choose a location.")
            is_valid = False
        if data['language'] == "empty":
            flash("Please select a language.")
            is_valid = False
        return is_valid
