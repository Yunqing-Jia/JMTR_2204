function [D,D2,A11,rem] = ten2cycIII(A1,A2,D1,C,g,r1,rem)
    k=(A2-A1)/(300+rem);n=floor((300+rem)/C);rem=mod(300+rem,C);GA1=A1;%C=round(C);
    A1=A1-D1;D=0;a1=zeros(1,n);u=zeros(1,n);d1=zeros(1,n+1);g=g-3;s=900/3600;%A2=A2-D1;
    X=k/(s*g/C);%tu=min(n*C,A1/(s*g/C*(1-min(1,X))));
    if n*k ~= 0
    for i = 1 : n
        a1(i)=k*(i-1)*C+A1-d1(i);
        %a2(i)=k*i*C+A1-d1(i);
        u(i)=(a1(i)+r1*k)/(s-k);
        
            if u(i)<=g&&u(i)>=0 %k*g+a1(i) <= 0.5*g
            D=D+0.5*u(i)*u(i)*s+0.5*(g-u(i))*(u(i)*s+k*(r1+g)+a1(i))+(k*(r1+g)+a1(i))*(C-r1-g)+d1(i)*C+D1*C;
            d1(i+1)=d1(i)+k*(g+r1)+a1(i);
            
            else
            D=D+0.5*g*s*g+g*s*(C-g-r1)+d1(i)*C+D1*C;            
            d1(i+1)=d1(i)+g*s;
            end
        %D=D+0.5*C*(1-g/C)^2/(1-min(1,X)*g/C)+900/12*(X-1+((X-1)^2+4*X/C*12)^0.5);

        
    end

    D2=D1+d1(n+1);
    a11=k*n*C;
    A11=GA1+a11;
    %if n*k ~= 0
    
    D=0.5*(GA1+A11)*n*C-D;D=D/k/n/C;
    %    if X < 0.85
    %        D=D;%+0.5*C*(1-g/C)^2/(1-k/s);
    %    elseif X > 1.15
    %        D=D;%+0.5*n*C*(X-1);
    %    else
    %        D=D+0.25*(s*g/C)*(n*C/3600)*(X-1+((X-1)^2+12*(X-0.67+s*g/600)/(n*C/3600)/(s*g/C))^0.5);
    %    end
    
    D=D+900*n*C*(X-1+((X-1)^2+4*X/(s*g/C*n*C))^0.5);%D=D/a11;
    
    
    %D=0.5*C*(1-g/C)*tu/n/C+0.5*C*(1-g/C)^2/(1-min(1,X)*g/C)*(n*C-tu)/n/C+900*n*C*(X-1+((X-1)^2+4*X/(s*g/C*n*C))^0.5)+(tu==n*C)*(3600*A1/(s*g/C)-1800*n*C*(1-min(1,X)))+(tu<n*C)*(1800*A1*tu/(s*g/C*n*C));

    %D=D+0.5*C*(1-g/C)^2/(1-min(1,X)*g/C)+900/12*(X-1+((X-1)^2+4*X/C*12)^0.5);
    
    else
        D=0;A11=GA1;D2=D1;
    end
    
end