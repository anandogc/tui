import dataclasses
from typing import List, Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

# @dataclass
# class Decay:
#     pass


@dataclass
class Global:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class complex_field:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class field_frequent:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class field_reduced:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)
   Nx:int = dataclasses.field(default=16)
   Ny:int = dataclasses.field(default=16)
   Nz:int = dataclasses.field(default=16)

@dataclass
class real_field:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class field_k:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class field_r:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class spectrum:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class pressure:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class pressure_spectrum:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class flux:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class shell_to_shell:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class ring_spectrum:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class ring_to_ring:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class cylindrical_ring_spectrum:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class cylindrical_ring_to_ring:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class structure_fn:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class Tk_shell_spectrum:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class Tk_ring_spectrum:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class Tk_cylindrical_ring_spectrum:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)

@dataclass
class cout:
   time_start: float = dataclasses.field(default=0.0)
   time_interval: float = dataclasses.field(default=0.0)
   time_last: bool = dataclasses.field(default=True)
