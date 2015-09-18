#!/usr/bin/env python
#
# Deploy beaglebone artifacts to an SD Card
#

import argparse
import subprocess
import shutil
import os
import sys

THIS_DIR = os.path.dirname(__file__)
DEPLOY_DIR = os.path.join(THIS_DIR, "tmp/deploy/images/beaglebone")
MLO = os.path.join(DEPLOY_DIR, "MLO-beaglebone")
UBOOT = os.path.join(DEPLOY_DIR, "u-boot.img")
ZIMAGE = os.path.join(DEPLOY_DIR, "zImage-beaglebone.bin")
DTB = os.path.join(DEPLOY_DIR, "zImage-bbb-nh5cape.dtb")

# Files that must be moved to the boot volume
BOOT_MAPPING = [
    (MLO, "MLO"),
    (UBOOT, "u-boot.img"),
]

ROOT_MAPPING = [
    (ZIMAGE, "boot/zImage"),
    (DTB, "boot/am335x-boneblack.dtb"),
]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("bootmnt", help="The mountpoint of the boot volume")
    parser.add_argument("rootmnt", help="The mountpoint of the root volume")
    return parser.parse_args()

def install_boot(args):
    print "== Installing BOOT Partition Artifacts =="
    sys.stdout.write("Removing existing contents... ")
    sys.stdout.flush()
    for f in os.listdir(args.rootmnt):
        shutil.rmtree(args.rootmnt, ignore_errors=True)
    print "Done"
    for src, dstrelpath in BOOT_MAPPING:
        dst = os.path.join(args.bootmnt, dstrelpath)
        print "{} -> {}".format(src, dst)
        shutil.copy2(src, dst)


def install_root(args):
    print "== Install ROOT Partition Artifacts =="
    sys.stdout.write("Removing existing contents... ")
    sys.stdout.flush()
    for f in os.listdir(args.rootmnt):
        shutil.rmtree(args.rootmnt, ignore_errors=True)
    print "Done"
    sys.stdout.write("Extracting image to root partition")
    sys.stdout.flush()
    subprocess.check_call([
        "tar", "xjvf",
        os.path.join(DEPLOY_DIR, "rustbone-image-beaglebone.tar.bz2"),
        "-C", args.rootmnt,
    ])

    # Write additional files
    for src, dstrelpath in ROOT_MAPPING:
        dst = os.path.join(args.rootmnt, dstrelpath)
        print "{} -> {}".format(src, dst)
        shutil.copy2(src, dst)

    print "Done"


def sync():
    sys.stdout.write("Syncing writes to disk... ")
    sys.stdout.flush()
    subprocess.check_call("sync")
    subprocess.check_call("sync")
    print "Done"


def main():
    args = parse_arguments()
    install_boot(args)
    install_root(args)
    sync()

if __name__ == "__main__":
    main()
