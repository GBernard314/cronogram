# Cronogram

## Goal

This is a telegram notifier when a cron job worked properly.

## Setup

And then we need to create the bot:

1. Contact the ```@BotFather```.
    ![image](./screenshots/Screenshot_1.png)
<br />

2. Give your bot a name (we will refer to it as ```@your_bot_name```, in my case it's ```@cronogramed_bot```).
    ![image](./screenshots/Screenshot_2.png)
    And here you have the ```API token```.  
<br />

3. You need to install Python dependencies.
    In a Terminal write :

    ```bash
    pip3 install telegram-send
    ```
<br />

4. Configure your sender :

    ```bash
    telegram-send --configure
    ```
<br />

5. You are prompted to enter your ```API token``` you obtained in ```step 2```.
<br />

6. You obtain a ```code``` you will need in few steps.
<br />

7. Contact ```@your_bot_name```.
    ![image](./screenshots/Screenshot_3.png)
    And click the ```start``` button.
<br />

8. Enter the ```code``` you obtained in ```step 6```.
    ![image](./screenshots/Screenshot_3.png)
<br />

9. ```@your_bot_name``` is ready !