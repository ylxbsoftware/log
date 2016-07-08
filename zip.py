#! /usr/bin/env python
# -*- coding: utf-8 -*-
#created by wanbao 2016.7.8
#python 2.7.10
#git打包仅导出不同提交记录中被更新过的文件

import os

name = str.strip(raw_input('请输入最终打包名称(默认为update): '));
new = str.strip(raw_input('请输入new-commit-id(默认为HEAD): '));
old = str.strip(raw_input('请输入old-commit-id: '));
if(len(name)==0):
  name = 'update';

if(len(new)==0):
  new = 'HEAD'
os.system('git archive -o ' + name + '.zip ' + new +' $(git diff --name-only --diff-filter=ACMRT ' + old + ' ' + new + ')')
