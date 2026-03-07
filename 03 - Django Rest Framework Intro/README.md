# Django Rest Framework

### Requirements:

REST framework requires the following:
- Python
- Django

The following packages are optional:

- `PyYAML`, `uritemplate` (5.1+, 3.0.0+) - Schema generation support.
- `Markdown` (3.3.0+) - Markdown support for the browsable API.
- `Pygments` (2.7.0+) - Add syntax highlighting to Markdown processing.
- `django-filter` (1.0.1+) - Filtering support.
- `django-guardian` (1.1.1+) - Object level permissions support.

### Installation

```shell
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter
```

### Setup

Add `rest_framework` to your INSTALLED_APPS setting.

```python
INSTALLED_APPS = [
    # ...
    "rest_framework",
]
```

If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.

```python
urlpatterns = [
    # ...
    path("api-auth/", include("rest_framework.urls"))
]
```

### Example

References:
1. https://www.django-rest-framework.org/
