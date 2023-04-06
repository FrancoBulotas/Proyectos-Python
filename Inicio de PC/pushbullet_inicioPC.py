from pushbullet import PushBullet
from time import sleep


sleep(10)

access_token = "o.NnReSMrcQgk0s0WdrRLDWNvZpqWn7bAt"
text = "TU PC SE ENCENDIO"
pb = PushBullet(access_token)
push = pb.push_note("ALERTA", text)

