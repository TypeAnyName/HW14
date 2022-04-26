import sqlite3


def bd_connect(query):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def get_actors(name_1, name_2):
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
    return result


def get_films(type_film, release_year, genre):
    query = f"""
                SELECT title, description, "type"
                FROM netflix
                WHERE "type" = "{type_film}"
                AND release_year = "{release_year}"
                AND listed_in LIKE '%{genre}%'
    """
    response = bd_connect(query)
    response_json = []
    for film in response:
        response_json.append({
            "title": film[0],
            "description": film[1],
            "type": film[2],
        })
    return response_json


print(get_actors("Jack Black", "Dustin Hoffman"))
print(get_films("Movie", 2016, "Dramas"))
