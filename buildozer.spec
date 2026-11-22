[app]
title = Assistente Baixar Video
package.name = assistentevideo
package.domain = org.assistente
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requests,certifi python3,kivy,requests,certifi
android.accept_sdk_license = True
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE e WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0
android.accept_sdk_license = True
[buildozer]
log_level = 2
warn_on_root = 1