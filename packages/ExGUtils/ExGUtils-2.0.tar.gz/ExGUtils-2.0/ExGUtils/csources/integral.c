/*#    Copyright (C) 2012 Daniel Gamermann <gamermann@gmail.com>
#
#    This file is part of ExGUtils
#
#    ExGUtils is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    ExGUtils is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with ExGUtils.  If not, see <http://www.gnu.org/licenses/>.
#
#    
#    Please, cite us in your reasearch!
# */


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "integral.h"
#include "routs.h"

/* ******************
      Integrals
  ****************** */


double const Xs[10] = {.993128599185094924786,.963971927277913791268,.912234428251325905868,
       .839116971822218823395,.74633190646015079614,.636053680726515025453,
       .510867001950827098004,.373706088715419560673,.227785851141645078080,
                     .076526521133497333755};

double const Ws[10] = {.017614007139152118312,.040601429800386941331,.062672048334109063570,
      .083276741576704748725,.101930119817240435037,.118194531961518417312,
      .131688638449176626898,.142096109318382051329,.149172986472603746788,
                   .152753387130725850698};


void gen_points(double ini, double fin, int N, double *XXX) {
/* Generates the points in the X axis */
    int ii, jj;
    double dxi, bet, alp, A, B;
    dxi = (fin - ini) / N;
    bet = (dxi)*.5;
    for (ii=0; ii<N; ii++) {
        A = ini + ii*dxi;
        B = A + dxi;
        alp = (A+B)*.5;
        for (jj=0; jj<10; jj++){
            *(XXX + jj + ii*20) = -bet*Xs[jj]+alp;
        }
        for (jj=0; jj<10; jj++){
            *(XXX + jj + 10 + ii*20) = bet*Xs[9-jj]+alp;
        }
    }
}


double integrate(double ini, double fin, int N, double *YYY){
/* Integrates the function */
    int ii, jj;
    double sum = 0., dxi;
    dxi = (fin - ini) / N;
    for (ii=0; ii<N; ii++) {
        for (jj=0; jj<10; jj++){
            sum += Ws[jj]* *(YYY+20*ii+jj);
        }
        for (jj=0; jj<10; jj++){
            sum += Ws[9-jj]* *(YYY+20*ii+jj+10);
        }
    }
    return(.5*dxi*sum);
}




double exgauss_lt(double z, double mu, double sig, double tau, double eps, int N) {
    double inf, inte, ninte;
    double xxx[20*N], yyy[20*N], xx2[40*N], yy2[40*N];
    double M, S, lamb;
    double *xx3, *yy3;
    int i;
    
    xx3 = malloc(sizeof(double)*20*N);
    yy3 = malloc(sizeof(double)*20*N);
 
    pars_to_stats(mu, sig, tau, &M, &S, &lamb);
    inf = M - 10.*S;
    
    gen_points(inf, z, N, &xxx[0]);
    for (i=0; i<20*N; i++) {
        yyy[i] = exgauss(xxx[i], mu, sig, tau);
    }
    inte = integrate(inf, z, N, &yyy[0]);

    gen_points(inf, z, 2*N, &xx2[0]);
    for (i=0; i<40*N; i++) {
        yy2[i] = exgauss(xx2[i], mu, sig, tau);
    }
    ninte = integrate(inf, z, 2*N, &yy2[0]);
    N *= 2;
    while (fabs(ninte-inte)>eps) {
        N *= 2;
        xx3 = realloc(xx3, sizeof(double)*20*N);
        yy3 = realloc(yy3, sizeof(double)*20*N);
        inte = ninte;
        //printf("aqui estou %d\n", N);
        gen_points(inf, z, N, xx3);
        for (i=0; i<20*N; i++) {
            *(yy3+i) = exgauss(*(xx3+i), mu, sig, tau);
        }
        ninte = integrate(inf, z, N, yy3);
    }
    free(xx3);
    free(yy3);
    return ninte;
}




double exgauss_lamb_lt(double z, double lamb, double eps, int N) {
    double inf, inte, ninte;
    double xxx[20*N], yyy[20*N], xx2[40*N], yy2[40*N];
    int i;
    
    inf = - 8.;
    
    gen_points(inf, z, N, &xxx[0]);
    for (i=0; i<20*N; i++) {
        yyy[i] = exgauss_lamb(xxx[i], lamb);
    }
    inte = integrate(inf, z, N, &yyy[0]);

    gen_points(inf, z, 2*N, &xx2[0]);
    for (i=0; i<40*N; i++) {
        yy2[i] = exgauss_lamb(xx2[i], lamb);
    }
    ninte = integrate(inf, z, 2*N, &yy2[0]);
    N *= 2;
    while (fabs(ninte-inte)>eps) {
        inte = ninte;
        N *= 2;
        double *xx3, *yy3;
        xx3 = malloc(sizeof(double)*20*N);
        yy3 = malloc(sizeof(double)*20*N);
        gen_points(inf, z, N, xx3);
        for (i=0; i<20*N; i++) {
            *(yy3+i) = exgauss_lamb(*(xx3+i), lamb);
        }
        ninte = integrate(inf, z, N, yy3);
        free(xx3);
        free(yy3);
    }
    return ninte;
}



double zalp_exgauss(double alp, double mu, double sig, double tau, double eps) {
    double inte, z, delta;
    
    z = mu+tau;
    delta = sig;
    inte = exgauss_lt(z, mu, sig, tau, eps, 10);
    while (fabs(alp-inte)>eps) {
        if ((alp>=inte)&(delta>0.)) {
            z += delta;
        } else if ((alp<inte)&(delta>0.)) {
            delta *= -1.;
            z += delta;
        } else if ((alp<inte)&(delta<0.)) {
            z += delta;
        } else {
            delta *= -.5;
            z += delta;
        }
        inte = exgauss_lt(z, mu, sig, tau, eps, 10);
    }
    return z;
}






double zalp_exgauss_lamb(double alp, double lamb, double z, double delta, double eps) {
    double inte;
    
    inte = exgauss_lamb_lt(z, lamb, eps, 10);
    if (fabs(alp-inte)<eps) {
        return z;
    } else {
        if ((alp>=inte)&(delta>0.)) {
            return zalp_exgauss_lamb(alp, lamb, z+delta, delta, eps);
        } else if ((alp>=inte)&(delta<0)) {
            return zalp_exgauss_lamb(alp, lamb, z-0.5*delta, -0.5*delta, eps);
        } else if ((alp<inte)&(delta>0.)) {
            return zalp_exgauss_lamb(alp, lamb, z-0.5*delta, -0.5*delta, eps);
        } else {
            return zalp_exgauss_lamb(alp, lamb, z+delta, delta, eps);
        }
    }
}





