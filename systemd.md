---
autnor: Jordan Mandel
date: 2002-07-25
title: "digitalocean systemd article notes"
geometry: margin=2.54cm
---

type of unit determined by suffix at end of file: many have the `.service`

to execute instructions in the service file:

```
sudo systemctl start application.service
sudo systemctl stop application.service
```

can leave off `.service` it is the default

```
sudo systemctl reload-or-restart application.service
```


```
sudo systemctl enable application.service
sudo systemctl disable application.service
```

creates symlink from either `/lib/systemd/system` or `/etc/systemd/system` to `/etc/systemd/system/some_target.target.wants`


enabling does not start service.


# checking status

```
systemctl status application.service
```

```
systemctl is-active application.service
systemctl is-enabled application.service
systemctl is-failed application.service
```


```
systemctl list-units
systemctl list-units --type=service
systemctl list-units --all
systemctl list-unit-files # static means just a dependency of another unit
```

will show loaded/active


to get details we can do, for example:

```
systemctl cat atd.service
```


we can also go

```
systemctl list-dependencies sshd.service
systemctl list-dependencies --all sshd.service
systemctl list-dependencies --reverse sshd.service # for reverse dependencies
systemctl list-dependencies --before sshd.service # have to start before
systemctl list-dependencies --after sshd.service # have to start after
```


to get more details we can go:

```
systemctl show sshd.service
systemctl show sshd.service -p Conflicts # look at a particular property
```

# Masking and Unmasking Units

```
systemctl mask nginx.service
```

links it to `/dev/null`

```
systemctl unmask nginx.service
```

# editing unit files

can go 

```
sudo systemctl edit nginx.service
```

will create folder `name.service.d` with file `override.conf` that overrides the basic config.


```
sudo systemctl edit --full nginx.service
```

writes full file to `/etc/systemd/system`

undo changes by removing corresponding `.d` directory or the right file from `/etc/systemd/system`.

after doing this we should go `sudo sytemctl daemon-reload`


# targets
used to bring system to certain states
can learn more later
there is a default target when booting the system

can get it like 

```
systemctl get-default
```


for example to get the system to boot into gui by default part of it is:
```
sudo systemctl set-default graphical.target
```


```
systemctl list-unit-files --type=target #all available targets
systemctl list-unis --type=target # all active targets
```

# isolating
will make just one target active; be aware of dependencies

```
systemctl list-dependencies multi-user.target
sudo systemctl isolate multi-user.target
```

# aliases

`rescue` = `isolate rescue.target`
`halt` = `sudo systemctl halt`
there is `poweroff` and `reboot`

# there is also 
`jounald`/`journalctl`
and
`logind`/`lodinctl`
