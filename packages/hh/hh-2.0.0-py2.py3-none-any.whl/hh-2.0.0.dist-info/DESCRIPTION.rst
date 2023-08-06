# H<sub>ttp</sub> H<sub>eaders</sub>
The enumeration which contains all headers constants from RFC1945, RFC2518, RFC2616.

# Usage
```python
import requests 
import hh

requests.get('https://yandex.com', headers={hh.CONTENT_TYPE: "text/html"})
```


