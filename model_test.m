load app_model;

testing_data_store = imageDatastore('./images/fruits/test/',...
    'IncludeSubfolders', true, 'FileExtensions', '.png', 'LabelSource', 'foldernames');

testing_labeled_count = countEachLabel(testing_data_store);

testing_image_count = [0];
for i = 1:size(testing_labeled_count,2)
    testing_image_count = testing_image_count + testing_labeled_count{i,2};
end

testing_labels = [];
k = 0;
for i = 1:size(testing_labeled_count, 2)  
   for j = 1:testing_labeled_count{i,2}
       k = k+1;
       testing_labels(k) = i; 
   end
end

HOG = [];
res = [];

for i = 1:testing_image_count
    image = readimage(testing_data_store, i);
    hog_values = hog(image);
    res = [res ; app_model.predictFcn(hog_values)]
end
