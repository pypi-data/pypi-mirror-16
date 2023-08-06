Installing Wallace with Anaconda
================================

If you are interested in Wallace and use
`Anaconda <https://www.continuum.io/downloads>`__, you'll need to adapt
the standard instructions slightly.

Install psycopg2
----------------

In order to get the correct bindings, you need to install ``psycopg2``
before you use ``requirements.txt``; otherwise, everything will fail and
you will be endlessly frustrated.

::

    conda install psycopg2

Install Wallace
---------------

You'll follow all of the :doc:`Wallace development installation
instructions <developing_wallace_setup_guide>`,
**with the exception of the virtual environment step**.  Then return here.

Confirm Wallace works
---------------------

Now, we need to make sure that Wallace and Anaconda play nice with one
another. At this point, we'd check to make sure that Wallace is properly
installed by typing

::

    wallace --version

into the command line. For those of us with Anaconda, we'll get a long
error message. Don't panic! Add the following to your ``.bash_profile``:

::

    export DYLD_FALLBACK_LIBRARY_PATH=$HOME/anaconda/lib/:$DYLD_FALLBACK_LIBRARY_PATH

If you installed anaconda using ``Python 3``, you will need to change
``anaconda`` in that path to ``anaconda3``.

After you ``source`` your ``.bash_profile``, you can check your Wallace
version (using the same command that we used earlier), which should
return the Wallace version that you've installed.

Re-link Open SSL
----------------

Finally, you'll need to re-link ``openssl``. Run the following:

::

    brew install --upgrade openssl
    brew unlink openssl && brew link openssl --force
