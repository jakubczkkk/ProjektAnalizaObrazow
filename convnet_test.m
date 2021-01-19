load convnet

testing_data_store = imageDatastore('./images/fruits/testprep/',...
    'IncludeSubfolders', true, 'FileExtensions', {'.png', '.jpg'}, 'LabelSource', 'foldernames');

[pred, scores] = classify(convnet, testing_data_store)