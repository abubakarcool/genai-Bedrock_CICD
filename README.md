### search Bedrock and get start and request model request for first time
### create envirnment and activate it and then install the requirements
```
conda create -n llmops python=3.8 -y
conda activate llmops
pip install -r requirements.txt
```
### search IAM(identity access management) and create user and give permission of bedrock to it 
### create user -> name and next -> attach policy and AmazonBedrockFullAccess and check it and create user
### to get the API key click on created user and click security credentials and create access key and check command line interface CLI and click next and create the access key. download the csv file.
### next we need to configure it, download AWS cli and install it
```
aws configure
```
## give the access key and secret key and also the location as ap-south-1

```
streamlit run .\main.py
```


