// Auto-generated constants for TST report
// Generated from Python calculations
// Usage: #import "constants.typ": *

// Physical Constants
#let const_kB = $1.3807 times 10^(-23)$
#let const_h = $6.6262 times 10^(-34)$
#let const_c = $2.9979 times 10^(8)$
#let const_c_cm = $2.9979 times 10^(10)$
#let const_NA = $6.0221 times 10^(23)$
#let const_R = $8.3147$

// Molecular Data
#let mol_M_H = $1.01$
#let mol_M_HBr = $80.91$
#let mol_M_Br = $79.90$
#let mol_M_TS = $81.92$
#let mol_R_HBr_nm = $0.1414$
#let mol_R_HBr_m = $1.4140 times 10^(-10)$
#let mol_R_HH_TS_nm = $0.150$
#let mol_R_HH_TS_m = $1.500 times 10^(-10)$
#let mol_R_HBr_TS_nm = $0.142$
#let mol_R_HBr_TS_m = $1.420 times 10^(-10)$
#let mol_E0_eV = $0.052$
#let mol_E0_J = $8.3313 times 10^(-21)$
#let mol_nu_HBr = $2650$
#let mol_nu_TS_1 = $2340$
#let mol_nu_TS_2 = $460$
#let mol_nu_TS_3 = $460$
#let mol_g_H = $2$
#let mol_g_HBr = $1$
#let mol_g_TS = $2$

// Translational Partition Functions at 300K
#let trans_q_H_V = $9.912 times 10^(29)$
#let trans_q_HBr_V = $7.107 times 10^(32)$
#let trans_q_TS_V = $7.240 times 10^(32)$

// Rotational - HBr at 300K
#let rot_mu_HBr = $1.656 times 10^(-27)$
#let rot_I_HBr = $3.312 times 10^(-47)$
#let rot_theta_HBr = $12.16$
#let rot_q_HBr = $24.67$

// Rotational - Transition State at 300K
#let rot_x_cm = $2.866 times 10^(-10)$
#let rot_I_TS = $1.729 times 10^(-46)$
#let rot_theta_TS = $2.33$
#let rot_q_TS = $128.80$

// Vibrational - HBr at 300K
#let vib_theta_HBr = $3813$
#let vib_q_HBr = $1.000003$

// Vibrational - Transition State at 300K
#let vib_theta_TS_1 = $3367$
#let vib_theta_TS_2 = $662$
#let vib_theta_TS_3 = $662$
#let vib_q_TS_1 = $1.000$
#let vib_q_TS_2 = $1.124$
#let vib_q_TS_3 = $1.124$
#let vib_q_TS_total = $1.263$

// Complete Partition Functions at 300K
#let Z_H_V = $1.982 times 10^(30)$
#let Z_HBr_V = $1.753 times 10^(34)$
#let Z_TS_V = $2.355 times 10^(35)$

// Rate Constant Calculation at 300K
#let rate_prefactor = $6.251 times 10^(12)$
#let rate_partition_ratio = $6.777 times 10^(-30)$
#let rate_boltzmann = $0.1338$
#let rate_k_300_SI = $5.669 times 10^(-18)$
#let rate_k_300_cm3 = $5.669 times 10^(-12)$
#let rate_k_300_L_mol = $3.414 times 10^(9)$

// Helper function to format numbers with times notation
#let sci(mantissa, exp) = $#mantissa times 10^(#exp)$

// Pre-formatted values for direct use
#let trans_q_H_V_fmt = sci("9.912", 29)
#let trans_q_HBr_V_fmt = sci("7.107", 32)
#let trans_q_TS_V_fmt = sci("7.240", 32)

#let Z_H_V_fmt = sci("1.982", 30)
#let Z_HBr_V_fmt = sci("1.753", 34)
#let Z_TS_V_fmt = sci("2.355", 35)

#let rate_k_300_SI_fmt = sci("5.669", -18)
#let rate_k_300_cm3_fmt = sci("5.669", -12)
#let rate_k_300_L_mol_fmt = sci("3.414", 9)
