load app_model;

camera = webcam;
camera.Resolution = '640x480';

figure;
for i = 1:2000
    image = snapshot(camera);
  
    imshow(image);
    hold on;
    
    hog_values = hog(image);
    prediction = app_model.predictFcn(hog_values);
    
    if prediction == 1
       text(20,20, 'Jablko', 'Color', 'red', 'FontSize', 20); 
    elseif prediction == 2
       text(20,20, 'Banan', 'Color', 'yellow', 'FontSize', 20);
    end
end
