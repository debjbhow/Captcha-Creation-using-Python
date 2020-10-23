from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha


image = ImageCaptcha()
audio = AudioCaptcha()

data = audio.generate('1234')
audio.write('1234', 'aud.wav')


data = image.generate('CzbA')
image.write('CzbA', 'img.png')
