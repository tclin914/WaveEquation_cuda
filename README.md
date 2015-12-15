# CUDA Programming

The purpose of this assignment is to familiarize yourself with CUDA programming.

## Problem Statement

In this problem, you need to use CUDA to parallelize concurrent wave equation `serial_wave.c`.

## Requirements

* The output format should not be changed.
* Your submitted solution contains only one source file, which is named `wave.cu`.
* Your program take two command-line arguments, which indicate the number of points and the number of iterations, respectively.

## Evaluation

Usage:`python test/run_test.py n steps`

number of points and steps | 100000 2000   | 1000000 20000  |
---------------------------|---------------|----------------|
Serial (seconds)           | 33.0460920334 | 324.630088091  |
Cuda   (seconds)           | 8.08702301979 | 74.1598510742  |

The difference of serial output with cuda output in fourth decimal place is normal.
