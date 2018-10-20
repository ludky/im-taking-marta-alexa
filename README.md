# I'm Taking MARTA Alexa Skill

## Objectives
* Make taking public transit more convenient
* Increase usage of public transit

## Summary

Alexa skill for getting real-time Marta transit information.  Basic intents supported are:

* Get next train arrival times by departure station and destination
* Get next train arrival times by departure station, direction, and line
* Get next train arrival times by departure station 

## Basic usage
* Alexa, ask train tracker: when is the next train from Chamblee to Five Points?
* Alexa: The next train from Chamblee station to Five Points station will arrive at 08:14:09.


## Developer resources
### Requirements

* AWS CLI already configured with at least PowerUser permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)
* [Python Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### Structure
- marta (app directory)
- tests (unit tests)
- deploy_dev.sh (deployment script)

### Packaging and deployment

This project utilizes AWS CodeBuild and AWS CodePipeline to automatically build and deploy the application code.
If for some reason the CI server isn't working and you'd like to deploy from local machine, you can run:
  
`./deploy_dev.sh`

If a new Lambda function is created, you'll need to manually update the Alexa skill trigger.  Right now, the CF script
does not do this.

### Testing

This project uses the Python unittest library.  Run unit tests in `tests/unit`