% Inizializzazione dell'ambiente
 close all
 clc
 clearvars
 
 % Carica il file
 failureTimes = load("failureI_gr1.txt");
 censoringData = load("censoring_gr1.txt");
 
 % Seleziona solo i tempi di guasto non censurati
 nonCensoredFailureTimes = failureTimes(censoringData == 0);
 % Calcola il numero di campioni censuratie e non
 nsamps_nocens = length(nonCensoredFailureTimes);
 nsamps_tot = length(failureTimes);
 fprintf('Campioni totali: %d\n', nsamps_tot);
 fprintf('Campioni non censurati: %d\n', nsamps_nocens);
 fprintf('Campioni censurati: %d\n', nsamps_tot- nsamps_nocens);
 % Stima del parametro lambda_PHY
 %% Metodo 1
 MTTF_mean = sum(failureTimes) / nsamps_nocens;
 MTTF_wr_mean = sum(failureTimes) / nsamps_tot;
 fprintf('\nMetod 1\nMTTF est.: %f [h]\n', MTTF_mean);
 fprintf('Failure rate est.: %f [1/h]\n\n', 1/MTTF_mean);
 fprintf('MTTF wrong est.: %f [h]\n', MTTF_wr_mean);
 fprintf('Failure rate wrong est.: %f [1/h]\n\n', 1/MTTF_wr_mean);
 %% Metodo 2
 % mle() function with right censoring
 MTTF_mle = mle(failureTimes, 'Distribution', 'Exponential', 'Censoring',censoringData);
 fprintf('Metod 2\nMTTF est.: %f [h]\n', MTTF_mle);
 fprintf('Failure rate est.: %f [1/h]\n\n', 1/MTTF_mle);
 %% Metodo 3
 options = optimset('Display', 'off', 'MaxIter', 10000);
 theta0 = 10;
 [theta, fval, exitflag, output, grad, hessian] = fminunc('log_lik_cens', theta0, options, censoringData, failureTimes);
 exp(theta);
 fprintf('Metod 3\nMTTF est.: %f [h]\n', exp(theta));
 
 fprintf('Failure rate est.: %f [1/h]\n\n', 1/exp(theta));
 %% Plot
 figure
 histogram(failureTimes(censoringData == 0), 'Normalization', 'pdf');
 title('Failure times: type I right censoring', 'FontSize', 24);
 xlabel('failureTimes (uncensored)', 'FontSize', 20);
 ylabel('pdf', 'FontSize', 20);
 ax = gca;
 ax.FontSize = 16;
 hold on;
 xax = linspace(0, ax.XLim(2), 100);
 plot(xax, exppdf(xax, MTTF_mean), 'r:', 'LineWidth', 2);
 plot(xax, exppdf(xax, MTTF_wr_mean), 'k:', 'LineWidth', 2);
 legend('hist', 'est.', 'wrong est. with stopping times', 'FontSize', 20);