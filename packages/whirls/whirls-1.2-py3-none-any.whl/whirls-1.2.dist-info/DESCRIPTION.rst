.. image:: http://i.imgur.com/AWQmNsd.png

A fullscreen program that displays an animated, twisting tessellation of whirls. Click to show or hide a panel of sliders to adjust the whirls. Press Esc to exit.

Links
-----

- `Releases <https://pypi.python.org/pypi/whirls>`_
- `Source <https://bitbucket.org/David_Nickerson/whirls>`_
- `API Reference (Recommended) <https://pythonhosted.org/whirls/#id1>`_
- `API Reference (Alternate) <https://whirls.readthedocs.io/#id1>`_

What is a Whirl?
----------------

Begin with an arbitrary polygon. Construct a nested polygon by joining points that are a fractional distance along each edge. Repeat this process ad infinitum.

The vertices of the whirl form a logarithmic spiral, and they approximate a pursuit curve. The center of the spiral is the centroid of the polygon.

If the constructed polygon's vertices lie on midpoints of the base polygon, then it's called a midpoint polygon. If the constructed polygon has an even number of sides, then it's called a derived polygon.

Dependencies
------------

This program was developed against:

- Python 3.5
- NumPy 1.10
- SciPy 0.17
- Matplotlib 1.5
- Pygame 1.9
- PGU 0.18

Older versions may or may not work.

Installation
------------

These are minimal instructions to install and run this program on Windows 64 bit, including all dependencies. These instructions will not interfere with any other installed versions of Python and do not affect your PATH environment variable.

#. Download `WinPython-64bit-3.5.1.3.exe <http://winpython.github.io/>`_ and install to **C:\\py\\WinPython-64bit-3.5.1.3**
#. Download `pygame-1.9.2a0-cp35-none-win_amd64.whl <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame>`_ and `pgu-0.18.zip <https://code.google.com/archive/p/pgu/downloads>`_.
#. Open Command Prompt and run the following::

    C:\py\WinPython-64bit-3.5.1.3\python-3.5.1.amd64\python -m pip install C:\Users\<user>\Downloads\pygame-1.9.2a0-cp35-none-win_amd64.whl
    C:\py\WinPython-64bit-3.5.1.3\python-3.5.1.amd64\python -m pip install C:\Users\<user>\Downloads\pgu-0.18.zip
    C:\py\WinPython-64bit-3.5.1.3\python-3.5.1.amd64\python -m pip install whirls
    C:\py\WinPython-64bit-3.5.1.3\python-3.5.1.amd64\python -m whirls

Troubleshooting
---------------

DLL load failed
^^^^^^^^^^^^^^^

::

    ImportError: DLL load failed: The specified module could not be found.

If you installed Pygame for Python 3.5 from the link provided, then you need to install the `Microsoft Visual C++ 2015 Redistributable <https://www.visualstudio.com/downloads/download-visual-studio-vs#d-visual-c>`_.

SyntaxError
^^^^^^^^^^^

If you get an error like this::

      File "C:\py\WinPython-32bit-3.5.1.3\python-3.5.1\lib\site-packages\pgu\gui\container.py", line 57
        except StyleError,e:
                         ^
    SyntaxError: invalid syntax

Then change that line to read::

    except StyleError as e:

That file does not belong to this project.

