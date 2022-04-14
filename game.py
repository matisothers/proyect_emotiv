from cortex import Cortex
import threading
import time
import random


class Game():
    """
    A class to use BCI API to control the training of the mental command detections.

    Attributes
    ----------
    c : Cortex
        Cortex communicate with Emotiv Cortex Service

    Methods
    -------
    do_prepare_steps():
        Do prepare steps before training.
    subscribe_data():
        To subscribe to one or more data streams.
    live(profile_name):
        Load a trained profiles then subscribe mental command data to enter live mode
    on_new_data(*args, **kwargs):
        To handle mental command data emitted from Cortex
    """

    def __init__(self):
        """
        Constructs cortex client and bind a function to handle subscribed data streams for the Train object
        If you do not want to log request and response message , set debug_mode = False. The default is True
        """
        self.c = Cortex(user, debug_mode=False)
        self.c.bind(new_com_data=self.on_new_data)
        self.time_game = float("inf")

    def do_prepare_steps(self):
        """
        Do prepare steps before training.
        Step 1: Connect a headset. For simplicity, the first headset in the list will be connected in the example.
                If you use EPOC Flex headset, you should connect the headset with a proper mappings via EMOTIV Launcher first 
        Step 2: requestAccess: Request user approval for the current application for first time.
                       You need to open EMOTIV Launcher to approve the access
        Step 3: authorize: to generate a Cortex access token which is required parameter of many APIs
        Step 4: Create a working session with the connected headset
        Returns
        -------
        None
        """
        self.c.do_prepare_steps()

    def subscribe_data(self, streams):
        """
        To subscribe to one or more data streams
        'com': Mental command
        'fac' : Facial expression

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['com']

        Returns
        -------
        None
        """
        self.c.sub_request(streams)


    def live(self, profile_name):
        """
        Load a trained profiles then subscribe mental command data to enter live mode

        Returns
        -------
        None
        """
        
        # load profile
        status = 'load'
        self.c.setup_profile(profile_name, status)

        # sub 'com' stream and view live mode
        stream = ['com']
        self.c.sub_request(stream)

    def on_new_data(self, *args, **kwargs):
        """
        To handle mental command data emitted from Cortex

        Returns
        -------
        data: dictionary
             the format such as {'action': 'neutral', 'power': 0.0, 'time': 1590736942.8479}
        """
        data = kwargs.get('data')
        # print(data)
        dt = time.time() - self.time_game 
        # print(dt)
        if dt >= 0:
            # print(dt)
            if data['action'] == 'push':
                print("your reaction time was: " + str(dt) + " sec")
                self.time_game = time.time() + random.random() *15
    
                


# -----------------------------------------------------------

'''
SETTING
    - replace your license, client_id, client_secret to user dic
    - naming your profile
    - connect your headset with dongle or bluetooth, you should saw headset on EmotivApp.
      make sure the headset at good contact quality.

TRAIN
    you need to folow steps:
        1) do_prepare_steps: for authorization, connect headset and create working session.
        2) subscribe 'sys' data for Training Event
        3) load a profile with the connected headset
        4) do training actions one by one. Begin with neutral action

LIVE
    you can run live mode with the trained profile. the data as below:

    {'action': 'neutral', 'power': 0.0, 'time': 1590736942.8479}
    {'action': 'neutral', 'power': 0.0, 'time': 1590736942.9729}
    {'action': 'push', 'power': 0.345774, 'time': 1590736943.0979}
    {'action': 'push', 'power': 0.294056, 'time': 1590736943.2229}
    {'action': 'push', 'power': 0.112473, 'time': 1590736943.3479}
'''

"""
    client_id, client_secret:
    To get a client id and a client secret, you must connect to your Emotiv account on emotiv.com and create a Cortex app
    For training purpose, you should set empty string for license
"""
user = {
    "client_id" : "KD7TAk1pdrSLO42V3XrYJhxv6d15zgmyRsVwRT98",
    "client_secret" : "vwBoZJiw0fWgKHMweEBRRDkRjGcfk9TK0X95lUcgOuEd2enAqKnYt9T9nsfdaDOtUwd5nie1XFw1wjuQtF7HzATBRbB09L35yHcHRWhAVAFd318ZNrtN7yfEU4sjm6nX",
    "debit" : 100
}

# name of training profile
profile_name = 'Matias Sothers'


# Init Train
g=Game()

# Do prepare steps
g.do_prepare_steps()



x = threading.Thread(target=g.live, args=(profile_name,))

x.start()
r = random.random() *15
g.time_game = time.time() + r
print('********** begin game ***********')



while True:
    time.sleep(r)
    print("******** PUSH NOW! ********")
    


# -----------------------------------------------------------