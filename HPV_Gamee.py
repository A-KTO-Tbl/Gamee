from requests import post
from urllib.parse import unquote
from colorama import Fore
from hashlib import md5
from datetime import datetime, timedelta
from threading import Thread, Lock
from typing import Literal
from random import randint
from os import system as sys
from platform import system as s_name
from time import sleep
from itertools import cycle

from Core.Tools.HPV_Getting_File_Paths import HPV_Get_Accounts
from Core.Tools.HPV_Proxy import HPV_Proxy_Checker
from Core.Tools.HPV_User_Agent import HPV_User_Agent

from Core.Config.HPV_Config import *



class HPV_Gamee:
    '''
    AutoBot Ferma /// HPV
    ---------------------
    [1] - `Unlock mining when it is blocked`
    
    [2] - `Collect WP when mining is unlocked`
    
    [3] - `Attempt to upgrade for WP mining`
    
    [4] - `Get information about the availability of spins`
    
    [5] - `Spin all available spins`
    
    [6] - `Get information about the availability of games`
    
    [7] - `Play all available games`
    
    [8] - `Wait from 30 to 60 minutes`
    
    [9] - `Repeat actions every 30-60 minutes`
    '''



    def __init__(self, Name: str, URL: str, Proxy: dict = None) -> None:
        self.Name = Name                         # Account nickname
        self.URL = self.URL_Clean(URL)           # Unique link for authorization in mini app
        self.Proxy = Proxy                       # Proxy (if available)
        self.UA = HPV_User_Agent()               # Generate unique User Agent
        self.Domain = 'https://api.gamee.com/'   # Game domain
        INFO = self.Authentication()
        self.Token = INFO['Token']               # Account token
        self.Games = str(INFO['Games'] + 1)      # Number of games played



    def URL_Clean(self, URL: str) -> str:
        '''Clean the unique link from unnecessary elements'''

        try:
            return unquote(URL.split('#tgWebAppData=')[1].split('&tgWebAppVersion')[0])
        except:
            return ''



    def Current_Time(self) -> str:
        '''Current time'''

        return Fore.BLUE + f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'



    def Logging(self, Type: Literal['Success', 'Warning', 'Error'], Name: str, Smile: str, Text: str) -> None:
        '''Logging'''

        with Console_Lock:
            COLOR = Fore.GREEN if Type == 'Success' else Fore.YELLOW if Type == 'Warning' else Fore.RED # Text color
            DIVIDER = Fore.BLACK + ' | '   # Divider

            Time = self.Current_Time()     # Current time
            Name = Fore.MAGENTA + Name     # Account nickname
            Smile = COLOR + str(Smile)     # Emoji
            Text = COLOR + Text            # Log text

            print(Time + DIVIDER + Smile + DIVIDER + Text + DIVIDER + Name)



    def Authentication(self) -> dict:
        '''Account authentication'''

        Headers = {'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'client-language': 'en', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://prizes.gamee.com', 'priority': 'u=1, i', 'referer': 'https://prizes.gamee.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': self.UA, 'x-install-uuid': 'a5658ae5-54e4-447c-a8cc-d1859be596ea'}
        Data = '{"jsonrpc":"2.0","id":"user.authentication.loginUsingTelegram","method":"user.authentication.loginUsingTelegram","params":{"initData":"' + self.URL + '"}}'

        try:
            HPV = post(self.Domain, headers=Headers, data=Data, proxies=self.Proxy).json()['result']

            Token = HPV['tokens']['authenticate'] # Account token
            Games = HPV['user']['gamee']['gameplays'] # Number of games played

            self.Logging('Success', self.Name, '🟢', 'Initialization successful!')
            return {'Token': Token, 'Games': Games}
        except:
            self.Logging('Error', self.Name, '🔴', 'Initialization error!')
            return {'Token': '', 'Games': 0}



    def ReAuthentication(self) -> None:
        '''Re-authentication of the account'''

        INFO = self.Authentication()
        self.Token = INFO['Token']               # Account token
        self.Games = str(INFO['Games'] + 1)      # Number of games played



    def Get_Info(self) -> dict:
        '''Get information about the balance and end of mining'''

        Headers = {'accept': '*/*', 'accept-language': 'ru,en;q=0.9,uz;q=0.8', 'authorization': f'Bearer {self.Token}', 'client-language': 'en', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://prizes.gamee.com', 'priority': 'u=1, i', 'referer': 'https://prizes.gamee.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': self.UA, 'x-install-uuid': '927fcdde-8b83-4e37-9862-24e9611fb9c2'}
        Data = '{"jsonrpc":"2.0","id":"miningEvent.getAll","method":"miningEvent.getAll","params":{"pagination":{"offset":0,"limit":10}}}'

        try:
            HPV = post(self.Domain, headers=Headers, data=Data, proxies=self.Proxy).json()

            USER_INFO = HPV['user'] # Information about the balance of tickets and dollars
            Tickets = USER_INFO['tickets']['count'] # Ticket balance
            WP = '' # WP balance
            COIN = '' # COIN balance

            try:Dollars = USER_INFO['money']['usdCents'] / 100 # Dollar balance
            except:Dollars = USER_INFO['money']['usdCents']

            for Token in USER_INFO['assets']:
                if Token['currency']['ticker'] == 'WP':
                    WP = f"{Token['amountMicroToken'] / 1_000_000:,.2f}"
                elif Token['currency']['ticker'] == 'COIN':
                    COIN = f"{Token['amountMicroToken'] / 1_000_000:,.0f}"

            WP_INFO = HPV['result']['miningEvents'] # Information about WP mining
            for WP_Mining in WP_INFO:
                try:Mining_Over = WP_Mining['miningUser']['miningSessionEnded'] # Whether the mining cycle has ended [True or False]
                except:pass

            return {'Tickets': f'{Tickets:,}', 'WP': WP, 'COIN': COIN, 'Dollars': Dollars, 'Mining_Over': Mining_Over}
        except:
            return {'Tickets': None, 'WP': None, 'COIN': None, 'Dollars': None, 'Mining_Over': None}



    def Get_Info_Spin(self) -> int:
        '''Get information about the availability of spins'''

        Headers = {'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'authorization': f'Bearer {self.Token}', 'client-language': 'en', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://prizes.gamee.com', 'priority': 'u=1, i', 'referer': 'https://prizes.gamee.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': self.UA, 'x-install-uuid': 'a5658ae5-54e4-447c-a8cc-d1859be596ea'}
        Data = '{"jsonrpc":"2.0","id":"dailyReward.getPrizes","method":"dailyReward.getPrizes","params":{}}'

        try:
            HPV = post(self.Domain, headers=Headers, data=Data, proxies=self.Proxy).json()['result']['dailyReward']

            Spins = HPV['spinsCountAvailable'] # Regular spins
            Gold_Spins = HPV['wheelOfCashSpinsCountAvailable'] # Spins for cash prizes

            return Spins + Gold_Spins
        except:
            return 0



    def Claim_WP(self) -> bool:
        '''Collect WP'''

        Headers = {'accept': '*/*', 'accept-language': 'ru,en;q=0.9,uz;q=0.8', 'authorization': f'Bearer {self.Token}', 'client-language': 'en', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://prizes.gamee.com', 'priority': 'u=1, i', 'referer': 'https://prizes.gamee.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': self.UA, 'x-install-uuid': '927fcdde-8b83-4e37-9862-24e9611fb9c2'}
        Data1 = '{"jsonrpc":"2.0","id":"miningEvent.claim","method":"miningEvent.claim","params":{"miningEventId":26}}'
        Data2 = '{"jsonrpc":"2.0","id":"miningEvent.startSession","method":"miningEvent.startSession","params":{"miningEventId":26}}'

        try:
            post(self.Domain, headers=Headers, data=Data1, proxies=self.Proxy).json()['result'] # Claim
            post(self.Domain, headers=Headers, data=Data2, proxies=self.Proxy).json()['result'] # Start Session
            self.Logging('Success', self.Name, '🟢', 'Coins collected!')
            return True
        except:
            self.Logging('Error', self.Name, '🔴', 'Coins not collected!')
            return False



    def WP_Mining_Update(self) -> bool:
        '''Upgrade for WP mining'''

        Headers = {'accept': '*/*', 'accept-language': 'ru,en;q=0.9,uz;q=0.8', 'authorization': f'Bearer {self.Token}', 'client-language': 'en', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://prizes.gamee.com', 'priority': 'u=1, i', 'referer': 'https://prizes.gamee.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': self.UA, 'x-install-uuid': '927fcdde-8b83-4e37-9862-24e9611fb9c2'}
        Data = '{"jsonrpc":"2.0","id":"miningEvent.upgrade","method":"miningEvent.upgrade","params":{"miningEventId":26,"upgrade":"storage"}}'

        try:
            post(self.Domain, headers=Headers, data=Data, proxies=self.Proxy).json()['result']
            return True
        except:
            return False



    def Spin(self) -> None:
        '''Spin all available spins'''

        Headers = {'accept': '*/*', 'accept-language': 'ru,en;q=0.9,uz;q=0.8', 'authorization': f'Bearer {self.Token}', 'client-language': 'en', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://prizes.gamee.com', 'priority': 'u=1, i', 'referer': 'https://prizes.gamee.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': self.UA, 'x-install-uuid': '927fcdde-8b83-4e37-9862-24e9611fb9c2'}
        Data = '[{"jsonrpc":"2.0","id":"dailyReward.claimPrize","method":"dailyReward.claimPrize","params":{}},{"jsonrpc":"2.0","id":"dailyReward.getPrizes","method":"dailyReward.getPrizes","params":{}}]'

        try:
            HPV = post(self.Domain, headers=Headers, data=Data, proxies=self.Proxy).json()[0]['result']['reward']

            Prize = ''
            if HPV['type'] == 'money' or HPV['type'] == 'wheelOfCash':
                Prize = f'{HPV["usdCents"] / 100:,.2f}$'
            else:
                Prize = f'{HPV["tickets"]} tickets'

            self.Logging('Success', self.Name, '🟢', f'Spin completed! Received: {Prize}')
        except:
            self.Logging('Error', self.Name, '🔴', 'Spin not completed!')



    def Get_Plays(self) -> int:
        '''Get the number of available games'''

        Headers = {'accept': '*/*', 'accept-language': 'ru,en;q=0.9,uz;q=0.8', 'authorization': f'Bearer {self.Token}', 'client-language': 'en', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://prizes.gamee.com', 'priority': 'u=1, i', 'referer': 'https://prizes.gamee.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': self.UA, 'x-install-uuid': '927fcdde-8b83-4e37-9862-24e9611fb9c2'}
        Data = '{"jsonrpc":"2.0","id":"telegram.getGameAndLives","method":"telegram.getGameAndLives","params":{"gameId":null}}'

        try:
            return int(post(self.Domain, headers=Headers, data=Data, proxies=self.Proxy).json()['result']['lives']['numberOfLives'] / 30)
        except:
            return 0



    def Play(self) -> None:
        '''Play the car game'''

        def Checksum_Generation(WP, COIN):
            gameStateData = '{"usedLives":30,"reward":{"WP":'+WP+',"COIN":'+COIN+'}}'
            return md5(f'0:32::{gameStateData}:crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen'.encode()).hexdigest()

        WP, COIN = str(randint(WPs[0], WPs[1])), str(randint(COINs[0], COINs[1]))
        Headers = {'accept': '*/*', 'accept-language': 'ru,en;q=0.9,uz;q=0.8', 'authorization': f'Bearer {self.Token}', 'client-language': 'en', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://prizes.gamee.com', 'priority': 'u=1, i', 'referer': 'https://prizes.gamee.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': self.UA, 'x-install-uuid': '927fcdde-8b83-4e37-9862-24e9611fb9c2'}
        Data = '{"jsonrpc":"2.0","id":"game.saveTelegramMainGameplay","method":"game.saveTelegramMainGameplay","params":{"gameplayData":{"gameId":294,"score":0,"playTime":32,"releaseNumber":4,"createdTime":"2024-07-28T16:05:36+05:00","metadata":{"gameplayId":' + self.Games + '},"checksum":"' + Checksum_Generation(WP, COIN) + '","gameStateData":"{\\"usedLives\\":30,\\"reward\\":{\\"WP\\":'+WP+',\\"COIN\\":'+COIN+'}}","replayData":"AgAAABIAHnkD5cwAbgBvBQAe","replayVariant":null,"replayDataChecksum":null}}}'

        try:
            HPV = post(self.Domain, headers=Headers, data=Data, proxies=self.Proxy).json()['result']['rewardVirtualTokens']

            WP = ''
            COIN = ''

            for Token in HPV:
                if Token['currency']['ticker'] == 'WP':
                    WP = int(Token['amountMicroToken'] / 1_000_000)
                if Token['currency']['ticker'] == 'COIN':
                    COIN = int(Token['amountMicroToken'] / 1_000_000)

            self.Logging('Success', self.Name, '🟢', f'Game played! Received: +{WP} WP and +{COIN} COIN')
        except:
            self.Logging('Error', self.Name, '🔴', 'Game not played!')



    def Run(self) -> None:
        '''Activate the bot'''

        while True:
            try:
                if self.Token: # If authentication is successful
                    INFO = self.Get_Info()


                    Tickets = INFO['Tickets'] # Ticket balance
                    WP = INFO['WP'] # WP balance
                    COIN = INFO['COIN'] # COIN balance
                    Dollars = INFO['Dollars'] # Dollar balance
                    Mining_Over = INFO['Mining_Over'] # Has the mining cycle ended [True or False]


                    self.Logging('Success', self.Name, '💰', f'Current balance: {Dollars}$, {Tickets} tickets, {WP} WP and {COIN} COIN')


                    # Check if WP mining has ended, and restart it if necessary
                    try: # If mining is unlocked
                        if Mining_Over:
                            if self.Claim_WP():
                                INFO = self.Get_Info()
                                Tickets, WP, COIN, Dollars = INFO['Tickets'], INFO['WP'], INFO['COIN'], INFO['Dollars']
                                self.Logging('Success', self.Name, '💰', f'Current balance: {Dollars}$, {Tickets} tickets, {WP} WP and {COIN} COIN')
                                sleep(randint(33, 103)) # Intermediate wait
                    except: # If mining is locked
                        self.Claim_WP() # Unlock mining
                        sleep(randint(33, 103)) # Intermediate wait


                    # Attempt to upgrade WP mining
                    if UPDATE:
                        if self.WP_Mining_Update():
                            self.Logging('Success', self.Name, '🟢', 'Mining upgrade successful!')
                            INFO = self.Get_Info()
                            Tickets, WP, COIN, Dollars = INFO['Tickets'], INFO['WP'], INFO['COIN'], INFO['Dollars']
                            self.Logging('Success', self.Name, '💰', f'Current balance: {Dollars}$, {Tickets} tickets, {WP} WP and {COIN} COIN')
                            sleep(randint(33, 103)) # Intermediate wait


                    # Get the number of available spins and start spinning
                    Get_Spins = self.Get_Info_Spin()
                    if Get_Spins > 0:
                        self.Logging('Success', self.Name, '🎮', f'Spins available: {Get_Spins}!')
                        for _ in range(Get_Spins):
                            self.Spin()
                            sleep(randint(12, 23))

                            INFO = self.Get_Info()
                            Tickets, WP, COIN, Dollars = INFO['Tickets'], INFO['WP'], INFO['COIN'], INFO['Dollars']
                            self.Logging('Success', self.Name, '💰', f'Current balance: {Dollars}$, {Tickets} tickets, {WP} WP and {COIN} COIN')


                    # Get the number of available games and start playing them
                    Get_Plays = self.Get_Plays()
                    if Get_Plays > 0:
                        self.Logging('Success', self.Name, '🎮', f'Games available: {Get_Plays}!')
                        for _ in range(Get_Plays):
                            self.Play()
                            sleep(randint(12, 23))

                            INFO = self.Get_Info()
                            Tickets, WP, COIN, Dollars = INFO['Tickets'], INFO['WP'], INFO['COIN'], INFO['Dollars']
                            self.Logging('Success', self.Name, '💰', f'Current balance: {Dollars}$, {Tickets} tickets, {WP} WP and {COIN} COIN')


                    Waiting = randint(1_800, 3_600) # Waiting time in seconds
                    Waiting_STR = (datetime.now() + timedelta(seconds=Waiting)).strftime('%Y-%m-%d %H:%M:%S') # Readable waiting time

                    self.Logging('Warning', self.Name, '⏳', f'Next spin check: {Waiting_STR}!')

                    sleep(Waiting) # Wait from 30 to 60 minutes
                    self.ReAuthentication() # Re-authenticate the account

                else: # If authentication is not successful
                    sleep(randint(33, 66)) # Wait from 33 to 66 seconds
                    self.ReAuthentication() # Re-authenticate the account
            except:
                pass





if __name__ == '__main__':
    sys('cls') if s_name() == 'Windows' else sys('clear')

    Console_Lock = Lock()
    Proxy = HPV_Proxy_Checker()

    def Start_Thread(Account, URL, Proxy = None):
        Gamee = HPV_Gamee(Account, URL, Proxy)
        Gamee.Run()

    if Proxy:
        DIVIDER = Fore.BLACK + ' | '
        Time = Fore.BLUE + f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        Text = Fore.GREEN + f'Proxy check completed! Working: {len(Proxy)}'
        print(Time + DIVIDER + '🌐' + DIVIDER + Text)
        sleep(5)

    try:
        for Account, URL in HPV_Get_Accounts().items():
            if Proxy:
                Proxy = cycle(Proxy)
                Thread(target=Start_Thread, args=(Account, URL, next(Proxy),)).start()
            else:
                Thread(target=Start_Thread, args=(Account, URL,)).start()
    except:
        print(Fore.RED + '\n\tError reading `HPV_Account.json`, links are incorrect!')