#!/usr/bin/env bash
#pip install -r requirements.txt -t marta/build/
mkdir marta/build
cp marta/*.py marta/build/
aws cloudformation package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket im-taking-marta-deployments \
    --profile imtakingmarta
sam deploy \
    --template-file packaged.yaml \
    --stack-name im-taking-marta-dev \
    --capabilities CAPABILITY_IAM \
    --profile imtakingmarta