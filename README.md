# SimpleAPI
Simple python backend framework ):
<br />

## How to run
Note that to test this in windows you need waitress, becuase gunicorn didn't supported in windows.
To run waitress (windows):
  
```shell
$ waitress-serve --listen=127.0.0.1:8000 app:app
```

To run gunicorn (Linux, Mac):
```shell
$ gunicorn app:app
```
Otherwise gunicorn works well in other platforms.
