Wagtail Dependencies
====================
This package for Wagtail makes it easy to manage front-end dependencies for admin plugins.

#### The problem
Multiple Wagtail plugins may require the same front-end dependency, ex. Font Awesome. But we don't want to require that dependency twice on the admin screen, so we need to detect that duplication and only include it only once.

#### The solution
We can use named dependencies to prevent duplication, as long as developers can agree to use the same name. For instance, if we name Font Awesome `fontawesome`, then multiple projects can enqueue the `fontawesome` CSS, and this app will be sure it's only imported once.

Usage
-----
Add `wagtaildependencies` to your `INSTALLED_APPS`, then you can use the following hooks:

* `enqueue_scripts`
* `enqueue_styles`

The system will automatically detect duplicates among enqueued media throughout apps and will only include the library once.

Example
-------
```python
@hooks.register('enqueue_scripts')
def enqueue_jquery():
    return {
        'jquery': {
            'source': 'lib/js/jquery.js',
            'version' '3.1.0',
        }
    }

@hooks.register('enqueue_styles')
def enqueue_fontawesome():
    return {
        'fontawesome': {
            'source': 'lib/css/fontawesome.css',
            'version': '4.6.3',
        }
    }
```


