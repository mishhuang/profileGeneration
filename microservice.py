import flask
import random

app = flask.Flask(__name__)

class CatProfile():
    """The CatProfile object will fetch some
    randomlized cat data in order to build a virtual
    cat profile.
    """
    name = ''
    age = ''
    coloring = ''
    personality = ''
    coat = ''
    toy = ''
    like = ''
    dislike = ''

    def __init__(self) -> None:
        catInfo = getCatInfo()

        self.name = catInfo['name']
        self.age = catInfo['age']
        self.coloring = catInfo['coloring']
        self.personality = catInfo['personality']
        self.coat = catInfo['coat']
        self.toy = catInfo['toy']
        self.like = catInfo['like']
        self.dislike = catInfo['dislike']


# get cat info from static source to start
def getCatInfo() -> dict:
    names = ['Jolly', 'Shadow', 'Pumpkin', 'Wallyjoe', 'Runner', 'Queen', 'Floofy', 'Biscuit', 'Nibbles', 'Ghost']
    colorings = ['black', 'white', 'orange', 'tabby', 'calico', 'tortie']
    personalities = ['active', 'aloof', 'bold', 'calm', 'friendly', 'intolerant', 'shy', 'stubborn', 'tolerant']
    coats = ['short hair', 'long hair', 'medium hair']
    toys = ['ball', 'laser', 'wheel', 'string', 'flying', 'crinkle', 'squeky', ]
    likes = ['catnip', 'naps', 'sunshine', 'warmth', 'treats', 'brushing', 'playtime']
    dislikes = ['children', 'other cats', 'petting', 'loud noises', 'thunder storms', 'getting wet']

    name = random.choice(names)
    age = random.randint(1, 15)
    coloring = random.choice(colorings)
    personality = random.choice(personalities)
    coat = random.choice(coats)
    toy = random.choice(toys)
    like = random.choice(likes)
    dislike = random.choice(dislikes)

    catData = {
        'name': name,
        'age': age,
        'coloring': coloring,
        'personality': personality,
        'coat': coat,
        'toy': toy,
        'like': like,
        'dislike': dislike
    }

    return catData

@app.route('/catprofile', methods=['GET'])
def get_cat_profile():
    profiles = [CatProfile().__dict__ for index in range(3)]  # Generate 3 randomized cat profiles
    return flask.jsonify(profiles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)                        # Run flask app on default port 5000