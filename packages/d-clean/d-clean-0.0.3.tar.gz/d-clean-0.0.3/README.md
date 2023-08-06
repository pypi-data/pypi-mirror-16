# d-clean
small commmnd to run docker cleanup


## install

```bash
$ pip3 install d-clean
```


command d-clean (docker clean command)
```
Usage: d-clean [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  all                Run stopped, images-not-in-use, dangling
  dangling           Remove all dangling images
  images-not-in-use  Remove all images not in use
  stopped            Remove all stopped containers
```
