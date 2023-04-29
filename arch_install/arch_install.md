In this markdown document I will ask you some questions about an arch linux installation that I am going through that has these commands. 

```
cryptsetup luksFormat /dev/sda2
cryptsetup open /dev/sda2 luks
mkfs.vfat -F32 -n EFI /dev/sda1
mkfs.btrfs -L ROOT /dev/mapper/luks
mount /dev/mapper/luks /mnt
btrfs sub create /mnt/@
btrfs sub create /mnt/@swap
btrfs sub create /mnt/@home
btrfs sub create /mnt/@pkg
btrfs sub create /mnt/@snapshots
umount /mnt
```

Mount the sub volumes:

```
mount -o noatime,nodiratime,compress=zstd,space_cache=v2,ssd,subvol=@ /dev/mapper/luks /mnt
mkdir -p /mnt/{boot,home,var/cache/pacman/pkg,.snapshots,btrfs}
mount -o noatime,nodiratime,compress=zstd,space_cache=v2,ssd,subvol=@home /dev/mapper/luks /mnt/home
mount -o noatime,nodiratime,compress=zstd,space_cache=v2,ssd,subvol=@pkg /dev/mapper/luks /mnt/var/cache/pacman/pkg
mount -o noatime,nodiratime,compress=zstd,space_cache=v2,ssd,subvol=@snapshots /dev/mapper/luks /mnt/.snapshots
mount -o noatime,nodiratime,compress=zstd,space_cache=v2,ssd,subvolid=5 /dev/mapper/luks /mnt/btrfs
```


what is the meaning of the command `mount /dev/mapper/luks /mnt`? why do we unmount, and then remount in the second set of commands?
