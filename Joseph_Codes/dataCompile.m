%% dataCompile: take data from .txt created by sonar head on pan-tilt
function dataCompile(folderName, dataIDname)
% folderName = 'cube_middle\dynamic';
% dataIDname = 'cube_middle_dyn';

home = pwd;
cd(folderName);
lib = dir(pwd);
dirLocS = find([lib.isdir]);
dirName = zeros(length(dirLocS),1);
for i = 1:length(dirLocS)
    name = lib(i).name;
    dirName(i) = str2double(name);
end
dataLoc = find(dirName < 1e6);

dirNameData = dirName(~isnan(dirName));
dirNameData = dirNameData + 31;
for i = 1:length(dirNameData)
    if (isnan(dirNameData(i)) || dirNameData(i) > 61)
        error('fix data naming');
    end
end
dataCompileL = zeros(10E3,200,61);
dataCompileR = zeros(10E3,200,61);
for i = 1:length(dataLoc)
   cd(lib(dataLoc(i)).name);
   k = dirNameData(i);
   dataLib = dir(pwd);
   dataFiles = find(~[dataLib.isdir]);
   for j = 1:length(dataFiles)
%        d = zeros(20000,1);
%        dx = load(dataLib(dataFiles(j)).name);
%        d(1:length(dx)) = dx;
        d = load(dataLib(dataFiles(j)).name);
       try
       dataCompileL(:,j,k) = d(1:10000); 
       dataCompileR(:,j,k) = d(10001:20000);
       catch
           fprintf('failed at %d_%d_%d\n',i,j,k)
       end
   end
   cd ..
   
end

cd(home);
% save([dataIDname '_left' '.mat'],'dataCompileL');
% save([dataIDname '_right' '.mat'],'dataCompileR');

