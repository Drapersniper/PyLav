from __future__ import annotations

import datetime
from dataclasses import dataclass

from iso8601 import iso8601

from pylav.query import Query


@dataclass(eq=True)
class Station:
    changeuuid: str = None
    stationuuid: str = None
    serveruuid: str = None
    name: str = None
    url: str = None
    url_resolved: str = None
    homepage: str = None
    favicon: str = None
    tags: str = None
    country: str = None
    countrycode: str = None
    iso_3166_2: str = None
    state: str = None
    language: str = None
    languagecodes: str = None
    votes: int = None
    lastchangetime: str = None
    lastchangetime_iso8601: str | datetime.datetime = None
    codec: str = None
    bitrate: int = None
    hls: int = None
    lastcheckok: int = None
    lastchecktime: str = None
    lastchecktime_iso8601: str | datetime.datetime = None
    lastcheckoktime: str = None
    lastcheckoktime_iso8601: str | datetime.datetime = None
    lastlocalchecktime: str = None
    lastlocalchecktime_iso8601: str | datetime.datetime = None
    clicktimestamp: str = None
    clicktimestamp_iso8601: str | datetime.datetime = None
    clickcount: int = None
    clicktrend: int = None
    ssl_error: int = None
    geo_lat: float = None
    geo_long: float = None
    has_extended_info: int = None

    def __post_init__(self):
        if isinstance(self.lastchangetime_iso8601, str):
            self.lastchangetime_iso8601 = iso8601.parse_date(self.lastchangetime_iso8601)
        if isinstance(self.lastchecktime_iso8601, str):
            self.lastchecktime_iso8601 = iso8601.parse_date(self.lastchecktime_iso8601)
        if isinstance(self.lastcheckoktime_iso8601, str):
            self.lastcheckoktime_iso8601 = iso8601.parse_date(self.lastcheckoktime_iso8601)
        if isinstance(self.lastlocalchecktime_iso8601, str):
            self.lastlocalchecktime_iso8601 = iso8601.parse_date(self.lastlocalchecktime_iso8601)
        if isinstance(self.clicktimestamp_iso8601, str):
            self.clicktimestamp_iso8601 = iso8601.parse_date(self.clicktimestamp_iso8601)

    async def get_query(self) -> Query:
        return await Query.from_string(self.url_resolved or self.url)


@dataclass(eq=True)
class Tag:
    name: str = None
    stationcount: int = None


@dataclass(eq=True)
class Language:
    name: str = None
    iso_639: str = None
    stationcount: int = None


@dataclass(eq=True)
class State:
    name: str = None
    country: str = None
    stationcount: int = None


@dataclass(eq=True)
class Codec:
    name: str = None
    stationcount: int = None


@dataclass(eq=True)
class CountryCode:
    name: str = None
    stationcount: int = None


@dataclass(eq=True)
class Country:
    name: str = None
    iso_3166_1: str = None
    stationcount: int = None
