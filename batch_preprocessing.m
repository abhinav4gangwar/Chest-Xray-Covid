function [output] = image_loader(direc)
%LOOP Summary of this function goes here
%   Detailed explanation goes here

for i=3:932
    img_name = direc(i).name;
    img = imread(join(["raw_data/images/",img_name],''));
    disp(img_name);
    preprocessed_image = preprocessing(img);
    imwrite(preprocessed_image, join(["./preprocessed_data/images/",img_name],''));
    
    
end

end

