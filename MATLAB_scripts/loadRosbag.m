function bagSelect = loadRosbag(filePath, topics)

% disp(filePath)
bagInfo = rosbag('info',filePath);
% disp(bagInfo.Topics)

bag = rosbag(filePath);

N = numel(topics);

for n = 1:N
    topic = topics{n};
    bagSelect(n) = select(bag,'Topic',topic);
end

end