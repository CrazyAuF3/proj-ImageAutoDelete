import shutil
import os
from sys import exit
from colourPrint import colourPrint

res = None
with open("config.txt") as configFile:
    namelist = configFile.readlines()
    namelist = list(map(lambda s: s.strip(), namelist))
    colourPrint(1, 34, 40, '<Info>Reading config.txt file.')

with open("numberNUsername.txt") as configFile:
    defaultParamList = configFile.readlines()
    defaultParamList = list(map(lambda s: s.strip(), defaultParamList))
    colourPrint(1, 34, 40, '<Info>Reading numberNUsername.txt file.')


def shield(originalFunc):
    def returnFunc(*args, **kwargs):
        global res
        try:
            res = originalFunc(*args, **kwargs)
        except Exception as e:
            colourPrint(1, 31, 40, f"<Error>Error @ function {originalFunc.__name__}: {e}")
        return res

    return returnFunc


@shield
def getNumberNUsername() -> list:
    colourPrint(1, 32, 40,
                '<Input>Input the QQ number and the system username. Both Enter for default(numberNUsername.txt).')
    colourPrint(1, 32, 40, "<Input>QQ number: ", end='')
    number = input()
    colourPrint(1, 32, 40, "<Input>System username: ", end='')
    userName = input()
    return [number, userName]


@shield
def delete(number: str, dire: str, userName: str = "Administrator") -> None:
    colourPrint(1, 34, 40, f'<Info>Removing files of user {userName}, QQ number {number}, removing dir: {dire}.')
    shutil.rmtree(rf'C:\Users\{userName}\Documents\Tencent Files\{number}\Image\{dire}')
    colourPrint(1, 34, 40, '<Info>Operation completed.')


@shield
def searchDir(Dirs: list, number: str, userName: str) -> dict:
    returnList = {}
    for directory in Dirs:
        if os.path.exists(rf'C:\Users\{userName}\Documents\Tencent Files\{number}\Image\{directory}'):
            colourPrint(1, 34, 40,
                        rf'<Info>Dir found: C:\Users\{userName}\Documents\Tencent Files\{number}\Image\{directory}',
                        )
            returnList[directory] = True

        else:
            colourPrint(1, 34, 40,
                        rf'<Info>Dir not found: C:\Users\{userName}\Documents\Tencent Files\{number}\Image\{directory}',
                        )
            returnList[directory] = False
    # print(returnList)
    return returnList


def listDir(number: str, userName: str) -> list:
    return os.listdir(rf'C:\Users\{userName}\Documents\Tencent Files\{number}\Image')


@shield
def main():
    paramList = getNumberNUsername()
    if paramList == ['', '']:
        paramList = defaultParamList
    if paramList[0] == "config":
        os.startfile("config.txt")
        exit(0)
    if paramList[0] == 'name':
        os.startfile("numberNUsername.txt")
        exit(0)

    deleteList = searchDir(namelist, paramList[0], paramList[1])
    colourPrint(1, 34, 40, f'<Info>Search result: {deleteList}')
    colourPrint(1, 34, 40, f'<Info>Your current config: {deleteList}')
    colourPrint(1, 32, 40, '<Input>Ready to delete files. Type Q to abort the operation: ', end='')
    isContinue = input()
    if isContinue.lower().startswith('q'):
        colourPrint(1, 34, 40, '<Info>Operation aborted.')
        exit(0)

    isAllFalse = True
    for flag in deleteList:
        if deleteList[flag]:
            delete(paramList[0], flag, userName=paramList[1])
            isAllFalse = False

    if isAllFalse:
        colourPrint(1, 34, 40, '<Info>There\'s nothing to remove...')

    probableDirs = ['C2C', 'Group', 'Group2', 'Thumbnails', 'PicFileThumbnails', 'MsgWander',
                    'MarktingMsgCachePic', 'ImageEditor']

    for file in listDir(*paramList):
        if file not in probableDirs:
            colourPrint(1, 34, 40,
                        rf'<Info>Found C:\Users\{paramList[1]}\Documents\Tencent Files\{paramList[0]}\Image\{file}')

    colourPrint(1, 32, 40, '<Input>Ready to delete files. Type Q to abort the operation: ', end='')
    isContinue = input()
    if isContinue.lower().startswith('q'):
        exit(0)
    if not list(set(listDir(*paramList)) - set(probableDirs)):
        colourPrint(1, 34, 40, '<Info>There\'s nothing to remove...')
    else:
        for file in listDir(*paramList):
            if file not in probableDirs:
                colourPrint(1, 34, 40,
                            rf'<Info>Removing C:\Users\{paramList[1]}' +
                            rf'\Documents\Tencent Files\{paramList[0]}\Image\{file}')
                if os.path.isdir(rf'C:\Users\{paramList[1]}\Documents\Tencent Files\{paramList[0]}\Image\{file}'):
                    os.removedirs(rf'C:\Users\{paramList[1]}\Documents\Tencent Files\{paramList[0]}\Image\{file}')
                else:
                    os.remove(rf'C:\Users\{paramList[1]}\Documents\Tencent Files\{paramList[0]}\Image\{file}')


if __name__ == '__main__':
    main()
    colourPrint(1, 34, 40, '<Info>Operation completed, exiting...')
