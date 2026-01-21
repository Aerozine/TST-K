#import "@preview/subpar:0.2.2"
#import "lib.typ": project
#import "@preview/dashy-todo:0.1.3": todo
#import "@preview/wrap-it:0.1.1": *
#import "constants.typ": *

#set text(font: "xits")
#set cite(style: "ieee")
#show: project.with(
  title: "Numerical homework: Rate constant using the Transition State Theory",
  subtitle: "CHIM9308-1 Physical Chemistry",
  authors: (
    "Loïc DELBARRE",
    "S215072"
  ),
  school-logo: image("ulgfsa.svg"),
  jury: ("Bernard LEYH",),
  juryname: "Professor",
  branch: "Engineering physics",
  academic-year: "2025-2026",
  tof: false,
  tot: false,
  toc: false,
  footer-text: "Numerical homework"
)

#set par(justify: true)
#set page(paper: "a4")
#set text(size: 12pt)
#set page(numbering: "1")
#set math.equation(numbering: "(1)", number-align: bottom)
#import "@preview/zero:0.5.0": ztable
#import "@preview/theorion:0.4.1": *
#import cosmos.clouds: *
#show: show-theorion
#let theorem = theorem.with(fill: blue.lighten(85%))
#let theorem-box = theorem-box.with(fill: blue.lighten(85%))
#let theorem-box = theorem-box.with(radius: 5pt)
#import "@preview/physica:0.9.7": *

= Introduction

This report presents the calculation of the rate constant for the elementary gas phase exchange reaction:

$ "H"_((g)) + "HBr"_((g)) -> "H"_(2(g)) + "Br"_((g)) $

using Transition State Theory (TST) over the temperature range 300-1000 K. The transition state is assumed to be linear with the configuration H-H-Br.

= Theoretical Background

== Transition State Theory

Transition State Theory provides a framework for calculating rate constants from molecular properties. The fundamental TST equation is:

$ k(T) = frac(k_B T, h) times frac(Z^‡, Z_"H" Z_"HBr") times exp(-frac(E_0, k_B T)) $ <tst-equation>

where:
- $k_B$ is the Boltzmann constant (#const_kB J/K)
- $h$ is the Planck constant (#const_h J·s)
- $Z^‡$ is the partition function of the transition state
- $Z_"H"$ and $Z_"HBr"$ are the partition functions of the reactants
- $E_0$ is the activation energy barrier (#mol_E0_eV eV)

The partition functions $Z$ are expressed per unit volume $V$ to maintain dimensional consistency.

== Molecular Partition Functions

The total partition function for a molecule is factored into the contributions from different degrees of freedom:

$ Z = z_"trans" dot z_"rot" dot z_"vib" dot z_"elec" $

where:
- $z_"trans"$ is the contribution from translational degrees of freedom.
- $z_"rot"$ is the contribution from rotational degrees of freedom.
- $z_"vib"$ is contribution from vibrational degrees of freedom.
- $z_"elec"$ is contribution from electronic degrees of freedom.
  
Each contribution is calculated separately as described in the following sections.

= Computational Methodology

== Code Structure

The Python implementation is organized into modular files:

- `constants.py`: Defines all physical constants and molecular data
- `partfunc.py`: Computes all partition functions
- `ratecst.py`: Implements the TST rate constant calculation
- `run.py`: Generates rate constants over the temperature range
- `requirements.txt`: Lists dependencies (numpy and matplotlib)
- `gen_typcst.py`: Generates values for the report

= Partition Function Calculations

== Translational Partition Function

The translational partition function $z_"trans"$ per unit of volume $V$ for a molecule of mass $m$ at temperature $T$ is:

#theorem-box(title: "Translational Partition Function")[
$ frac(z_"trans", V) = (frac(2 pi m k_B T, h^2))^(3\/2) $
]

For standard state calculations, we use the molar volume $V = R T \/ P^⊖$ where $P^⊖ = 10^5$ Pa.

*Numerical values at T = 300 K:*
- H atom: $z_"trans"\/V = #trans_q_H_V_fmt "m"^(-3)$
- HBr molecule: $z_"trans"\/V = #trans_q_HBr_V_fmt "m"^(-3)$
- Transition state: $z_"trans"\/V = #trans_q_TS_V_fmt "m"^(-3)$

== Rotational Partition Function

=== Diatomic Molecules (HBr)

For a diatomic molecule, the moment of inertia is calculated from the reduced mass:

#theorem-box(title: "Diatomic Moment of Inertia")[
$ I = mu R^2 "where" mu = frac(m_1 m_2, m_1 + m_2) $
]

The rotational temperature $theta_"rot"$ is:
$ theta_"rot" = frac(h^2, 8 pi^2 k_B I) $

The rotational partition function for a heteronuclear diatomic molecule is:
$ z_"rot" = frac(T, theta_"rot") $

*For HBr:*
- Reduced mass: $mu = #rot_mu_HBr$ kg
- Bond distance: $R = #mol_R_HBr_m$ m
- Moment of inertia: $I_"HBr" = #rot_I_HBr$ kg·m²
- Rotational temperature: $theta_"rot" = #rot_theta_HBr$ K
- At 300 K: $z_"rot"("HBr") = #rot_q_HBr$

=== Linear Triatomic Molecules (Transition State)

For a linear triatomic molecule (H-H-Br), we first locate the center of mass:

#theorem-box(title: "Center of Mass Position")[
$ x_"cm" = frac(sum_i m_i x_i, sum_i m_i) $

For H-H-Br with H₁ at origin, H₂ at distance $d_1$, and Br at distance $d_1 + d_2$:

$ x_"cm" = frac(m_"H1" dot 0 + m_"H2" dot d_1 + m_"Br" dot (d_1 + d_2), m_"H1" + m_"H2" + m_"Br") $
]

