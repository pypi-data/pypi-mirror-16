#include <stdlib.h>
#include "gsl/gsl_sf_legendre.h"
#include "gsl/gsl_sf_gegenbauer.h"
#include "gsl/gsl_sf_gamma.h"
#include <math.h>
#include "coeff_helper.h"
#include "bfe_helper.h"
#include <complex.h>

#define SQRT_FOURPI 3.544907701811031

double STnlm_integrand_help(double phi, double X, double xsi,
                            double density, int n, int l, int m) {
    /*
    Computes the integrand used to compute the expansion
    coefficients, Snlm, Tnlm. The integral is done over:

        * phi: azimuthal angle
        * X: cos(theta), where theta is the colatitude
            (e.g., from spherical coordinates typical to physicists)
        * xsi: (s-1)/(s+1), a radial coordinate mapped to the interval
            [-1,1] rather than [0,inf].
    */
    double s = (1 + xsi) / (1 - xsi);
    double sinth = sqrt(1 - X*X);

    // temporary variables
    double Knl, Anl_til, krond, numer, denom, ds;

    Knl = 0.5*n*(n + 4*l + 3) + (l + 1)*(2*l + 1);
    if (m == 0) {
        krond = 1.;
    } else {
        krond = 0.;
    }

    numer = gsl_sf_fact(n) * (n + 2*l + 1.5) * pow(gsl_sf_gamma(2*l + 1.5),2);
    denom = gsl_sf_gamma(n + 4*l + 3);
    Anl_til = -(pow(2., 8*l+6) / (4*M_PI*Knl)) * numer / denom;

    ds = s*s*(s+1)*(s+1) / 2; // change of variables ds -> dxsi
    return (2 - krond) * phi_nlm(s, phi, X, n, l, m) * Anl_til * density * ds;

}

extern double c_Snlm_integrand(double phi, double X, double xsi,
                               double density, int n, int l, int m) {
    return STnlm_integrand_help(phi, X, xsi, density, n, l, m) * cos(m*phi);
}

extern double c_Tnlm_integrand(double phi, double X, double xsi,
                               double density, int n, int l, int m) {
    return STnlm_integrand_help(phi, X, xsi, density, n, l, m) * sin(m*phi);
}

extern void c_STnlm_discrete(double *s, double *phi, double *X, double *m_k, int K,
                             int n, int l, int m, double *ST) {
    // temporary variables
    double Knl, Anl_til, krond, numer, denom, coeff, _tmp;

    Knl = 0.5*n*(n + 4*l + 3) + (l + 1)*(2*l + 1);
    if (m == 0) {
        krond = 1.;
    } else {
        krond = 0.;
    }

    numer = gsl_sf_fact(n) * (n + 2*l + 1.5) * pow(gsl_sf_gamma(2*l + 1.5),2);
    denom = gsl_sf_gamma(n + 4*l + 3);
    Anl_til = -(pow(2., 8*l+6) / (4*M_PI*Knl)) * numer / denom;
    coeff = (2 - krond) * Anl_til;

    // zero out coeff storage array
    ST[0] = 0.;
    ST[1] = 0.;
    for (int k=0; k<K; k++) {
        _tmp = coeff * m_k[k] * phi_nlm(s[k], phi[k], X[k], n, l, m);
        ST[0] += _tmp * cos(m*phi[k]); // Snlm
        ST[1] += _tmp * sin(m*phi[k]); // Tnlm
    }
}
