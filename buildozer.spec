[app]

# (A) Basic Configuration
title = Calculatrice Kivy Pro
package.name = calculatrice
package.domain = com.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,spec
version = 0.1
# Ligne corrigée et rendue active pour résoudre l'erreur :
orientation = portrait,landscape,sensor
fullscreen = 0
android.arch = armeabi-v7a
presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png
log_level = 1
requirements = python3,kivy,ast,math

# (B) Main file setting: IMPORTANT
main.pyc = %(source.dir)s/calculatrice.py

# (C) Android SDK/NDK Settings (Required by Buildozer)
android.sdk = 29
android.ndk = 25b
android.api = 29
android.minapi = 21

# (D) Permissions
android.permissions = INTERNET
