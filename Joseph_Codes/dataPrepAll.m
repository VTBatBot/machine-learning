
for i = 1:61
n1 = i;
n2 = i;

load('cube_middle_stc_right.mat')
dataPrep = sonar.AutoRegression(dataCompileR(:,:,n1:n2));
load('sphere_middle_stc_right.mat')
dataPrep2 = sonar.AutoRegression(dataCompileR(:,:,n1:n2));
load('cylinder_middle_stc_right.mat')
dataPrep3 = sonar.AutoRegression(dataCompileR(:,:,n1:n2));
load('disc_middle_stc_right.mat')
dataPrep4 = sonar.AutoRegression(dataCompileR(:,:,n1:n2));
load('fol_solo_stc_right.mat')
dataPrep5 = sonar.AutoRegression(dataCompileR(:,:,n1:n2));

dataPrep = dataPrep(:,1:250)./max(max(dataPrep(:,1:250)));
dataPrep2 = dataPrep2(:,1:250)./max(max(dataPrep2(:,1:250)));
dataPrep3 = dataPrep3(:,1:250)./max(max(dataPrep3(:,1:250)));
dataPrep4 = dataPrep4(:,1:250)./max(max(dataPrep4(:,1:250)));
dataPrep5 = dataPrep5(:,1:250)./max(max(dataPrep5(:,1:250)));

dataset = [dataPrep;dataPrep2;dataPrep3;dataPrep4;dataPrep5];
targets3 = zeros(1,1000);
targets3(201:400) = 1; targets3(401:600) = 2; targets3(601:800) = 3;
targets3(801:1000) = 4;
dataset(:,251) = targets3;

save(sprintf('dataset_stc%d%df.dat',n1,n2),'dataset','-ascii');
fprintf('%d of 61 completed',i);
end
%%
for i = 1:61
dat = cube.data.xdata;
dat = double(dat(:,:,i+10:i+10));
dataOGScb = sonar.AutoRegression(dat);
 
dat = sph.data.xdata;
dat = double(dat(:,:,i+10:i+10));
dataOGSph = sonar.AutoRegression(dat);
dataPrepx_og = dataOGScb(:,1:250)./max(max(dataOGScb(:,1:250)));
dataPrep2x_og = dataOGSph(:,1:250)./max(max(dataOGSph(:,1:250)));
datasetx_og = [dataPrepx_og; dataPrep2x_og];
targets2 = zeros(1,500);
targets2(251:500) = 1;
datasetx_og(:,251) = targets2;
save(sprintf('datasetx_og%d.dat', i),'datasetx_og','-ascii');
end