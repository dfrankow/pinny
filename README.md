## How to Use

To use this project, follow these steps:

1. Create your working environment with virtualenv.
2. Install requirements with `pip install -r requirements.txt`
3. Test locally with `./manage.py runserver`

An example URL: `http://localhost:8000/slack/puppies`

## Deployment to Heroku

    $ heroku create
    $ git push heroku master

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
