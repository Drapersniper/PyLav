from __future__ import annotations

import collections
from typing import Final

from pylav.filters.utils import FilterMixin


class Equalizer(FilterMixin):
    """Class representing a usable equalizer.
    Parameters
    ------------
    levels: List[Tuple[int, float]]
        A list of tuple pairs containing a band int and gain float.
    name: str
        An Optional string to name this Equalizer. Defaults to 'CustomEqualizer'
    """

    def __init__(self, *, levels: list, name: str = "CustomEqualizer"):
        self.band_count: Final[int] = 15
        self._eq = self._factory(levels)
        self._raw = levels
        self._name = name
        self.off = False

    def to_dict(self) -> dict:
        return {"equalizer": self._eq, "name": self._name, "off": self.off}

    @classmethod
    def from_dict(cls, data: dict) -> Equalizer:
        c = cls(levels=data["equalizer"], name=data["name"])
        c.off = data["off"]
        return c

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"<Equalizer: name={self._name}, eq={self._eq}>"

    @property
    def index(self):
        return {d["band"]: dict(d, index=index) for (index, d) in enumerate(self._eq)}

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Equalizer):
            return self.__dict__.keys() == other.__dict__.keys() and self._eq == other._eq and self.name == other.name
        return NotImplemented

    @property
    def name(self) -> str:
        """The Equalizers friendly name."""
        return self._name

    def _factory(self, levels: list) -> list[dict[str, int | float]]:
        if not levels:
            return self.default()._eq
        if not isinstance(levels[0], dict):
            raise TypeError("Equalizer levels should be a list of dictionaries.")

        _dict = collections.defaultdict(float)
        _dict.update(d.values() for d in levels)
        _dict = [{"band": i, "gain": _dict[i]} for i in range(self.band_count)]

        return _dict

    @classmethod
    def build(cls, *, levels: list, name: str = "CustomEqualizer") -> Equalizer:
        """Build a custom Equalizer class with the provided levels.
        Parameters
        ------------
        levels: List[Dict[str, Union[int, float]]]
            [
            {"band": 0, "gain": 0.0},
            {"band": 1, "gain": 0.0},
            ...
            ]
        name: str
            An Optional string to name this Equalizer. Defaults to 'CustomEqualizer'
        """
        return cls(levels=levels, name=name)

    @classmethod
    def flat(cls) -> Equalizer:
        """Flat Equalizer.
        Resets your EQ to Flat.
        """
        return cls(
            levels=[
                {"band": 0, "gain": 0.0},
                {"band": 1, "gain": 0.0},
                {"band": 2, "gain": 0.0},
                {"band": 3, "gain": 0.0},
                {"band": 4, "gain": 0.0},
                {"band": 5, "gain": 0.0},
                {"band": 6, "gain": 0.0},
                {"band": 7, "gain": 0.0},
                {"band": 8, "gain": 0.0},
                {"band": 9, "gain": 0.0},
                {"band": 10, "gain": 0.0},
                {"band": 11, "gain": 0.0},
                {"band": 12, "gain": 0.0},
                {"band": 13, "gain": 0.0},
                {"band": 14, "gain": 0.0},
            ],
            name="Default",
        )

    @classmethod
    def default(cls) -> Equalizer:
        return cls.flat()

    def get(self) -> list[dict[str, int | float]]:
        return [] if self.off else self._eq

    def reset(self) -> None:
        self.off = True
        eq = Equalizer.flat()
        self._eq = eq._eq
        self._name = eq._name
        self._raw = eq._raw

    def set_gain(self, band: int, gain: float) -> None:
        if band < 0 or band >= self.band_count:
            raise IndexError(f"Band {band} does not exist!")

        gain = float(min(max(gain, -0.25), 1.0))
        band = next((index for (index, d) in enumerate(self._eq) if d["band"] == band), None)
        self._eq[band]["gain"] = gain

    def get_gain(self, band: int) -> float:
        if band < 0 or band >= self.band_count:
            raise IndexError(f"Band {band} does not exist!")
        return self.index[band].get("gain", 0.0)

    def visualise(self):
        block = ""
        bands = [str(band + 1).zfill(2) for band in range(self.band_count)]
        bottom = (" " * 8) + " ".join(bands)
        gains = [x * 0.01 for x in range(-25, 105, 5)]
        gains.reverse()

        for gain in gains:
            prefix = ""
            if gain > 0:
                prefix = "+"
            elif gain == 0:
                prefix = " "

            block += f"{prefix}{gain:.2f} | "

            for value in self._eq:
                cur_gain = value.get("gain", 0.0)
                block += "[] " if cur_gain >= gain else "   "
            block += "\n"

        block += bottom
        return block
