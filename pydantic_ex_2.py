import json
import dataclasses
from typing import List, Optional

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    friends: List[int] = dataclasses.field(default_factory=lambda: [0])
    age: Optional[int] = dataclasses.field(
        default=None,
        metadata=dict(title='The age of the user', description='do not lie!')
    )
    height: Optional[int] = Field(None, title='The height in cm', ge=50, le=300)

@dataclass
class Taylor_Green:
   k0: int = dataclasses.field(default=1)
   force_amp: float = dataclasses.field(default=0.1)


user = User(id='42')
s = Taylor_Green.__pydantic_model__.schema()['properties']
for f in s:
    print(f.title())
"""
{
    'title': 'User',
    'type': 'object',
    'properties': {
        'id': {'title': 'Id', 'type': 'integer'},
        'name': {
            'title': 'Name',
            'default': 'John Doe',
            'type': 'string',
        },
        'friends': {
            'title': 'Friends',
            'type': 'array',
            'items': {'type': 'integer'},
        },
        'age': {
            'title': 'The age of the user',
            'description': 'do not lie!',
            'type': 'integer',
        },
        'height': {
            'title': 'The height in cm',
            'minimum': 50,
            'maximum': 300,
            'type': 'integer',
        },
    },
    'required': ['id'],
}
"""