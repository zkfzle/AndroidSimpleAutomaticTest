from ApkEntryActivityGetter import ApkEntryActivityGetter
import os,time

class AutoMaticTester:
    def __init__(self):
        self.pkgnames = []
        self.activities = []

    def touchscreen(self):
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 3, 53, 488))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 3, 54, 2472))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 3, 58, 287))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 3, 57, 0))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 3, 48, 67109084))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 3, 49, 220))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 3, 52, 0))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 0, 2, 0))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 1, 330, 1))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 0, 0, 0))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 0, 2, 0))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 1, 330, 0))
        os.system("adb shell \"sendevent %s %s %s %s\"" % ("/dev/input/event5", 0, 0, 0))

    def processOneApk(self, activityPath):
        os.system("adb shell \"am start -n %s\"" % activityPath)
        time.sleep(15)
        self.touchscreen()
        time.sleep(15)
        self.touchscreen()
        time.sleep(15)
        self.touchscreen()
        time.sleep(15)
        self.touchscreen()
        time.sleep(2)

    def process(self):
        self.loadActivities()
        # print self.activities
        # start one of them for test
        for i in range(len(self.pkgnames)):
            self.processOneApk(self.pkgnames[i] + "/" + self.activities[i])



    def loadActivities(self):
        getter = ApkEntryActivityGetter()
        self.pkgnames, self.activities = getter.process()

if __name__ == '__main__':
    tester = AutoMaticTester()
    tester.process()