Django-Linked-Select2
=====

Django-Linked-Select2 is an extension to
[Django-Select2](https://github.com/applegrew/django-select2/),
which allows to create some simple inter-widget dependencies, like limiting choices of one widget based on value of other widget or even querying instances of specific model for generic relations.

This app does not support linked FormSets with variable amount of widgets.


## Installation

1. Add `linked_select2` to your `INSTALLED_APPS` setting before `django_select2`:


```
#!python

INSTALLED_APPS = [
    ...
    'linked_select2',
    'django_select2',
]
```

2. Add `linked_select` to your urlconf if you use any 'Auto' fields:


```
#!python

url(r'^select2/', include('linked_select2.urls')),
```


## Documentation
Documentation available at http://django-linked-select2.readthedocs.io/.

## License

>Copyright 2016 Miron Olszewski

>Licensed under the Apache License, Version 2.0 (the "License");
>you may not use this file except in compliance with the License.
>You may obtain a copy of the License at

>    http://www.apache.org/licenses/LICENSE-2.0

>Unless required by applicable law or agreed to in writing, software
>distributed under the License is distributed on an "AS IS" BASIS,
>WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
>See the License for the specific language governing permissions and
>limitations under the License.

