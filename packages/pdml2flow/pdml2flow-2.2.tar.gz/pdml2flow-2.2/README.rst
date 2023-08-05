pdml2flow `|PyPI version| <https://badge.fury.io/py/pdml2flow>`_
================================================================

*Aggregates wireshark pdml to flows*

\| Branch \| Build \| Coverage \| \| ------- \| ------ \| -------- \| \|
master \| `|Build Status
master| <https://travis-ci.org/Enteee/pdml2flow>`_ \| `|Coverage Status
master| <https://coveralls.io/github/Enteee/pdml2flow?branch=master>`_
\| \| develop \| `|Build Status
develop| <https://travis-ci.org/Enteee/pdml2flow>`_ \| `|Coverage Status
develop| <https://coveralls.io/github/Enteee/pdml2flow?branch=develop>`_
\|

Prerequisites
-------------

-  `python <https://www.python.org/>`_:
-  3.4
-  3.5
-  3.5-dev
-  nightly
-  `pip <https://pypi.python.org/pypi/pip>`_

Installation
------------

::

        $ sudo pip install pdml2flow

Usage
-----

::

    $ pdml2flow -h
    usage: pdml2flow [-h] [-f FLOW_DEF_STR] [-t FLOW_BUFFER_TIME] [-l DATA_MAXLEN]
                     [-s] [-x] [-c] [-a] [-m] [-d]

    Aggregates wireshark pdml to flows

    optional arguments:
      -h, --help           show this help message and exit
      -f FLOW_DEF_STR      Fields which define the flow, nesting with: '.'
                           [default: ['vlan.id', 'ip.src', 'ip.dst', 'ipv6.src',
                           'ipv6.dst', 'udp.stream', 'tcp.stream']]
      -t FLOW_BUFFER_TIME  Lenght (in seconds) to buffer a flow before writing the
                           packets [default: 180]
      -l DATA_MAXLEN       Maximum lenght of data in tshark pdml-field [default:
                           200]
      -s                   Extract show names, every data leave will now look like
                           { raw : [] , show: [] } [default: False]
      -x                   Switch to xml output [default: False]
      -c                   Removes duplicate data when merging objects, will not
                           preserve order of leaves [default: False]
      -a                   Instaead of merging the frames will append them to an
                           array [default: False]
      -m                   Appends flow metadata [default: False]
      -d                   Debug mode [default: False]

Example
-------

Sniff from interface: ``shell $ tshark -i interface -Tpdml | pdml2flow``

Write xml output ``shell $ tshark -i interface -Tpdml | pdml2flow -x``

Read a .pcap file ``shell $ tshark -r pcap_file -Tpdml | pdml2flow``

Aggregate based on ethernet source and ethernet destination address
``shell $ tshark -i interface -Tpdml | pdml2flow -f eth.src -f eth.dst``

Pretty print flows using `jq <https://stedolan.github.io/jq/>`_
``shell $ tshark -i interface -Tpdml | pdml2flow | jq``

Post-process flows using
`FluentFlow <https://github.com/t-moe/FluentFlow>`_
``shell $ tshark -i interface -Tpdml | pdml2flow | fluentflow rules.js``

Utils
-----

The following utils are part of this project

pdml2json
~~~~~~~~~

*Converts pdml to json*

Usage
~~~~~

::

    $ pdml2json -h
    usage: pdml2json [-h] [-s] [-d]

    Converts wireshark pdml to json

    optional arguments:
      -h, --help  show this help message and exit
      -s          Extract show names, every data leave will now look like { raw :
                  [] , show: [] } [default: False]
      -d          Debug mode [default: False]

pdml2xml
~~~~~~~~

*Converts pdml to xml*

Usage
~~~~~

::

    $ pdml2xml -h
    usage: pdml2xml [-h] [-s] [-d]

    Converts wireshark pdml to xml

    optional arguments:
      -h, --help  show this help message and exit
      -s          Extract show names, every data leave will now look like { raw :
                  [] , show: [] } [default: False]
      -d          Debug mode [default: False]

.. |PyPI version| image:: https://badge.fury.io/py/pdml2flow.svg
.. |Build Status
master| image:: https://travis-ci.org/Enteee/pdml2flow.svg?branch=master
.. |Coverage Status
master| image:: https://coveralls.io/repos/github/Enteee/pdml2flow/badge.svg?branch=master
.. |Build Status
develop| image:: https://travis-ci.org/Enteee/pdml2flow.svg?branch=develop
.. |Coverage Status
develop| image:: https://coveralls.io/repos/github/Enteee/pdml2flow/badge.svg?branch=develop
