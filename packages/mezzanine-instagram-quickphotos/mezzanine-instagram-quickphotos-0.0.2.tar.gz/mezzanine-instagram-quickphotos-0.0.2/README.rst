===================
Mezzanine Quick Photos
===================
A Mezzanine app to store the latest photos from Instagram.

Installation
---------
```
$ pip install mezzanine-instagram-quickphotos
```

Configuration
---------
In `settings.py`:
```
INSTALLED_APPS = (
    ...
    'mezzanine_quickphotos',
)
```
Configure `INSTAGRAM_ACCESS_TOKEN` and `INSTAGRAM_CLIENT_SECRET` in Mezzanine admin configuration setting
Register site application in https://www.instagram.com/developer/clients/register/ and enable implicit OAuth
Get ACCESS-TOKEN
```
https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=token
```