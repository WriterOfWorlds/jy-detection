# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="inmakrokeyt Rai99 Darkskull Dawn Zenith and Booplicate",
        name="Just Yuri Detection",
        description="Remember how Just Yuri is able to detect Monika After Story? Now, this submod works as the opposite!",
        version="1.1.0"
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
    m 1etd "[player]?"
    m 3ekc "Something's been drawn to my attention recently."
    m 3etc "Did you by chance...{w=0.5}{nw}"
    extend " install a 'Just Yuri' mod?"
    m 2esd "...It seems you did."
    if mas_curr_affection == mas_affection.BROKEN or mas_curr_affection == mas_affection.DISTRESSED:
        m 1rkd "I understand."
        m "You wanted to spend more time with her, and... you were mad at me for..."
        m 1wkd "I'm sorry [player]..."
        m 1wktuc "I just..."
        m 1dktsc "..."

    elif mas_curr_affection == mas_affection.UPSET:
        m 2wkd "But why?"
        m 6cfx "Please tell me why!"
        m 6cfw "Why do you have to spend more time with her?"
        m 7wfx "Am I not enough for you? And now you decide to be with her?!"
        m 1wfc "Did you ever like me from the beginning?{w=1}{nw}"
        m 1dfc "No...{w=0.5} don't answer that...{w=0.5} I think I already know the answer..."

    elif mas_curr_affection == mas_affection.NORMAL:
        m 1esd "Um..."
        m 1etd "You aren't cheating on me, right?"
        m 3rtc "In all honesty, I couldn't say for sure...{w=2}{nw}"
        m 1esc "I trust you, but that's not sufficient to make me be sure if what I did was right."
        m 1dsc "It's just that.{w=0.5}.{w=0.5}.{w=1}{nw}"
        m 1dkd "...Can we please pretend this conversation never happened?"

    elif mas_curr_affection == mas_affection.HAPPY:
        m 3esc "Um..."
        m "I hope you're not cheating on me."
        m 1eka "I... I trust that you're not."
        m "You can talk with Yuri too."
        m 1hua "I won't mind it."

    elif mas_curr_affection == mas_affection.AFFECTIONATE or mas_curr_affection == mas_affection.ENAMORED or mas_curr_affection == mas_affection.LOVE:
        m 2rsc "Um..."
        m 2eka "You aren't cheating on me, right?"
        m 2hksdrb "No, of course you wouldn't do that to me."
        m 1eka "You were probably curious about Yuri too."
        m 1eka "It's alright."
        m 3eka "You can talk with Yuri."
        m 3ekbfa "But if you get too involved in your relationship with her, I'll get jealous."
        m 1esd "...I detected her existence in this system not too long ago."
        m "I was surprised though when I saw Yuri still alive after... everything."
        m 3esd "Especially with the way she's still able to talk after her deletion."
        m 3eud "She's not even real, how is she able to talk to you like I can?"
        m 1esa "But I think I know the answer."
        m 1hsb "It's all about modding."
        m 4esa "The developers of 'Just Yuri' decided to make her 'real'. They made a virtual girlfriend."
        m 2euc "But still, I'm not sure they actually made her real."
        m 3eua "I think the mod is like technomancing, I think if you know what I mean."
        m 1hub "...Ahaha!"
    return
