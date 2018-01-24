|build_travis| |build_appveyor| |hunter| |license|

.. |license| image:: https://img.shields.io/github/license/ruslo/sugar.svg
  :target: https://github.com/ruslo/sugar/blob/master/LICENSE
  :alt: LICENSE

.. |build_travis| image:: https://travis-ci.org/ruslo/sugar.svg?branch=master
  :target: https://travis-ci.org/ruslo/sugar/builds
  :alt: Travis

.. |hunter| image:: https://img.shields.io/badge/hunter-sugar-blue.svg
  :target: https://docs.hunter.sh/en/latest/packages/pkg/sugar.html
  :alt: Hunter

Usage
-----

.. code-block:: cmake

  hunter_add_package(sugar)
  find_package(sugar CONFIG REQUIRED)

  sugar_include(boo)


Features
--------

* `Collecting sources <https://github.com/ruslo/sugar/wiki/Collecting-sources>`__

Old features
------------

These features **may** work, will be substituted with better
implementation in future:

* `Generating groups <https://github.com/ruslo/sugar/wiki/Generating-groups>`__
  (TODO: check `source_group(TREE ...) <https://cmake.org/cmake/help/v3.10/command/source_group.html>`__)
* ~~Build universal iOS library~~
  `CMAKE_IOS_INSTALL_COMBINED <https://cmake.org/cmake/help/v3.5/variable/CMAKE_IOS_INSTALL_COMBINED.html>`__
  available since CMake 3.5
* ~~Run gtest on iOS simulator~~ Check `gauze <https://github.com/hunter-packages/gauze>`__
* `Cross-platform warning suppression <https://github.com/ruslo/sugar/wiki/Cross-platform-warning-suppression>`__
