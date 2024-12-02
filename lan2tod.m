function lanedelay = lan2tod(A2,y,x)
    lanedelay=0;x(1:20)=round(x(1:20));C(1)=sum(x(1:4));C(2)=sum(x(5:8));C(3)=sum(x(9:12));C(4)=sum(x(13:16));C(5)=sum(x(17:20));
    y=round(y);y(2)=y(1)+y(2);y(3)=y(2)+y(3);y(4)=y(3)+y(4);
    for i = 1 : 8
    switch i
        case 1
        lanedelay=lanedelay+tod2ten(A2(:,:,i),y,C,[x(1) x(5) x(9) x(13) x(17)],zeros(1,5));
        case 2
        lanedelay=lanedelay+tod2ten(A2(:,:,i),y,C,[x(4) x(7) x(12) x(15) x(20)],[C(1)-x(4) x(5)+x(6) C(3)-x(12) x(13)+x(14) C(5)-x(20)]);
        case 3
        lanedelay=lanedelay+tod2ten(A2(:,:,i),y,C,[x(4) x(7) x(11) x(15) x(20)],[C(1)-x(4) x(5)+x(6) x(9)+x(10) x(13)+x(14) C(5)-x(20)]);
        case 4
        lanedelay=lanedelay+tod2ten(A2(:,:,i),y,C,[x(2) x(6) x(10) x(14) x(18)],[x(1) x(5) x(9) x(13) x(17)]);
        case 5        
        lanedelay=lanedelay+tod2ten(A2(:,:,i),y,C,[x(2) x(5) x(9) x(13) x(18)],[x(1) 0 0 0 x(17)]);
        case 6        
        lanedelay=lanedelay+tod2ten(A2(:,:,i),y,C,[x(3) x(8) x(12) x(16) x(19)],[x(1)+x(2) C(2)-x(8) C(3)-x(12) C(4)-x(16) x(17)+x(18)]);
        case 7        
        lanedelay=lanedelay+tod2ten(A2(:,:,i),y,C,[x(3) x(8) x(11) x(16) x(19)],[x(1)+x(2) C(2)-x(8) x(9)+x(10) C(4)-x(16) x(17)+x(18)]);
        case 8
        lanedelay=lanedelay+tod2ten(A2(:,:,i),y,C,[x(1) x(6) x(10) x(14) x(17)],[0 x(5) x(9) x(13) 0]);
    end
    end
        
end