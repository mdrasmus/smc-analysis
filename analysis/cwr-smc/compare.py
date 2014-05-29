
from rasmus.common import *

from compbio import arglib

if 1:
    cwr_coals_list = []
    smc_coals_list = []

    for i in range(20):
        k = 10
        n = 10e3
        length = 500e3
        rho = 1.5e-8

        # simulate an ARG from the CwR and convert it into SMC-style
        tic("simulate %d" % i)
        cwr_arg = arglib.sample_arg(k, n, rho, start=0, end=length)
        cwr_arg_converted = arglib.smcify_arg(cwr_arg)
        toc()

        # simulate an ARG directly from SMC process
        smc_arg = arglib.sample_arg_smc(k, n, rho, start=0, end=length)

        # gather all coalescence times
        cwr_coals = [node.age for node in cwr_arg_converted
                     if node.event == 'coal']
        smc_coals = [node.age for node in smc_arg
                     if node.event == 'coal']
        print len(cwr_coals), len(smc_coals)

        cwr_coals_list.append(cwr_coals)
        smc_coals_list.append(smc_coals)


    rplot_start('figures/cwr-smc-coals.pdf')
    rp.plot([], main='Comparison of CwR and SMC coalescence times',
            xlab='generations', ylab='', xlim=[50, 100e3], ylim=[0, 1],
            log='x', t='n')

    for cwr_coals in cwr_coals_list:
        x, y = cdf(cwr_coals)
        rp.lines(x, y, col='#00000080')

    for smc_coals in smc_coals_list:
        x, y = cdf(smc_coals)
        rp.lines(x, y, col='#0000ff80')
    rplot_end(False)
