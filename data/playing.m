% Fs = 8000;
% soundsc(y(:,4), Fs)

recObj = audiorecorder;
disp('Start speaking.')
recordblocking(recObj, 1.5);
disp('End of Recording.');
play(recObj);
