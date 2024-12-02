function totmv = tod2tenR(A2,Y,C,X,R)
   a=zeros(800,4);delay=zeros(4,5);gamma=2.1;%veh=zeros(144,1);%Y=round(sort(Y));X=round(X);R=round(R);
for j = 1 : 7
    for i = 1 : 288
        if i == 1
            [a(i,1),a(i,2),a(i,3),a(i,4)]=ten2cycIII(0,A2(j,i),0,C(1),X(1),R(1),0);
        elseif  i<=Y(1)&&i>1
            [a(i,1),a(i,2),a(i,3),a(i,4)]=ten2cycIII(a(i-1,3),A2(j,i),a(i-1,2),C(1),X(1),R(1),a(i-1,4));
        elseif i <=Y(2)&&i>Y(1)
            [a(i,1),a(i,2),a(i,3),a(i,4)]=ten2cycIII(a(i-1,3),A2(j,i),a(i-1,2),C(2),X(2),R(2),a(i-1,4));
        elseif i <=Y(3)&&i>Y(2) 
            [a(i,1),a(i,2),a(i,3),a(i,4)]=ten2cycIII(a(i-1,3),A2(j,i),a(i-1,2),C(3),X(3),R(3),a(i-1,4));
        elseif i <=Y(4)&&i>Y(3)
            [a(i,1),a(i,2),a(i,3),a(i,4)]=ten2cycIII(a(i-1,3),A2(j,i),a(i-1,2),C(4),X(4),R(4),a(i-1,4));
        %elseif Y(4)< i <=Y(5)
        %    [a(i,1),a(i,2),a(i,3),a(i,4)]=ten2cycIII(a(i-1,3),A2(i),a(i-1,2),C(5),X(5),0,a(i-1,4));           
        %elseif Y(5)< i <=Y(6) 
        %    [a(i,1),a(i,2),a(i,3),a(i,4)]=ten2cycIII(a(i-1,3),A2(i),a(i-1,2),C(6),X(6),0,a(i-1,4));   
        elseif i<=288&&i>Y(4)
            [a(i,1),a(i,2),a(i,3),a(i,4)]=ten2cycIII(a(i-1,3),A2(j,i),a(i-1,2),C(5),X(5),R(5),a(i-1,4));
        end       
    end

    TODdelay(1)=sum(a(1:Y(1),1));TODdelay(2)=sum(a(Y(1)+1:Y(2),1));TODdelay(3)=sum(a(Y(2)+1:Y(3),1));
    TODdelay(4)=sum(a(Y(3)+1:Y(4),1));TODdelay(5)=sum(a(Y(4)+1:288,1));
    TODrem=[a(Y(1),4) a(Y(2),4) a(Y(3),4) a(Y(4),4) a(288,4)];
    delay(j,:)=TODdelay;
    
end

    var=sum(std(delay,1,1));
    totmv=sum(delay(:))/4+gamma*var;
end