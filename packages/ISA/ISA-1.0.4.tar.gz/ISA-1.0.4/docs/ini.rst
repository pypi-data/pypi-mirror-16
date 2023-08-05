.. _ini:

========
INI file
========

---------------
Minimal example
---------------

.. code-block:: text

   [node1]
   host = 127.0.0.1
   enabled = False

   [node2]
   host = 127.0.0.2

In this simplified example, there are two nodes. One of the nodes (`node1`) is disabled and will not be monitored. By default, nodes are enabled, so `node2` will be monitored. Furthermore, the host (which can be either an hostname or IP address) of `node1` is `127.0.0.1` and the host of `node2` is `127.0.0.2`.
Looking at the structure of the example, each section corresponds to a unique node name and every section contains flags which can be set. Some flags are optional and other flags are required.

-----
Flags
-----

This section explains all flags that can be used within a node section.

````
host
````
Required flag. Specifies the hostname or IP address of a node.

````````
username
````````

Optional flag, default `root`. The username to use for an SSH connection to the specified host.

````````
password
````````

Optional flag, default `None`. The password to use for the specified username and the SSH connection to the specified host.

`````````````
identity_file
`````````````

Optional flag, default `None`. The identity file to use to set up an SSH connection to the specified host.

```````
enabled
```````
Optional flag, default `True`. Possible values are `True` and `False` where `True` means that the node will be monitored and `False` means that the node will not be monitored. This is useful for defining a `via` node which should not be included into the monitoring.

```
via
```
Optional flag, default `None`. This is useful for connecting to a node via another node. For example, look at the following configuration:

.. code-block:: text

   [node1]
   host = 127.0.0.1
   via = login

   [node2]
   host = 127.0.0.2
   via = login

   [login]
   host = 127.0.0.3

In this configuration, an SSH connection to node `node1` is made by connecting first to node `login`. Also for `node2` holds that any connection is made via node `login`. The code will check whether a circular definition exists and throws a `CircularException` exception if that is the case.