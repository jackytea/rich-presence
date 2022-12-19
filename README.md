# Custom Discord Rich Presence

## Overview

This script is a wrapper for the [Pypresence](https://github.com/qwertyquerty/pypresence) package that allows for configuration and customization of [Discord User Rich Presences](https://discord.com/developers/docs/rich-presence/how-to).

## Table of Contents

- [Tech](#tech)<br/>
- [Setup](#setup)<br/>
- [Example](#example)<br/>

## Tech

This project utilizes the following technologies and packages:

- [Python](https://www.python.org/)
- [Python-Dotenv](https://pypi.org/project/python-dotenv/)
- [Pypresence](https://pypi.org/project/pypresence/)

## Setup

**Step 1**: Ensure you have the latest python3 and pip3 installed.

```bash
# check that python is installed
python3 --version

# check that pip3 is installed
pip3 --version
```

**Step 2**: Install the dependencies by running the `setup.py` script.

```bash
# install dependencies
python3 setup.py install --user
```

**Step 3**: Create an application on the [Discord Developers Portal](https://discord.com/developers/applications) and copy the `clientId` on the **OAuth2** tab.

**Step 4**: Make an `.env` file with the following key-value pairs.

```bash
# enviroment variables
CLIENT_ID=<CLIENT_ID>
JSON_FILE_PATH=<FILE_PATH>
SLEEP_DELAY_MS=<INTEGER>
```

**Step 5**: Edit the `config.json` to match the art assets in the **Rich Presence** tab of your Discord application. For more information on these fields see the [Pypresence documentation here](https://qwertyquerty.github.io/pypresence/html/doc/presence.html#update).

```json
{
    "state": "<YOUR_STATE_HERE>",
    "details": "<YOUR_DETAILS_HERE>",
    "start": 1,
    "end": 10,
    "large_image": "<LARGE_IMAGE_NAME>",
    "large_text": "<LARGE_IMAGE_HOVER_TEXT>",
    "small_image": "<SMALL_IMAGE_NAME>",
    "small_text": "<SMALL_IMAGE_HOVER_TEXT>",
    "party_id" : null,
    "party_size": [1, 10],
    "join": null,
    "spectate": null,
    "match": null,
    "buttons":  [
        {"label": "<EXAMPLE_SITE_1>", "url": "<URL_1_HERE>"}, 
        {"label": "<EXAMPLE_SITE_2>", "url": "<URL_2_HERE>"}
    ],
    "instance": true
}
```

**Step 6**: Start the script with the following command:

```bash
# start rich presence
python3 main.py
```

**Step 7**: Show off your custom rich presence on Discord!

## Example

![Custom Rich Presence on Discord](/demo/example.jpg)