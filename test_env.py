import sys
import lifelines
import matplotlib
import numpy as np
import pandas as pd
import scipy
import seaborn as sns
import sklearn
import statsmodels

print("=" * 50)
print(f"Python Version: {sys.version.split()[0]}")
print("SUCCESS: All core packages imported correctly!")
print("=" * 50)
print(f"Pandas version:      {pd.__version__}")
print(f"NumPy version:       {np.__version__}")
print(f"SciPy version:       {scipy.__version__}")
print(f"Statsmodels version: {statsmodels.__version__}")
print(f"Scikit-Learn version:{sklearn.__version__}")
print(f"Lifelines version:   {lifelines.__version__}")
print(f"Seaborn version:     {sns.__version__}")
print("=" * 50)
print("Environment is ready for Week 1!")
