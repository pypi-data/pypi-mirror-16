===
ISA
===

This is the documentation of **ISA** (Independent Statistics Aggregator). Independent means that the measurements are made independent of each other. The measurement on one machine does barely influence the measurement on another machine. Statistical Aggregator means that it is capable of collecting statistics of multiple nodes.

Why ISA?
========
Compared to other modern monitoring packages, ISA is easy to setup. You do not even have to setup software on the nodes which will be monitored!

Features
========
In the next list, the features of ISA are summed up.
- Measuring resource usage on a node or on a cluster of nodes
- Easy to setup
- Flexible configuration
- Low interference with the application
- Easy to start, pause and stop ISA

Comming up
==========
These features are not implemented yet, but are of big concern in future releases of ISA.
- Scalability
- Maintain logs

Short introduction
==================
Servers are specified in an INI file. The servers are monitored using plugins which execute code on each of the servers. When statistics are collected, they are written out to an output file.

Contents
========

.. toctree::
   :maxdepth: 2

   Installation <install>
   Usage <usage>
   INI file <ini>
   Plugins <plugins>
   License <license>
   Authors <authors>
   Changelog <changes>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
