# Deployment Walk Through

## Initialize
- `git init`
- `heroku apps:create snacks-deployment-fun`
- Check remote with `git remote -v`
- If heroku remote doesn't show then `heroku git:remote -a snacks-deployment-fun`
- Create `heroku.yml` in root folder.
- Add below text to `heroku.yml`

```yaml
build:
  docker:
    web: Dockerfile
release:
  image: web
run:
  web: gunicorn snacks_project.wsgi
```
 
 - **NOTE**: make sure your project name matches.
 - create `.gitignore`
   - Pro Tip: Use [gitignore.io](https://www.toptal.com/developers/gitignore)  
   - Enter `Python`,`Django` and `vscode`
- `heroku stack:set container`
- ACP initial files
- `poetry add django-environ`
- `poetry add psycopg2-binary`
- `poetry add django-cors-headers`
- `poetry export -o requirements.txt --without-hashes`

## Add/Update .env

- `touch snacks_project/.env`
- Add below text to `.env`
```
DEBUG=on
SECRET_KEY=REPLACE_ME
DATABASE_NAME=REPLACE_ME
DATABASE_USER=REPLACE_ME
DATABASE_PASSWORD=REPLACE_ME
DATABASE_HOST=REPLACE_ME
DATABASE_PORT=REPLACE_ME
ALLOWED_HOSTS=localhost,127.0.0.1
```

- Update `SECRET_KEY`
- Hold off on DATABASE values for a bit.

## Update Settings

Near top of `settings.py`

```python
import environ

env = environ.Env(
    # We are doing a default setting here because even if something happens to the .env, we set this to false to make sure Django dosn't start pusging out to much information on the error pages (you know, the good stuff we have been using to debug out pages until revently)
    DEBUG=(bool, False)
)

# read .env file
environ.Env.read_env()
``` 

Replace `SECRET_KEY`, `DEBUG` and `ALLOWED_HOSTS` with...

```python
# Read from Environment
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS'))
```

## Database Time

- Grab Database details from ElephantSQL and update `.env` file.
  - `DATABASE_NAME`, etc. 
- Replace `DATABASES` section of `settings.py` with...

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD':  env('DATABASE_PASSWORD'),
        'HOST':  env('DATABASE_HOST'),
        'PORT':  env('DATABASE_PORT')
    }
}
```

- Activate virtual environment
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `gunicorn snacks_project.wsgi`
- Check `http://localhost:8000/api/v1/snacks/` in browser.
- ctrl+c to shut down server.
- exit virtual environment


## Heroku Time

- Add/Commit
- `git push heroku master`
- Go to heroku dashboard
- Select current app
- Go to settings
- Click `reveal config vars` button
- Add config vars to match `.env` file
- `ALLOWED_HOSTS` should match the heroku URL for your app.
  - Click `Open app` button to see it
  - Leave out the `https://` and trailing slash.
  - E.g. snacks-deployment-fun.herokuapp.com 

## Stretch

- Add [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- Handle collecting static files so that styling doesn't go away with DEBUG off
  - There is some trickiness here, especially on Heroku. Often static assets would be on CDN so it's not an issue. 