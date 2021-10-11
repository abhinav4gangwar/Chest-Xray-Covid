function [b] = normalisation(a,step)
%NORMALISATION Summary of this function goes here
%   Detailed explanation goes here
maxi = double(max(max(a)));
mini = double(min(min(a)));


[m n] = size(a);

min_mat = ones(m,n)*mini;

b = ((double(a)-min_mat).*step/(maxi-mini));

end


