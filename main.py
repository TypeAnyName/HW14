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
            "description": response[4],
        }
        return jsonify(response_json)

    app.run(debug=True)


if __name__ == "__main__":
    main()
