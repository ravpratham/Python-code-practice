<h1>Django Setup</h1>

<h6>
<ol>
    <li>Open terminal in pycharm itself and select command prompt</li>
    <li>Set up an Environment where you want to save your code.</li>
    <li>Install django version</li>
    
    python -m pip install Django==5.1.1

<li>create a dedicated environment for django</li>

    django-admin startproject mysite
This will start a project in the name of mysite in the location where you are storing your code

<li>Create a python file or python jupyter notebook and write the below commands to check 
whether the django version is correctly installed or not</li>

    import django
    print(django.get_version())   

OUTPUT:
    
    5.1.1

<li>(For another verification) Change into the outer mysite directory</li>
write below command in cmd

    cd mysite

Then

    python manage.py runserver

OUTPUT

    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    September 05, 2024 - 22:24:23
    Django version 5.1.1, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

<h3>Ignore the warning about unapplied database migrations for now.</h3>
<br/>

<h4>Now that the server’s running, visit http://127.0.0.1:8000/ with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!</h4>

    http://127.0.0.1:8000/

<h3>For more information visit the below url

    https://docs.djangoproject.com/en/5.1/intro/tutorial01/

<h2>Installation is completed</h2>
</ol>
</h6>