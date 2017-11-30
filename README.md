# awesome-python-syntax
<a href="https://github.com/DennyZhang?tab=followers"><img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/fork_github.png" /></a>

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) [![LinkedIn](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/linkedin.png)](https://www.linkedin.com/in/dennyzhang001) [![Slack](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/slack.png)](https://www.dennyzhang.com/slack) [![Github](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/github.png)](https://github.com/DennyZhang)

File me [tickets](https://github.com/DennyZhang/awesome-python-syntax/issues) or star [the repo](https://github.com/DennyZhang/awesome-python-syntax).

Advanced Usage Of Python Syntax

Printable version on A4 page: [python_advanced_syntax.pdf](python_advanced_syntax.pdf)

See more CheatSheets from Denny: https://github.com/topics/denny-cheatsheets

- List

| Name                    | Comment                                               |
| :---------------------- | --------------------------------------------------    |
| map                     | `map(lambda x: str(x), [1, 2, 3])`                    |
| create fixed size array | `l = [None] * 5`                                      |
| insert elements to head | `array.insert(0,var)`                                 |
| delete a given element  | `del a[1]`                                            |
| list as stack           | `item = l.pop()`                                      |
| sort in descending      | `sorted([8, 2, 5], reverse=True)`                     |
| sort by attribute       | `sorted([('ebb',12),('abc',14)], key=lambda x: x[1])` |
| generate a-z            | `map(chr, range(ord('a'), ord('z')+1))`               |
| map/reduce              | `reduce((lambda x, y: "%s %s" % (x, y)), l)`          |
| return all but last     | `list[:-1]`                                           |
| replace ith to jth      | `list[i:j] = otherlist`                               |
| combine two list        | `list1 + list2`                                       |
| get sum                 | `sum(list)`                                           |
  
- Compact Coding

| Name                      | Comment                        |
| :------------------------ | ------------------------------ |
| return if.. else          | `return val if i>0 else 0`     |
| multiple assignment       | `l, r = 2, 3`                  |
| swap values               | `left, right = right, left`    |

- Integer

| Name                      | Comment                        |
| :------------------------ | ------------------------------ |
| min, max                  | `min(2, 3), max(5, 6, 2)`      |
| generate range            | `for num in range(10,20)`      |
| generate range            | `for num in xrange(20)`        |
| get ascii                 | `ord('a'), chr(97)`            |
| mininum, maximum in       | `sys.maxsize, -sys.maxsize-1`  |
| print integer in binary   | `"{0:b}".format(10)`           |

- String

| Name                      | Comment                      |
| :------------------------ | ---------------------------- |
| reverse string            |`"hello world"[::-1]`        |
| array to string           |`' '.join(['a', 'b'])`       |
| string to array           |`list("abc")`                |

- Set

| Name          | Comment                               |
| :------------ | -----------------------------------   |
| intersection  | `list(set(l1).intersection(set(l2)))` |
| list to set   | `set(list1)`                          |

- Bit Operator

| Name            | Comment            |
| :-------------  | ----------------   |
| mod             | `x % 2`            |
| shift left      | `x << 1 ; a <<= 2` |
| shift righ      | `x >> 2`           |
| and             | `x & y`            |
| complement      | `~x`               |
| xor             | `x ^ y`            |
| power           | `2 ** 3`           |
| bool complement | `not x`            |

# More links
- https://devhints.io/python

- TODO: use latex to generate a better format

# License
- Code is licensed under [MIT License](https://www.dennyzhang.com/wp-content/mit_license.txt).

<a href="https://www.dennyzhang.com"><img align="right" width="201" height="268" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/denny_201706.png"></a>

<a href="https://www.dennyzhang.com"><img align="right" width="185" height="37" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/dns_small.png"></a>
