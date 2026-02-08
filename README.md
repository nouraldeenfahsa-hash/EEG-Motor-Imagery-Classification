# EEG-Motor-Imagery-Classification
EEG-based classification of hand open/close and wrist rotation for BCI prosthetic control – Work in progress for MICCAI 2026
# EEG Motor Imagery Classification for BCI

This project focuses on classifying motor imagery tasks (hand open/close and wrist rotation) from EEG signals to control a transradial prosthetic hand.

## Current Status
- Preprocessing: Filtering, artifact removal using MNE-Python
- Features: CSP + band power (alpha/beta)
- Classifier: SVM / LDA (accuracy XX% with cross-validation)
- Paper: Work in progress – submitted to MICCAI 2026 (pending)

## Technologies
- Python, MNE, scikit-learn, NumPy, Matplotlib

## How to run
1. Install dependencies: `pip install mne scikit-learn numpy matplotlib`
2. Run `preprocessing.py` for data loading
3. Run `classification.ipynb` for model training

## Contact
Nour Aldeen Fahsa  
Email: nouraldeenfahsa@gmail.com  
LinkedIn: linkedin.com/in/nouraldeenfahsa
