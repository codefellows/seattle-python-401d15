## API Deployment Cheat Sheet

- `heroku apps:create your-app-name`
  - That should add a remote to you git repo
  - `git remote -v`
  - Can also do `heroku git:remote -a your-app-name`
  - Can't remember all that, `heroku create --help`
- `heroku stack:set container`
- `git push heroku main` or `git push heroku master`

If new files have been pushed then a Docker build will be triggered on Heroku.

- Add/Commit/Push a new file to Heroku
- `heroku logs --tail`
- Refer to demo `heroku.yml` and make sure your gunicorn line matches your project name.
- Refer to demo for how to update `settings.py` to use environment variables.
- Remember that `.env` file goes in project folder (e.g. `snacks_project/.env`)
- Remember to update both `.env` and the config vars on Heroku to connect to ElephantSQL
- Refer to demo `sample.env` for example `.env` entries. 

### Handy Links

- https://devcenter.heroku.com/articles/git#creating-a-heroku-remote
- https://devcenter.heroku.com/articles/git
- https://devcenter.heroku.com/articles/build-docker-images-heroku-yml
- https://stackoverflow.com/questions/61132518/how-to-debug-django-staticfiles-served-with-whitenoise-gunicorn-and-heroku
- https://devcenter.heroku.com/articles/heroku-cli
- https://help.heroku.com/O0EXQZTA/how-do-i-switch-branches-from-master-to-main
- https://www.elephantsql.com/
- https://github.com/adamchainz/django-cors-headers
- https://privacy.com/

