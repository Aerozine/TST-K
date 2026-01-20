# TST-K: Transition State Theory Rate Constant Calculator

Calculate the rate constant for the H + HBr → H₂ + Br reaction using Transition State Theory. This implementation computes molecular partition functions (translational, rotational, vibrational, electronic) from first principles and applies the Eyring equation to determine reaction rates across 300-1000 K.

### Usage

**Calculate rate constants:**
```bash
python run.py
```
Generates rate constants from 300-1000 K and creates a visualization plot.

**Generate Typst constants for reports:**
```bash
python gen_typcst.py
```
Creates `constants.typ` with formatted values for technical documents.

## Files

- `constants.py` - Physical constants and molecular parameters
- `partfunc.py` - Partition function calculations  
- `ratecst.py` - TST rate constant implementation
- `run.py` - Main execution script
- `gen_typcst.py` - Export values for Typst reports

## Documentation

See `report.pdf` for complete theoretical background and detailed results.

---

**Academic Project** - CHIM9308-1 Physical Chemistry, ULiège (2025-2026)  
Author: Loïc Delbarre (S215072)
