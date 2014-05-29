
from rasmus.common import *

from compbio import arglib

if 1:
    k = 10
    n = 10e3
    length = 1e6
    rho = 1.5e-8

    # simulate an ARG from the CwR
    cwr_arg = arglib.sample_arg(k, n, rho, start=0, end=length)

    # simulate an ARG from SMC
    smc_arg = arglib.smcify_arg(cwr_arg)

    # gather all coalescence times
    cwr_coals = [node.age for node in cwr_arg
                 if node.event == 'coal']
    smc_coals = [node.age for node in smc_arg
                 if node.event == 'coal']

    print len(cwr_coals), len(smc_coals)


    rplot_start('figures/cwr-smc-coals.pdf')
    x, y = cdf(cwr_coals)
    rp.plot(x, y, main='Comparison of CwR and SMC coalescence times',
            xlab='generations', ylab='',
            log='x', t='l')

    x2, y2 = cdf(smc_coals)
    rp.lines(x2, y2, col='blue')
    rplot_end(False)
