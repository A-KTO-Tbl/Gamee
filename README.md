<div align="center">

![Screenshot_1](https://telegra.ph/file/894d3309c99cfcf28ceaa.png)

# 🟣 Gamee AutoBot /// HPV /// V1.07 🟣

| **Features**                                                        | **Supported**  |
|----------------------------------------------------------------|:---------------:|
| **Multifunctional** - *performs the same actions you would do manually:*<br>**—** *Unlocking mining when it is blocked*;<br>**—** *Collecting WP when mining is unlocked*;<br>**—** *Attempting to upgrade WP mining*;<br>**—** *Checking for available spins*;<br>**—** *Scrolling through all available spins*;<br>**—** *Checking for available games*🆕;<br>**—** *Playing all available games*🆕;<br>**—** *Waiting for 30 to 60 minutes*;<br>**—** *Repeating actions every 30-60 minutes*. |✅|
| **Cross-platform** - *the script can be run on any platform, whether it's Windows, Linux, or Android. This also allows for easy installation on a server and simply monitoring the farming process* |✅|
| **Multithreaded** - *thanks to the use of threading technology, the script allows farming on multiple accounts simultaneously. There are no limitations on the number of added accounts* |✅|
| **Proxy** - *the script supports adding an unlimited number of proxy servers. Even if the number of proxies is less than the number of accounts, they will be evenly distributed among all accounts after being checked for validity. Although using proxies is not mandatory, it is strongly recommended to use them to prevent blocking in Gamee (not in Telegram)* |✅|
| **Fine-tuning** - *the script allows you to enable or disable auto-updates for WP mining. By default, the value is set to True, which means enabling auto-updates. However, you can disable it by setting the value to False in the configuration. You can also configure the desired amount of coins earned per game. In the configuration, you can specify a range of numbers within which WP and COIN points will be credited. The default value is set from 159 to 357. It is not recommended to increase the maximum value above 550! In the best case, the coins will not be credited to the balance, and in the worst case, your account may be blocked in Gamee (not in Telegram)* |✅|
| **Adding accounts** - *thanks to my unique technology, unlike other similar scripts, you don't need to deal with API_ID and API_HASH for each account. This significantly reduces the entry threshold, protects your Telegram account from being banned, and saves precious time. To add an account, simply specify the special link obtained from the bot. Detailed instructions are provided below* |✅|
| **Sybil protection (bot detection)** - *in a world where projects like Gamee strive to block all bot users, my concern for your safety has not gone unnoticed. Implemented using the full power of Python, the script is designed to minimize the risk of blocking the farm accounts. Each account receives a unique User-Agent after initialization, making it impossible to identify as a bot. Additionally, the script randomly varies the execution time of each action to simulate natural behavior. And of course, there is support for proxies for maximum anonymity and protection. You can choose not to use them, but I strongly recommend it for your safety* |✅|

**<br>This script is intended solely for educational purposes. Use it responsibly and avoid abuse. You are fully responsible for any consequences of its use, including the risk of account blocking in the Gamee bot (not in Telegram)!**
***
</div>

# <br><br>🟡 Updated - 31.07.2024 🟡
- **Fixed a bug with game completion. Now games are played 100%.<br><br>**
- **Update for 28.07.2024:**
- - ***Removed the event ID config;<br>***
- - ***Updated all requests;<br>***
- - ***Updated spin scrolling and fixed a bug;<br>***
- - ***Updated WP claim;<br>***
- - ***Updated WP miner upgrade;<br>***
- - ***Changed authentication;<br>***
- - ***Added game completion;<br>***
- - ***Other minor but important changes.***<br><br>
- **Update for 23.07.2024:**
- - ***Added error message for incorrectly specified links in the config;<br>***
- - ***Added 7,500 User Agents.<br>***

# <br><br>🧬 Preliminary Setup
- **Linux**
  - ```
    apt update && apt upgrade -y
    ```
  - ```
    apt install -y python3 git
    ```
  - ```
    git clone https://github.com/A-KTO-Tbl/Gamee
    ```
  - ``` 
    pip3 install -r Gamee\Core\Tools\requirements.txt
    ```
- **Windows**
  - To begin, you need to install [Python](https://www.python.org/downloads/release/python-3103/) (versions above 3.10.3 are not recommended) and [Git](https://git-scm.com/download/win);
  - Create a folder anywhere, for example on the desktop. Then open it;
  - In the top part of the file explorer, click on the path ***([SCREENSHOT](https://telegra.ph/file/f4695bbc6a7c4e142c758.jpg))*** and type "*CMD*";
  - CMD will open in the current directory. Then simply enter the following commands:
    - ``` 
      git clone https://github.com/A-KTO-Tbl/Gamee
      ```
    - ``` 
      pip install -r Gamee\Core\Tools\requirements.txt
      ```
- **Android**
  - For your convenience, it is recommended to perform the initial setup of the script on a PC. After that, download the configured version of the script on GitHub and clone it into [Termux](https://github.com/termux/termux-app/releases). Then simply run the script with the following command:
    - ``` 
      python HPV_Gamee.py
      ```

# <br>🌐 Proxy Setup
- To add proxies, go to the ***Core*** > ***Proxy*** section and open the ***HPV_Proxy.txt*** file. Then simply enter your proxies in the format of one line - one proxy. SOCKS5 and HTTPS protocols are supported. An example of adding a proxy can be found in the same folder ***([SCREENSHOT](https://telegra.ph/file/828b1caf4e50e522ffb9e.jpg))***.

# <br>⚙️ Config Setup
- You can enable or disable WP mining upgrades. To change the configuration, go to ***Core*** > ***Config*** and open ***HPV_Config.py***. Find the ***UPDATE*** variable ***([SCREENSHOT](https://telegra.ph/file/249c22f89dde8b13867c8.png))***. By default, the value is set to ***True***, which is the optimal solution. If you want, you can change the value to ***False*** to disable mining updates.
- In addition, you can configure the desired amount of coins earned per game by specifying a range of numbers in the configuration file. To do this, go to ***Core*** > ***Config*** and open ***HPV_Config.py***. Find the two variables: ***WPs*** and ***COINs***. The first one is for the desired amount of WP earned per game, and the second one is for the desired amount of COIN earned per game. The default value is set from 159 to 357, which is optimal. You can change this range, but it is not recommended to increase the maximum value above 550. In the best case, the coins will not be credited to the balance, and in the worst case, your account may be blocked in Gamee (not in Telegram).

# <br>🔰 Adding Accounts
As mentioned earlier, adding accounts does not require dealing with **API_ID** and **API_HASH** for each of them, which significantly reduces the entry threshold and saves your time. All you need to do is add a special link to the config obtained from the bot. However, this process is only available on Android devices. iPhone users will need to find an Android device to obtain the link. **Android - One Love!** Now let's get down to business.

- **Instructions for obtaining a unique link:**
  ***
  **1)** *Go to the [bot](https://t.me/gamee/start?startapp=ref_1295320967);*<br>
  **2)** *Enter the command **/start**;*<br>
  **3)** *Click on the **"Spin"** button;<br>
  **4)** *As soon as you click the button, immediately turn off the internet so that the mini app starts but doesn't have time to load;*<br>
  **5)** *As a result, an error with the desired link will appear. If the link does not appear, try clicking on the three dots at the top without internet and select **"Reload"**. If the link still does not appear, repeat this step again. It is important that the link is very long;*<br>
  **6)** *Copy the entire text of the error, then paste it in any chat and find the desired link in the error text;*<br>
  **7)** *Next, go to **Core > Config** and open **HPV_Account.json**;*<br>
  **8)** *Enter the desired account name in the first key, which will be displayed in the logs (it is optimal to use the account's username). It is recommended to write no more than one word and in English **([SCREENSHOT](https://telegra.ph/file/9fea159d1ec26acd6778a.jpg))**;*<br>
  **9)** *Enter the previously obtained link next to the key **([SCREENSHOT](https://telegra.ph/file/e35b6a41d26d55c357a5e.jpg))**;*<br>
  **10)** *Add the farm accounts in this way;*<br>
  **11)** *It is important to note: **put commas after each penultimate element of the dictionary (i.e., account), and do not put a comma after the last element.** The config shows a clear example **([SCREENSHOT](https://telegra.ph/file/cf351db4e17e353fe6fc9.jpg))**.*
  ***
- **Video instructions for obtaining a unique link: [WATCH](https://telegra.ph/file/f8567f9c842ec2f656944.mp4)**

# <br>⚡️ Running
- **Linux**
  - ``` 
    cd Gamee && python3 HPV_Gamee.py
    ```
- **Windows**
  - Run ***"[HPV] Start on Windows.bat"***
- **Android**
  - After preparing the script on PC and cloning the downloaded repository from GitHub into [Termux](https://github.com/termux/termux-app/releases), run the script with the following command:
    - ``` 
      cd Gamee && python HPV_Gamee.py
      ```

# <br><br>💎 Additional Information
- **[Telegram channel](https://t.me/+nXUk0aZ0valjYmFi). Subscribing to our channel is the best support and motivation for continuing this and other projects! 💜**
- **[Owner](https://t.me/A_KTO_Tbl)**
- **TON:** ```UQChditl95Hy_kMektYwzpW7Os9OCmyriJaAD0YMdxJREp1s```
- **Base /// BNB Chain /// ETH (EVM):** ```0x4E7Fecf762295CB696e862F4c3a30Ffc586DeDb2```
- **NEAR:** ```a_kto_tbl.near```
- **Tron:** ```TSGP8XnjJ9wFNamYs3k17bN13Vg8WZE55s```
- **Solana:** ```wWMvNzKZFPTr96eGz5hi6aymYsycwvWWrWgHwdXNYPQ```

