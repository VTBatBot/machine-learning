%Main class for the autoregression data preparation 
classdef SonarAnalysis < handle
    properties
       Fs
       WinMin, WinMax, WinStep
       rms_v  %RMS value of the data
    end
    
    methods
        function obj = SonarAnalysis(fs,wni, wnx, wns,rms_v)
            obj.Fs = fs;
            obj.WinMin = wni;
            obj.WinMax = wnx;
            obj.WinStep = wns;
            obj.rms_v = rms_v;
        end
        function dataPrep = AutoRegression(obj, dat, plotARbool)
            win = obj.WinMin:obj.WinStep:obj.WinMax;
            number_of_windows = length(win) - 1;
            niter = 0;
            for i = 1:size(dat,2)
                for j = 1:size(dat,3)
                    niter = niter + 1;
                    for k = 1: number_of_windows                      
                        mn = win(k);
                        mx = win(k+1) - 1;
                        %[ax, px] = sonarAutoRegressive(dat(mn:mx,i,j), ...
                       %     plotARbool, obj.Fs);
                        ax = sonarPeriodogramPieces(dat(mn:mx,i,j), ...
                            obj.Fs);
                        len = length(ax);
                        dataPrep(niter,...
                            1+(len*(k-1)):len*k) = ax';
                        fprintf('%d..%d..%d\n',i,j,k);
                        %pause(0.5);
                    end
                    dataPrep(niter,len*k + 1) = j;
                end
            end
            for ii = 1:size(dataPrep,1)
                for jj = 1:size(dataPrep,2)
                    if isnan(dataPrep(ii,jj))
                        dataPrep(ii,jj) = 0;
                    end
                end
            end
        end    
        function T = CreateDataTable(obj,dataPrep)
            %targWin = zeros(61,1);
            %targWin(11:40) = 1;
            %tw = repmat(targWin,200,1);
            tw = zeros(2000,1); tw(1:1000) = 1;
            T = table(dataPrep(:,1),dataPrep(:,2),dataPrep(:,3),dataPrep(:,4),...,
                      dataPrep(:,5),dataPrep(:,6),dataPrep(:,7),dataPrep(:,8),...
                      dataPrep(:,9),dataPrep(:,10),dataPrep(:,11),dataPrep(:,12),...
                      dataPrep(:,13),dataPrep(:,14),dataPrep(:,15),dataPrep(:,16),...
                      dataPrep(:,17),dataPrep(:,18),dataPrep(:,19),dataPrep(:,20),...
                      dataPrep(:,21),dataPrep(:,22),dataPrep(:,23),dataPrep(:,24),...
                      dataPrep(:,25),dataPrep(:,26),dataPrep(:,27),dataPrep(:,28),...
                      dataPrep(:,29),dataPrep(:,30),dataPrep(:,31),dataPrep(:,32),...
                      dataPrep(:,33),dataPrep(:,34),dataPrep(:,35),dataPrep(:,36),...
                      dataPrep(:,37),dataPrep(:,38),dataPrep(:,39),dataPrep(:,40),...
                      dataPrep(:,41),dataPrep(:,42),dataPrep(:,43),dataPrep(:,44),...
                      dataPrep(:,45),dataPrep(:,46),dataPrep(:,47),dataPrep(:,48),...
                      dataPrep(:,49),dataPrep(:,50),dataPrep(:,51),dataPrep(:,52),...
                      dataPrep(:,53),dataPrep(:,54),dataPrep(:,55),dataPrep(:,56),...
                      dataPrep(:,57),dataPrep(:,58),dataPrep(:,59),dataPrep(:,60),...
                      dataPrep(:,61),dataPrep(:,62),dataPrep(:,63),dataPrep(:,64),...
                      dataPrep(:,65),dataPrep(:,66),dataPrep(:,67),dataPrep(:,68),...
                      dataPrep(:,69),dataPrep(:,70),dataPrep(:,71),dataPrep(:,72),...
                      dataPrep(:,73),dataPrep(:,74),dataPrep(:,75),dataPrep(:,76),...
                      dataPrep(:,77),dataPrep(:,78),dataPrep(:,79),dataPrep(:,80),...
                      dataPrep(:,81),dataPrep(:,82),dataPrep(:,83),dataPrep(:,84),...
                      dataPrep(:,85),dataPrep(:,86),dataPrep(:,87),dataPrep(:,88),...
                      dataPrep(:,89),dataPrep(:,90),dataPrep(:,91),dataPrep(:,92),...
                      dataPrep(:,93),dataPrep(:,94),dataPrep(:,95),dataPrep(:,96),...
                      dataPrep(:,97),dataPrep(:,98),dataPrep(:,99),dataPrep(:,100),...
                      dataPrep(:,101),tw);
            cols = {'w1a1', 'w1a2','w1a3','w1a4','w1a5','w1a6','w1a7','w1a8','w1a9','w1a10','w1a11','w1a12','w1a13','w1a14','w1a15','w1a16','w1a17','w1a18','w1a19','w1a20',...
                'w2a1','w2a2','w2a3','w2a4','w2a5','w2a6','w2a7','w2a8','w2a9','w2a10','w2a11','w2a12','w2a13','w2a14','w2a15','w2a16','w2a17','w2a18','w2a19','w2a20',...
                'w3a1','w3a2','w3a3','w3a4','w3a5','w3a6','w3a7','w3a8','w3a9','w3a10','w3a11','w3a12','w3a13','w3a14','w3a15','w3a16','w3a17','w3a18','w3a19','w3a20',...
                'w4a1','w4a2','w4a3','w4a4','w4a5','w4a6','w4a7','w4a8','w4a9','w4a10','w4a11','w4a12','w4a13','w4a14','w4a15','w4a16','w4a17','w4a18','w4a19','w4a20',...
                'w5a1','w5a2','w5a3','w5a4','w5a5','w5a6','w5a7','w5a8','w5a9','w5a10','w5a11','w5a12','w5a13','w5a14','w5a15','w5a16','w5a17','w5a18','w5a19','w5a20',...
                'azimuth','target'};
            T.Properties.VariableNames = cols;
            
        end
        function dataPlot(obj, dataCompileL, dataCompileR)
            %% Plots data from a given 2 datasets
            % sonar.dataplot(data1, data2)
            close all;
            ff = design(fdesign.bandpass...
                ('N,Fc1,Fc2',512,20e3/(obj.Fs/2),100e3/(obj.Fs/2)));

            xfdcL = zeros(10e3,200,61);
            for iCL = 1:size(dataCompileL,2)
                for jCL = 1:size(dataCompileL,3)
                    xf = filtfilt(ff.Numerator, 1, dataCompileL(:,iCL,jCL));
                    xfdcL(:,iCL,jCL) = abs(hilbert(xf));        
                end
            end
            %%
            xfdcR = zeros(10e3,200,61);
            for iCR = 1:size(dataCompileR,2)
                for jCR = 1:size(dataCompileR,3)
                    xf = filtfilt(ff.Numerator, 1, dataCompileR(:,iCR,jCR));
                    xfdcR(:,iCR,jCR) = abs(hilbert(xf));        
                end
            end

            %%
            xplt = squeeze(mean(xfdcL,2));
            xplt12 = xplt./(max(max(xplt)));
            xpltdB = mag2db(xplt12);
            xpltdB = medfilt2(xpltdB);
            figure; imagesc(xpltdB);
            set(gca,'Ydir','normal');
            ylim([3000,4250]);
            caxis([-25,0]);
            colormap('jet')

            xplt2 = squeeze(mean(xfdcR,2));
            xplt22 = xplt2./(max(max(xplt2)));
            xpltdB2 = mag2db(xplt22);
            xpltdB2 = medfilt2(xpltdB2);
            figure; imagesc(xpltdB2);
            set(gca,'Ydir','normal');
            ylim([3000,4250]);
            caxis([-25,0]);

            colormap('jet')

            %%
            prepIM(1,'fol_left_stc');
            prepIM(2,'fol_right_stc');
        end
    end
    methods(Static)
         function CompileData()
            fprintf('Working...\n');
            dataCompile('cylinder_middle\dynamic','cylinder_middle_dyn');
            fprintf('Compiled 1/6 datasets\n');
            dataCompile('cylinder_middle\static','cylinder_middle_stc');
            fprintf('Compiled 2/6 datasets\n');
            dataCompile('cube_middle\dynamic','cube_middle_dyn');
            fprintf('Compiled 1/6 datasets\n');
            dataCompile('cube_middle\static','cube_middle_stc');
            fprintf('Compiled 2/6 datasets\n');
            dataCompile('disc_middle\dynamic','disc_middle_dyn');
            fprintf('Compiled 3/6 datasets\n');
            dataCompile('disc_middle\static','disc_middle_stc');
            fprintf('Compiled 4/6 datasets\n');
            dataCompile('sphere_middle\dynamic','sphere_middle_dyn');
            fprintf('Compiled 5/6 datasets\n');
            dataCompile('sphere_middle\static','sphere_middle_stc');
            fprintf('Compiled 6/6 datasets\n');
            fprintf('\n\nJob Complete');

         end
         function ExportToCSV(T, name)
         writetable(T,[name '.csv']);
         end
    end
end