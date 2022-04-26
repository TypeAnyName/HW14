import sqlite3
from flask import jsonify


def bd_connect(query):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result



def get_actors(name_1="Jack Black", name_2="Dustin Hoffman"):
    query = f"""
        SELECT "cast"
        FROM netflix
        WHERE "cast" LIKE "%{name_1}%"
        AND "cast" LIKE "%{name_2}%"
        """
    response = bd_connect(query)
    actors = []
    for cast in response:
        actors.extend(cast[0].split(", "))
    result = []
    for i in actors:
        if i not in [name_1, name_2]:
            if actors.count(i) > 2:
                result.append(i)
    result = set(result)

