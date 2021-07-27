#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 01 demo1.py
# @Author: Stormzudi
# @Date  : 2021/7/13 16:02

import tensorflow as tf

A = tf.constant([[1, 2], [3, 4]])
B = tf.constant([[5, 6], [7, 8]])
C = tf.matmul(A, B)

print(C)
