Placebo |build|_
================

Placebo is a utility that help implenting mock api responses in a reusable and composable way.

(WORK IN PROGRESS)

Sample mock:
::

   class UsersResponse(BaseMock):
       url = 'http://www.acme.com/api/v1/users/'
       body = json.dumps([{'name': 'Huseyin',
                           'last_name': 'Yilmaz'}])

And usage of the mock will be like this:

::

   @Response.decorate
   def users_api_test(self):
       ...


You can decorate any function or method with this decorator. Even django views:

::

   @Response.decorate
   def users_list_view(request):
       ...


Details
=======

When a decorator is applied, I will be using httppretty or httmock libraries to mock
given endpoint from the socket or requests library layer. So I am thinking about creating a
backend structure that can be attach to the library. So I will be able switch between different
mocking library backends.

Bad side of this is I will need to create a generic structure and convert specific backend requests to generic PlaceboRequest backend.

Backends:
---------
I am thinking about creating 2 backends for now httpretty and httmock. In my expericence, httmock is a lot better choice for some usecases because httpretty cannot be applied on runtime. It must be applied on initialization. (This is not an issue for 90% of use cases.).

LastRequests:
-------------
To test request data, I will need to catch requests and provide some kind interface so request can be inspected on tests. interface for this can be a function on main module like placebo.get_last_reqest()

Debug mode:
-----------
This abstraction is good. But when urls needs to be updated it becomes really hard to debug those kind of interfaces. So there should be a debug mod that prints out all decision to console.

Regexp URL's
------------
There should be a way to define urls with some kind of regexp. For some cases, we might want to be able to mock whole sub directories.

https://github.com/gabrielfalcao/HTTPretty/blob/a77921aaa2d0a249ac20a789f03c869e4f5ed22e/tests/functional/test_httplib2.py#L299

https://github.com/patrys/httmock/blob/master/tests.py#L161

.. |build| image:: https://travis-ci.org/huseyinyilmaz/placebo.svg?branch=master
.. _build: https://travis-ci.org/huseyinyilmaz/placebo
