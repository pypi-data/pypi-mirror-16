Config
======

``/etc/bs/bs.conf``::

    [node_maker]
    nodes_dir = /home
    cache_dir = /tmp/cache
    range_ports = 5000,5500
    supervisor_conf_dir = /etc/supervisor/conf.d/


Simple example a file ``/etc/bs/ports.conf``::

    [default]
    node123 = 2222
    node135 = 2223


Tests
=====

::

    ./run_tests

