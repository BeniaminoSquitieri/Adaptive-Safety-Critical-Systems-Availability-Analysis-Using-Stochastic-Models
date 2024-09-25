
function val = log_lik_cens(theta1,censoring,x) % -loglikelihood of transf. exp parameter with censoring
    extheta = exp(theta1);
    % censoring: 0 time to event, 1 right censored
    val = -sum(log(exppdf(x.*(1-censoring),extheta)).*(1-censoring))...
        -sum(log(1-expcdf(x.*censoring,extheta)).*censoring); % - log-likelihood as a function of the new param.
end

