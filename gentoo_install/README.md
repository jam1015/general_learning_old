# Gentoo Install Notes

## Crypt benchmark
The minimal gentoo install CD doesn't have `cryptsetup` so on an existing installation or on a different livecd (Arch for example) we go

```
cryptsetup benchmark
```

and noet the keysize and algorithm that gives the fastes encryption and decryption times..


## Installation Media
[Followed the instructions from the Gentoo guide](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Media)

## Connecting To Network
[Followed the instructions from the Gentoo guide](https://wiki.gentoo.org/wikiiHandbook:AMD64/Installation/Networking)

## Preparing the Disks
The idea here is to do an install with `LUKS` incryption, `LVM`, and swap space on the LVM.

To do this I have combined advice from these sources:

- [official install guide](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks)
- [advice to make boot partition larger than the official install guide](https://forums.gentoo.org/viewtopic-t-1123855.html)
- [independent install guide with LVM and encryption](https://github.com/sergibarroso/gentoo_install)
- [this guide for adding swap space to LVM](https://www.2daygeek.com/how-to-create-extend-swap-partition-in-linux-using-lvm/)
- [this Arch linux install guide was also a neat reference](https://www.learnlinux.tv/arch-linux-full-installation-guide/)


start fdisk

```
fdisk /dev/sda
```

type `d` and `p` until all existing partitions are scheduled for deletion.

then:

```
Command (m for help): n
Partition number (1-128, default 1): 1
First sector (2048-60549086, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-60549086, default 60549086): +512
 
Created a new partition 1 of type 'Linux filesystem' and of size 512 MiB.
```

then `t` and `L` and the number of an `EFI` system.


Then the same procedure, designating the rest for `LVM` (find the right code when we press `L`).


## Prepare encrypted container

we make an encrupted container

```
cryptsetup -v --cipher aes-xts-plain64 --key-size 256 -y luksFormat /dev/sda2 
```

this is based on the results of the crypt benchmark for the first session.
