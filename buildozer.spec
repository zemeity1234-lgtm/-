[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# ØªÙ Ø¶Ø¨Ø· Ø§ÙÙØªØ·ÙØ¨Ø§Øª ÙØªØ´ÙÙ Ø§ÙØ£Ø¯ÙØ§Øª Ø§ÙØ£Ø³Ø§Ø³ÙØ©
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API - ØªÙ Ø§ÙØªØ¹Ø¯ÙÙ ÙÙØªÙØ§ÙÙ ÙØ¹ ÙØ¹Ø§ÙÙØ± 2026
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) ØªÙØ¹ÙÙ ÙØ¨ÙÙ Ø§ÙØªØ±Ø§Ø®ÙØµ ØªÙÙØ§Ø¦ÙØ§Ù ÙÙØ£ØªÙØªØ©
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

[buildozer]

# (int) Log level (2 = debug ÙÙØ­Ø§Ø±Ø
