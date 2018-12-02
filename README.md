# MARTA Train Tracker Alexa Skill

### Basic usage

* Alexa, ask train tracker when is the next southbound train arriving at Five Points?
* Alexa: The next southbound trains arrive at Five Points Station at 06:55 PM, 07:01 PM and 07:08 PM.


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

This project uses the Python unittest library.  From root directory, run 
```bash
python3 -m unittest discover -v
```