from requests import get as req_get

class FabricServerStarter:
    def __init__(self, version='latest', ver_type='release', loader='latest', installer='latest'):
        self.manifests_urls = {
            'mojang': 'https://launchermeta.mojang.com/mc/game/version_manifest.json',
            'fabric_loader': 'https://meta.fabricmc.net/v2/versions/loader',
            'fabric_installer': 'https://meta.fabricmc.net/v2/versions/installer'
        }

        self.manifests = {}
        for manifest_id, manifest_url in self.manifests_urls.items():
            with req_get(manifest_url) as http:
                self.manifests[manifest_id] = http.json()

        if version == 'latest':
            self.version = self.manifests["mojang"]["latest"][ver_type]
        else:
            self.version = version
        
        if loader == 'latest':
            self.loader = self.manifests["fabric_loader"][0]["version"]
        else:
            self.loader = loader
        
        if installer == 'latest':
            self.installer = self.manifests["fabric_installer"][0]["version"]
        else:
            self.installer = installer
        
        self.get_jar()
        
    def get_jar(self):
        self.jar_url = f"{self.manifests_urls['fabric_loader']}/{self.version}/{self.loader}/{self.installer}/server/jar"
    
    def download_jar(self):
        with req_get(self.jar_url) as http:
            self.jar = http.content
        
        with open('fabric.jar', 'wb') as jarf:
            jarf.write(self.jar)
        
    