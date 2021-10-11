function [norm] = preprocessing(img)
%PREPROCESSING Summary of this function goes here
%   Detailed explanation goes here
resized = imresize (img,[255,255]);  %resizing image
if ndims(resized) == 3
    bw = rgb2gray(resized);      %color to bw
else
    bw = resized;
end
contrast = imadjust(bw); %contrast enhancing
norm = normalisation(contrast,1.2);  %normalising image

end

