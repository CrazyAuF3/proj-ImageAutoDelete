This is the README file of the project ImageAutoDelete.
===

Introduction
---
Automatically delete the cache images of the tencent QQ and TIM.

Basic Usage
---

Open the "config.txt", add the directories you want to delete
in the file (one per line, not include empty lines, not include
empty lines at the end of the file).

For example:
```
Group2
C2C
Thumbnails
MarktingMsgCachePic
...
```

Open the "numberNUsername.txt", write your QQ-number at the
first line, and the system username at the second line.

For example:
```
<Your QQ number>
Administrator
```

The probable directories are:

 - C2C: client to client chat
 - Group: group chat(rare for new TIM)
 - Group2: group chat
 - Thumbnails: unknown
 - PicFileThumbnails: unknown
 - MsgWander: unknown
 - MarktingMsgCachePic: unknown
 - ImageEditor: image editor

If you want to open the config file or the name file,
you can type "config" or "name" when the program let 
you type your QQ-number.