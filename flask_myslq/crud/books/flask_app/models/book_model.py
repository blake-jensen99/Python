from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DB




class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DB).query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books



    @classmethod
    def save(cls, data ):
        query = "INSERT INTO books ( title, num_of_pages, created_at, updated_at ) VALUES ( %(title)s, %(pages)s, NOW() , NOW() );"
        return connectToMySQL(DB).query_db( query, data )
    

    @classmethod
    def get_books_with_users( cls , id ):
        from flask_app.models.user_model import User
        data = {'id': id}
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN users ON favorites.user_id = users.id WHERE books.id = %(id)s;"
        results = connectToMySQL(DB).query_db( query , data )
        users = []
        book = cls(results[0])
        if results:
                
            for row_from_db in results:
                    
                users_data = {
                    "id":row_from_db["users.id"],
                    "first_name":row_from_db["first_name"],
                    "last_name":row_from_db["last_name"],
                    "created_at" : row_from_db["users.created_at"],
                    "updated_at" : row_from_db["users.updated_at"]
                }

                user = User(users_data)
                users.append(user)   
        book.users = users
        
        return book
    

    @classmethod
    def add_user(cls, data ):
        print(data)
        query = "INSERT INTO favorites ( user_id, book_id) VALUES ( %(user_id)s, %(book_id)s);"
        return connectToMySQL(DB).query_db( query, data )