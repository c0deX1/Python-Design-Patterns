class Amplifier:
    """Amp real"""

    def on(self):
        print("Top-O-Line Amplifier on")


class Tuner:
    """Tuner"""


class DvdPlayer:
    """DvdPlayer"""


class CdPlayer:
    """CdPlayer"""


class Projector:
    """Proj"""

    def on(self):
        print("Top-O-Line projector on")

    def off(self):
        print("Top-O-Line projector off")

    def wideScreenMode(self):
        print("Top-O-Line projector in widescreen mode")


class TheaterLights:
    def on(self):
        print("Set on threater lights")

    def dim(self, dim):
        print("Ceiling Lights dimming to " + str(dim) + "%")


class Screen:
    """Screen"""


class PopcornPopper:
    """Popcorn"""

    def on(self):
        print("Popcorn popper is on")

    def pop(self):
        print("Popcorn popper is pop'd")
