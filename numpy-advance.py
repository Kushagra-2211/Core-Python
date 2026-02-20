#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 19:52:46 2026

@author: kush
"""

import numpy as np
#%%
# Here we will perform a deep numpy master excercise
# We will generate synthetic market data, create a portfolio and perform core numpy operations.
# This excercise will cover-
# Broadcasting
# Masking
# Advanced indexing
# Axis operations
# Vectorization (no loops allowed)
# Performance thinking
# Numerical stability
# Reshaping + stacking
# Correlation + covariance
# Memory awareness
#%%
#
years = 5
trading_days = 252
n_stocks = 1000

n_days = years * trading_days
#%%
np.random.seed(42)
returns = np.random.normal(loc=.0005, scale= 0.02, size=(n_days,n_stocks))
#%%
returns.shape    #(1260, 1000)
#%%
returns.mean()   #0.0005
returns.std()    #0.02
#%%
