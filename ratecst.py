from constants import *
from partfunc import * 
import numpy as np 


def calculate_rate_constant(T):
    
    # Translational partition functions (per unit volume)
    q_trans_H = calc_translational_partition_function(M_H, T)
    q_trans_HBr = calc_translational_partition_function(M_HBr, T)
    q_trans_TS = calc_translational_partition_function(M_TS, T)
    
    # Rotational partition functions
    q_rot_HBr = calc_rotational_partition_function(I_HBr, T)
    q_rot_TS = calc_rotational_partition_function(I_TS, T)
    
    # Vibrational partition functions
    q_vib_HBr = calc_vibrational_partition_function(nu_HBr, T)
    q_vib_TS = np.prod([calc_vibrational_partition_function(nu, T) for nu in nu_TS])
    
    # Electronic partition functions
    q_elec_H = g_H
    q_elec_HBr = g_HBr
    q_elec_TS = g_TS
    
    # Total partition functions (per unit volume)
    Q_H = q_trans_H * q_elec_H
    Q_HBr = q_trans_HBr * q_rot_HBr * q_vib_HBr * q_elec_HBr
    Q_TS = q_trans_TS * q_rot_TS * q_vib_TS * q_elec_TS
    
    # TST rate constant
    prefactor = kB * T / h
    partition_ratio = Q_TS / (Q_H * Q_HBr)
    boltzmann_factor = np.exp(-E0 / (kB * T))
    
    k = prefactor * partition_ratio * boltzmann_factor
    
    return k  # m³/(molecule·s)

