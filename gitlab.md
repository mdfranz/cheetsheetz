# Docs
- [Tutorial: Create and run your first GitLab CI/CD pipeline](https://docs.gitlab.com/ee/ci/quick_start/index.html)


# Blogs & Videos

## Ansible
- [How to automate your DevOps using GitLab CI/CD + Docker + Ansible](https://medium.com/@a.golmirzaei/how-to-automate-your-devops-using-gitlab-ci-cd-docker-ansible-a32de7a116fc) - April 2022
- [GitLab E2E Pipeline — Logger Application+ELK Stack Deployment Using Terraform+Ansible on AWS](https://awstip.com/gitlab-e2e-pipeline-logger-application-elk-stack-deployment-using-terraform-ansible-on-aws-78e5d94bd088)
- [Automating Patching Activity Using Ansible & GitLab CI](https://aws.plainenglish.io/automating-patching-activity-using-ansible-gitlab-ci-f63747515a12)
- [Ansible CICD pipeline with GitLab](https://kruyt.org/ansible-ci-with-gitlab/) - Jan 2020

## Terraform
- [Create CI/CD Pipelines for Terraform in GitLab](https://medium.com/aws-in-plain-english/create-ci-cd-pipelines-for-terraform-in-gitlab-f3f6239b6724) - Oct 2022
- [Staying DRY Using Terraform Workspaces with GitLab-CI](https://www.youtube.com/watch?v=PtxtGPxCaQ8)
- [Terraform Gitlab CI/CD Pipeline](https://blog.terraforge.io/posts/terraform-gitlab-ci-cd-pipeline/) - Aug 2019
- [Manage Terraform With GitLab CI](https://medium.com/@dbourgeois23/manage-terraform-with-gitlab-ci-5c24005eb62a) - Mar 2019
- [Terraform Pipelines in GitLab](https://medium.com/@timhberry/terraform-pipelines-in-gitlab-415b9d842596) - 2018
- [Terraform Automation with GitLab & AWS](https://www.nvisia.com/insights/terraform-automation-with-gitlab-aws) - 2018
- [How to Govern Terraform States Using GitLab Enterprise](https://www.gofirefly.io/blog/how-to-govern-terraform-states-using-gitlab-enterprise)

Also see [Gitlab Terraform Images](https://gitlab.com/gitlab-org/terraform-images) and [GitLab CI template for Terraform](https://to-be-continuous.gitlab.io/doc/ref/terraform/)



# CI Configuration

This uses tags and specifies a docker image

`NOTE` tags are specified in each stage not for the entire .yml file

See https://docs.gitlab.com/ee/ci/variables/ and https://docs.gitlab.com/ee/ci/yaml/ and https://docs.gitlab.com/ee/ci/yaml/#needs


```
variables:
  REGION: us-east-2
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
    - export

test:
  stage: test
  tags:
    - arm64
  script:
    - echo "Do a test here"
    - echo "For example run a test suite"
```




## Runners

- https://docs.gitlab.com/ee/ci/runners/README.html 
- https://gitlab-runner-downloads.s3.amazonaws.com/latest/index.html


Process

```
root      1334  0.1  3.2 829060 30864 ?        Ssl  20:48   0:07 /usr/bin/gitlab-runner run --working-directory /home/gitlab-runner --config /etc/gitlab-runner/config.toml --service gitlab-runner --user gitlab-runner
```

Runs are root so why it doesn't need to be added to the docker group

# Executors

I've tested

## Shell

## Docker

# Troubleshooting

## Runner

```
ubuntu@pi4b-b7ead551:~$ journalctl -f -u gitlab-runner
-- Logs begin at Mon 2022-01-10 04:56:39 UTC. --
Dec 11 23:51:09 pi4b-b7ead551 gitlab-runner[821]: Checking for jobs...nothing                         runner=H9ZYz2v8
Dec 11 23:51:12 pi4b-b7ead551 gitlab-runner[821]: Checking for jobs...nothing                         runner=H9ZYz2v8
Dec 11 23:51:15 pi4b-b7ead551 gitlab-runner[821]: Checking for jobs...nothing                         runner=H9ZYz2v8
```


