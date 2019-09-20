data = dataCompileL;
    p = 19;
    a = zeros(size(data));
    i = 1;
    j = 1;
    %for i = 1:size(data,2)
     %   for j = 1:size(data,3)
            [a1, p1] = aryule(data(1:2500,i,j), p);
            [a2, p2] = aryule(data(2501:5000,i,j), p);
            [a3, p3] = aryule(data(5001:7500,i,j), p);
            [a4, p4] = aryule(data(7501:10000,i,j), p);
            [ax, px] = aryule(xdata(3001:3250),p);
      %  end
    %end
    data1 = data(1:2500,i,j);
    data2 = data(2501:5000,i,j);
    data3 = data(5001:7500,i,j);
    data4 = data(7501:10000,i,j);

    [H1,w1] = freqz(sqrt(px),ax);
    myFunction(true)
    figure;
    periodogram(xdata)
    hold on
    hp = plot(w1/pi,20*log10(2*abs(H1)/(2*pi)),'r'); % Scale to make one-sided PSD
    hp.LineWidth = 2;
    xlabel('Normalized frequency (\times \pi rad/sample)')
    ylabel('One-sided PSD (dB/rad/sample)')
    legend('PSD estimate of x','PSD of model output')

    function myFunction(doStuff)
    if doStuff
    fprintf('hi')
    end
    end