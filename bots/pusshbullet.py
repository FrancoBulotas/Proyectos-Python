from time import sleep
from pushbullet import PushBullet

access_token = "o.NnReSMrcQgk0s0WdrRLDWNvZpqWn7bAt"
text = "1 2 3 4 probando"

pb = PushBullet(access_token)

push = pb.push_note("Estamos probando", text)

sleep(3)
