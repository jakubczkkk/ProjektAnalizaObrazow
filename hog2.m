function [featureVector] = hog2(image)

im = image;
imageSize = 256;
cellSize = 32;
im = imresize(im, [imageSize imageSize]);

featureVector = extractHOGFeatures(im, 'CellSize', [cellSize cellSize]);

end