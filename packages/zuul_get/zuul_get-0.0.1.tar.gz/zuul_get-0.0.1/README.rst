========
zuul_get
========

Retrieves job URLs from OpenStack Zuul for a particular review number.

Installation
------------

The easiest method is to use pip:

.. code-block:: console

   pip install zuul_get


Running the script
------------------

Provide a six-digit gerrit review number as an argument to retrieve the CI job
URLs from Zuul's JSON status file:

.. code-block:: console

   $ python zuul_get.py 345997
   +-------------------------------------+---------+--------------------------------+
   | Jobs for 345997                     |         |                                |
   +-------------------------------------+---------+--------------------------------+
   | gate-openstack-ansible-releasenotes | SUCCESS | telnet://149.202.190.246:19885 |
   | gate-openstack-ansible-docs         | SUCCESS | telnet://172.99.106.146:19885  |
   | gate-openstack-ansible-linters      | None    | telnet://23.253.148.52:19885   |
   | gate-openstack-ansible-dsvm-commit  | None    | telnet://23.253.151.120:19885  |
   +-------------------------------------+---------+--------------------------------+

The script will throw an error if the review doesn't have an acttive CI job:

.. code-block:: console

   $ python zuul_get.py 345998
   Couldn't find any jobs for review 345998

Contributing
------------

Pull requests and GitHub issues are always welcome!
