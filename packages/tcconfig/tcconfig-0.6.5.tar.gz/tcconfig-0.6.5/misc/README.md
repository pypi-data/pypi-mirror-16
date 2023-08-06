# Traffic control features
## Network
Traffic control can be specified network to apply to:

- Outgoing/Incoming packets
- Certain IP address/network and port

## Available parameters
The following parameters can be set to network interfaces.

- Network bandwidth rate [G/M/K bps]
- Network latency [milliseconds]
- Packet loss rate [%]
- Packet corruption rate [%]


# Installation
## Install via pip
`tcconfig` can be installed via [pip](https://pip.pypa.io/en/stable/installing/) (Python package manager).

```console
sudo pip install tcconfig
```


# Usage
## Set traffic control (`tcset` command)
`tcset` is a command to impose traffic control to a network interface (device).

### `tcset` help
```console
usage: tcset [-h] [--version] [--logging] [--stacktrace] [--debug | --quiet]
             (--device DEVICE | -f CONFIG_FILE) [--overwrite]
             [--direction {outgoing,incoming}] [--rate BANDWIDTH_RATE]
             [--delay NETWORK_LATENCY] [--delay-distro LATENCY_DISTRO_MS]
             [--loss PACKET_LOSS_RATE] [--corrupt CORRUPTION_RATE]
             [--network NETWORK] [--port PORT]

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --debug               for debug print.
  --quiet               suppress output of execution log message.
  --device DEVICE       network device name (e.g. eth0)
  -f CONFIG_FILE, --config-file CONFIG_FILE
                        setting traffic controls from configuration file.
                        output file of the tcshow.

Miscellaneous:
  --logging             output execution log to a file (tcset.log).
  --stacktrace          display stack trace when an error occurred.

Network Interface:
  --overwrite           overwrite existing settings

Traffic Control:
  --direction {outgoing,incoming}
                        direction of network communication that impose traffic
                        control. "incoming" requires linux kernel version
                        2.6.20 or later. (default=outgoing)
  --rate BANDWIDTH_RATE
                        network bandwidth rate [K|M|G bps]
  --delay NETWORK_LATENCY
                        round trip network delay [ms] (default=0)
  --delay-distro LATENCY_DISTRO_MS
                        distribution of network latency becomes X +- Y [ms]
                        (normal distribution), with this option. (X: value of
                        --delay option, Y: value of --delay-dist opion)
                        network latency distribution will uniform without this
                        option.
  --loss PACKET_LOSS_RATE
                        round trip packet loss rate [%] (default=0)
  --corrupt CORRUPTION_RATE
                        packet corruption rate [%]. packet corruption means
                        single bit error at a random offset in the packet.
                        (default=0)
  --network NETWORK     IP address/network of traffic control
  --port PORT           port number of traffic control
```

### Basic usage
Outgoing packet traffic control settings are as follows

#### e.g. Set a limit on bandwidth up to 100Kbps
```console
# tcset --device eth0 --rate 100k
```

#### e.g. Set 100ms network latency
```console
# tcset --device eth0 --delay 100
```

#### e.g. Set 0.1% packet loss
```console
# tcset --device eth0 --loss 0.1
```

#### e.g. All of the above at onece
```console
# tcset --device eth0 --rate 100k --delay 100 --loss 0.1
```

#### e.g. Specify the IP address of traffic control
```console
# tcset --device eth0 --delay 100 --network 192.168.0.10
```

#### e.g. Specify the IP network and port of traffic control
```console
# tcset --device eth0 --delay 100 --network 192.168.0.0/24 --port 80
```


### Advanced usage
#### Traffic control of incoming packets
Execute `tcset` command with `--direction incoming` option to set incoming traffic control.
Other options are the same as in the case of the basic usage.

##### e.g. Set traffic control both incoming and outgoing network
```console
tcset --device eth0 --direction outgoing --rate 200K --network 192.168.0.0/24
tcset --device eth0 --direction incoming --rate 1M --network 192.168.0.0/24
```

##### Requirements
Incoming packet traffic control requires additional ifb module, 
Which need to the following conditions:

- Equal or later than Linux kernel version 2.6.20
- Equal or later than iproute2 package version 20070313

#### e.g. Set 100ms +- 20ms network latency with normal distribution
```console
# tcset --device eth0 --delay 100 --delay-distro 20
```


## Delete traffic control (`tcdel` command)
`tcdel` is a command to delete traffic control from a network interface (device).

### `tcdel` help
```console
usage: tcdel [-h] [--version] [--logging] [--stacktrace] [--debug | --quiet]
             --device DEVICE

optional arguments:
  -h, --help       show this help message and exit
  --version        show program's version number and exit
  --debug          for debug print.
  --quiet          suppress output of execution log message.

Miscellaneous:
  --logging        output execution log to a file (tcdel.log).
  --stacktrace     display stack trace when an error occurred.

Traffic Control:
  --device DEVICE  network device name (e.g. eth0)
```

### e.g. Delete traffic control of eth0
```console
# tcdel --device eth0
```


## Display traffic control configurations (`tcshow` command)
`tcshow` is a command to display traffic control to network interface(s).

Note: scope of `tcshow` command is limited to parameters that can be set with tcset
(`tcshow` is not a general purpose tool to display all of the parameters of the tc command).

### `tcshow` help
```console
usage: tcshow [-h] [--version] [--logging] [--stacktrace] [--debug | --quiet]
              --device DEVICE

optional arguments:
  -h, --help       show this help message and exit
  --version        show program's version number and exit
  --debug          for debug print.
  --quiet          suppress output of execution log message.

Miscellaneous:
  --logging        output execution log to a file (tcshow.log).
  --stacktrace     display stack trace when an error occurred.

Traffic Control:
  --device DEVICE  network device name (e.g. eth0)
```

### Example
```console
# tcset --device eth0 --delay 10 --delay-distro 2  --loss 0.01 --rate 0.25M --network 192.168.0.10 --port 8080
# tcset --device eth0 --delay 1 --loss 0.02 --rate 500K --direction incoming
# tcshow --device eth0
{
    "eth0": {
        "outgoing": {
            "network=192.168.0.10/32, port=8080": {
                "delay": "10.0",
                "loss": "0.01",
                "rate": "250K",
                "delay-distro": "2.0"
            },
            "network=0.0.0.0/0": {}
        },
        "incoming": {
            "network=0.0.0.0/0": {
                "delay": "1.0",
                "loss": "0.02",
                "rate": "500K"
            }
        }
    }
}
```

## Backup and restore traffic control configurations
### Backup configurations
```console
# tcset --device eth0 --delay 10 --delay-distro 2  --loss 0.01 --rate 0.25M --network 192.168.0.10 --port 8080
# tcset --device eth0 --delay 1 --loss 0.02 --rate 500K --direction incoming
# tcset --device eth1 --delay 2.5 --delay-distro 1.2 --loss 0.01 --rate 0.25M --port 80
# tcset --device eth1 --corrupt 0.02 --rate 1.5M --direction incoming --network 192.168.10.0/24
```

```console
# tcshow --device eth0 --device eth1 > tcconfig.json
```

### Restore configurations
Before restore

```console
# tcshow --device eth0 --device eth1
{
    "eth1": {
        "outgoing": {},
        "incoming": {}
    },
    "eth0": {
        "outgoing": {},
        "incoming": {}
    }
}
```

Restore from a configuration file.

```console
# tcset -f tcconfig.json
```

After restore

```console
# tcshow --device eth0 --device eth1
{
    "eth1": {
        "outgoing": {
            "port=80": {
                "delay": "2.5",
                "loss": "0.01",
                "rate": "250K",
                "delay-distro": "1.2"
            },
            "network=0.0.0.0/0": {}
        },
        "incoming": {
            "network=192.168.10.0/24": {
                "corrupt": "0.02",
                "rate": "1500K"
            },
            "network=0.0.0.0/0": {}
        }
    },
    "eth0": {
        "outgoing": {
            "network=192.168.0.10/32, port=8080": {
                "delay": "10.0",
                "loss": "0.01",
                "rate": "250K",
                "delay-distro": "2.0"
            },
            "network=0.0.0.0/0": {}
        },
        "incoming": {
            "network=0.0.0.0/0": {
                "delay": "1.0",
                "loss": "0.02",
                "rate": "500K"
            }
        }
    }
}
```


# Dependencies
## Linux package
- iproute2 (reqrequired for tc commandured)

## Python packagge
Dependency python packages are automatically installed during `tcconfig` installation via pip.

- [DataPropery](https://github.com/thombashi/DataProperty)
- [ipaddress](https://pypi.python.org/pypi/ipaddress)
- [pyparsing](https://pyparsing.wikispaces.com/)
- [six](https://pypi.python.org/pypi/six/)
- [thutils](https://github.com/thombashi/thutils)

### Test dependencies
- [pingparsing](https://github.com/thombashi/pingparsing)
- [pytest](https://pypi.python.org/pypi/pytest)
- [pytest-runner](https://pypi.python.org/pypi/pytest-runner)
- [tox](https://pypi.python.org/pypi/tox)
