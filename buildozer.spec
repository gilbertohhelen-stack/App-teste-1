[app]
title = Assistente Baixar Video
package.name = assistentevideo
package.domain = org.assistente
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,yt-dlp
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECORD_AUDIO
android.api = 33
android.minapi = 21
android.ndk = 25b
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1