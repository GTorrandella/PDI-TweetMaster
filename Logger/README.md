# How to

## Import
```
from Logger.Rsyslog import createLogger
```

## Uso
 1. Crear el Logger:
 ```
 log = createLogger(name=__name__)
 ```
 "name=__name__" es necesario el para el correcto funcionamiento del resto del sistema.
 
 2. Crear mensajes:
 ```
 log.<LogLevel>(<msg>)
 log.info('Mensaje')
 ```
 
 3. En test:
 Agregar 'test' como argumento 'context'.
 ```
 log = createLogger(name=__name__, context='test')
 ```
 
 ## Formato del mesaje final:
 ```
 <Module.Name> - <Time>: <LogLevel>: <msg>, from <Function>
 Fetcher.fetcher - %Y-%m-%d %H:%M:%S: INFO: Mensaje, from fetchTweets
 ```
