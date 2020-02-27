clear all

fs=8000;

for i=1:30
    recObj = audiorecorder(fs, 16, 1);
    disp(num2str(i))
    disp('Start speaking.')
    recordblocking(recObj, 1.1);
    disp('End of Recording.');
    y(:,i) = getaudiodata(recObj);
    pause(0.5);
end
