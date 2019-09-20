function pxx = sonarPeriodogramPieces(dat, Fs)
Fs = 400e3;
hann_win = hann(length(dat));
freqs = [20e3:(60/50)*1000:79e3];
[pxx,f] = periodogram(dat,hann_win,freqs,Fs);
