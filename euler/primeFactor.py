import primefac

n= 600851475143
factorint(n, trial_limit=1000, rho_rounds=42000,
          methods=(pollardRho_brent, pollard_pm1, williams_pp1, ecm, mpqs))
