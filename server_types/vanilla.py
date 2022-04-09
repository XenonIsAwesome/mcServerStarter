from requests import get as req_get

class ServerStarter:
    def __init__(self, version='latest', ver_type='release'):
        self.manifest_url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

        with req_get(self.manifest_url) as http:
            self.manifest = http.json()


        if version == 'latest':
            self.version = self.manifest["latest"][ver_type]
        else:
            self.version = version
        
        self.get_version()
        self.get_jar()
    
    def get_version(self):
        versions = self.manifest["versions"]
        for v in versions:
            if v["id"] == self.version:
                self.ver_manifest_url = v["url"]
                return

    def get_jar(self):
        with req_get(self.ver_manifest_url) as http:
            self.ver_manifest_url = http.json()
        
        self.jar_url = self.ver_manifest_url["downloads"]["server"]["url"]
    
    def download_jar(self):
        with req_get(self.jar_url) as http:
            self.jar = http.content
        
        with open('server.jar', 'wb') as jarf:
            jarf.write(self.jar)
        
    