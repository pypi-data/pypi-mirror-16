djangocms-markdown
==================

This is a plugin for django-cms that aims to replace the standard text plugin
with it's WYSIWYG editors. With cmsplugin-markdown you can write your content
in Markdown using EpicEditor (http://oscargodson.github.com/EpicEditor/)

Changelog
---------

### 0.3.2 - 2016/08/09
* Now uses (and embed) jQuery 3.1.0 (thanks to David D Lowe)
* Set text direction correctly, now works with RTL languages (thanks to David D Lowe)
* Minor JS fixes (thanks to David D Lowe)

### 0.3.1 - 2015/04/30 (Forked from https://github.com/ovidner/djangocms-markdown)
* Support Django Migrations, now works with Django 1.7+

Installation
------------

Install from GitHub::

    $ pip install git+https://github.com/niconoe/djangocms-markdown.git#egg=djangocms_markdown

Add ``djangocms_markdown`` and ``markdown_deux`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'markdown_deux',
        'djangocms_markdown',
    )

Migrate your database::

    ./manage.py migrate djangocms_markdown

Usage
-----

Just go to the page admin of django-cms (or the Entries admin of
cmsplugin-blog) and add a markdown plugin to a placeholder. It should be pretty
much self-explanatory.

Contribute
----------

You are very welcome to contribute! Fork off, make a branch and do a pull request.

License
-------

**Major components:**

* EpicEditor: [MIT license](https://github.com/OscarGodson/EpicEditor/blob/develop/LICENSE)
* jQuery: MIT license
* Everything else: [MIT license](https://github.com/niconoe/djangocms-markdown/blob/master/LICENSE)
