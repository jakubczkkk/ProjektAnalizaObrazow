function [featureVector] = hog2(image)

im = image;
imageSize = 256;
cellSize = 32;
im = imresize(im, [imageSize imageSize]);

featureVector1 = extractHOGFeatures(im, 'CellSize', [cellSize cellSize]);
image = rgb2gray(image);
featureVector2 = extractLBPFeatures(image);
featureVector = [featureVector1 featureVector2 ];
end