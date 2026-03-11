# Bacteria Simulator

## Version 1.1

### Improvements
- Replaced fixed environmental death modifiers with dynamic stress calculations
- Temperature, pH, humidity, and nutrients now scale gradually with environmental deviation
- Improved realism of bacteria survival under unstable conditions

### Simulation Changes
- Temperature stress increases deaths gradually based on distance from optimal range
- pH stress now scales with distance from neutral (pH 7)
- Humidity stress scales with deviation from ideal humidity
- Nutrient stress dynamically affects survival rate

### Repository Improvements
- Added .gitignore to remove unnecessary files
- Removed PyCharm configuration and cache files
- Cleaned repository structure