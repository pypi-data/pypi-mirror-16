PDKUtil
=============================================

Stores a pdk file to a barbican container.

Installation
------------

Pip is the preferred way to install PDKUtil: ::

    pip install pdkutil

Command-line interface
----------------------

PDKUtil uses Keystone for identity management. Credentials and endpoints can
be provided via environment variables or command line parameters in the same
way supported by most OpenStack command line interface (CLI) tools, e.g.: ::

    export OS_AUTH_URL=http://example.com:5000/v2.0
    export OS_USERNAME=admin
    export OS_PASSWORD=password
    export OS_TENANT_NAME=admin


Store a pdk file
----------------

This command stores the specified pdk file to a container, returning
container's reference: ::

    pdkutil store <filename> <container-name>

Get container's information
---------------------------

This command retrieves container's information (container's name,
secrets references, etc) by its specified reference: ::

    pdkutil get <container-reference>
