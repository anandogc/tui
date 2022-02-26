import dataclasses
from typing import List, Optional

from pydantic.dataclasses import dataclass

@dataclass
class Complex_field:
	"""Takes input from a complex field of size Nx x Ny x Nz/2+1. Change Nx, Ny, Nz in Field tab"""
	pass

@dataclass
class Reduced_complex_field:
	Nx: int = dataclasses.field(default=16)
	Ny: int = dataclasses.field(default=16)
	Nz: int = dataclasses.field(default=16)

"""
		case (1) : Init_cond_complex_field(U);	break;					
		// read from field_in_file
		
		case (2) : Init_cond_reduced_complex_field(U);	break;	
		// read from field_in_file with Nreduced D
		
		case (3): Init_cond_real_field(U); break; 
		
		case (4) : Init_cond_modes(U);	break;		
		// Modes - ki, Vx, (Vy:3D),Theta
		
		case (5) : Init_cond_energy_helicity_spectrum(U); break;	
		// given energy and hel spectrum
        
		
		case (6) : Init_cond_Taylor_Green(U); break;
		
		case (7) : Init_cond_ABC(U); break;
        
        case (8) : Init_cond_non_helical_to_helical(U); break;
        
        case (400): Init_cond_vortex(U); break;
            
        case (420) : Init_cond_channel_flow(U); break;
            
        case (501) : Init_cond_user_defined1(U); break;
        case (502) : Init_cond_user_defined2(U); break;
"""