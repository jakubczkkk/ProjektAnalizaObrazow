clc;
clearvars;
% defining storages for images
training_data_store = imageDatastore('./images/fruits/train/',...
    'IncludeSubfolders', true, 'FileExtensions', {'.png', '.jpg'}, 'LabelSource', 'foldernames');


training_labeled_count = countEachLabel(training_data_store)

% 
% labels for network output testing
training_labels = [];
k = 0;
for i = 1:size(training_labeled_count, 1)  
   for j = 1:training_labeled_count{i,2}
       k = k+1;
       training_labels = [training_labels training_labeled_count{i,1}]; 
   end
end

% done labels
training_labels = training_labels.';

% amount of images used for training
training_image_count = [0];
for i = 1:size(training_labeled_count,1)
    training_image_count = training_image_count + training_labeled_count{i,2};
end

HOG = [];
for i = 1:training_image_count
    image = readimage(training_data_store, i);
    color_f = get_color_features(image);
    new_row = hog(image);
    HOG = [HOG ; [new_row color_f]];
end