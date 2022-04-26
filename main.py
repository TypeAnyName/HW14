from flask import Flask, jsonify
import utils


def main():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False
    app.config['DEBUG'] = True

    @app.route("/movie/<title>")
    def title_search(title):
        query = f"""
                SELECT title, country, release_year, listed_in as genre, description
                FROM netflix
                WHERE title = "{title}"
                ORDER BY release_year DESC
                LIMIT 1
        """
        response = utils.bd_connect(query)[0]
        response_json = {
            "title": response[0],
            "country": response[1],
            "release_year": response[2],
            "genre": response[3],
            "description": response[4].strip(),
        }
        return jsonify(response_json)

    @app.route("/movie/<int:start>/to/<int:end>")
    def release_year_search(start, end):
        query = f"""
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {start} AND {end}
                    ORDER BY release_year
                    LIMIT 100
            """
        response = utils.bd_connect(query)
        response_json = []
        for film in response:
            response_json.append({
                "title": film[0],
                "release_year": film[1],
            })
        return jsonify(response_json)

    app.run(debug=True)


if __name__ == "__main__":
    main()
