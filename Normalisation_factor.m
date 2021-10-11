function [] = loop(m)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
for i=1:.05:2
    b = normalisation(m,i);
    figure, imshow(b);
end

