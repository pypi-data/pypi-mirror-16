# djmessenger

[![PyPI version](https://badge.fury.io/py/djmessenger.svg)](https://badge.fury.io/py/djmessenger)

djmessenger provides a simple way to build a Facebook Messenger BOT

## Overview

![Overview](https://www.lucidchart.com/publicSegments/view/75d4b7e2-b509-4a06-a7b9-7273b1cc4cf5/image.png)

djmessenger is essentially a REST API. djmessenger simply exposes a REST API
endpoint for Facebook Messenger webhook so that Facebook will send a 
request to djmessenger endpoint when subscribed events happen. 

## Features

1. For each message sent, record sender's PSID (page-scoped ID) so that
   we can send something back to the sender
2. Save user basic info
3. If the user sends a location, save it into database
5. Easy to setup
6. Flexible to extend

## Next Features

- More handlers
- More senders
- i18n support

## Install

    ```
    pip install djmessenger
    ```

## Prerequisites

1. You must have a Facebook page, this is different from having a personal account, but you can always create a page as you like for free
2. Obtain your page access token
    - Login to [Facebook Developers](https://developers.facebook.com)
    - From top right **My Apps**, click on **Add a New App**
    - Enter this new app
    - From left side, **+ Add Product**
    - Click **Get Started** on **Messenger** and **Webhooks**
    - Go to **Messenger**, in **Token Generation**, choose a page and copy the token for later use
    - Click **Webhooks** and leave this page open for later

## django Setup

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
    
    `http://localhost:8000/abcdef`

3. In `settings.py`, define your page access token

    ```
    DJM_PAGE_ACCESS_TOKEN = '<Page Access Token>'
    ```
    
## Minimal BOT Setup

Check [here](https://github.com/ifanchu/djmessenger/wiki/Minimal-BOT-Setup)

## Detailed customized BOT

check [here](https://github.com/ifanchu/djmessenger/wiki/Customized-BOT-Showcase)
