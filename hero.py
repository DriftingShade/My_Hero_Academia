from mysqlconnection import connectToMySQL


class Hero:
    DB = "hero_db"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.quirk = data["quirk"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = """INSERT INTO heroes (first_name, last_name, quirk, age, created_at, 
        updated_at) VALUES (%(first_name)s, %(last_name)s, %(quirk)s, %(age)s, NOW(), NOW());"""

        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM heroes;"
        print(query)
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        heroes = []
        for hero in results:
            heroes.append(cls(hero))
        return heroes
