p_list = 0:0.005:1;
T = 1;
%% Goodput of using (25,20) Hamming code

P_TF_25_list=zeros(1,length(p_list));
Goodput_TF_25_list = zeros(1,length(p_list));
for index = 1:length(p_list)
    p=p_list(index);
    P_TF_25 = 1-((1-p)^25)-(25*p*(1-p)^24);
    Goodput_TF_25 = 20*(1-P_TF_25)/(25*T);
    
    P_TF_25_list(index)=P_TF_25;
    Goodput_TF_25_list(index)=Goodput_TF_25;

end

%% Goodput of using (7,4) 5 times

Goodput_TF_7_5times_list = zeros(1,length(p_list));
for index = 1:length(p_list)
    p = p_list(index);
    P_TF_7= 1-((1-p)^7) - (7*p*(1-p)^6);
    Goodput_TF_7_5times=(20*(1-P_TF_7)^5)/(35*T);
    Goodput_TF_7_5times_list(index)=Goodput_TF_7_5times;
end
%%
figure;
plot(p_list, Goodput_TF_25_list, 'b', 'LineWidth', 1.5); % (25, 20) 曲线
hold on;
plot(p_list, Goodput_TF_7_5times_list, 'r', 'LineWidth', 1.5); % (7, 4) 曲线
hold off;

% 添加图例、标题和标签
legend('(25, 20) Hamming Code', '(7, 4) Hamming Code Repeated 5 Times', 'Location', 'northeast');
xlabel('Bit Error Probability (p)');
ylabel('Goodput (bits/sec)');
title('Goodput Comparison: (25, 20) vs. (7, 4) Hamming Code');
grid on;