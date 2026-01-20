import numpy as np
from constants import *
from partfunc import *
from ratecst import *

# Helper function to format scientific notation for Typst
def format_sci(value, decimals=3):
    """Convert scientific notation to Typst format: a.bbb × 10^c"""
    s = f"{value:.{decimals}e}"
    parts = s.split('e')
    mantissa = parts[0]
    exponent = int(parts[1])
    return f"{mantissa} times 10^({exponent})"

# Open file for writing
with open('constants.typ', 'w') as f:
    f.write("// Auto-generated constants for TST report\n")
    f.write("// Generated from Python calculations\n")
    f.write("// Usage: #import \"constants.typ\": *\n\n")
    
    # PHYSICAL CONSTANTS
    f.write("// Physical Constants\n")
    f.write(f"#let const_kB = ${format_sci(kB, 4)}$\n")
    f.write(f"#let const_h = ${format_sci(h, 4)}$\n")
    f.write(f"#let const_c = ${format_sci(c, 4)}$\n")
    f.write(f"#let const_c_cm = ${format_sci(c_cm, 4)}$\n")
    f.write(f"#let const_NA = ${format_sci(N_A, 4)}$\n")
    f.write(f"#let const_R = ${R:.4f}$\n\n")
    
    # MOLECULAR DATA
    f.write("// Molecular Data\n")
    f.write(f"#let mol_M_H = ${M_H*1000:.2f}$\n")
    f.write(f"#let mol_M_HBr = ${M_HBr*1000:.2f}$\n")
    f.write(f"#let mol_M_Br = ${M_Br*1000:.2f}$\n")
    f.write(f"#let mol_M_TS = ${M_TS*1000:.2f}$\n")
    f.write(f"#let mol_R_HBr_nm = ${R_HBr*1e9:.4f}$\n")
    f.write(f"#let mol_R_HBr_m = ${format_sci(R_HBr, 4)}$\n")
    f.write(f"#let mol_R_HH_TS_nm = ${R_HH_TS*1e9:.3f}$\n")
    f.write(f"#let mol_R_HH_TS_m = ${format_sci(R_HH_TS, 3)}$\n")
    f.write(f"#let mol_R_HBr_TS_nm = ${R_HBr_TS*1e9:.3f}$\n")
    f.write(f"#let mol_R_HBr_TS_m = ${format_sci(R_HBr_TS, 3)}$\n")
    f.write(f"#let mol_E0_eV = ${E0_eV}$\n")
    f.write(f"#let mol_E0_J = ${format_sci(E0, 4)}$\n")
    f.write(f"#let mol_nu_HBr = ${nu_HBr}$\n")
    f.write(f"#let mol_nu_TS_1 = ${nu_TS[0]}$\n")
    f.write(f"#let mol_nu_TS_2 = ${nu_TS[1]}$\n")
    f.write(f"#let mol_nu_TS_3 = ${nu_TS[2]}$\n")
    f.write(f"#let mol_g_H = ${g_H}$\n")
    f.write(f"#let mol_g_HBr = ${g_HBr}$\n")
    f.write(f"#let mol_g_TS = ${g_TS}$\n\n")
    
    # TRANSLATIONAL PARTITION FUNCTIONS (T=300K)
    T = 300
    q_trans_H_V = calc_translational_partition_function(M_H, T)
    q_trans_HBr_V = calc_translational_partition_function(M_HBr, T)
    q_trans_TS_V = calc_translational_partition_function(M_TS, T)
    
    f.write("// Translational Partition Functions at 300K\n")
    f.write(f"#let trans_q_H_V = ${format_sci(q_trans_H_V)}$\n")
    f.write(f"#let trans_q_HBr_V = ${format_sci(q_trans_HBr_V)}$\n")
    f.write(f"#let trans_q_TS_V = ${format_sci(q_trans_TS_V)}$\n\n")
    
    # ROTATIONAL - HBr
    m_H = M_H / N_A
    m_Br_approx = M_Br / N_A
    mu_HBr = (m_H * m_Br_approx) / (m_H + m_Br_approx)
    theta_rot_HBr = h**2 / (8 * np.pi**2 * kB * I_HBr)
    q_rot_HBr = calc_rotational_partition_function(I_HBr, T)
    
    f.write("// Rotational - HBr at 300K\n")
    f.write(f"#let rot_mu_HBr = ${format_sci(mu_HBr)}$\n")
    f.write(f"#let rot_I_HBr = ${format_sci(I_HBr)}$\n")
    f.write(f"#let rot_theta_HBr = ${theta_rot_HBr:.2f}$\n")
    f.write(f"#let rot_q_HBr = ${q_rot_HBr:.2f}$\n\n")
    
    # ROTATIONAL - TS
    m_H1 = M_H / N_A
    m_H2 = M_H / N_A
    m_Br = M_Br / N_A
    
    x1 = 0
    x2 = R_HH_TS
    x3 = R_HH_TS + R_HBr_TS
    
    total_mass = m_H1 + m_H2 + m_Br
    x_cm = (m_H1*x1 + m_H2*x2 + m_Br*x3) / total_mass
    
    theta_rot_TS = h**2 / (8 * np.pi**2 * kB * I_TS)
    q_rot_TS = calc_rotational_partition_function(I_TS, T)
    
    f.write("// Rotational - Transition State at 300K\n")
    f.write(f"#let rot_x_cm = ${format_sci(x_cm)}$\n")
    f.write(f"#let rot_I_TS = ${format_sci(I_TS)}$\n")
    f.write(f"#let rot_theta_TS = ${theta_rot_TS:.2f}$\n")
    f.write(f"#let rot_q_TS = ${q_rot_TS:.2f}$\n\n")
    
    # VIBRATIONAL - HBr
    theta_vib_HBr = h * c_cm * nu_HBr / kB
    q_vib_HBr = calc_vibrational_partition_function(nu_HBr, T)
    
    f.write("// Vibrational - HBr at 300K\n")
    f.write(f"#let vib_theta_HBr = ${theta_vib_HBr:.0f}$\n")
    f.write(f"#let vib_q_HBr = ${q_vib_HBr:.6f}$\n\n")
    
    # VIBRATIONAL - TS
    q_vib_TS_modes = []
    theta_vib_TS_modes = []
    for nu in nu_TS:
        theta_vib = h * c_cm * nu / kB
        q_vib = calc_vibrational_partition_function(nu, T)
        theta_vib_TS_modes.append(theta_vib)
        q_vib_TS_modes.append(q_vib)
    
    q_vib_TS_total = np.prod(q_vib_TS_modes)
    
    f.write("// Vibrational - Transition State at 300K\n")
    f.write(f"#let vib_theta_TS_1 = ${theta_vib_TS_modes[0]:.0f}$\n")
    f.write(f"#let vib_theta_TS_2 = ${theta_vib_TS_modes[1]:.0f}$\n")
    f.write(f"#let vib_theta_TS_3 = ${theta_vib_TS_modes[2]:.0f}$\n")
    f.write(f"#let vib_q_TS_1 = ${q_vib_TS_modes[0]:.3f}$\n")
    f.write(f"#let vib_q_TS_2 = ${q_vib_TS_modes[1]:.3f}$\n")
    f.write(f"#let vib_q_TS_3 = ${q_vib_TS_modes[2]:.3f}$\n")
    f.write(f"#let vib_q_TS_total = ${q_vib_TS_total:.3f}$\n\n")
    
    # COMPLETE PARTITION FUNCTIONS
    Z_H_V = q_trans_H_V * g_H
    Z_HBr_V = q_trans_HBr_V * q_rot_HBr * q_vib_HBr * g_HBr
    Z_TS_V = q_trans_TS_V * q_rot_TS * q_vib_TS_total * g_TS
    
    f.write("// Complete Partition Functions at 300K\n")
    f.write(f"#let Z_H_V = ${format_sci(Z_H_V)}$\n")
    f.write(f"#let Z_HBr_V = ${format_sci(Z_HBr_V)}$\n")
    f.write(f"#let Z_TS_V = ${format_sci(Z_TS_V)}$\n\n")
    
    # RATE CONSTANT AT 300K
    prefactor = kB * T / h
    partition_ratio = Z_TS_V / (Z_H_V * Z_HBr_V)
    boltzmann = np.exp(-E0 / (kB * T))
    k_300 = calculate_rate_constant(T)
    k_300_cm3 = k_300 * 1e6
    k_300_L_mol = k_300 * N_A * 1000
    
    f.write("// Rate Constant Calculation at 300K\n")
    f.write(f"#let rate_prefactor = ${format_sci(prefactor)}$\n")
    f.write(f"#let rate_partition_ratio = ${format_sci(partition_ratio)}$\n")
    f.write(f"#let rate_boltzmann = ${boltzmann:.4f}$\n")
    f.write(f"#let rate_k_300_SI = ${format_sci(k_300)}$\n")
    f.write(f"#let rate_k_300_cm3 = ${format_sci(k_300_cm3)}$\n")
    f.write(f"#let rate_k_300_L_mol = ${format_sci(k_300_L_mol)}$\n\n")
    
    # HELPER FUNCTIONS FOR FORMATTING
    f.write("// Helper function to format numbers with times notation\n")
    f.write("#let sci(mantissa, exp) = $#mantissa times 10^(#exp)$\n\n")
    
    # Function to split scientific notation
    def split_sci(value):
        s = f"{value:.3e}"
        parts = s.split('e')
        mantissa = parts[0]
        exp = int(parts[1])
        return mantissa, exp
    
    # FORMATTED VERSIONS (for easy use in report)
    f.write("// Pre-formatted values for direct use\n")
    
    m, e = split_sci(q_trans_H_V)
    f.write(f"#let trans_q_H_V_fmt = sci(\"{m}\", {e})\n")
    
    m, e = split_sci(q_trans_HBr_V)
    f.write(f"#let trans_q_HBr_V_fmt = sci(\"{m}\", {e})\n")
    
    m, e = split_sci(q_trans_TS_V)
    f.write(f"#let trans_q_TS_V_fmt = sci(\"{m}\", {e})\n\n")
    
    m, e = split_sci(Z_H_V)
    f.write(f"#let Z_H_V_fmt = sci(\"{m}\", {e})\n")
    
    m, e = split_sci(Z_HBr_V)
    f.write(f"#let Z_HBr_V_fmt = sci(\"{m}\", {e})\n")
    
    m, e = split_sci(Z_TS_V)
    f.write(f"#let Z_TS_V_fmt = sci(\"{m}\", {e})\n\n")
    
    m, e = split_sci(k_300)
    f.write(f"#let rate_k_300_SI_fmt = sci(\"{m}\", {e})\n")
    
    m, e = split_sci(k_300_cm3)
    f.write(f"#let rate_k_300_cm3_fmt = sci(\"{m}\", {e})\n")
    
    m, e = split_sci(k_300_L_mol)
    f.write(f"#let rate_k_300_L_mol_fmt = sci(\"{m}\", {e})\n")

print("done")
