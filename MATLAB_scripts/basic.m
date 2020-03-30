
close all;

topics = {'/vibe_ros/left/image_rect_raw','/vibe_ros/right/image_rect_raw'};


disp('Loading Rosbag to Memory')
bagSelect = loadRosbag('../vibe_0322_run1.bag',topics);
disp('Generating Message One by One')

% left camera
N_images = bagSelect(1).NumMessages;

figure(1)
%initialise
tempimg = readMessages(bagSelect(1),1);
subplot(1,2,1);
hs1 = imshow(I1);
subplot(1,2,2);
hs2 = imshow(I2);

for i = 1:N_images
    leftCam = readMessages(bagSelect(1),i);
    rightCam = readMessages(bagSelect(2),i);
    
    I1 = readImage(leftCam{1});
    I2 = readImage(rightCam{1});
    
    subplot(1,2,1);
    title(num2str(i))
    hold on
%     imshow(I1); % SLOW
    set(hs1,'CData',I1);
%     impixelinfo
    subplot(1,2,2);
%     imshow(I2);
    set(hs2,'CData',I2);
    
    w = waitforbuttonpress;
end