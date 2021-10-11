function [output] = batch_resizing(a,b,c,d)
%LOOP Summary of this function goes here
%   Detailed explanation goes here

for i=3:52
    img_name = a(i).name;
    img = imread(join(["./2/test/covid/",img_name],''));
    disp(img_name);
    resized = imresize (img,[224,224]); 
    imwrite(resized, join(["./2/test/covid/",img_name],'')); 
end

for i=3:52
    img_name = b(i).name;
    img = imread(join(["./2/test/normal/",img_name],''));
    disp(img_name);
    resized = imresize (img,[224,224]); 
    imwrite(resized, join(["./2/test/normal/",img_name],'')); 
end

for i=3:515
    img_name = c(i).name;
    img = imread(join(["./2/train/covid/",img_name],''));
    disp(img_name);
    resized = imresize (img,[224,224]); 
    imwrite(resized, join(["./2/train/covid/",img_name],'')); 
end

for i=3:319
    img_name = d(i).name;
    img = imread(join(["./2/train/normal/",img_name],''));
    disp(img_name);
    resized = imresize (img,[224,224]); 
    imwrite(resized, join(["./2/train/normal/",img_name],'')); 
end

end