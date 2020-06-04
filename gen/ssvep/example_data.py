import mne
import os.path

length = 5
samplefreq = 256
nelectrodes = 10
stimfreq = 15
nepochs = 20

rootpath, _ = os.path.split(__file__)
epochfile = os.path.join(rootpath, "data", "example-epo.fif")
epoch_example = mne.read_epochs(epochfile)
