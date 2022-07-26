# FE automation case for Insider

This repo is created for FE automation for Insider. Page Object Model is used.
- Browser type and headless options can be changed using parameters in *config.json*.

This repo can be cloned using following command:

```bash
git clone https://github.com/azmiyuksel/insider_fe_automation_case.git
```

## Installing Dependencies

After cloning the repo, related directory should be opened and dependencies should be installed with following command (Virtual environment can be used):

```bash
cd insider_fe_automation_case
pip install -r requirements.txt
```

## Executing Tests

Tests can be executed  with following command:

```bash
pytest --alluredir=report --clean-alluredir
```

Test Report can be displayed with following command:

```bash
allure serve report
```
Screenshots can be seen in the report for failed scenarios:
![image](https://user-images.githubusercontent.com/2384320/181058139-a06268ed-3ef2-4f35-9e6f-5956887fc127.png)
