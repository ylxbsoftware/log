#! /usr/bin/env python
# -*- coding: utf-8 -*-
#created by wanbao 2016.7.8
#python 2.7.10
#git打包仅导出不同提交记录中被更新过的文件

import os
new = str.strip(raw_input('请输入new-commit-id(不输入默认为HEAD): '));
old = str.strip(raw_input('请输入old-commit-id: '));
if(len(new)==0):
  new = 'HEAD'

os.system('git archive -o update.zip ' + new +' $(git diff --name-only --diff-filter=ACMRT ' + old + ' ' + new + ')')
