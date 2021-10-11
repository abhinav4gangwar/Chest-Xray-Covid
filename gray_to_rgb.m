function [output] = gray_to_rgb(direc)
%GRAY_TO_RGB Summary of this function goes here
%   Detailed explanation goes here
for i=3:52
    img_name = direc(i).name;
    img = imread(join(["preprocessed_data/test/covid/",img_name],''));
    disp(img_name);
    rgb=img(:,:,[1 1 1]);
    imwrite(rgb, join(["./preprocessed_data/test/covid1/",img_name],''));
    
    
end
end

