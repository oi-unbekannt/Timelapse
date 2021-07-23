# Timelapse
Timelapse ist ein kleines Python3 Werkzeug, um mit einem Raspberry Pi und einer Pi Kamera in einem vordefiniertem Intervall Fotos aufzunehmen. Diese können dann mit zb. ffmpeg oder jeder anderen Video Software zu einem Zeitraffer Video konvertiert werden.

![timelapse console log](/media/timelapse.jpg)

## Vorwort
Verzeiht den Namen, ich bin was das angeht nicht wirklich kreativ 😅. Anstelle dieses Tools kannst du auch einfach das Command Line Tool raspistill nutzen. 
Dieses liefert dir mit einem Kommando fast das gleiche Ergebnis. Warum also habe ich dieses Tool geschrieben? Ganz einfach, 
ich brauchte ein Use Case um meine neu erlernten Python Fähigkeiten zu trainieren und mir war langweilig. 

## Hardware
Um dieses Tool nutzen zu können brauchst du einen Raspberry Pi. Ich nutze für meine Aufnahmen einen Raspberry Pi 3b, du kannst aber auch jede andere Variante nutzen. 
Außerdem brauchst du eine der folgenden Pi Kameras:
- [Camera Module v1](https://www.raspberrypi.org/blog/camera-board-available-for-sale/)
- [Camera Module v2](https://www.raspberrypi.org/blog/new-8-megapixel-camera-board-sale-25/)
- [HQ Camera](https://www.raspberrypi.org/blog/new-product-raspberry-pi-high-quality-camera-on-sale-now-at-50/) An diesem Modell können via Adapter auch große Objektive verwendet werden.

> *Mit einer Powerbank kannst du das Setup auch in der Natur nutzen :wink:.*

## Software

- [Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit) *empfohlen*
- [Python3](https://www.python.org/)
- [python-picamera](https://picamera.readthedocs.io/en/release-1.13/install.html)

Ich nutze für dieses Projekt die neuste Version des [Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit), da dieses bereits alles benötigte an Board hat.

Du kannst auch ein anderes OS wie Ubuntu nutzen, dazu muss aber das nötige Python Modul installiert werden. 
Eine ausführliche Anleitung findest du in der [Picamera Dokumentation](https://picamera.readthedocs.io/en/release-1.13/install.html).

## Funktionsweise
### Installation und Ausführen von timelapse.py
```
git clone http://gitea.ori:3000/Python/timelapse.git
cd timelapse
python3 timelapse.py
```

### Speicherort der Aufnahmen
```
./captures/[Datum und Uhrzeit der Aufnahme]/
```

### Konfiguration via settings.json
![timelapse settings-full](/media/settings-full.jpg)

### Auflösung und Bild Rotation
![timelapse setting-format](/media/settings-format.jpg)

```JSON
"rotation": "0 = Normal; 90 = Dreht das Bild um 90°, 180 = Dreht das Bild um 180°, etc."
"resolution": { 
    "width": "Bildbreite",
    "height": "Bildhöhe"
} 
```

### Beschriftung im Bild
![timelapse settings-text](/media/setting-text.jpg)

```JSON 
"text": { 
    "size": "Schriftgröße",
    "foreground": "Schriftfarbe",
    "background": "Hintergrundfarbe der Beschriftung"
} 
```

### Aufnahme Einstellungen
![timelapse settings-timelapse](/media/settings-timelapse.jpg)

```JSON 
"timelapse": { 
    "auto_mode": "Wenn 'true' wird Timelapse mit der in 'auto_capture_mode' eingetragenen Option gestartet.",
    "auto_capture_mode": "Timelapse biete zwei Modi: day und night.", 
    "images": "Gesamtanzahl der Bilder die gemacht werden, zb: 5.",                
    "interval": "Intervall in dem die Bilder gemacht werden in Sekunden. Hier sollte ggf. 'shutter_speed' mit einbezogen werden. zb: 10."
}
```
```JSON
"day": { 
    "iso": "Iso in der das Bild aufgenommen wird. 0 = Iso 0, 800 = Iso 800, etc.." 
}
```
```JSON
"night": { 
    "iso": "Iso in der das Bild aufgenommen wird. 0 = Iso 0, 800 = Iso 800, etc..",
    "shutter_speed": "Verschlusszeit in Mikrosekunden 6000000 = 6 Sekunden."
}
```

### Statistik
![timelapse settings-statistics](/media/settings-statistics.jpg)

```JSON 
"statistics": { 
    "enable": "Wenn 'true' schreibt Timelapse Statistiken zu der Bilder Serie in die Datei: data/statistics.json.",
    "json": "Speicherort der Statistiken, zb: ./data/statistics.json"   
}  
```