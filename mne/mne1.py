from mne.io import concatenate_raws, read_raw_edf
import matplotlib.pyplot as plt


raw=read_raw_edf('E:\桌面\EEGdata\Subject01_1 - 副本.edf',preload=False)
events_from_annot, event_dict = mne.events_from_annotations(raw)
print(event_dict)
print(events_from_annot)
print(raw.info)
raw.plot(duration=5, n_channels=32, clipping=None)
plt.show()