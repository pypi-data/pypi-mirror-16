.. _plugins:

=======
Plugins
=======

There are a lot of measurement tools for specific servers. Therefore, ISA has a plugin structure so that it is easy to add new monitors. You can call ISA with specifying plugins in the `--plugins` argument which is a comma separated list of plugins that will be used. Below you will find an example of in which multiple plugins are loaded. Note that there are no spaces in the list of plugins.

.. code-block:: text

   isa nodes.ini --plugins iostat,free

------------------------
List of build-in plugins
------------------------
``````
iostat
``````
A plugin which collects information (I/O) from the server. `iostat` must be installed on the node.

````
free
````
A module which uses the information from `free -m`. This `free` application must be available on the machine.

````````
collectl
````````
A module which uses the information from `collectl`. The `collectl` application must be available on the machine.

-----------------
Creating a plugin
-----------------
A plugin file is named as follows: `plugin_pluginname.py`. Then, you can call ISA with a list of plugins and you can add `pluginname` to the comma separated list of the plugins argument of ISA.
It is very easy to create a new plugin. The plugin script should have the following structure:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin(...)

   class MyPlugin(Plugin):
      def install(self, server):
         server.execute(...)
      def collect(self, server):
         server.execute(...)

You see a `collect` method and a `install` method. The install method is called once after logging in to all the servers and its aim is to install software when it is not installed yet on the server. The `collect` method is used for collecting statistics on the server. The `install` method is not required! If you use the `install` method for installing a package, you can use the `install_package` method from the `Plugin` class. This is demonstrated in the next example:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin(...)

   class MyPlugin(Plugin):
      def install(self, server):
         self.install_package(server, 'sysstat')
      def collect(self, server):
         server.execute(...)

This example tries to install `sysstat` using different package managers (like `yum` and `apt-get`).

It is also possible to leave out the install method as is shown in the next example:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin(...)

   class MyPlugin(Plugin):
      def collect(self, server):
         server.execute(...)

The plugin is first initialized. You can use arguments from the original ISA call. For example, suppose ISA is called as follows:

.. code-block:: text

   isa nodes.ini --timeout 3

Then you can use `args.timeout` to refer to the `timeout` argument:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin(args.timeout)

   class MyPlugin(Plugin):
      def install(self, server):
         print("I assume my monitoring software is already installed on the server.")
   
      def __init__(self, timeout):
         print("I am called with timeout=%s" % timeout)

      def collect(self, server):
         server.execute(...)

The `collect` method should return either a list of dictionaries or a dictionary which specifies the collected data in key-value pairs:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin()

   class MyPlugin(Plugin):
      def install(self, server):
         pass
   
      def collect(self, server):
         return {
            'temperature': 25.0
         }

Or you can use a list:

.. code-block:: python

   def plugin_init(args):
      return MyPlugin()

   class MyPlugin(Plugin):
      def install(self, server):
         pass
   
      def collect(self, server):
         return [{
            'sensor': 'A',
            'temperature': 15.0
         }, {
            'sensor': 'B',
            'temperature': 35.0
         }]