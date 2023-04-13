from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja_model
from flask_app.models.ninja_model import Ninja

from flask_app import DB

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def get_one(cls, id):
            query = "SELECT * FROM dojos WHERE id = %(id)s"
            data = {'id':id}
            results = connectToMySQL(DB).query_db(query, data)
            return cls(results[0])



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL(DB).query_db( query, data )
    


    @classmethod
    def get_dojos_with_ninjas( cls , id ):
        data = {'id': id}
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DB).query_db( query , data )
        ninjas = []
        dojo = cls(results[0])
        if results:
            
            for row_from_db in results:
                
                ninjas_data = {
                    "id" : row_from_db["ninjas.id"],
                    "first_name" : row_from_db["first_name"],
                    "last_name" : row_from_db["last_name"],
                    "age" : row_from_db["age"],
                    "created_at" : row_from_db["ninjas.created_at"],
                    "updated_at" : row_from_db["ninjas.updated_at"]
                }

                ninja = Ninja(ninjas_data)
                ninjas.append(ninja)
            
        dojo.ninjas = ninjas
        return dojo