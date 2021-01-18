function [featureVector] = hog(imageName)

im = imread(imageName);
imageSize = 256;
cellSize = 16;
im = imresize(im, [imageSize imageSize]);

% konwersja do szarosci
new_im = double(rgb2gray(im)) / 255;

Gx = zeros(imageSize, imageSize);
Gy = zeros(imageSize, imageSize);

% liczymy gradienty
for i = 2:imageSize-1
    for j = 2:imageSize-1
        
        Gx(i, j) = new_im(i-1, j) - new_im(i+1, j);
        Gy(i, j) = new_im(i, j-1) - new_im(i, j+1);
        
    end
end

angle = atand(Gx ./ Gy);
angle = imadd(angle, 90);
magnitude = sqrt(Gx.^2 + Gy.^2);

angle(isnan(angle)) = 0;
magnitude(isnan(magnitude)) = 0;

featureVector = [];

% petla po blokach

for i = 1:imageSize/cellSize-1
    
    for j = 1:imageSize/cellSize-1
       
        angleFromCurrentBlock = angle(cellSize*(i-1)+1 : cellSize*(i-1)+cellSize*2, cellSize*(j-1)+1 : cellSize*(j-1)+cellSize*2);
        magnitudeFromCurrentBlock = magnitude(cellSize*(i-1)+1 : cellSize*(i-1)+cellSize*2, cellSize*(j-1)+1 : cellSize*(j-1)+cellSize*2);
        
        blockFeatureVector = [];
        
        % petla po komorkach w bloku
        
        for a = 1:2
            
            for b = 1:2
                
                % petla po pikselach w komorce
                
                bins = zeros(1, 9);
                
                for k = 1:cellSize

                    for l = 1:cellSize

                        pixelAngle = angleFromCurrentBlock(k + cellSize *(a-1), l + cellSize *(b-1));
                        pixelMagnitude = magnitudeFromCurrentBlock(k + cellSize *(a-1), l + cellSize *(b-1));

                        if pixelAngle <= 10
                            bins(9) = bins(9) + pixelMagnitude * (10 - pixelAngle) / 20;
                            bins(1) = bins(1) + pixelMagnitude * (pixelAngle + 10) / 20;
                        elseif pixelAngle <= 30
                           bins(1) = bins(1) + pixelMagnitude * (30 - pixelAngle) / 20;
                           bins(2) = bins(2) + pixelMagnitude * (pixelAngle - 10) / 20;
                        elseif pixelAngle <= 50
                           bins(2) = bins(2) + pixelMagnitude * (50 - pixelAngle) / 20;
                           bins(3) = bins(3) + pixelMagnitude * (pixelAngle - 30) / 20;
                        elseif pixelAngle <= 70
                           bins(3) = bins(3) + pixelMagnitude * (70 - pixelAngle) / 20;
                           bins(4) = bins(4) + pixelMagnitude * (pixelAngle - 50) / 20;
                        elseif pixelAngle <= 90
                           bins(4) = bins(4) + pixelMagnitude * (90 - pixelAngle) / 20;
                           bins(5) = bins(5) + pixelMagnitude * (pixelAngle - 70) / 20;
                        elseif pixelAngle <= 110
                           bins(5) = bins(5) + pixelMagnitude * (110 - pixelAngle) / 20;
                           bins(6) = bins(6) + pixelMagnitude * (pixelAngle - 90) / 20;
                        elseif pixelAngle <= 130
                           bins(6) = bins(6) + pixelMagnitude * (130 - pixelAngle) / 20;
                           bins(7) = bins(7) + pixelMagnitude * (pixelAngle - 110) / 20;
                        elseif pixelAngle <= 150
                           bins(7) = bins(7) + pixelMagnitude * (150 - pixelAngle) / 20;
                           bins(8) = bins(8) + pixelMagnitude * (pixelAngle - 130) / 20;
                        elseif pixelAngle <= 170
                           bins(8) = bins(8) + pixelMagnitude * (170 - pixelAngle) / 20;
                           bins(9) = bins(9) + pixelMagnitude * (pixelAngle - 150) / 20;
                        elseif pixelAngle <= 180
                           bins(9) = bins(9) + pixelMagnitude * (190 - pixelAngle) / 20;
                           bins(1) = bins(1) + pixelMagnitude * (pixelAngle - 170) / 20;
                        end

                    end

                end
                
                bins(isnan(bins)) = 0;
                blockFeatureVector = [blockFeatureVector, bins];
                
            end
            
        end
        
        % po zebraniu bins ze wszystkich komórek z bloku, normalizujemy
        % blockFeatureVector
        
        blockFeatureVector = blockFeatureVector / sqrt(sum(blockFeatureVector.^2) + .001);
        
        featureVector = [featureVector, blockFeatureVector];
        
    end
    
end