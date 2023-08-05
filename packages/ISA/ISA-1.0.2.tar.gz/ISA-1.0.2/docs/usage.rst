.. _usage:

=====
Usage
=====

You can call ISA using the following code:

.. code-block:: text

   isa /path/to/nodes.ini

Where `path/to/nodes.ini` is an INI file specifying the nodes that should be monitored. The structure of the INI file is explained in the :doc:`ini` chapter.

There are more arguments which can be specified. These are explained in this document. In the next example, a call with many arguments is shown and explained.

.. code-block:: text

   isa nodes.ini --out results.csv --timeout 3 --interval 1

In this example, `nodes.ini` is parsed for the node information. It tries to connect to all the specified servers with a maximum of 3 seconds. When the script is connected to all the nodes, it collects data every 1 second and writes the statistics to `results.csv`.

---------
Arguments
---------

``````
output
``````
.. code-block:: text

   isa nodes.ini --output results.csv
   isa nodes.ini -o results.csv

Optional argument, this specifies where the results will be stored. In this version of ISA, only files ending on `.csv` are allowed.

```````
plugins
```````
.. code-block:: text

   isa nodes.ini --plugins iostat,myplugin

Optional argument, a comma separated list (without spaces) of plugins to use for monitoring the cluster.


```````
timeout
```````
.. code-block:: text

   isa nodes.ini --timeout 10

Optional argument, this specifies the maximum amount of time (in seconds) in which the script tries to connect to a SSH server.


````````
interval
````````
.. code-block:: text

   isa nodes.ini --interval 5

Optional argument, this specifies the amount of time (in seconds) in which the script collects and processes the statistics on the servers. The shorter the time, the less accurate the statistics, the longer the time, the longer one has to wait on the statistics.

