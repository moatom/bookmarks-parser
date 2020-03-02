# bookmarks-parser
Parsing Netscape bookmark (Google Chrome, Firefox, ... export files) .

## Installation
```
$ pip install -e "git+https://github.com/moatom/bookmarks-parser.git#egg=bookmarks-parser"
```

## Usage
```python
import pprint
import bookmarks_parser

bookmarks = bookmarks_parser.parse("bookmarks.html")

pprint.pprint(bookmarks)
```

```python
import pprint
from bookmarks_parser import bookmarks_parser

bookmarks = bookmarks_parser.parse("tests/tests_data/chrome_bookmarks.html")

pprint.pprint(bookmarks)
```

[output example](https://github.com/andriyor/bookmarks-parser/tree/master/tests/tests_data)

<!-- ## Development
Install [Poetry](https://poetry.eustace.io/docs/)   
```
$ poetry install
```
run tests
```
$ poetry run pytest --cov=bookmarks_parser
``` -->

## License
[MIT](https://choosealicense.com/licenses/mit/)