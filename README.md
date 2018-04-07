# Artifact-Deployer

![screenshot](https://github.com/pipizhang/artifact-deployer/blob/master/screenshots/00.png)

Artifact-Deployer is a small tool designed to deploy Jenkins artifacts to remote server. Although there are various way on Jenkins CI/CD pipelines, this tool is more meet my requirement on controling, enalbe the right version of builds be depoyed to prodution server. Particully for a small team which lackof testers.

### Features
* List the latest builds info
* Deploy a specific version of build to remote via SSH

### Getting started
Copy env.example to .env, put settings.

```bash
make install
source venv/bin/activate
make run
```

### Requires
* Python3
* Virtualenv
* SSH

