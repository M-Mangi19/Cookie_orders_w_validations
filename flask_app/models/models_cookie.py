from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

db = "Cookie_order_w_validations_schema"

class Cookie:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies;"
        results = connectToMySQL(db).query_db(query)
        cookies = []
        for cookie in results:
            cookies.append(cls(cookie))
        return cookies

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cookies WHERE id = %(id)s"
        # data = {'id':user_id}
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])


    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO cookies ( name , cookie_type , number_of_boxes)
                VALUE ( %(name)s, %(cookie_type)s, %(number_of_boxes)s);
                """
        results = connectToMySQL(db).query_db(query,data)
        return results

    @classmethod
    def update(cls, form_data, cookie_id):
        query = f"UPDATE cookies SET name = %(name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s WHERE id = {cookie_id}"
        results = connectToMySQL(db).query_db(query, form_data)
        return results

    @staticmethod
    def order_validator(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['name']) < 2:
            flash("Name must be at least 2 characters!")
            is_valid = False
        if len(data['cookie_type']) < 2:
            flash("Cookie must be at least 2 characters!")
            is_valid = False
        if int(data['number_of_boxes']) <= 0:
            flash("You must have at least 1 box in your order!")
            is_valid = False
        return is_valid

    @staticmethod
    def edit_validator(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['name']) < 2:
            flash("Name must be at least 2 characters!")
            is_valid = False
        if len(data['cookie_type']) < 2:
            flash("Cookie must be at least 2 characters!")
            is_valid = False
        if int(data['number_of_boxes']) <= 0:
            flash("You must have at least 1 box in your order!")
            is_valid = False
        return is_valid