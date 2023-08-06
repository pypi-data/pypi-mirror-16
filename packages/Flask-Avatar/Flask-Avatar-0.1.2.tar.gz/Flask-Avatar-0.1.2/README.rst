    :Author: jianglin

.. contents::

1 flask-avatar
--------------

`.. image:: //img.shields.io/badge/pypi-v0.1.2-brightgreen.svg
 <https://pypi.python.org/pypi/Flask-Avatar>`_
`.. image:: //img.shields.io/badge/python-3.4-brightgreen.svg
 <https://pypi.python.org/pypi/Flask-Avatar>`_

1.1 Example
~~~~~~~~~~~

.. image:: //raw.githubusercontent.com/honmaple/flask-avatar/master/example/avatar1.png

.. image:: //raw.githubusercontent.com/honmaple/flask-avatar/master/example/avatar2.png

.. image:: //raw.githubusercontent.com/honmaple/flask-avatar/master/example/avatar3.png

1.2 Installation
~~~~~~~~~~~~~~~~

To install Flask-Avatar:

.. code-block:: shell
    :number-lines: 0

    pip install flask-avatar

Or alternatively, you can download the repository and install manually by doing:

.. code-block:: sehll
    :number-lines: 0

    git clone git@github.com:honmaple/flask-avatar.git
    cd flask-avatar
    python setup.py install

1.3 Usage
~~~~~~~~~

.. code-block:: python
    :number-lines: 0

    from flask_avatar import Avatar
    [...]
    Avatar(app)

Templates:

.. code-block:: html
    :number-lines: 0

    {{ url_for('avatar',text = user.username )}}

or set **width** with:

.. code-block:: html
    :number-lines: 0

    {{ url_for('avatar',text = user.username,width=60)}}

1.4 Config
~~~~~~~~~~

AVATAR\ :sub:`URL`\ = '/avatar' #The avatar url,default '/avatar/<text>/<width>'
AVATAR\ :sub:`RANGE`\ = [0,512] #set avatar range to allow generate,if disallow,abort(404).Default [0,512]

1.5 Thanks to
~~~~~~~~~~~~~

``https://github.com/maethor/avatar-generator <https://github.com/maethor/avatar-generator>`_ <https://github.com/maethor/avatar-generator>`_