The moment of inertia about the center of mass is:
$ I = sum_i m_i (x_i - x_"cm")^2 $

*For the transition state H-H-Br:*
- H-H distance: $d_1 = #mol_R_HH_TS_m$ m
- H-Br distance: $d_2 = #mol_R_HBr_TS_m$ m
- Center of mass position: $x_"cm" = #rot_x_cm$ m
- Moment of inertia: $I^‡ = #rot_I_TS$ kg·m²
- Rotational temperature: $theta_"rot" = #rot_theta_TS$ K
- At 300 K: $z_"rot"^‡ = #rot_q_TS$

The larger moment of inertia of the transition state (due to greater spatial extent) results in a lower rotational temperature and higher partition function.

== Vibrational Partition Function

The vibrational partition function for a single harmonic oscillator mode is:

#theorem-box(title: "Vibrational Partition Function")[
$ z_"vib" = frac(1, 1 - exp(-theta_"vib" \/ T)) $

where the vibrational temperature is:
$ theta_"vib" = frac(h c tilde(nu), k_B) $

and $tilde(nu)$ is the vibrational wavenumber in cm⁻¹.
]

For a polyatomic molecule, the total vibrational partition function is the product over all normal modes:
$ z_"vib"^"total" = product_i z_"vib,i" $

=== HBr Vibrational Mode

*Given data:* $tilde(nu)_"HBr" = #mol_nu_HBr$ cm⁻¹

- Vibrational temperature: $theta_"vib" = #vib_theta_HBr$ K
- At 300 K: $z_"vib"("HBr") approx #vib_q_HBr$

The high vibrational frequency means this mode is essentially "frozen" at room temperature and only becomes significantly populated at very high temperatures.

=== Transition State Vibrational Modes

The transition state has *three real vibrational modes* (the imaginary frequency corresponding to the reaction coordinate is excluded from the partition function):

*Mode 1:* $tilde(nu)_1 = #mol_nu_TS_1$ cm⁻¹ (H-H stretch)
- $theta_"vib,1" = #vib_theta_TS_1$ K
- At 300 K: $z_"vib,1" = #vib_q_TS_1$

*Mode 2:* $tilde(nu)_2 = #mol_nu_TS_2$ cm⁻¹ (bend)
- $theta_"vib,2" = #vib_theta_TS_2$ K  
- At 300 K: $z_"vib,2" = #vib_q_TS_2$

*Mode 3:* $tilde(nu)_3 = #mol_nu_TS_3$ cm⁻¹ (bend, degenerate)
- $theta_"vib,3" = #vib_theta_TS_3$ K
- At 300 K: $z_"vib,3" = #vib_q_TS_3$

*Total vibrational partition function at 300 K:*
$ z_"vib"^‡ = #vib_q_TS_1 times #vib_q_TS_2 times #vib_q_TS_3 = #vib_q_TS_total $

The low-frequency bending modes contribute significantly to the partition function even at 300 K, increasing the entropy of the transition state.

== Electronic Partition Function

The electronic partition function is the degeneracy of the ground electronic state:

$ z_"elec" = g $

*Given degeneracies:*
- H atom: $g_"H" = #mol_g_H$
- HBr molecule: $g_"HBr" = #mol_g_HBr$
- Transition state: $g^‡ = #mol_g_TS$

= Rate Constant Calculation

== Complete Partition Functions

The total partition functions per unit volume at T = 300 K are calculated by combining all contributions:

$ Z_"H" / V = (z_"trans" / V) dot z_"elec" = #Z_H_V_fmt "m"^(-3) $

$ Z_"HBr" / V = (z_"trans" / V) dot z_"rot" dot z_"vib" dot z_"elec" = #Z_HBr_V_fmt "m"^(-3) $

$ Z^‡ / V = (z_"trans" / V) dot z_"rot" dot z_"vib" dot z_"elec" = #Z_TS_V_fmt "m"^(-3) $

== TST Rate Constant at 300 K

Using @tst-equation with the calculated partition functions:

*Step 1: Prefactor*
$ frac(k_B T, h) = #rate_prefactor "s"^(-1) $

*Step 2: Partition function ratio*
$ frac(Z^‡, Z_"H" dot Z_"HBr") = #rate_partition_ratio "m"^3 $

*Step 3: Boltzmann factor*
$ exp(-frac(E_0, k_B T)) = #rate_boltzmann $

*Step 4: Rate constant*
$ k(300 "K") = #rate_k_300_SI_fmt "m"^3 /("molecule" dot "s") $

*Unit conversions:* $k = #rate_k_300_L_mol_fmt "L"\/("mol"·"s")$

= Results

== Temperature Dependence

The rate constant was calculated over the temperature range 300-1000 K with 50 K increments. 

#figure(
  image("tst_rate_constants.pdf", width: 100%),
  caption: [
Graphical evolution of the rate constant with respect to the temperature
  ]
)

#let results = csv("result.csv")

#figure(
  ztable(
    columns: 4,
    format: ((digits: 0), (digits: 3), (digits: 3), (digits: 3)),
    [T [K]], [k [m³/(molecule·s)]], [k [cm³/(molecule·s)]], [k [L/(mol·s)]],
    ..results.flatten(),
  ),
  caption: [Calculated rate constants at different temperatures]
)

