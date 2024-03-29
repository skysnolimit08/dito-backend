# Dialect Interpretation and Translation Backend

This is the back end repo for Dito (dialect interpretation and translation online), a project by Tracy Burnett.  Dito -
- lets public and private teams collaboratively annotate audio data
- includes an auto-segmenter for transcribing audio data
- calculates explicit phrase alignment between written translations
- auto-highlights nested aligned phrases simultaneously in multiple written translations
- uses phrase alignment information to automatically generate language lessons

Visit [Rain Story](https://dev.dito.live/storybook/8F43-Wdn_gU.wav?open=7h70ZiG6bwEavy1PMVUL8w) to see a sample project created for a software demonstration (video below) of Dito.  
Visit [Little Horse Crosses River](https://yakaloco.dito.live/storybook/S65cMnPPpJA.m4a?open=aQ_XB5yrA6QkB8X4sUIHyc) to see a sample project created by an undergraduate student team using Dito.

Dito backend was created using Django, a Python framework.  The [views.py](https://github.com/skysnolimit08/dito-backend/blob/main/storybooks/views.py) file contains the most handwritten code.

## User Interface Demo Videos

[Part 1](https://www.dropbox.com/scl/fi/qpckg5la7yd9254k1gmn7/points-1-3-Audio-Leveled.mp4?rlkey=o1lq8m5nzbuleywbgxa2v8e2v&dl=0 "Demo Video Part 1") (7:31)  
[Part 2](https://www.dropbox.com/scl/fi/ehfri9kken39v2y40eg7g/points-4-6-Audio-Leveled.mp4?rlkey=i2424wnwi3uhlhang3epz7d1g&dl=0 "Demo Video Part 2") (10:44)

## Status

Dito is live and can be [used/sampled online](https://dev.dito.live "Dito"), and Tracy Burnett offers unique subdomains to users for larger projects.  Tracy Burnett makes Dito free to users as a tool for revitalizing low-resource languages, especially those with no dedicated orthography/written script.  However, Tracy Burnett reserves the right to terminate these services at any point.

## Update Notes
 - 06/20/2023: Sample workflow for converting the user interface into other languages
   - update Language model with new categories on local computer
   - update frontend code on local computer to use the new translations (and/or make new language(s) available for selecting)
   - run python manage.py makemigrations and then python manage.py migrate and test the changes
   - push the backend code to github and merge it to main in a pull request
   - verify that heroku has finished deploying the new code
   - "heroku run python manage.py migrate --app ditotranslationtool"
   - log in to api.dito.live/admin/ using a superuser with a capital letter as the first character
   - enter the new translations in for each language for the new categories you've made in the model
   - push the new frontend code
   - verify that Netlify has deployed the new frontend code
   - verify that the translations are displaying as expected
 - 11/08/2022: Main branch code auto-deploys to api.dito.live.  Migrations must be made locally and pushed to the repository and the build/deploy needs to finish on Heroku, after which skysnolimit08 needs to run heroku run python manage.py migrate --app ditotranslationtool to bring things up to speed on Heroku after database format changes.
- 6/16/2022: if you ever need to reset your local database, try running pipenv shell, then running python manage.py migrate storybooks zero, then running python manage.py makemigrations, and finally running python manage.py migrate.
 - For future reference on database upgrades with Heroku Postgres: https://gist.github.com/simonw/50e14b9a3e829355d6d43f0f12f91e74

# Project Setup

### Prerequisites

- Git
- Python 3
- Pip

You can check if you have these by typing

(Windows)
```
$ git --version
$ python --version
$ python -m pip --version
```

(Mac)
```
$ git --version
$ python3 --version
$ pip3 --version
```

- If you don't have Git, download it from git-scm.com/downloads/
- If you don't have Python 3, you can download it from https://www.python.org/downloads/
- - on Windows if you install this, you will want to check the box for "add Python to PATH", or else you will have to retroactively do it manually or do it by modifying the install.
- Pip or Pip 3 will install automatically when you install Python 3, which is great (unless you somehow prevent it, which you shouldn't).

**Installing Dependencies**

In your terminal, change directories into the folder you want to keep the project in.  Then:

Windows
```
$ git clone https://github.com/skysnolimit08/dialecttranslationtool-backend backend
$ cd backend
$ python -m pip install pipenv
$ pipenv install
```

Mac
```
$ git clone https://github.com/skysnolimit08/dialecttranslationtool-backend backend
$ cd backend
$ pip3 install pipenv
$ pipenv install
```

(The pip command will work on Windows; the pip3 command will work on Mac)

From now on, if you install a new package for the project, please do so using the command 'pipenv install package-name' from that same backend folder so that the Pipfile keeps track of what package dependencies our project needs for future developers and hosting servers.


**Configuring Environmental Variables**

Rename ".env-example" to ".env".  Paste the following code into it.  Create your own randomized value for SECRET_KEY.  You can use python secrets to help you do that.  Setting debug to True in your local environment will be helpful for debugging your code.  You probably do not need to use the DATABASE_URL environmental variable, since our settings.py file includes a default database URL, but you are welcome to if you want to host your database in a special place. Fill in the `AWS` related variables with values from `dito_env_variables.txt` in the project Google Drive.

```
SECRET_KEY='SECRET_KEY'
DEBUG_VALUE='True'
# DATABASE_URL=mysql://xygil:<password>@localhost:3306/xygil
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_STORAGE_BUCKET_NAME=...
AWS_REGION=...
AWS_S3_ENDPOINT_URL=...
```
Now, restart your terminal.


**Connecting MySQL with Django**


Windows
```
$ cd backend
$ pipenv shell
(venv) $ python manage.py migrate
```
Mac
```
$ cd backend
$ pipenv shell
(venv) $ python3 manage.py migrate
```

**Configuring an administrative "superuser" for MySQL**

Windows
```
$ pipenv shell
(venv) $ python manage.py createsuperuser
Username: 
Email address: 
Password: 
Password (again):
```
Mac
```
$ pipenv shell
(venv) $ python3 manage.py createsuperuser
Username: 
Email address: 
Password: 
Password (again):
```


## Running the Server
Windows
```
$ pipenv shell
(venv) $ python manage.py runserver # Defaults to http://localhost:8000
```
Mac
```
$ pipenv shell
(venv) $ python3 manage.py runserver # Defaults to http://localhost:8000
```
Now, navigate to http://localhost:8000 and you should see the server running!

# Models   (ALL TEXT BELOW THIS POINT IS OUTDATED)
## `Extended_User`

```python
class Extended_User(models.Model):
    # The default for Django Models CharField is 255, which should be enough for both user_ID and display_name
    user_ID = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # basically adds the timestamp when the record is added
    anonymous = models.BooleanField(default=False)

```
Note: Other files changed due to this model include `views.py` for the request handling, `urls.py` to point URL to function. 

## `Audio`
```python
class Audio:
    class Meta:
        verbose_name = "audio file"
        verbose_name_plural = "audio files"

    url             = CharField(max_length=255)
    title           = CharField(default="Untitled", max_length=255)
    archived        = BooleanField(default=False)

    # Metadata
    createdAt       = DateTimeField()
    updatedAt       = DateTimeField()
    lastUpdatedBy   = ForeignKey(User, null=True, on_delete=SET_NULL)
```
## `Translation`
```python
class Translation:
    class Meta:
        verbose_name = "translation"
        verbose_name_plural = "translations"

    title           = CharField(max_length=255)
    audio           = ForeignKey(Audio, on_delete=CASCADE)
    published       = BooleanField(default=False)

    # Metadata
    author          = ForeignKey(User, null=True, on_delete=SET_NULL)
    createdAt       = DateTimeField()
    updatedAt       = DateTimeField()
    lastUpdatedBy   = ForeignKey(User, null=True, on_delete=SET_NULL)
```
## `Story`
```python
class Story:
    class Meta:
        verbose_name = "story"
        verbose_name_plural = "stories"

    translation     = ForeignKey(Translation, null=True, on_delete=SET_NULL)
```


##  API  (OUTDATED)

# Extended Users 
Create, update, and retrieve 

### Create User 
It takes the following payload JSON and then creates a 
user for the request. 
```python
user_ID=data['user_id'], 
description=data['description']
display_name=data['display_name'],
anonymous=data['anonymous']
```
This will return a JSON serialized object and the user object will be saved.

### Update User 
Update the fields in the User object. Currently, the `permission_classes` is commented. It also returns the serialized, updated User object. 

The request payload can have the following fields: 
1. Description
2. Display Name 
3. Anonymous

### Retrieve/Get User 
Return the user object. This function call requires the user_id to be passed in. Otherwise, the request payload must contain the user_id. 

This function returns the serialized, JSON User object for that specific user_id. 

# Users
Create, read, update, and delete user.

## Create User
Working 3/7/2022.  Did not test authentication.  Is not safe and code needs to be deprecated and replaced with Django Auth functions.

**URL** : `/user/`

**Method** : `POST`

**Auth required** : Yes

**Data example**

```json
{
    "username": "user1",
    "name": "Xygil Net",
    "email": "example@xygil.net",
    "password": "xygil123",
    "description": "A dude"
}
```
## Read User
Working 3/7/2022.

**URL** : `/user/:id`

**Method** : `GET`

**Auth required** : No

**Content example**

```json
{
    "email": "example@xygil.net",
    "name": "Xygil Net",
    "description": "A dude"
}
```

## Update User
Is probably not safe and code needs to be deprecated and replaced with Django Auth functions.

**URL** : `/user/:id`

**Method** : `PATCH`

**Auth required** : Yes

**Data example**

```json
{
    "email": "example@dito.live",
    "password": "ditodito123"
}
```

## Delete User
May not be safe to the point that code needs to be deprecated and replaced with Django Auth functions.

**URL** : `/user/:id`

**Method** : `DELETE`

**Auth required** : Admin

## Index User Audios
3/7/2022 Can't get this to work, and not sure where to find the code for it in the backend.

**URL** : `/user/:id/audio`

**Method** : `GET`

**Auth required** : No

**Content example**

```json
{
    "num": 2,
    "audio": [
        {
            "url": "aws.amazon.com/cloudfront/136523",
            "title": "Audio1",
            "id": 1,
            "description": "War and Peace",
            "public": true
        },
        {
            "url": "aws.amazon.com/cloudfront/12395323",
            "title": "Audio2",
            "id": 2,
            "description": "Gettysberg Address",
            "public": false
        },
    ]
}
```

# Audio
Create, read, update, and delete audio.

## Create Audio
Working on 4/26/2022.  

**URL** : `/storybooks/audio/`

**Method** : `POST`

**Auth required** : Yes

**Data example**

```json
{
    "id": "1",
    "url": "aws.amazon.com/cloudfront/1249513",
    "title": "A random audio file",
    "description": "a description",
    "archived": false,
    "uploaded_at": "2022-04-26T06:29:06.159347Z",
    "uploaded_by": 1,
    "last_updated_at": "2022-04-26T06:29:06.159356Z",
    "last_updated_by": 1,
    "shared_with": [
        1,
        2
    ],
    "public": false,
    "id_token": "randomToken"
}
```
## Read Public Audio
Returns a list of public, non- archived audio files.\
**URL** : `/storybooks/audio/`

**Method** : `GET`

**Auth required** : No

**Content example**

```json
{
    "audio": [
        {
            "title": "Audio 3",
            "id": "3",
            "description": "A description",
            "url": "aws.amazon.com/cloudfront/12395324"
        },
        {
            "title": "Audio 2",
            "id": "2",
            "description": "A description",
            "url": "aws.amazon.com/cloudfront/12395325"
        },
        {
            "title": "Audio",
            "id": "5",
            "description": "A description",
            "url": "aws.amazon.com/cloudfront/12395326"
        }
    ]
}
```

## Read Public Audio for a User
Returns a list of public, non- archived audio files for a specific user.\
**URL** : `/storybooks/audio/user/<int:uid>`

**Method** : `GET`

**Auth required** : No

**Content example**

```json
{
    "audio": [
        {
            "title": "Audio 1",
            "id": "3",
            "description": "A description",
            "url": "aws.amazon.com/cloudfront/123953124"
        },
        {
            "title": "Audio",
            "id": "5",
            "description": "A description",
            "url": "aws.amazon.com/cloudfront/12313"
        }
    ]
}
```

## Read Private Audio for a User
Returns a list of audio files that a user created, or (which have been shared with them and  not archived).\
**URL** : `/storybooks/audio/user/`

**Method** : `GET`

**Auth required** : Yes

**Content example**

```json
{
    "audio": [
        {
            "id": "1",
            "url": "aws.amazon.com/cloudfront/12313",
            "title": "A random audio file",
            "description": "a description",
            "archived": false,
            "uploaded_at": "2022-04-26T06:29:06.159347Z",
            "uploaded_by": 1,
            "last_updated_at": "2022-04-26T06:29:06.159356Z",
            "last_updated_by": 1,
            "shared_with": [
                1,
                2
            ],
            "public": false
        },
        {
            "id": "1",
            "url": "aws.amazon.com/cloudfront/12313",
            "title": "A random audio file",
            "description": "a description",
            "archived": false,
            "uploaded_at": "2022-04-26T06:29:06.159347Z",
            "uploaded_by": 1,
            "last_updated_at": "2022-04-26T06:29:06.159356Z",
            "last_updated_by": 1,
            "shared_with": [
                1,
                2
            ],
            "public": false
        }
    ]
}
```

## Update Audio as an editor
A logged-in user can update some fields of audio entries that have been shared with them and not archived. Working as of 4/26/2022.

**URL** : `/storybooks/audio/<int:audio_id>/editor`

**Method** : `PATCH`

**Auth required** : Yes

**Data example**

```json
{
    "title": "A new title",
    "description": "Twenty-seven minutes of people coughing",
}
```

## Update Audio as an owner
A logged-in user can update most fields of audio entries they created. Working as of 4/26/2022.

**URL** : `/storybooks/audio/<int:audio_id>/owner`

**Method** : `PATCH`

**Auth required** : Yes

**Data example**

```json
{
    "title": "A new title owner",
    "description": "Making the audio public since I'm an owner",
    "public": true
}
```



## Delete Audio
Working on 3/7/2022.  Authentication not tested.

**URL** : `/audio/:id`

**Method** : `DELETE`

**Auth required** : Yes



# Translations
Create, read, update, and delete translations associated with an audio.

## Create Translation
Creates translation object.  Returns the translation with language `:lid` of an audio `:id`.  3/7/2022 For this to work, need to comment out the Check unique section of views.py.  But then that breaks some other things down the line.\
**URL** : `/audio/:id/translations/:lid`

**Method** : `POST`

**Auth required** : Yes

**Data example**

```json
{
    "user": "user1", 
    "title": "test title",
    "text": "Four score and seven years ago, our fathers brought forth on this continent...",
    "lid": 5,
    "public": false
}
```
## Read Translation
Returns entire translation if public or authenticated and private.  Working as of 3/7/2022.  Did not test authentication.\
**URL** : `/audio/:id/translations/:lid`

**Method** : `GET`

**Auth required** : Yes/No

**Content example**

```json
{
    "text": "Four score and seven years ago, our fathers brought forth on this continent...",
}
```

## Update Translation
Updates the entire text. This operation will automatically maintain existing associations for words that aren't deleted and insert NULL associations for newly inserted words.  Working as of 3/7/2022. Did not test authentication.\
**URL** : `/audio/:id/translations/:lid/`

**Method** : `PATCH`

**Auth required** : Yes

**Data example**

```json
{
    "text": "Eighty-seven years ago, our fathers brought forth on this continent..."
}
```

## Delete Translation
Works 3/7/2022.  But doesn't delete or archive the associated stories.

**URL** : `/audio/:id/translations/:lid`

**Method** : `DELETE`

**Auth required** : Yes

## Index Translation Languages
Returns a list of all available public languages for the translation.\
**URL** : `/audio/:id/translations`

**Method** : `GET`

**Auth required** : No

**Content example**

```json
{
    "languages": [0, 1, 3, 5, 6]
}
```

# Languages

## LanguageID to Language

**URL** : `/languages`

**Method** : `GET`

**Auth required** : No

**Content example**

```json
{
    0: "English",
    1: "Spanish",
    2: "Chinese"
}
```

# Associations

## Get Associations for Highlighting
Returns the text between `ts1` and `ts2` along with a dictionary which maps sorted timestamp intervals to highlighted portions of text. Ex. From 0 to 3000 ms, characters between character index 0-9 and 16-20 (inclusive) should be highlighted (Four score/seven). From 3500 to 5000 ms, character from index 11-15 should be highlighted (and). If there are no configured associations, returns the entire text.\
**URL** :  `/audio/:id/translations/:lid/associations?ts1=int&ts2=int`

**Method** : `GET`

**Auth required** : No

**Content example**

```json
{
    "text": "Four score and seven years ago, our fathers brought forth on this continent...",
    "associations": {
        "0-3000": ["0-9", "15-19"],
        "3500-5000": ["11-13"]        
    }
}
```
## Update Associations
Given a portion of the text, associates particular indexes with timestamps(ms). The specific way how this works is the first portion of exclusive text matching this substring will be updated which is not ideal (since there may be infrequent cases of unintended associations if the "text" is too short) but simplifies the work done front end and the amount of text metadata needed immensely.\
**URL** :  `/audio/:id/translations/:lid/associations`

**Method** : `POST`

**Auth required** : Yes

**Content example**

```json
{
    "text": "seven years ago, our fathers brought forth on this continent",
    "associations": {
        15: 2400,
        23: 1500,
        34: 3567
    }
}
```


# Interpretations
Create, retrieve, update, and delete interpretations associated with an audio.

## Create
Creates interpretation object. Have not completed after HTTP request endpoints as of 4/27/22.

**URL** : `/storybooks/interpretations/audio/<int:audio_id>/`

**Method** : `POST`

**Auth required** : Yes

**Data example**

```json
{
    "id": "5", 
    "public": true,
    "shared_editors": [1, 2, 3],
    "shared_viewers": [1, 2, 3],
    "audio_ID": "5",
    "title": "test title",
    "latest_text": "Four score and seven years ago, our fathers brought forth on this continent...",
    "archived": false,
    "language_name": "English",
    "spaced_by": "_",
    "created_by": "me",
    "created_at": "2022-04-29T07:39:06.159347Z",
    "last_edited_by": "him",
    "last_edited_at": "2022-04-26T08:29:06.159347Z",
    "version": 1
}
```
## Retrieve Audios
For a given audio file, a user can get a list of interpretations that they created, or which are shared with them for viewing and not archived, or which are shared with them for editing and not archived, or which are public and not archived. As of 4/27/2022, returns the entire interpretation, but should only return ID, title, created_by, language_name. Have not completed after HTTP request endpoints as of 4/27/22.

**URL** : `/storybooks/interpretations/audio/<int:audio_id>/`

**Method** : `GET`

**Auth required** : Yes

**Content example**

```json
{
    "id": "5", 
    "title": "test title",
    "language_name": "English",
    "created_by": "me"
}
```

## Retrieve Editors
A user can view an interpretation that is shared with them for editing and not archived. As of 4/27/2022, returns the entire interpretation, but should only return ID, public, title, latest_text, created_by, language_name, audio_id, last_edited_at.

**URL** : `/storybooks/interpretations/<int:interpretation_id>/audio/<int:audio_id>/editor`

**Method** : `GET`

**Auth required** : Yes

**Content example**

```json
{
    "id": "5", 
    "public": true,
    "audio_ID": "5",
    "title": "test title",
    "latest_text": "Four score and seven years ago, our fathers brought forth on this continent...",
    "language_name": "English",
    "created_by": "me",
    "last_edited_at": "2022-04-26T06:29:06.159347Z",
}
```

## Update Editors
If interpretation is not archived and shared_editors includes the current user, they can edit some fields of the interpretation. Title, public, language_name, and latest_text should be populated by logged-in user. Last_updated_by and last_updated_at should be autopopulated with logged-in user's uid and the timestamp of the fetch. Version should increment by 1. Have not completed after HTTP request endpoints as of 4/27/22.

**URL** : `/storybooks/interpretations/<int:interpretation_id>/audio/<int:audio_id>/editor`

**Method** : `PATCH`

**Auth required** : Yes


## Retrieve Owners
A user can view an interpretation that they created. Returns all attributes of the interpretation.

**URL** : `/storybooks/interpretations/<int:interpretation_id>/audio/<int:audio_id>/owner`

**Method** : `GET`

**Auth required** : Yes

**Content example**

```json
{
    "id": "5", 
    "public": true,
    "shared_editors": [1, 2, 3],
    "shared_viewers": [1, 2, 3],
    "audio_ID": "5",
    "title": "test title",
    "latest_text": "Four score and seven years ago, our fathers brought forth on this continent...",
    "archived": false,
    "language_name": "English",
    "spaced_by": "_",
    "created_by": "me",
    "created_at": "2022-04-26T06:29:06.159347Z",
    "last_edited_by": "him",
    "last_edited_at": "2022-04-26T06:29:06.159347Z",
    "version": 1
}
```

## Update Owners
A logged-in user can edit all of the information about an interpretation that they created. Public, shared_editors, shared_viewers, audio_id, title, latest_text, archived, language_name, and spaced_by can be populated by the logged-in user. Last_updated_by and last_updated_at should be autopopulated with logged-in user's uid and the timestamp of the fetch. Version should increment by 1. Have not completed after HTTP request endpoints as of 4/27/22.

**URL** : `/storybooks/interpretations/<int:interpretation_id>/audio/<int:audio_id>/owner`

**Method** : `PATCH`

**Auth required** : Yes


## Destroy
A logged-in user can delete all of the information about an interpretation that they created. Have not completed after HTTP request endpoints as of 4/27/22.

**URL** : `/storybooks/interpretations/<int:interpretation_id>/audio/<int:audio_id>/owner`

**Method** : `DELETE`

**Auth required** : Yes


## Retrieve All
A user can get a list of interpretations that they created, or which are shared_with them for viewing and not archived, or which are shared_with them for editing and not archived. As of 4/27/2022, returns the entire interpretation, but should only return ID, public, title, archived, spaced_by, created_by, language_name, audio_id, last_edited_at.

**URL** : `/storybooks/interpretations/`

**Method** : `GET`

**Auth required** : Yes

**Content example**

```json
{
    "id": "5", 
    "public": true,
    "audio_ID": "5",
    "title": "test title",
    "archived": false,
    "language_name": "English",
    "spaced_by": "_",
    "created_by": "me",
    "created_at": "2022-04-26T06:29:06.159347Z",
    "last_edited_at": "2022-05-01T06:29:06.159347Z",
}
```

## Retrieve User
Anybody can get a list of interpretations created by a user and public and not archived. As of 4/27/2022, returns the entire interpretation, but should only return ID, title, created_by, language_name, audio_id.

**URL** : `/storybooks/interpretations/`

**Method** : `GET`

**Auth required** : No

**Content example**

```json
{
    "id": "5", 
    "audio_ID": "5",
    "title": "test title",
    "language_name": "English",
    "created_by": "me",
}
```
