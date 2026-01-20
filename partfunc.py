from constants import *
def calc_moment_of_inertia_diatomic(m1, m2, r):
    """Calculate moment of inertia for diatomic molecule"""
    mu = (m1 * m2) / (m1 + m2) / N_A  # Reduced mass per molecule
    return mu * r**2

def calc_moment_of_inertia_linear_triatomic(m1, m2, m3, r12, r23):
    """
    Calculate moment of inertia for linear triatomic molecule
    Atoms positioned at: 0, r12, r12+r23
    """
    # Convert to per-molecule masses
    m1 = m1 / N_A
    m2 = m2 / N_A
    m3 = m3 / N_A
    
    # Positions along the axis
    x1 = 0
    x2 = r12
    x3 = r12 + r23
    # Center of mass
    total_mass = m1 + m2 + m3
    x_cm = (m1*x1 + m2*x2 + m3*x3) / total_mass
    
    # Moment of inertia about center of mass
    I = m1*(x1 - x_cm)**2 + m2*(x2 - x_cm)**2 + m3*(x3 - x_cm)**2
    return I

def calc_vibrational_partition_function(nu_cm, T):
    """Calculate vibrational partition function"""
    theta_vib = h * c_cm * nu_cm / kB
    return 1 / (1 - np.exp(-theta_vib / T))

def calc_rotational_partition_function(I, T):
    """Calculate rotational partition function for linear molecule"""
    theta_rot = h**2 / (8 * np.pi**2 * kB * I)
    return T / theta_rot

def calc_translational_partition_function(M, T):
    """Calculate translational partition function per unit volume"""
    m = M / N_A 
    V = R * T / 1e5  # Standard molar volume at 1 bar (m³/mol)
    q_trans = (2 * np.pi * m * kB * T / h**2)**(3/2) * V
    return q_trans / V  # Return per unit volume

# HBr moment of inertia
I_HBr = calc_moment_of_inertia_diatomic(M_H, M_HBr, R_HBr)

# Transition state moment of inertia (H-H-Br linear)
I_TS = calc_moment_of_inertia_linear_triatomic(M_H, M_H, M_Br, R_HH_TS, R_HBr_TS)
