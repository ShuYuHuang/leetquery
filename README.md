# LeetQuery

[![PyPI version](https://badge.fury.io/py/leetquery.svg)](https://badge.fury.io/py/leetquery) ![Test](https://github.com/ShuYuHuang/leetquery/actions/workflows/python-app.yml/badge.svg)  [![Downloads](https://static.pepy.tech/badge/leetquery)](https://pepy.tech/project/leetquery)

A library for retriving Human Resource information from Leetcode.

## Install
``` shell
    pip install leetquery
```
## Usage
### Retriving User Submissions
Just enter user name and limit of query!
``` python
from leetquery import get_submissions

submissions = get_submissions(username="syhaung", limit=12)
```
return value:
```
["question1", "question2", ...]
```