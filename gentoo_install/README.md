# Gentoo Install Notes

## Crypt benchmark
The minimal gentoo install CD doesn't have `cryptsetup` so on an existing installation or on a different livecd (Arch for example) we go

```
cryptsetup benchmark
```

## set video parameters
we go:

```
videoinfo
set gfxmode=1920x1080 
terminal_output gfxterm
normal
```

but replace  the `1920x1080` with whatever is output as `optimal` by `videoinfo`


and noet the keysize and algorithm that gives the fastes encryption and decryption times..


## Installation Media
[Followed the instructions from the Gentoo guide](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Media)

```
root #passwd

New password: (Enter the new password)
Re-enter password: (Re-enter the password)
```

```

root #useradd -m -G users john
root #passwd john

New password: (Enter john's password)
Re-enter password: (Re-enter john's password)
```

## Connecting To Network
[Followed the instructions from the Gentoo guide](https://wiki.gentoo.org/wikiiHandbook:AMD64/Installation/Networking)

`ip addr` to show the network interfaces or `ifconfig`


```
net-setup wlp3s0
```

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

then `g`

then:

```
Command (m for help): n
Partition number (1-128, default 1): 1
First sector (2048-60549086, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-60549086, default 60549086): +512M
 
Created a new partition 1 of type 'Linux filesystem' and of size 512 MiB.
```

then `t` and `L` and the number of an `EFI` system.


Then the same procedure, designating the rest for `LVM` (find the right code when we press `L`), accept defaults for sector boundaries.


## Prepare encrypted container

we make an encrupted container

```
cryptsetup -v --cipher aes-xts-plain64 --key-size 256 -y luksFormat /dev/sda2 
```




see [the documentation on dm-crypt](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/DMCrypt) or
[the Gentoo Wiki article on dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt) or 
and [this step by sep guide on the gentoo wiki](https://wiki.gentoo.org/wiki/Dm-crypt_full_disk_encryption) for more details; I dont' completely understand myself.

this is based on the results of the crypt benchmark for the first section.


Then we go

```
cryptsetup open --type luks /dev/nvme0n1p2 cryptcontainer
pvcreate /dev/mapper/cryptcontainer
vgcreate vg00 /dev/mapper/cryptcontainer
```

here is where we diverge and add some swap space on the lvm:

```
lvcreate -C y -L 8.0G -n lv_swap vg00
```

this makes it contidgious. to undo at some time in the future go: 

```
lvchange --alloc inherit lv_swap
```

```
mkswap /dev/vg00/lv_swap
```

add to `/etc/fstab/` file:

```
/dev/mapper/vg00-lv_swap   swap     swap    defaults     0 0
```

then 

```
sudo swapon -va
```

now we proceed with installation:

```
lvcreate --size 50G vg00 --name root
lvcreate --l 100%FREE vg00 --name home
```

now we make file systems:

```
mkfs.vfat -F 32 /dev/sda1
mkfs.ext4 /dev/mapper/vg00-lv_root
mkfs.ext4 /dev/mapper/vg00-lv_home
```


then we mount:

```
mkdir -p /mnt/gentoo
mount /dev/mapper/vg00-lv_root /mnt/gentoo
mkdir -p /mnt/gentoo/boot
mount /dev/sda1 /mnt/gentoo/lv_boot
mkdir /mnt/gentoo/home
mount /dev/mapper/vg00-lv_home /mnt/gentoo/home
```

## Rest of Install Guide


- [go through Xorg installation guide](https://wiki.gentoo.org/wiki/Xorg/Guide#Make.conf_configuration)
- [go through systemd installation guide](https://wiki.gentoo.org/wiki/Systemd)
- [microcode guide, after installation](https://wiki.gentoo.org/wiki/Microcode)
- [read binary package guide]()
- [had to edit gentoo.conf to disable tree verification] (https://forums.gentoo.org/viewtopic-p-8358476.html#8358476)
	- problem arose when I tried `emerge-webrsync`

	`libtool --finish /usr/lib64`
