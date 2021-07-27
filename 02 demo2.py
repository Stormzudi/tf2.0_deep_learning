#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 02 demo2.py
# @Author: Stormzudi
# @Date  : 2021/7/13 16:06

import tensorflow as tf

# 定义一个随机数（标量）
random_float = tf.random.uniform(shape=())

# 定义一个有2个元素的零向量
zero_vector = tf.zeros(shape=(2))

print(random_float, zero_vector)


# 定义两个2×2的常量矩阵
A = tf.constant([[1., 2.], [3., 4.]])
B = tf.constant([[5., 6.], [7., 8.]])
print(A, B, '\n')



# 查看矩阵A的形状、类型和值
print(A.shape)      # 输出(2, 2)，即矩阵的长和宽均为2
print(A.dtype)      # 输出<dtype: 'float32'>
print(A.numpy(),'\n')    # 输出[[1. 2.]
                    #      [3. 4.]]


D = tf.matmul(A, B)
print(D)
