Rustbone
========

What is this?
-------------

Rustbone is an example Embedded Linux system built using Yocto that
provides nice facilities for working with and testing Rust in the
context of an embedded Linux Image.

How do I build and deploy an image
----------------------------------

For convenience, a basic set of configuration is included that is
"ready to build" out of the box.  You may need to create your own
build directory if your changes are significant.

### Clone the repo

The following commands will clone this repo and the subrepositories on
which this repository depends:

```
$ git clone git://github.com/posborne/rustbone.git
$ cd rustbone
$ git submodule update --init
```

### Install Dependencies and Other Setup

There's a few depeendencies that must be satisfied in order to build
any Yocto project.  These instructions assume you are running Ubuntu
14.04 or similar.  See the Yocto project documentation for more
details on how to get going on your platform.

```
$ sudo apt-get install gawk wget git-core diffstat unzip texinfo \
    gcc-multilib build-essential chrpath socat libdsl1.2-dev xterm\
```

The built-in local.conf also assumes a shared build directory and
sstate-cache at a fixed location.  You will need to create those in
order for the build to work without modification.

```
$ sudo mkdir -p /export/var/yocto/downloads /export/var/yocto/sstate-cache
$ sudo chown <user> -R /export/var/yocto
```

### Build It

Before building, you will need to activate the build environment.
Doing that any building may be done as follows:

```
$ source poky/oe-init-build-env build
$ bitbake rustbone-image-basic
```

Deploy It
---------

Deploying to an SD card is currently supported.  You must first
partition the device into two partitions as documented on this page:
https://www.yoctoproject.org/downloads/bsps/daisy16/beaglebone.

After partitioning, you should have something similar to the following
set up:

```
$ lsblk /dev/sdc
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sdc      8:32   1   7.3G  0 disk
├─sdc1   8:33   1    40M  0 part /media/posborne/BOOT
└─sdc2   8:34   1   7.3G  0 part /media/posborne/ROOT
```

Note that on my machine, the mount points for the BOOT and ROOT
volumes are /media/posborne/{BOOT,ROOT}.

There are a few steps to get the necessary pieces from the Yocto build
environment and onto the SD card.  Those have been automated with the
deploy-sd.py script.  You can deploy to the SD card after building by
doing the following:

```
$ sudo ./deploy-sd.py /path/to/BOOT /path/to/ROOT
```

With that done, throw the SD card into your beaglebone and give it a
whirl!  You may need to blow away the first bit of data on the
internal eMMC to force the device to boot from the SD Card.  More
information on that is available here:
https://www.yoctoproject.org/downloads/bsps/daisy16/beaglebone

Contributing
------------

Bug reports on Github and Pull Requests are both very welcome!

License
-------

All content in this repository is licensed under the terms of the MIT
License unless otherwise specified.  Copyright (c) 2015, Paul Osborne.
See the LICENSE file in the root of the repository for additional
details.
