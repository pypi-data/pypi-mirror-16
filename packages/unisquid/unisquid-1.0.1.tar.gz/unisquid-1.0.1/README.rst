********
unisquid
********

Yet another unittest extension for python.

Live Server Test Case 
---------------------

The LiveServerTestCase extension does basically the same as
unittest.TestCase but also launches a live http server in a 
separate thread.

A comma-separated list of ports or a range of ports can be specified
in the hope the live server can find one that is free to use for the
WSGI server. The range may be of the form: '8000-8010,8080,9020-9300'
and will be read from the 'LIVE_TEST_SERVER_ADDRESS' environment variable.

The function create_app() is used to return the handler used by the WSGI server.

Example
-------

.. code-block:: python

    import unisquid
    import urllib
    import wsgiref


    class TestLiveServer(unisquid.LiveServerTestCase):
        def create_app(self):
            return wsgiref.simple_server.demo_app

        def test_server_process_listening(self):
            response = urllib.urlopen(self.live_server_url)
            self.assertTrue(b'Hello world!' in response.read())
            self.assertEqual(response.code, 200)
