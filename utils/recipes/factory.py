from random import randint
from faker import Faker


def randRatio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')


def makeRecipe():
    return {
            'title' : fake.sentence(nb_words=6),
            'id' : fake.random_number(digits=2, fix_len=True),
            'description' : fake.sentence(nb_words=13),
            'preparation_time' : fake.random_number(digits=2, fix_len=True),
            'preparation_time_unit' : 'Minutos',
            'servings' : fake.random_number(digits=2, fix_len=True),
            'servings_unit' : 'Porção',
            'preparation_steps' : fake.text(3000),
            'creation_date' : fake.date_time(),
            'author' : { 
                'first_name' : fake.first_name(),
                'last_name' : fake.last_name(),
                },
            'category' : { 
                'name' : fake.word()
            },
             'cover': {
                'url': 'https://loremflickr.com/%s/%s/food,cook' % randRatio(),
            },
             }


if __name__ == '__main__':
    from pprint import pprint
    pprint(makeRecipe())
