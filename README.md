# newrelic-synthetics-management
Python 2.7.14 script for enabling or disable one or more New Relic Synthetic checks.

required packages: requests, argparse

```
usage: checkManagement.py [-h] apikey {enable,disable} checkId [checkId ...]

Enable/Disable one or more New Relic Synthetic checks

positional arguments:
  apikey            New Relic Admin User API Key
  {enable,disable}  Enable or Disable Synthetic checks
  checkId           Whitespace seperated list of Synthetic Check ID's to act
                    upon (example: -c aab91f1a-75c4-49bd-b5c9-a78957bddc87
                    9878f17f-aa12-43a9-8510-6b9ca61ad465)

optional arguments:
  -h, --help        show this help message and exit
```
