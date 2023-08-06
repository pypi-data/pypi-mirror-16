# djmessenger

## Install

1. TBD

## Setup

1. In your `settings.py`, ensure that

    ```
    INSTALLED_APPS = {
        ...
        'djmessenger'
    }
    ```

2. You need to decide the endpoint in your server for Facebook to send the callback

    It is recommended to use a randomly-generated string as the endpoint, you can get one using management command
    
    ```
    python manage.py get_random_endpoint
    ```
    
    And then copy paste to `settings.py` 
     
    ```
    DJM_ENDPOINT = 'abcdef'
    ```
    
    this will result in a url like
    
    `https://localhost:8000/abcdef`

3. In `settings.py`, define your page access token

    ```
    DJM_PAGE_ACCESS_TOKEN = '<Page Access Token>'
    ```
    
4. Now run your local server `python manage.py runserver`

5. Access your endpoint `http://localhost:8000/abcdef/`

    You should see `Error, invalid token`
    
## Overview

TBD
    
## Usage

1. TBD

## i18n

**djmessenger** supports django i18n settings, all you need to do is

1. Make sure that your marked all the strings that you wish to be localized with ugettext_lazy

    `from django.utils.translation import ugettext_lazy as _`
    
2. You need to following django i18n instructions to define LOCALE_PATH, LANGUAGES and etc in settings.py

3. make and compile messages

    ```
    python manage.py makemessages
    python manage.py compilemessages
    ```
    
4. djmessenger settings `DJM_SAVE_USER_PROFILE` must be set to True in order for i18n to take effect

    > Because djmessenger simply uses the locale reported by Facebook,
    > as a result, if DJM_SAVE_USER_PROFILE was not enabled, we won't 
    > have locale info and thus i18n won't work
    
5. When subclassing `CommonSender`, be sure to use `install_user_locale(psid)` and `reset_locale()` when you init your sender and it contains strings that will be displayed to user

    **djmessenger** provides 2 convenience method to install user langauge and reset it
    
    ```
    djmessenger.utils.i18n.install_user_locale
    djmessenger.utils.i18n.reset_locale
    ```

    To make sure `CommonSender.send()` correctly sends i18n'ed message,
     
    ```
    import gettext
    
    ... 
    ...
    
    
    def __init__(self, psid, text):
        super().__init__(psid)
        install_user_locale(psid)
        try:
            text = _(text).encode('utf-8')
        except:
            # if the locale is not supported, _() will fail, so catch it and
            # fallback to English
            text = text.encode('utf-8')
        self.message = {"text": text}
        reset_locale()
    ```
