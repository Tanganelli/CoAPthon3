from coapthon.resources.resource import Resource
from coapthon.server.coap import CoAP


class DimmerResource(Resource):
    def __init__(self, name="DimmerResource", coap_server=None):
        super(DimmerResource, self).__init__(name, coap_server, visible=True,
                                             observable=True, allow_children=True)
        self.value = 0
        self.payload = str(self.value)
        self.resource_type = "dimmer"
        self.content_type = "text/plain"
        self.interface_type = "urn:oma:lwm2m:ext:3311:5851"

    def render_GET(self, request):
        self.payload = str(self.value)
        return self

    def render_PUT(self, request):
        if request.payload.isdigit():
            amount = int(request.payload)
            if 0 <= amount <= 100:
                self.value = amount
                self.edit_resource(request)
                return self
        return None


class SwitchResource(Resource):
    def __init__(self, name="SwitchResource", coap_server=None):
        super(SwitchResource, self).__init__(name, coap_server, visible=True,
                                             observable=True, allow_children=True)
        self.value = 0
        self.payload = str(self.value)
        self.resource_type = "switch"
        self.content_type = "text/plain"
        self.interface_type = "urn:oma:lwm2m:ext:3311:5850"

    def render_GET(self, request):
        self.payload = str(self.value)
        return self

    def render_PUT(self, request):
        if request.payload.isdigit():
            status = int(request.payload)
            if 0 <= status <= 1:
                self.value = status
                self.edit_resource(request)
                return self
        return None


class CoAPServer(CoAP):
    def __init__(self, host, port, multicast=False):
        CoAP.__init__(self, (host, port), multicast)
        self.add_resource('dimmer/', DimmerResource())
        self.add_resource('switch/', SwitchResource())


def main():  # pragma: no cover
    ip = "127.0.0.1"
    port = 5683

    server = CoAPServer(ip, port, False)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == "__main__":  # pragma: no cover
    main()
