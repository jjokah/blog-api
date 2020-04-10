# Blog API

A blog-post django rest api project

## Table of Contents

- [Example](#example)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [Deployment](#deployment)

## Example

```python
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

```

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

project that uses django rest api and react to create a todo list app

What things you need to install the software and how to install them

- Python 3
- Pip install packages

## Installation

To get a development env running:

> clone this repo to your local machine

```
git clone https://github.com/JohnJohnsonOkah/library.git
```

> install requirements

```
pip install -r requirements.txt
```

> setup database

```
python manage.py migrate
```

> create superuser

```
python manage.py createsuperuser
```

> run development server

```
python manage.py runserver
```

... 👯 Now development server is up and running...

## Features

-

## Deployment

Additional notes about how to deploy this on a live system
