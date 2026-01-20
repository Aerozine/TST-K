import numpy as np
# Physical constants
kB = 1.3807 * 1e-23 # JK-1
c = 2.9979 * 1e8 # m s-1
# Convert speed of light to cm/s
c_cm = c * 100  # m/s to cm/s
N_A = 6.0221 *1e23 # mol-1 
# based on hbar to match precision
h= 2*np.pi*1.0546 * 1e-34 # J s
R = N_A * kB

# Molar masses (kg/mol)
M_H = 1.01e-3
M_HBr = 80.91e-3
M_Br = M_HBr - M_H 
M_TS = M_H + M_HBr

# Bond distances (m)
R_HBr = 0.1414e-9
R_HH_TS = 0.150e-9
R_HBr_TS = 0.142e-9

# Activation energy
E0_eV = 0.052 # eV
E0 = E0_eV * 1.60218e-19  # J 

# Vibrational wavenumbers (cm^-1)
nu_HBr = 2650
nu_TS = [2340, 460, 460]

# Electronic degeneracies
g_H = 2
g_HBr = 1
g_TS = 2
