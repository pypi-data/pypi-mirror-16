############
Installation
############

Installing the SDK
******************

Getting Started
===============
You will need the following

- GitHub
- Python 2.7 or 3.4+
- DataRobot account
- pip

Installing from a source distribution
*************************************

You should receieve a `.tar.gz` file that you will install from.
We recommend installing the DataRobot Python SDK using a virtual
environment to avoid having dependency conflicts with existing
packages on your system.

.. code-block:: shell

    pip install datarobot-2.0.32.tar.gz

.. note::
   If you are not running in a Python ``virtualenv``, you may need to run
   the above commands with ``sudo`` permissions.

Installing pyOpenSSL
====================
On versions of Python earlier than 2.7.9 you might have InsecurePlatformWarning_ in your output.
To prevent this without updating your Python version you should install pyOpenSSL_ package:

.. _pyOpenSSL: https://urllib3.readthedocs.org/en/latest/security.html#pyopenssl
.. _InsecurePlatformWarning: https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning

.. code-block:: shell

    pip install pyopenssl ndg-httpsclient pyasn1

Configure the SDK
*****************
Each authentication method will specify credentials for DataRobot, as well as
the location of the DataRobot deployment. We currently support configuration
of the SDK using a configuration file, by setting environment variables, or
within the code itself.

Credentials
===========
Each of the following methods supports using an authentication token or pair of
user name and password as login credentials.
However, for security reasons it is recommended that you use
token authentication.

.. note::

   When using token authentication, only the token needs to be provided.
   The user name and password are both unnecessary if the token is available
   in the configuration.

Use a Configuration File
========================
You can use a configuration file to specify the client setup.

The following is an example configuration file that should be saved as ``~/.datarobotrc``:

.. code-block:: aconf

    [datarobot]
    username = youruser@yourdomain.com
    password = yoursecret
    endpoint = https://app.datarobot.com/api/v2

or alternatively

.. code-block:: aconf

    [datarobot]
    token = yourtoken
    endpoint = https://app.datarobot.com/api/v2

.. note::

   The above endpoint should be adjusted to point to the installation
   of DataRobot available on your local network, if you have a local
   installation.

You can specify a different location for the DataRobot configuration file by setting
the ``DATAROBOT_CONFIG_FILE`` environment variable.

Set Credentials Explicitly in Code
==================================

Explicitly set credentials in code:

.. code-block:: python

   from datarobot import Client
   Client(username='your_username',
          password='your_password',
          endpoint='https://app.datarobot.com/api/v2')

As mentioned previously, you can also use an authentication token rather than
user name and password authentication:

.. code-block:: python

   from datarobot import Client
   Client(token='your_token', endpoint='https://app.datarobot.com/api/v2')


Set Credentials Using Environment Variables
===========================================

Set up an endpoint by setting environment variables in the UNIX shell:

.. code-block:: shell

   export DATAROBOT_ENDPOINT='https://app.datarobot.com/api/v2'

You can also set up your authentication in the shell:

.. code-block:: shell

   export DATAROBOT_USERNAME=your_username
   export DATAROBOT_PASSWORD=your_password

Or if you have a token:

.. code-block:: shell

   export DATAROBOT_API_TOKEN=your_token


Creating an Authentication Token
================================

You can use the following HTTP request method to create an authorization token:

``POST /v2/api_token/``


Include your user name and password in the request body as shown in the following example:

.. code-block:: text

    curl -X POST https://app.datarobot.com/api/v2/api_token/ \
    -H "Content-Type: application/json" \
    -d '{"username": "john.smith@acmedata.com","password": "js123@tyR"}'


The request response includes an authentication token:

.. code-block:: text

    {"api_token": "DnwzBUNTOtKBO6Sp1hoUByG4YgZwCCw4"}

After you have created an API token, it will be listed on the My Account page in the DataRobot UI.
