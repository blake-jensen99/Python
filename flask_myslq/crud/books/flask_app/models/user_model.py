from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DB





class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users





    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name, last_name, created_at, updated_at ) VALUES ( %(fname)s, %(lname)s, NOW() , NOW() );"
        return connectToMySQL(DB).query_db( query, data )
    


    @classmethod
    def get_users_with_books( cls , id ):
        from flask_app.models.book_model import Book
        data = {'id': id}
        query = "SELECT * FROM users LEFT JOIN favorites ON favorites.user_id = users.id LEFT JOIN books ON favorites.book_id = books.id WHERE users.id = %(id)s;"
        results = connectToMySQL(DB).query_db( query , data )
        books = []
        user = cls(results[0])
        if results:
                
            for row_from_db in results:
                    
                books_data = {
                    "id":row_from_db["books.id"],
                    "title":row_from_db["title"],
                    "num_of_pages":row_from_db["num_of_pages"],
                    "created_at" : row_from_db["books.created_at"],
                    "updated_at" : row_from_db["books.updated_at"]
                }

                book = Book(books_data)
                books.append(book)
                
        user.books = books
        return user
    

    @classmethod
    def add_book(cls, data ):
        print(data)
        query = "INSERT INTO favorites ( user_id, book_id) VALUES ( %(user_id)s, %(book_id)s);"
        return connectToMySQL(DB).query_db( query, data )