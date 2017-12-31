class ApkEntryActivityGetter:
    def process(self):
        pkgnames = []
        activitys = []
        with open("apklauncherActivity.txt") as f:
            for line in f:

                items = line.strip().split()
                pkgname = items[0]
                activity = items[-1]
                pkgnames.append(pkgname)
                activitys.append(activity)
        return [pkgnames, activitys]
if __name__ == '__main__':
    entryGetter = ApkEntryActivityGetter()
    print entryGetter.process()[0]
    print entryGetter.process()[1]