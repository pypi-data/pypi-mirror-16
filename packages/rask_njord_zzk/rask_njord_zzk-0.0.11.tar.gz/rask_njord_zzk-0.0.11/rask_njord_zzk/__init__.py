from rask.base import Base
from rask.parser.json import jsonify

__all__ = ['ZZK']

class ZZK(Base):
    options = {
        'content-type':'application/json;charset=UTF-8',
        'request_timeout':60.0,
        'url':'https://api.00k.srv.br'
    }

    def __init__(self,token,http):
        self.http = http
        self.token = token

    @property
    def request(self):
        return {'headers':{'Authorization':self.token,'Content-Type':self.options['content-type']},'request_timeout':self.options['request_timeout']}

    def get_brands(self,uid,future):
        def on_fetch(_):
            future.set_result(_.result())
            return True

        request = self.request
        request['method'] = 'GET'
        request['url'] = '%s/catalog/brands/?externalid=%s' % (self.options['url'],uid)

        self.http.fetch(request,future=self.ioengine.future(on_fetch))
        return True

    def get_category(self,uid,future):
        def on_fetch(_):
            future.set_result(_.result())
            return True

        request = self.request
        request['method'] = 'GET'
        request['url'] = '%s/catalog/categories?externalid=%s' % (self.options['url'],uid)

        self.http.fetch(request,future=self.ioengine.future(on_fetch))
        return True

    def get_sku(self,sku,future):
        def on_fetch(_):
            future.set_result(_.result())
            return True

        request = self.request
        request['method'] = 'GET'
        request['url'] = '%s/catalog/products/all?sku=%s' % (self.options['url'],sku)

        self.http.fetch(request,future=self.ioengine.future(on_fetch))
        return True

    def set_brands(self,payload,future):
        def on_fetch(_):
            future.set_result(_.result())
            return True

        request = self.request
        request['method'] = 'POST'
        request['url'] = '%s/catalog/brands' % (self.options['url'])
        return True

    def set_category(self,payload,future):
        def on_fetch(_):
            future.set_result(_.result())
            return True

        requert = self.request
        request['body'] = jsonify(payload)
        request['method'] = 'POST'
        request['url'] = '%s/catalog/categories' % self.options['url']

        self.http.fetch(request,future=self.ioengine.future(on_fetch))
        return True

    def set_stock_bulk(self,payload,future):
        def on_fetch(_):
            future.set_result(_.result())
            return True

        request = self.request
        request['body'] = jsonify(payload)
        request['method'] = 'PUT'
        request['url'] = '%s/catalog/products/stock' % self.options['url']

        self.http.fetch(request,future=self.ioengine.future(on_fetch))
        return True
