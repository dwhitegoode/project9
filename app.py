from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('planets', user='davidwhite-goode',
                        password='nasa3993', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Planets(BaseModel):
    name = CharField()
    image = CharField()
    description = CharField()
    distance = IntegerField()


db.connect()
db.create_tables([Planets])
db.drop_tables([Planets])
db.create_tables([Planets])

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

    if request.method == 'PUT':
        data = request.get_json()
        Planets.update(data).where(Planets.name == name).execute()
        return ("update complete")

    if request.method == 'POST':
        name = dict_to_model(Planets, request.get_json())
        name.save()
        return jsonify({"post complete": True})

    if request.method == 'DELETE':
        Planets.delete().where(Planets.name == name).execute()
        return ("deleted")


app.run(debug=True, port=9000)
