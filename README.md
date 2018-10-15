# I'm Taking MARTA Alexa Skill

Alexa skill for getting real-time Marta transit information.  Basic utterances supported are:
* Alexa, open train tracker
* User: I'm taking Marta from Chamblee station to Five Points station
* Alexa: Okay, the next train southbound train will depart from Chamblee station in 15 minutes


## Requirements

* AWS CLI already configured with at least PowerUser permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)
* [Python Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## Structure
- marta (app directory)
- tests (unit tests)
- deploy_dev.sh (deployment script)

## Local development

### Packaging and deployment

This project utilizes AWS CodeBuild and AWS CodePipeline to automatically build and deploy the application code.
If for some reason the CI server isn't working and you'd like to deploy from local machine, you can run:
  
`./deploy_dev.sh`

If a new Lambda function is created, you'll need to manually update the Alexa skill trigger.  Right now, the CF script
does not do this.

### Testing

This project uses the Python unittest library.  Run unit tests in `tests/unit`