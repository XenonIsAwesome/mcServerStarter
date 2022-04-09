from server_types.fabric import FabricServerStarter
from server_types.vanilla import ServerStarter

x = input('vanilla/fabric >> ').lower()
if x == 'vanilla':
    server = ServerStarter()

if x == 'fabric':
    server = FabricServerStarter()

server.download_jar()
print('done')