
for j = 1 : 7
for i = 1 : 288
    Asum(j,i)=sum(lana2vol(j,i,1:8));
end
end
xx(2,:)=mean(Asum,1);
xx(1,:)=1:288;
[IDX,C]=kmeans(xx',5);
plot(IDX,'*');