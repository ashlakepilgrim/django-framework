# Django Rest Framework

Django REST Framework (DRF) is an extension for Django that simplifies building web APIs by providing serializers, class-based views, authentication systems, and tools for handling HTTP requests and responses in RESTful applications.

DRF provides higher-level abstractions for building APIs so developers don't need to manually handle serialization, validation, authentication, and routing.

Some reasons you might want to use REST framework:

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.

### Comments from Reddit

Comment 1:

```
Django Rest Framework requires Django as a dependency. Further, Django can do everything that Django Rest Framework can do, you'd just have to write a lot of code to replicate the functionality of Django Rest Framework. DRF gives you a lot of convenience, like authentication modules, json serializers/deserializers, API routing and documentation, etc.
```

Comment 2:

```
Very easy to create CRUD apis for individual models. Nested models get hairy, especially for writable serializers.

I think the serializers have too much responsibility. They handle serialization, validation, and model creation. Doesn't fit well with stuff like Clean Architecture, etc. Of course you can just avoid ModelSerializer and use Serializer's for strictly serialization and handle validation, model creation etc in the view but it's kinda throwing away DRF's features.

As far as using Serializer's, the whole to_internal_value and to_representation thing takes awhile to get used to, and ideally you don't need to mess with that kind of thing but there are some places you have to mess with it like removing nulls for optional+non-nullable fields.
```

Comment 3:

```
It's a lot of abstraction with a lot of benefit, as you mention. But, like you, I found it to be quite heavy weight. I end up just doing simple deserialization with django forms and rolling a serialization framework like you're describing (a to_json method). It works quite well.

The biggest thing I disagree with DRF (or perhaps I don't understand... it's been a while) is how they tie deserialization, validation & serialization together. I personally prefer validation and serialization to be separate.
```

### The 3 Things DRF Adds to Django

When you were writing raw APIs with Django, you had to manually do:

1️⃣ Convert model → JSON
2️⃣ Handle request/response
3️⃣ Validate input

DRF introduces three core components:

| Concept                | What it replaces                          |
| -----------------------| ----------------------------------------- |
| **Serializer**         | your manual JSON conversion               |
| **APIView**            | your Django view returning `JsonResponse` |
| **Response**           | DRF's smarter JSON response               |

But DRF also adds routers/viewsets, which are a major abstraction.

| Concept                | What it replaces                          |
| ---------------------- | ----------------------------------------- |
| **ViewSets + Routers** | manual URL routing for CRUD endpoints     |

### Compare Your Code vs DRF

Manual serialization

```python
data = [
    {
        "id": b.id,
        "title": b.title,
        "author": b.author
    }
    for b in books
]
```

DRF serialization

```python
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
```

### DRF Mental Model

```
Client Request
      ↓
APIView / ViewSet
      ↓
Queryset (ORM)
      ↓
Serializer
      ↓
Response (JSON)
```

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

If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root `urls.py` file.

```python
urlpatterns = [
    # ...
    path("api-auth/", include("rest_framework.urls"))
]
```

### Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API.

We'll create a read-write API for accessing information on the users of our project.

Any global settings for a REST framework API are kept in a single configuration dictionary named `REST_FRAMEWORK`. Start off by adding the following to your `settings.py` module:

```python
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}
```

Don't forget to make sure you've also added `rest_framework` to your `INSTALLED_APPS`.

We're ready to create our API now. Here's our project's root `urls.py` module:

```python
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
```

You can now open the API in your browser at `http://127.0.0.1:8000/`, and view your new `users` API. If you use the login control in the top right corner you'll also be able to add, create and delete users from the system.

References:
1. https://www.django-rest-framework.org/
