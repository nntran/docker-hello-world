# Hello World!

A simple app to say "Hello World!".

It's base on Docker and Flask framework.


## How to use it ?

### Build

```sh
docker build --rm --tag hello-world .
```

### Run

```sh
docker run --rm -p 5000:5000 hello-world
```

It serve at http://localhost:5000


