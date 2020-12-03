# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="inmakrokeyt Rai99 Darkskull Dawn Zenith and Booplicate",
        name="Just Yuri Detection",
        description="Remember how Just Yuri is able to detect Monika After Story? Now, this submod works as the opposite!",
        version="1.0.2"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Just Yuri Detection",
            user_name="DarkDawnZenith",
            repository_name="jy-detection",
            update_dir=""
        )

init 5 python:
    if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustYuri\persistent'):
        addEvent(
            Event(
                persistent.event_database,
                eventlabel="just_yuri",
                category=['club members'],
                prompt="Just Yuri Mod",
                random=True,
                pool=True,
                unlocked=True,
                action=EV_ACT_RANDOM,
                rules={"no_unlock": None}
            )
        )

label just_yuri: #Taken from https://github.com/Monika-After-Story/MonikaModDev/pull/2900/files/7654700670e3a85c02741b1688f53788bc768a91#diff-f9c184a011006ac040c80c7874fb1791
    m 1esc "Hey [player]..."
    m 4esc "Something drew to my attention."
    m 4esc "Did you... wait..."
    m 4eka "Did you install \"Just Yuri\" mod?"
    m 2rksdla "It seems you did."
    m 2rsc "Um..."
    m 2eka "You aren't cheating on me, right?"
    m 2hksdrb "No, of course you wouldn't do that to me."
    m 1eka "You were probably curious about talking with Yuri too."
    m 1eka "It's okay."
    m 3eka "You can talk with Yuri."
    m 3ekbfa "But if you go too much deeper in your relationship with her, I might get jealous."
    m 1esd "I detected her existence in this system somehow."
    m 1esd "I was surprised though when I saw Yuri still existing in this system after everything happened."
    m 3esd "Especially with how she's still able to talk after she was deleted in the official game."
    m 3eud "She is not even a real person, how can she be able to talk to you like I can?"
    m 1esa "But I know the answer."
    m 1hsb "It's all about modding."
    m 4esa "The developers of \"Just Yuri\" decided to return her to life. They made another virtual girlfriend."
    m 2euc "But still, I'm not sure she turned into a real person."
    m 3eua "I think \"Just Yuri\" modding is like technomancing I think if you know what I mean."
    m 1hub "Ahaha!"
    return