## Python and Flask Project

Creating an Planetary API using Python, Flask, and PostgreSQL.

### Description

Users will be able to retrieve information about our solar stystem. 

### The Code
```
Planets(name='Mercury', image='http://space-facts.com/wp-content/uploads/mercury-transparent.png',
        distance='77000000', description='Mercury is the closest planet to the Sun and due to its proximity it is not easily seen except during twilight.').save()
Planets(name='Mars', image='http://space-facts.com/wp-content/uploads/mars-transparent.png',
        distance='54600000', description='Mars is the fourth planet from the Sun and is the second smallest planet in the solar system.').save()


app = Flask(__name__)


@app.route('/Planets', methods=['GET', 'POST'])
@app.route('/Planets/<name>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(name=None):
    if request.method == 'GET':
        if name:
            return jsonify(model_to_dict(Planets.get(Planets.name == name)))
        else:
            planetList = []
            for name in Planets.select():
                planetList.append(model_to_dict(name))
            return jsonify(planetList)

```

### API End Points 

| Method   |      Endpoint      |  Description |
|----------|:------------------:|-----------------:|
| GET |    /api/planets   |   gets all planets |
| GET | /api/planets/{name of planet} |    gets a single planet |
| POST |    /api/planets   |   posts a planet |
| PUT | /api/planets/:planet |    updates a planet |
| DEL |    /api/planets/:planet   |   deletes a planet |


### Built With 

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [PostgreSQL](https://www.postgresql.org/)

