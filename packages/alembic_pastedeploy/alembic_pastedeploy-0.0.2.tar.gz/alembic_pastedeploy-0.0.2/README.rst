alembic-pastedeploy
===================

This is a thin-wrapper of alembic which allows alembic to read pastedeploy-flavored ini config files.


Supported features
------------------

- Importing defaults by ``get`` and ``set`` directive::

    [alembic]
    get sqlalchemy.url = sqlalchemy.url

- Giving global-conf interpolants by ``--paste-global`` option from the commandline::

  $ alembic_pastedeploy --paste-global sqlalchemy.url=sqlite:///test.db upgrade head

