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
# Vectorization (no loops)
# Performance thinking
# Numerical stability
# Reshaping + stacking
# Correlation + covariance
# Memory awareness
#%%
# Task 1
# Returns matrix
# Portfolio weights
# Portfolio returns
# Covariance matrix
# Portfolio variance
# Portfolio volatility
# Annualized volatility
#%% Defining variables to stimulate returns data
#
years = 5
trading_days = 252
n_stocks = 1000

n_days = years * trading_days
#%% Fixing the starting point for reproducable backtests 
np.random.seed(42)
#%% Generating returns data for 1000 stocks
returns = np.random.normal(loc=.0005, scale= 0.02, size=(n_days,n_stocks))
#%%
returns.shape    #(1260, 1000)
#%% Sanity check
returns.mean()   #0.0005
returns.std()    #0.02
#%% generating random weights 
weights = np.random.random(1000)
weights /= weights.sum()
#%% Sanity check
weights.sum()
#%% Computing portfolio returns using weights and returns data
portfolio_returns = returns @ weights
#%% Computing the covriance matrix
T, N = returns.shape
returns_mean = returns.mean(axis= 0)
demeaned_returns = returns - returns_mean

cov_matrix = (demeaned_returns.T @ demeaned_returns) / (T - 1)
#%% Computing Portfolio Variance
portfolio_variance = weights.T @ cov_matrix @ weights
#%%
portfolio_volatility = np.sqrt(portfolio_variance)
#%%
annual_volatility = portfolio_volatility*np.sqrt(252)
#%%
# Task 2
# Rolling 30 day volatility
# Advanced indexing and filtering
# Signal creation
#
#
#%% Computing 30 days rolling vol
#%% 
# Method 1 - Using Index Matrix
T,N = returns.shape
window = 30
idx_matrix = np.arange(window)[None,:] + np.arange(T-window+1)[:,None] 
#%%
idx_matrix.shape  #(1231,30)
#%% Advanced Indexing
rolling_windows = returns[idx_matrix]
#%%
rolling_windows.shape   #(1231, 30, 1000)
#%% computing rolling vol
rolling_vol = rolling_windows.std(axis=1)
#%%
# Method 2 - Using numpy Stride trick
window = 30
rolling_window = np.lib.stride_tricks.sliding_window_view(returns, window_shape = window, axis=0)
#%%
rolling_window.shape    #(1231, 1000, 30)
#%%
rolling_vol_2 = rolling_window.std(axis=2)















