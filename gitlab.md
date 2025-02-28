# References
- [Upgrade tool](https://gitlab-com.gitlab.io/support/toolbox/upgrade-path/)

# My Installation

See https://about.gitlab.com/install/#ubuntu

## Minimum KVM Settings

4 Cores x 8GB

# Docs
- [Tutorial: Create and run your first GitLab CI/CD pipeline](https://docs.gitlab.com/ee/ci/quick_start/index.html)

## CI References
- [Variables](https://docs.gitlab.com/ci/variables/) and [predefined variables](https://docs.gitlab.com/ci/variables/predefined_variables/)
- [Push Options](https://docs.gitlab.com/topics/git/commit/#push-options-for-gitlab-cicd)

# Blogs & Videos
- [What Happens on GitLab When You do git push?](https://nanmu.me/en/posts/2022/what-happens-on-gitlab-when-you-do-git-push/)

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

# Self Hosting Junk

- 2 vCPUs and 8GB RAM is minimum resources

Save the stuff in /etc/gitlab after the initial install

```
root@gitlab16:/etc/gitlab# ls
gitlab-secrets.json  gitlab.rb  initial_root_password  trusted-certs
```
