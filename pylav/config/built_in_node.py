from __future__ import annotations

import secrets

from pylav._config import __VERSION__

NODE_DEFAULT_SETTINGS = {
    "server": {"port": 2154, "address": "0.0.0.0"},
    "lavalink": {
        "plugins": [
            {
                "dependency": "com.github.Topis-Lavalink-Plugins:Topis-Source-Managers-Plugin:v2.0.5",
                "repository": "https://jitpack.io",
            },
            {
                "dependency": "com.dunctebot:skybot-lavalink-plugin:1.3.3",
                "repository": "https://m2.duncte123.dev/releases",
            },
            {"dependency": "com.github.topisenpai:sponsorblock-plugin:v1.0.3", "repository": "https://jitpack.io"},
        ],
        "server": {
            "password": secrets.token_urlsafe(32),
            "sources": {
                "youtube": True,
                "bandcamp": True,
                "soundcloud": True,
                "twitch": True,
                "vimeo": True,
                "http": True,
                "local": True,
            },
            "bufferDurationMs": 1000,
            "youtubePlaylistLoadLimit": 10000,
            "playerUpdateInterval": 1,
            "youtubeSearchEnabled": True,
            "soundcloudSearchEnabled": True,
            "gc-warnings": True,
            "ratelimit": {
                "ipBlocks": [],
                "excludedIps": [],
                "strategy": "RotateOnBan",
                "searchTriggersFail": True,
                "retryLimit": -1,
            },
            "youtubeConfig": {
                "PAPISID": "",
                "PSID": "",
            },
        },
    },
    "plugins": {
        "topissourcemanagers": {
            "providers": [
                'ytmsearch:"%ISRC%"',
                'ytsearch:"%ISRC%"',
                "ytmsearch:%QUERY%",
                "ytsearch:%QUERY%",
                "scsearch:%QUERY%",
            ],
            "sources": {"spotify": True, "applemusic": True},
            "spotify": {
                "clientId": "3d5cd36c73924786aa290798b2131c58",
                "clientSecret": "edee5eb255a846fbac8297069debea2e",
                "countryCode": "US",
            },
            "applemusic": {"countryCode": "US"},
        },
        "dunctebot": {
            "ttsLanguage": "en-US",
            "sources": {
                "getyarn": True,
                "clypit": True,
                "tts": True,
                "pornhub": True,
                "reddit": True,
                "ocremix": True,
                "tiktok": True,
                "mixcloud": True,
            },
        },
    },
    "metrics": {"prometheus": {"enabled": False, "endpoint": "/metrics"}},
    "sentry": {"dsn": "", "environment": "", "tags": {"pylav_version": __VERSION__}},
    "logging": {
        "file": {"max-history": 7, "max-size": "25MB"},
        "path": "./logs/",
        "level": {"root": "INFO", "lavalink": "INFO"},
    },
}