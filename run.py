from constants import *
from ratecst import *
import matplotlib.pyplot as plt

temperatures = np.arange(300, 1001, 50)
rate_constants = np.array([calculate_rate_constant(T) for T in temperatures])

# Convert to different units
k_SI = rate_constants  # m³/(molecule·s)
k_cm3 = rate_constants * 1e6  # cm³/(molecule·s)
k_molar = rate_constants * N_A * 1000  # L/(mol·s)
np.savetxt(
    "result.csv",
    np.column_stack((temperatures, k_SI, k_cm3, k_molar)),
    delimiter=","
)
plt.figure()
plt.plot(temperatures, k_molar, 'o-', linewidth=2, markersize=6)
plt.xlabel('Temperature [K]', fontsize=12)
plt.ylabel(r'$K [L/(mol . s)]$', fontsize=12)
plt.title('Rate Constant vs Temperature (molar units)', fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3, which='both')
plt.tight_layout()
plt.savefig('tst_rate_constants.pdf', dpi=300, bbox_inches='tight')
plt.show()
