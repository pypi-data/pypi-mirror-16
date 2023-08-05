
## Org


org is a simple Django frontend GUI for registering and managing organizations on the Marjoram suite.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

```
    INSTALLED_APPS = [
        ...
        'orgapp',
    ]
```

2. Include the polls URLconf in your project urls.py like this::

    ```url(r'^org/', include('orgapp.urls')),
    ```

3. Run `python manage.py migrate` to create the orgs models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an organization (you'll need the Admin app enabled).
