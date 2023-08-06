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

-------
Example
-------
In this section, an example is given with many flags. If some flags are not clear, these can be looked up in the Arguments section of this document.

.. code-block:: text

   isa nodes.ini --out results.csv -f -p collectl -t 5 -i 10 --interlogin 3 --max-nodes 2

This snippet reads the `nodes.ini` file for node configuration. Results are written to `results.csv` and since it ends on `.csv`, the output type is automatically set to `csv`. The `-f` flag makes sure to force the recreation of the output file even if the file already exists. The `collectl` plugin is used for gathering node information. The timeout is set to 5 seconds (`-t 5`), so nodes try to login for at most 5 seconds. The interval time is set to 10 seconds (`-i 10`), which makes sure that information is gathered every 10 seconds. The interlogin time is set to 3 seconds, so between consecutive logins of groups of 2 nodes (specified by `--max-nodes 2`) the script will wait 3 seconds (`--interlogin 3`). Notice that a mixture of shortcut arguments and normal arguments is used. It is up to you what you prefer.

---------
Debugging
---------
If there is not enough information visible, you can add the `-v` flag for seeing `INFO` logs (this is also the default if no `-v` or `-vv` flag is present). If this is still not enough, you can use the `-vv` flag (which stands for Very Verbose) to see `DEBUG` logs and `INFO` logs. This is illustrated by the following example:

.. code-block:: text

   isa nodes.ini --vv


---------
Arguments
---------

````````````````````````````
output (-o, --out, --output)
````````````````````````````
.. code-block:: text

   isa nodes.ini --output results.csv
   isa nodes.ini -o results.csv

Optional argument, this specifies where the results will be stored. In this version of ISA, only files ending on `.csv` are allowed.

```````````````````````````````
output_type (-x, --output-type)
```````````````````````````````
.. code-block:: text

   isa nodes.ini --out output.csv --output-type csv

Optional argument, default `standard_output`, `csv` if `--out` ends on `.csv`. When this is set to `csv`, a CSV file will be filled with the output where the path is specified by the `--output` argument. When this is set to `standard_output`, all results are written to the standard output (this is useful for testing).

```````````````````
force (-f, --force)
```````````````````
.. code-block:: text

   isa nodes.ini --out output.csv --force

Optional argument. If this flag is present and if the file specified by the `--output` flag already exists, then this file will be removed and recreated.

```````````````````````````
max-nodes (-m, --max-nodes)
```````````````````````````
.. code-block:: text

   isa nodes.ini --interlogin 1 --max-nodes 5

Optional argument, in combination with `interlogin`. Specifies how many nodes can login simultaneously. After this number of nodes are logging in, the script pauses for `interlogin` amount of time before it logs in the next group of nodes (with a maximum of `max-nodes` again).

```````````````````````
plugins (-p, --plugins)
```````````````````````
.. code-block:: text

   isa nodes.ini --plugins iostat,myplugin

Optional argument, a comma separated list (without spaces) of plugins to use for monitoring the cluster.


```````````````````````
timeout (-t, --timeout)
```````````````````````
.. code-block:: text

   isa nodes.ini --timeout 10

Optional argument, this specifies the maximum amount of time (in seconds) in which the script tries to connect to a SSH server.


`````````````````````````
interval (-i, --interval)
`````````````````````````
.. code-block:: text

   isa nodes.ini --interval 5

Optional argument, this specifies the amount of time (in seconds) in which the script collects and processes the statistics on the servers. The shorter the time, the less accurate the statistics, the longer the time, the longer one has to wait on the statistics.

`````````````````````````````
interlogin (-l, --interlogin)
`````````````````````````````
.. code-block:: text

   isa nodes.ini --interlogin 1

Optional argument. Specify the time needed between two consecutive logins. If this is too small, then a server can deny a connection and errors will appear which are hard to debug. This is very useful if all connections go through one `via` node.

```````````````````````````
max-nodes (-m, --max-nodes)
```````````````````````````
.. code-block:: text

   isa nodes.ini --interlogin 1 --max-nodes 5

Optional argument, in combination with `interlogin`. Specifies how many nodes can login simultaneously. After this number of nodes are logging in, the script pauses for `interlogin` amount of time before it logs in the next group of nodes (with a maximum of `max-nodes` again).

`````````````````````````````````
skip-install (-s, --skip-install)
`````````````````````````````````
.. code-block:: text

   isa nodes.ini --skip-install

Optional argument. When set, installation of the packages is skipped and can save some amount of time.

`````````````````
verbose (-v, -vv)
`````````````````

.. code-block:: text

   isa nodes.ini -vv

Optional argument, sets the log level. For `-v` or when this is not set at all, the log level is set to `INFO`. This shows you the basic information that is available. If the `-vv` flag is set, then then log level is set to `DEBUG`. Not only `INFO` messages are shown, but also more detailed information is given.