name = "NukeSurvivalToolkit"

version = "2.1.1"

authors = [
    "Leo Depoix",
    "CreativeLyons",
]

description = \
    """
    The Nuke Survival Toolkit is a portable tool menu for the Foundry’s Nuke with a hand-picked selection of nuke gizmos collected from all over the web, organized into 1 easy to install toolbar..
    """

requires = [
    "python-3+",
    "nuke",
]

uuid = "CreativeLyons.NukeSurvivalToolkit"

build_command = 'python {root}/build.py {install}'

def commands():
    env.NUKE_PATH.append("{root}/python/NukeSurvivalToolkit")