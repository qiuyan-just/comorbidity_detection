#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
将sentiment.csv前三列的TRUE/FALSE替换为1/0
"""

# import pandas as pd
# from datetime import datetime
#
# print("开始处理sentiment.csv文件...")
#
# # 读取数据
# df = pd.read_csv("E:/comorbidity/feature_normalization/sentiment_results.csv")
#
# print(f"数据加载完成: {df.shape[0]} 行, {df.shape[1]} 列")
# print(f"列名: {df.columns.tolist()}")
#
# # 显示前三列的原始数据情况
# for i in range(min(3, len(df.columns))):
#     col_name = df.columns[i]
#     unique_values = df[col_name].unique()
#     print(f"   第{i+1}列 '{col_name}': {unique_values}")
#
# # 替换前三列的TRUE/FALSE为1/0
# for i in range(min(3, len(df.columns))):
#     col_name = df.columns[i]
#     # 替换TRUE为1，FALSE为0（不区分大小写）
#     df[col_name] = df[col_name].astype(str).str.upper().replace({'TRUE': 1, 'FALSE': 0})
#     print(f"已处理第{i+1}列: {col_name}")
#
# # 显示替换后的数据情况
# print(f"\n替换后数据预览:")
# for i in range(min(3, len(df.columns))):
#     col_name = df.columns[i]
#     unique_values = df[col_name].unique()
#     print(f"   第{i+1}列 '{col_name}': {unique_values}")
#
# # 保存结果
# output_file = f"sentiment_converted_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
# df.to_csv(output_file, index=False, encoding='utf-8-sig')
#
# print(f"\n处理完成，已保存到: {output_file}")
# print(f"输出数据: {df.shape[0]} 行, {df.shape[1]} 列")


import pandas as pd
from datetime import datetime

print("开始处理post.csv文件...")

# 读取数据
df = pd.read_csv("E:/comorbidity/feature_normalization/post.csv")

print(f"数据加载完成: {df.shape[0]} 行, {df.shape[1]} 列")
print(f"列名: {df.columns.tolist()}")

# 显示前三列的原始数据情况
for i in range(min(2, len(df.columns))):
    col_name = df.columns[i]
    unique_values = df[col_name].unique()
    print(f"   第{i+1}列 '{col_name}': {unique_values}")

# 替换前三列的TRUE/FALSE为1/0
for i in range(min(3, len(df.columns))):
    col_name = df.columns[i]
    # 替换TRUE为1，FALSE为0（不区分大小写）
    df[col_name] = df[col_name].astype(str).str.upper().replace({'TRUE': 1, 'FALSE': 0})
    print(f"已处理第{i+1}列: {col_name}")

# 显示替换后的数据情况
print(f"\n替换后数据预览:")
for i in range(min(3, len(df.columns))):
    col_name = df.columns[i]
    unique_values = df[col_name].unique()
    print(f"   第{i+1}列 '{col_name}': {unique_values}")

# 保存结果
output_file = f"post_converted_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n处理完成，已保存到: {output_file}")
print(f"输出数据: {df.shape[0]} 行, {df.shape[1]} 列")