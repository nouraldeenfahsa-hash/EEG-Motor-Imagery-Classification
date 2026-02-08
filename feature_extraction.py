# feature_extraction.py
from mne.decoding import CSP

# Assume epochs is loaded
# epochs = mne.Epochs(...)

# CSP feature extraction
csp = CSP(n_components=4, reg='empirical', log=True)
X = epochs.get_data(picks=['C3', 'C4'])
y = epochs.events[:, -1]
csp.fit(X, y)
features = csp.transform(X)

print("CSP features shape:", features.shape)
