from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Pokemon</h1>'

@app.route('/search')
def search():
    pokemon_name = request.args.get('pokemon')
    if pokemon_name:
        return redirect(url_for('search_pokemon', id_or_name_of_pokemon=pokemon_name))
    else:
        return "Please enter a Pokémon name or ID."

@app.route('/search/<id_or_name_of_pokemon>')
def search_pokemon(id_or_name_of_pokemon):
    api_url = f"https://api.pokemon.project.projectrexa.dedyn.io/pokeapi/{id_or_name_of_pokemon}?authorization=622BEB8354BCDC1C94E1B5B414C66"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return render_template('pokemon.html', pokemon=pokemon_data)
    else:
        return f"Error: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
