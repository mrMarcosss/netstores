from django.contrib.auth import get_user_model
from skd_smoke import SmokeTestCase
from person.models import Person


def create_persons(testcase):
    for i in range(3):
        Person.objects.create(first_name='one%s', last_name='two%s', gender=0, email='bla%s@gmail.com' % i)


def create_one_person(commit=True):
    person = Person.objects.create(first_name='one', last_name='two', gender=0, email='bla@gmail.com', pk=1)
    if commit:
        person.save()
    return person


def edit_person(test):
    return {'first_name': 'blabla'}


def person_pk(testcase):
    pk = create_one_person().pk
    return {'pk': pk}


def get_user_credentials(testcase):
    username = 'test_user'
    password = '123456'
    credentials = {'username': 'test_user', 'password': '123456'}
    User = get_user_model()
    new_user = User.objects.create(username=username)
    new_user.set_password(password)
    new_user.save()
    testcase.user = new_user
    return credentials


def get_person_data(testcase):
    return {'first_name': 'one'}


class SimpleSmokeTestCase(SmokeTestCase):
    TESTS_CONFIGURATION = (
        ('persons', 200, 'GET', {'initialize': create_persons}),
        ('persons', 200, 'GET', {'initialize': create_one_person}),

        ('person', 200, 'GET', {'url_kwargs': person_pk, 'request_data': get_person_data}),
        ('person', 404, 'GET', {'url_kwargs': {'pk': 5}}),

        ('person_edit', 302, 'POST', {'url_kwargs': person_pk, 'request_data': edit_person}),
        ('person_edit', 200, 'POST', {'user_credentials': get_user_credentials, 'url_kwargs': {'pk': 'new'}}),
        ('person_edit', 404, 'POST', {'user_credentials': get_user_credentials, 'url_kwargs': {'pk': 5}}),

        ('person_delete', 302, 'POST', {'initialize': create_one_person, 'url_kwargs': {'pk': 1}}),
    )
