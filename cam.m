camera = webcam;
camera.Resolution = '1280x720';

figure;
for i = 1:2000
    image = snapshot(camera);
    image = cast(image, 'double');
    image = image/255.0;
    image = imresize(image, [300, 300]);
    [new_row, vis] = extractHOGFeatures(image, 'CellSize', [30,30]);
    
  
    imshow(image);
    hold on;
    plot(vis);
    
    new_column = transpose(new_row);
    prediction = trainedModel1.predictFcn(new_column);
    if prediction == 1
       text(20,20, 'Jablko', 'Color', 'red', 'FontSize', 20); 
    elseif prediction == 2
       text(20,20, 'Banan', 'Color', 'yellow', 'FontSize', 20);
    end

end
