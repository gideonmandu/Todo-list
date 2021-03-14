todolist
======

The basic todo list app built in Flask.


Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the master branch. ::

    # clone the repository
    $ git clone 
    $ cd flask
    # checkout the correct version
    $ git tag  # shows the tagged versions
    $ git checkout latest-tag-found-above
    $ cd examples/tutorial

Create a virtualenv and activate it::

    $ python3 -m venv ll_env
    $ . ll_env/bin/activate

Or on Windows cmd::

    $ py -3 -m venv ll_env
    $ ll_env\Scripts\activate.bat

Install todolist::

    $ pip install -e .

Or if you are using the master branch, install Flask from source before
installing todolist::

    $ pip install -e ../..
    $ pip install -e .


Run
---

::

    $ export FLASK_APP=todolist
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=todolist
    > set FLASK_ENV=development
    > flask init-db
    > flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser

Some ideas for what to try next:
· A detail view to show a single post. Click a post’s title to go to its page.
· Like / unlike a post.
· Comments.
· Tags. Clicking a tag shows all the posts with that tag.
· A search box that filters the index page by name.
· Paged display. Only show 5 posts per page.
· Upload an image to go along with a post.
· Format posts using Markdown.
· An RSS feed of new posts.