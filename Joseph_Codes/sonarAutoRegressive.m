function [ax,px]  = sonarAutoRegressive(data, plotARbool, Fs)
   
    p = 19;
    [ax, px] = aryule(data, p);
    
    if plotARbool
        plotAR(data, ax, px, Fs)
    end
    
    function plotAR(data, ax, px, Fs)
    [H1,w1] = freqz(sqrt(px),ax);
    figure;
    len = length(data);
    itv = Fs/(512*2);
%     periodogram(data,kaiser(len),512, Fs)
    periodogram(data)
    hold on
    hp = plot(w1/pi,20*log10(2*abs(H1)/(2*pi)),'r'); % Scale to make one-sided PSD
%     hp = plot(itv:itv:Fs/2,20*log10(2*abs(H1)/(2*pi)),'r')
    hp.LineWidth = 2;
    xlabel('Normalized frequency (\times \pi rad/sample)')
    ylabel('One-sided PSD (dB/rad/sample)')
    legend('PSD estimate of x','PSD of model output')

    end
end