## CI Configuration

This uses tags and specifies a docker image

```
image: debian
before_script:
  - echo "Before script section"
  - echo "For example you might run an update here or install a build dependency"
  - echo "Or perhaps you might print out some debugging details"

after_script:
  - echo "After script section"
  - echo "For example you might do some cleanup here"

build:
  stage: build
  tags:
    - docker
  script:
    - echo "Do your build here"

test:
  stage: test
  tags:
    - arm64
  script:
    - echo "Do a test here"
    - echo "For example run a test suite"
```

- https://docs.gitlab.com/ee/ci/docker/using_docker_images.html


## Runners

- https://docs.gitlab.com/ee/ci/runners/README.html 
- https://gitlab-runner-downloads.s3.amazonaws.com/latest/index.html


Process

```
root      1334  0.1  3.2 829060 30864 ?        Ssl  20:48   0:07 /usr/bin/gitlab-runner run --working-directory /home/gitlab-runner --config /etc/gitlab-runner/config.toml --service gitlab-runner --user gitlab-runner
```

Runs are root so why it doesn't need to be added to the docker group

## Executors

I've tested

### Shell

### Docker

### Troubleshooting
