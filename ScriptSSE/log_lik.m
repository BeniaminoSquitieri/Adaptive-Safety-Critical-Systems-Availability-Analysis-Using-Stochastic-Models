
function val = log_lik(theta,x) % -loglikelihood of transf. exp parameter
    extheta = exp(theta); % transform constrained opt into uncontrained opt. prb.
    val = -sum(log(exppdf(x,extheta))); % -loglikelihood as a function of the new param.
end

