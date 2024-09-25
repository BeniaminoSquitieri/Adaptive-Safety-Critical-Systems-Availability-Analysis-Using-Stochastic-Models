close all
clc

%Carica il file
repairTimes = load ("repairs_gr1.txt")

%Calcolo del numero di campioni
nsamps = length (repairTimes)

%Stima del parametro mu_PHY

%%Metodo 1
MTTR_mean = sum (repairTimes) / nsamps;

% o equivalentemente MTTR_mean = mean (repairTimes)

fprintf ('Metod 1\nMTTR est. : %f [h]\n', MTTR_mean)
fprintf ('Repair rate  est. : %f [1/h]\n\n', 1/MTTR_mean)

%%Metodo 2
MTTR_mle = mle (repairTimes, 'Distribution', 'Exponential')

fprintf ('Metod 2\nMTTR est. : %f [h]\n', MTTR_mean)
fprintf ('Repair rate  est. : %f [1/h]\n\n', 1/MTTR_mean)

%%Metodo 3
[MTTR_exp , MTTR_ci] = expfit (repairTimes)
fprintf ('Metod 3\nMTTR est. : %f [h] \nMTTR est. 95%% codifence interval : \nlower bound: %f [h]\nupper_bound: %f [h]\n', MTTR_exp, MTTR_ci(1), MTTR_ci(2));
fprintf ('Repair rate  est. : %f [1/h]\n\n', 1/MTTR_exp)

%%Metodo 4
options = optimset ('Display', 'off' , 'MaxIter', 10000)
theta0 = 2
[theta, fval , exitflag, output , grad , hessian] = fminunc ('log_lik', theta0, options, repairTimes);
exp (theta);
fprintf ('Metod 4\nMTTR est. : %f [h]\n', exp (theta))
fprintf ('Repair rate  est. : %f [1/h]\n\n', 1/exp (theta))

% Plot
figure
histogram(repairTimes, 'Normalization', 'pdf');
title('Repair Times - Complete Sample', 'FontSize', 24);
xlabel('Repair Times', 'FontSize', 20);
ylabel('pdf', 'FontSize', 20);

% Personalizza la scala dell'asse x
ax = gca;
ax.FontSize = 16;

% Imposta la scala dell'asse y da 0 a 1
ax.YLim = [0 0.13];
ax.XLim = [0 40];

hold on;

% Genera il vettore xax
xax = linspace(0, ax.XLim(2), 100);

% Plot con scala logaritmica sull'asse y
plot(xax, exppdf(xax, MTTR_exp), 'r:', 'LineWidth', 2);

legend('Hist', 'Est.', 'FontSize', 20);

% Imposta ticks sull'asse y ogni 0.01
%yticks(0:0.01:0.13);

