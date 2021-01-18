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
    image = cast(readimage(testing_data_store, i), 'double');
    image = image/255.0;
    image = imresize(image, [300, 300]);
    [new_row, vis] = extractHOGFeatures(image, 'CellSize', [30,30]);
    new_column = transpose(new_row);
    res = [res trainedModel1.predictFcn(new_column)]
end

% difss = res ~= testing_labels;
% 
% proc = 100 * (cast(testing_image_count, 'double'))-...
%     (cast(sum(diffs), 'double'))/(cast(testing_image_count,'double'))