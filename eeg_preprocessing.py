# eeg_preprocessing.py
import mne
import numpy as np

# Load EEG data
raw = mne.io.read_raw_edf('path/to/your/edf/file.edf', preload=True)

# Filter 1-40 Hz
raw.filter(1, 40, fir_design='firwin')

# Plot raw data
raw.plot(duration=10, n_channels=10, scalings='auto')

print("Preprocessing complete! Filtered data ready for analysis.")
