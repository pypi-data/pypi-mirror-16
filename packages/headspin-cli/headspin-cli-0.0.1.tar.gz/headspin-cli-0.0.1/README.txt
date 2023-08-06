# headspin-cli
CLI for the HeadSpin platform API.

Installation/Upgrade:
--
```
pip install --upgrade headspin-cli
```

Usage:
--
```
  hs (-h | --help)
  hs auth init <token>
  hs auth info
  hs auth set-default <credentials_number>
  hs session ls [<num_sessions>] [-a] [--json]
  hs session inspect <session_uuid> [--writefiles] [--json]
  hs session start network_container <device_id> [--json]
  hs session stop <session_uuid> [--json]
  hs session mar <session_uuid>
  hs session har <session_uuid>
  hs companion ls [--json]
  hs companion inspect <companion_uuid> [--json]
  hs device ls [--json]
```

Detailed Description:
--
  hs auth init <token>

        Authorizes this device given a one-time token <token>. Contact
        support@headspin.io to request an authorization token.

  hs auth info

        Prints the current credentials.

  has auth set-default <credentials_number>

        Sets the credentials number <credentials_number> as the default.
        The numbering can be seen via the `hs auth info` command.

  hs session ls [<num_sessions>] [-a]

        Outputs a list of session metadata in reverse-chronological
        order. <num_sessions> is the number of sessions output, 5 by
        default. By default only active sessions are output. The `-a`
        flag will cause inactive sessions to be inclued in the result.

  hs session inspect <session_uuid> [--writefiles]

        Outputs details for a session given the session's UUID. If
        `--writefiles` is given, data associated with session endpoints
        is written to files.

  hs session start network_container <device_id>

        Starts a HeadSpin network container session on a device
        specified by <device_id>. The container's default network
        interface (eth0) is on the device's mobile network. The container
        can be accessed via SSH login. In addition, a device can access
        the remote mobile network by connecting to a VPN.

  hs session stop <session_uuid>

        Stops a session in progress.

  hs session mar <session_id>

        Downloads the captured network traffic from a HeadSpin session
        in HeadSpin's MAR format. MAR is a HAR-like JSON format that
        contains the data in a network capture at a high level.

  hs session har <session_id>

        Downloads the captured network traffic from a HeadSpin session
        in HAR format.

  hs device ls

        Lists all the devices.
