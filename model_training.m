% defining storages for images
training_data_store = imageDatastore('./images/fruits/train/',...
    'IncludeSubfolders', true, 'FileExtensions', '.png', 'LabelSource', 'foldernames');


training_labeled_count = countEachLabel(training_data_store);

% labels for network output testing
training_labels = [];
k = 0;
for i = 1:size(training_labeled_count, 2)  
   for j = 1:training_labeled_count{i,2}
       k = k+1;
       training_labels(k) = i; 
   end
end

% done labels
training_labels = training_labels.';

% amount of images used for training
training_image_count = [0];
for i = 1:size(training_labeled_count,2)
    training_image_count = training_image_count + training_labeled_count{i,2};
end

HOG = [];
for i = 1:training_image_count
    image = cast(readimage(training_data_store, i), 'double');
    image = image/255.0;
    image = imresize(image, [300, 300]);
    [new_row, vis] = extractHOGFeatures(image, 'CellSize', [30,30]);
    new_column = transpose(new_row);
    HOG = [HOG new_column];
end




