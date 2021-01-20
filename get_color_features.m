function [color_features] = get_color_features(image)
   
    [rows cols ch] = size(image);
    dx =  floor(rows/2);
    dy =  floor(cols/2);
    x =  floor(rows/4);
    y =  floor(cols/4);
    
    temp = image(x:x+dx, y:y+dy,:);
    [~,idx] = max(sum(sum(image,1),2),[],3);

    [color_features] = [0 0 0];
    color_features(idx) = 1;