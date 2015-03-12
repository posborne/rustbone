# Copyright (c) 2015, Paul Osborne
#
# MIT License

inherit cargo

SRC_URI = "git://github.com/posborne/rust-pstree.git"
SRCREV = "99b4bdd59629c238ac5a5ccedb1a5b094471aec2"
LIC_FILES_CHKSUM = "file://LICENSE;md5=6c9a18574bd77a5e2ee80204ba249a90"

SUMMARY = "pstree implemented in rust"
HOMEPAGE = "https://github.com/posborne/rust-pstree"
LICENSE = "MIT"

S = "${WORKDIR}/git"
