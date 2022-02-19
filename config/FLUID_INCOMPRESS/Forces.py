import dataclasses
from typing import List, Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

# @dataclass
# class Decay:
#     pass

@dataclass
class Carati_scheme:
   force_type: str = dataclasses.field(default="ENERGY_SUPPLY", metadata={"options": ["ENERGY_SUPPLY", "CONSTANT_ENERGY"]})
   global_alpha_beta: bool = dataclasses.field(default=True)


# @dataclass
# class Modes:
#    modes: List[Tuple[NewType("Coordinates", str), NewType("Amplitudes",str)]] = dataclasses.field(default_factory=lambda:[("2,1,1", "(0.10,0.10), (0.12,0.10), (0.10,0.20), (0.1,0.1)")])

@dataclass
class Taylor_Green:
   k0: int = dataclasses.field(default=1)
   force_amp: float = dataclasses.field(default=0.1)


# force_list =