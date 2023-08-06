# headspin-cli
Headspin command line interface.

Rough notes:
* can follow docker and aws
* spit out complete jsons
* thin CLI wrapper for a python module that can be imported

Session types:
* `http_proxy`
  * we provide a host:port
  * user can use it as a proxy
* `vpn_container`
  * vpn 
  * ssh access
  * user can connect to vpn and generate traffic
  * user can ssh
  * eth0: device, eth1: broadband
  * some open ports
* `device_container`
  * vpn
  * ssh access
  * adb
  * STF (SMS, voice, testing, adb proxy)
  * eth0: device, eth1: broadband
  * usb poked through the container
  * open ports

```yaml
# install
pip install headspin-cli

# authorize this device
# adds credentials to ~/.headspin/
hs auth pub_key priv_key

# list sessions
hs session ls
--> list active sessions
hs session ls 100
--> list last 100 sessions active or inactive

# start vpn capture session (you connect to vpn and all traffic is captured)
hs session start vpn_container jp-3g
--> vpn credentials
--> error if cannot find devices or connection failed
# start vpn container session and connect companion to it
hs session start vpn_container jp-3g --companion_id=<companion_id>
--> same as above
--> what if companion is on another session?
# start proxy capture session
hs session start proxy_capture jp-3g
--> same as above
# start device container session
hs session start device_container jp-3g
--> same as above
# dump session details
hs session inspect <session_id>
--> JSON with all the details
# terminate session
hs session stop <session_id>
--> error if not found
--> warning if already inactive
--> "Stopped."
# delete session
hs session rm <session_id>
--> error if not found
--> "Removed."
# get mar (error if this is not a capture session)
hs session mar <session_id>
--> mar JSON
# get har (error if this is not a capture session)
hs session har <session_id>
--> har JSON

# list connected companions
hs companion ls
--> connected companions one per line
# dump companion details
hs companion inspect <companion_id>
--> detailed JSON

# list devices for this org
hs device ls
--> list devices one per row
# filter devices by selector
hs device ls jp-3g
--> list devices one per row
# dump device details
hs device inspect <device_id
--> detailed JSON
```
