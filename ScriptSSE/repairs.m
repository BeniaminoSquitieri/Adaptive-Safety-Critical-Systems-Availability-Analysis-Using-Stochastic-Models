% Leggi i dati da un file di testo
% Sostituisci 'nome_file.txt' con il percorso e il nome del tuo file
dati = load('repairs_gr1.txt');

% Calcola il numero di campioni
numero_di_campioni = length(dati);
% Calcola la media
media = mean(dati);

% Calcola la deviazione standard
deviazione_standard = std(dati);

% Calcola il minimo
minimo = min(dati);

% Calcola il 25° percentile
percentile_25 = prctile(dati, 25);

% Calcola la mediana (50° percentile)
mediana = median(dati);

% Calcola il 75° percentile
percentile_75 = prctile(dati, 75);

% Calcola il massimo
massimo = max(dati);

% Visualizza i risultati
fprintf('Numero di campioni: %d\n', numero_di_campioni);
fprintf('Media: %.2f\n', media);
fprintf('Deviazione standard: %.2f\n', deviazione_standard);
fprintf('Minimo: %.2f\n', minimo);
fprintf('25° percentile: %.2f\n', percentile_25);
fprintf('Mediana: %.2f\n', mediana);
fprintf('75° percentile: %.2f\n', percentile_75);
fprintf('Massimo: %.2f\n', massimo);
