# awesome-python-syntax
<a href="https://github.com/DennyZhang?tab=followers"><img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/fork_github.png" /></a>

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) [![LinkedIn](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/linkedin.png)](https://www.linkedin.com/in/dennyzhang001) [![Twitter](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/twitter.png)](https://twitter.com/dennyzhang001) [![Slack](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/slack.png)](https://goo.gl/ozDDyL) [![Github](https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/github.png)](https://github.com/DennyZhang)

File me [tickets](https://github.com/DennyZhang/awesome-python-syntax/issues) or star [the repo](https://github.com/DennyZhang/awesome-python-syntax).

Advanced usage of Python Syntax
  
- List

| Name                           | Comment                                                 |
| :------------------------      | ----------------------------------------                |
| sort in descending             | sorted([8, 2, 5], reverse=True)                         |
| Sort by attribute              | sorted([('ebb', 121),('abc', 148)], key=lambda x: x[1]) |
| generate a-z                   | map(chr, range(ord('a'), ord('z')+1))                   |
| create array with given length | lst = [None] * 5                                        |
| Insert element to head         | array.insert(0,var)                                     |
| delete a given element         | del a[1]                                                |
| map                            | map(lambda x: str(x), [1, 2, 3])                        |
| map/reduce                     | reduce((lambda x, y: "%s %s" % (x, y)), l)              |
| list as stack                  | l.pop()                                                 | 
  
- Compact Coding

| Name                      | Comment                                  |
| :------------------------ | ---------------------------------------- |
| return if.. else          | return val if i>0 else 0)                |
| multiple assignment       | l, r = i+1, length-1                     |
| Swap Values                       | left, right = right, left                |

- Integer

| Name                              | Comment                                  |
| :------------------------         | ---------------------------------------- |
| min, max                          | min(2, 3), max(5, 6, 2)                  |
| generate range                    | for num in range(10,20)                  |
| generate range                    | for num in xrange(20)                    |
| get ascii                         | ord('a'), chr(97)                        |
| mininum integer, maximum interger | sys.maxsize, -sys.maxsize-1              |
| print integer in binary           | "{0:b}".format(10)                       |

- String

| Name                      | Comment                                  |
| :------------------------ | ---------------------------------------- |
| Reverse string            | "hello world"[::-1]                      |
| array to string           | ' '.join(['a', 'b'])                     |
| string to array           | list("abc")                              |

- Bit Operator

| Name            | Comment                   |
| :-------------  | ------------------------- |
| mod             | x % 2                     |
| shift left      | x << 1                    |
| shift righ      | x >> 2                    |
| and             | x & y                     |
| complement      | ~x                        |
| xor             | x ^ y                     |
| power           | 2 ** 3                    |
| bool complement | not x                     |

# License
- Code is licensed under [MIT License](https://www.dennyzhang.com/wp-content/mit_license.txt).

<img align="right" width="200" height="183" src="https://raw.githubusercontent.com/USDevOps/mywechat-slack-group/master/images/magic.gif">
