# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random as rnd


def gauss_samples(mu, sigma, n):
    """
    Return n samples of N(mu, sigma^2)

    :param mu: expected value, passed to random.gauss()
    :param sigma: std deviation passed to random.gauss()
    :param n: num of samples required
    :return: list of random numbers of length n but at least 1
    """
    return list(map(lambda _: rnd.gauss(mu, sigma), range(max(n, 1))))

# simple histogram
samples = gauss_samples(5, 10, 100)
samples[0:4]

plt.hist(x=samples, bins=20, normed=True)

plt.boxplot(samples)
