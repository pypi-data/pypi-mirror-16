.. _installation:

Installing Glue
===============

.. note:: If you are interested in installing the experimental 3D viewers, see
          the :ref:`experimental_3d` page after following the instructions
          below.

There are several ways to install Glue on your computer:

Recommended: Anaconda Python Distribution
-----------------------------------------

**Platforms:** MacOS X, Linux, and Windows

We recommend using the `Anaconda <http://continuum.io/downloads.html>`_ Python
distribution from Continuum Analytics (or the related Miniconda distribution).
Anaconda includes all of Glue's main dependencies. There are two ways of
installing Glue with the Anaconda Python Distribution: graphically using the
Anaconda Launcher, or using the command-line, both of which are described below.

Graphical installation
^^^^^^^^^^^^^^^^^^^^^^

Once you have installed the Anaconda Python Distribution, open the Anaconda Launcher, and you will be presented with a window that looks like the following:

.. image:: images/anaconda_launcher.jpg
   :align: center
   :width: 100%

As you can see, glue is already in the list (under the name **glueviz**).
However, we need to tell Anaconda to get the latest version of glue from the
**conda-forge** channel (the default version available is otherwise not the
most recent). To do this, click on **Manage Channels** in the top right of the
window, which will bring up a small window - type **conda-forge** into the
field and click on **Add Channel**, then **Submit**:

.. image:: images/manage_conda_channels.jpg
   :align: center
   :width: 50%
   
Once you have done this, you can install glue by clicking on the **Install** button corresponding to the **glueviz** entry. If you have already installed glue, and want to update, you can click on the **Update** button.

Command-line installation
^^^^^^^^^^^^^^^^^^^^^^^^^

To install or update glue on the command-line, simply do::

    conda install -c conda-forge glueviz

.. note:: There is currently a known issue when running Anaconda's Qt on
          certain Linux distributions (including Kubuntu). See
          `Issue with PyQt4 from conda`_ for more details.
           
Enthought Canopy
----------------

**Platforms:** MacOS X, Linux, and Windows

The `Enthought Python Distribution <https://www.enthought.com/products/epd/>`_ includes most but not all
non-trivial dependencies.

You can install Glue using::

    pip install glueviz

You can then install any additional (optional) Glue dependencies by running::

    glue-deps install

on the command line. For more information on ``glue-deps``, see :ref:`below <glue-deps>`

Standalone Application
----------------------

**Platforms:** MacOS X

Mac users with OS X >= 10.7 can download Glue as a `standalone program
<http://mac.glueviz.org>`_. This is the fastest way to get started with using Glue, but this application includes its own version of Python, and will not recognize any packages in other Python installations. If you want to use glue in your existing Python installation, follow instructions in the other sections.

Building from Source (For the Brave)
------------------------------------

**Platforms:** MacOS X, Linux, and Windows

The source code for Glue is available on `GitHub
<http://www.github.com/glue-viz/glue>`_. Glue relies upon a number of
scientific python libraries, as well as the Qt GUI library. Installing
these packages is somewhat beyond the scope of this document, and
unforunately trickier than it should be. If you want to dive in, here
is the basic strategy:

 * Install `Qt 4 <http://download.qt.io/archive/qt/4.8/4.8.6/>`_ and either `PyQt4 <http://www.riverbankcomputing.com/software/pyqt/download>`_ or `PySide <http://qt-project.org/wiki/Get-PySide>`_. If at all possible, use the binary installers; building PyQt4 or PySide from source is tricky (this is a euphemism).

 * Install Glue using pip: ``pip install glueviz``. Alternatively, ``git clone`` the repository and install via ``python setup.py install``

 * Install Glue's remaining dependencies by running ``glue-deps install``. For more information on these dependencies see :ref:`below <glue-deps>`.


Dependencies
^^^^^^^^^^^^
.. _glue-deps:

Glue has the following required dependencies:

* Python 2.7, or 3.3 and higher
* `Numpy <http://www.numpy.org>`_
* `Matplotlib <http://www.matplotlib.org>`_
* `Pandas <http://pandas.pydata.org/>`_
* Either `PyQt4`_ or `PySide`_ (or `PyQt5 <https://riverbankcomputing.com/software/pyqt/download5>`_, but support is still
  experimental)

And the following optional dependencies are also highly recommended:

* `SciPy <http://www.scipy.org>`_
* `Astropy <http://www.astropy.org>`_ 0.4 or later
* `h5py <http://www.h5py.org>`_ (if using HDF5 files)

In addition to these, there are several other optional dependencies to suport
various I/O and other optional functionality. Glue includes a command line
utility ``glue-deps`` to manage dependencies:

* Calling ``glue-deps list`` displays all of Glue's required and optional
  dependencies, along with whether or not each library is already installed on
  your system. For missing dependencies, the program also provides a brief
  description of how it is used within Glue.

* Calling ``glue-deps install`` attempts to ``pip install`` all missing
  libraries. You can install single libraries or categories of libraries by
  providing additional arguments to ``glue-deps install``.

Tips for Ubuntu
^^^^^^^^^^^^^^^

Many dependencies can be reliably installed with ``apt``::

    sudo apt-get install python-numpy
    sudo apt-get install python-scipy
    sudo apt-get install python-matplotlib
    sudo apt-get install python-qt4
    sudo apt-get install pyqt4-dev-tools
    sudo apt-get install ipython
    sudo apt-get install python-zmq
    sudo apt-get install python-pygments


MacPorts
^^^^^^^^
Many dependencies can be reliably installed with::

    sudo port install python27
    sudo port install py27-numpy
    sudo port install py27-scipy
    sudo port install py27-matplotlib
    sudo port install py27-pyqt4
    sudo port install py27-ipython
    sudo port install py27-pip

For information about using MacPorts to manage your Python
installation, see `here
<http://astrofrog.github.com/macports-python/>`__

Running Glue
------------

Installing glue from source will create a executable ``glue`` script
that should be in your path. Running ``glue`` from the command line will
start the program. Glue accepts a variety of command-line
arguments. See ``glue --help`` for examples.

.. note:: On Windows, installation creates an executable ``glue.exe`` file
          within the python script directory (e.g., ``C:\Python27\Scripts``).
          Windows users can create a desktop shortcut for this file, and run
          Glue by double clicking on the icon.

Known issues
------------

Issue with PyQt4 from conda
^^^^^^^^^^^^^^^^^^^^^^^^^^^

On certain Linux installations, when using Anaconda/conda to manage the Python
installation you are using for glue, you may run into the following error when
launching glue::

    ImportError: /usr/lib/libkdecore.so.5: undefined symbol: _ZNK7QSslKey9algorithmEv

This is due to a known issue with Anaconda where the system installation of Qt
is used instead of the version shipped with Anaconda (see `this issue
<https://github.com/glue-viz/glue/issues/562>`_ if you are interested in a
discussion of the issue). A simple workaround is to force glue to use PySide
insead of PyQt4::

    conda install pyside
    export QT_API=pyside

after which glue will use PySide when started.