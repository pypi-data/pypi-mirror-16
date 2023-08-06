XD-Docker
=========

Python library for accessing Docker Remote API.

XD-Docker aims at providing an easy to use and Pythonic API for working with
the Docker Remote API in Python.


Developer resources
-------------------

- Source code, issue tracking, website and wiki is hosted on [GitHub](https://github.com)
- [![Documentation Status](https://readthedocs.org/projects/xd-docker/badge/?version=latest)](http://xd-docker.readthedocs.org/en/latest/?badge=latest) - Documentation hosted by [Read the Docs](https://readthedocs.org/)
- [![Stories in Ready](https://img.shields.io/waffle/label/XD-embedded/xd-docker/ready.svg) ![Stories in Progress](https://img.shields.io/waffle/label/XD-embedded/xd-docker/in%20progress.svg)](https://waffle.io/XD-embedded/xd-docker) - Kanban board provided by [waffle.io](https://waffle.io/)
- [![Travis CI Status](https://travis-ci.org/XD-embedded/xd-docker.svg?branch=master)](https://travis-ci.org/XD-embedded/xd-docker) - Continous Integration is provided by [Travis CI](https://travis-ci.org)
- [![Coverage Status](https://coveralls.io/repos/XD-embedded/xd-docker/badge.svg?branch=master)](https://coveralls.io/r/XD-embedded/xd-docker?branch=master) - Code coverage analysis is provided by [Coveralls](https://coveralls.io)
- [![Codacy Status](https://api.codacy.com/project/badge/grade/02460502b6bd4c069bcb757fce9344bb)](https://www.codacy.com/app/esben_2844/xd-docker) - Static code analysis by [Codacy](http://codacy.com)


License
-------

XD-Docker is released under the MIT License (see [LICENSE](LICENSE) file).


Test suites
-----------

XD-Docker includes both a unit test suite and an integration test suite.

The goal of the unit test suite is to test each module, achieving 100% code
and branch coverage.

The goal of the integration test suite is to test against different docker
versions.

The recommended way to run the test suites, is to use the shell scripts
`unit-test.sh` and `integration-test.sh`.

These scripts take care of building docker images with the necessary tools and
software, and runs the test in docker containers.
