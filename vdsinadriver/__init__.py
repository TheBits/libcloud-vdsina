from libcloud.common.base import ConnectionKey, JsonResponse
from libcloud.compute.base import KeyPair, NodeDriver, NodeImage, NodeLocation
from libcloud.utils.publickey import get_pubkey_openssh_fingerprint


class VdsinaConnection(ConnectionKey):
    responseCls = JsonResponse
    host = "userapi.vdsina.ru"

    def add_default_headers(self, headers):
        headers["Authorization"] = self.key
        return headers


class VdsinaDriver(NodeDriver):
    connectionCls = VdsinaConnection
    name = "Vdsina"
    website = "https://vdsina.ru/"

    def list_locations(self):
        response = self.connection.request("api/datacenter")
        country = {
            1: "RU",
            2: "CH",
            3: "GB",
            5: "RU",
            8: "RU",
            9: "RU",
            10: "RU",
            21: "DE",
        }

        locations = []
        for loc in response.object["datacenters"]:
            locations.append(NodeLocation(loc["id"], loc["name"], country[loc["id"]], self))
        return locations

    def list_images(self):
        images = []
        response = self.connection.request("api/os")
        for image in response.object["os"]:
            images.append(NodeImage(image["Id"], image["Name"], self))
        return images

    def list_size(self):
        pass

    def list_key_pairs(self):
        response = self.connection.request("v1/ssh-key")
        key_pairs = []
        for kp in response.object.get("data"):
            key_pair = KeyPair(
                name=kp["name"],
                public_key=kp["key"],
                fingerprint=get_pubkey_openssh_fingerprint(kp["key"]),
                driver=self,
                extra=dict(id=kp["id"]),
            )
            key_pairs.append(key_pair)
        return key_pairs
