function prepIM(h,name)
figure(h)
set(gca,'position',[0,0,1,1]);
cd('FIGS');
saveas(h,[name '.jpg']);
cd ..;